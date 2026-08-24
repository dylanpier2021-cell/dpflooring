/* ==========================================================================
   DP Flooring Services - instant estimate funnel
   No dependencies. No build step. Drop the three files on any static host.
   ========================================================================== */
(function () {
"use strict";

/* ==========================================================================
   1. PASTE YOUR GOHIGHLEVEL INBOUND WEBHOOK URL HERE
   --------------------------------------------------------------------------
   GHL: Automation > Workflows > new workflow > trigger "Inbound Webhook",
   copy the URL it gives you and paste it between the quotes below.
   Until you do, the funnel still runs end to end and logs each payload to the
   browser console so you can see exactly what GHL will receive.
   ========================================================================== */
const WEBHOOK_URL = "PASTE_GHL_WEBHOOK_HERE";


/* ==========================================================================
   2. PRICING ENGINE - edit these numbers, nothing else
   --------------------------------------------------------------------------
   All prices are per square foot unless noted. Ranges are inclusive.
   ========================================================================== */
const PRICING = {

  // Per-square-foot installed price by finish.
  finishes: {
    "Flake":        { low: 6,  high: 8  },
    "Solid color":  { low: 5,  high: 7  },
    "Metallic":     { low: 9,  high: 12 },
    // "Not sure yet" deliberately spans the cheapest low to the priciest high,
    // so nobody is quoted a floor they might later pick and find unaffordable.
    "Not sure yet": { low: 5,  high: 12 }
  },

  // Square footage we assume for each garage size.
  garageSqft: {
    "1-car": 250,
    "2-car": 450,
    "3-car": 650,
    "4+ car": 850
  },

  // Stairs are priced per step, not per square foot.
  stairsPerStep: { low: 50, high: 75 },

  // Extra prep cost as a fraction of the base price.
  conditionModifiers: {
    "Like new, no cracks":                  { low: 0.00, high: 0.00 },
    "A few cracks or small pits":           { low: 0.05, high: 0.05 },
    "Major cracks, pitting, or old coating":{ low: 0.15, high: 0.20 },
    // Unknown condition widens the range rather than guessing low.
    "Not sure":                             { low: 0.00, high: 0.20 }
  },

  // Smallest job worth mobilising for. Below this we show "$1,500+".
  minimumJob: 1500,

  // Round the displayed range to this increment.
  roundTo: 100,

  // true  -> round low DOWN and high UP (never quotes a floor above the math)
  // false -> round both to the nearest increment
  roundOutward: true
};


/* ==========================================================================
   3. Everything below is the funnel machinery. You should not need to edit it.
   ========================================================================== */

const BUSINESS = {
  name:  "DP Flooring Services LLC",
  phone: "(217) 372-7770",
  tel:   "+12173727770",
  email: "dpflooringservicesllc@gmail.com"
};

const STEPS = ["space", "size", "finish", "condition", "timeline", "contact"];
const QUESTION_COUNT = STEPS.length;

const answers = {
  space: null, size: null, sizeDetail: null,
  finish: null, condition: null, timeline: null,
  name: null, phone: null, email: null, address: null, city: null, sms_opt_in: true,
  preferred_day: null, time_window: null
};

let currentStep = 0;
let estimate = null;
let exitShown = false;
let leadSent = false;

const $  = (s, r) => (r || document).querySelector(s);
const $$ = (s, r) => Array.prototype.slice.call((r || document).querySelectorAll(s));


/* ---------------------------------------------------------------- pricing */

function roundTo(n, inc, dir) {
  if (!PRICING.roundOutward) return Math.round(n / inc) * inc;
  return dir === "down" ? Math.floor(n / inc) * inc : Math.ceil(n / inc) * inc;
}

function money(n) { return "$" + n.toLocaleString("en-US"); }

/**
 * Turn the collected answers into a price range.
 * Returns { low, high, atMinimum, basis } or null if we cannot price it yet.
 */
function calculateEstimate() {
  const finish = PRICING.finishes[answers.finish];
  const cond   = PRICING.conditionModifiers[answers.condition] || { low: 0, high: 0 };
  if (!finish) return null;

  let low, high, basis;

  if (answers.space === "Stairs / Steps") {
    const steps = Number(answers.sizeDetail) || 0;
    if (!steps) return null;
    low  = steps * PRICING.stairsPerStep.low;
    high = steps * PRICING.stairsPerStep.high;
    basis = steps + (steps === 1 ? " step" : " steps");
  } else {
    const sqft = Number(answers.sizeDetail) || 0;
    if (!sqft) return null;
    low  = sqft * finish.low;
    high = sqft * finish.high;
    basis = sqft.toLocaleString("en-US") + " sq ft";
  }

  // Condition premium sits on top of the base price.
  low  = low  * (1 + cond.low);
  high = high * (1 + cond.high);

  // A range must never invert, whatever the config says.
  if (high < low) { const t = low; low = high; high = t; }

  low  = roundTo(low,  PRICING.roundTo, "down");
  high = roundTo(high, PRICING.roundTo, "up");

  // Minimum job. If even the top of the range is under it, the whole job is
  // a "from" number rather than a range.
  let atMinimum = false;
  if (high <= PRICING.minimumJob) {
    atMinimum = true;
    low = high = PRICING.minimumJob;
  } else if (low < PRICING.minimumJob) {
    low = PRICING.minimumJob;
  }

  return { low, high, atMinimum, basis };
}

function renderEstimate() {
  estimate = calculateEstimate();
  const rangeEl = $("#estimateRange");
  const basisEl = $("#estimateBasis");
  if (!estimate) {                       // defensive: should not happen
    rangeEl.textContent = "Let's talk it through";
    basisEl.textContent = "Call " + BUSINESS.phone + " and we'll price it on the spot.";
    return;
  }
  rangeEl.textContent = estimate.atMinimum
    ? money(PRICING.minimumJob) + "+"
    : money(estimate.low) + " – " + money(estimate.high);

  const bits = [answers.space, estimate.basis, answers.finish + " finish"];
  basisEl.innerHTML = "Based on " + bits.filter(Boolean).join(" &middot; ") +
    ".<br>This is a planning range, not a contract price — we confirm it in writing " +
    "after we've seen the slab.";
}


/* -------------------------------------------------------------- analytics */

function track(event, data) {
  window.dataLayer = window.dataLayer || [];
  const payload = Object.assign({ event: event }, data || {});
  window.dataLayer.push(payload);
  if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") console.log("[dataLayer]", payload);
}


/* ------------------------------------------------------------ UTM capture */

function getUTMs() {
  const q = new URLSearchParams(window.location.search);
  const out = {};
  ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
   "fbclid", "gclid"].forEach(function (k) {
    const v = q.get(k);
    if (v) out[k] = v;
  });
  // Persist across a refresh so a lead does not lose its attribution.
  try {
    if (Object.keys(out).length) sessionStorage.setItem("dp_utm", JSON.stringify(out));
    else {
      const saved = sessionStorage.getItem("dp_utm");
      if (saved) return JSON.parse(saved);
    }
  } catch (e) { /* private mode - attribution is best effort */ }
  return out;
}
const UTMS = getUTMs();


/* ---------------------------------------------------------------- webhook */

function buildPayload(eventName) {
  const est = estimate || calculateEstimate();
  return {
    event: eventName,
    submitted_at: new Date().toISOString(),
    page_url: window.location.href,
    referrer: document.referrer || null,

    business: BUSINESS.name,

    // contact
    name: answers.name,
    phone: answers.phone,
    email: answers.email,
    address: answers.address,
    city: answers.city,
    sms_opt_in: answers.sms_opt_in,

    // funnel answers
    space: answers.space,
    size: answers.size,
    size_detail: answers.sizeDetail,
    size_unit: answers.space === "Stairs / Steps" ? "steps" : "sq_ft",
    finish: answers.finish,
    condition: answers.condition,
    timeline: answers.timeline,

    // calculated estimate
    estimate_low: est ? est.low : null,
    estimate_high: est ? est.high : null,
    estimate_display: est
      ? (est.atMinimum ? money(PRICING.minimumJob) + "+"
                       : money(est.low) + " - " + money(est.high))
      : null,
    estimate_at_minimum: est ? est.atMinimum : null,

    // booking (null until the last step)
    preferred_day: answers.preferred_day,
    time_window: answers.time_window,

    // ad tracking
    utm_source:   UTMS.utm_source   || null,
    utm_medium:   UTMS.utm_medium   || null,
    utm_campaign: UTMS.utm_campaign || null,
    utm_term:     UTMS.utm_term     || null,
    utm_content:  UTMS.utm_content  || null,
    fbclid:       UTMS.fbclid       || null,
    gclid:        UTMS.gclid        || null
  };
}

/**
 * Fire-and-forget POST. Never blocks the UI and never rejects - a lead must
 * never be trapped behind a network error.
 *
 * Content-Type is text/plain on purpose: it keeps the request "simple" so the
 * browser skips the CORS preflight that GHL inbound webhooks do not answer.
 * GHL parses the body as JSON regardless. Because the response is opaque we
 * cannot read a status, so anything that throws is queued for retry.
 */
function send(eventName) {
  const payload = buildPayload(eventName);

  if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") {
    console.warn("[DP Funnel] WEBHOOK_URL is still the placeholder. " +
                 "Payload that WOULD have been sent:", payload);
    showDevNote();
    return Promise.resolve(false);
  }

  return fetch(WEBHOOK_URL, {
    method: "POST",
    headers: { "Content-Type": "text/plain;charset=UTF-8" },
    body: JSON.stringify(payload),
    keepalive: true
  }).then(function () { return true; })
    .catch(function (err) {
      console.error("[DP Funnel] webhook failed, queued for retry:", err);
      queueRetry(payload);
      return false;
    });
}

function queueRetry(payload) {
  try {
    const q = JSON.parse(localStorage.getItem("dp_retry") || "[]");
    q.push(payload);
    localStorage.setItem("dp_retry", JSON.stringify(q.slice(-20)));
  } catch (e) { /* storage unavailable - nothing more we can do */ }
}

// On load, try anything that failed on a previous visit.
function flushRetries() {
  if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") return;
  let q;
  try { q = JSON.parse(localStorage.getItem("dp_retry") || "[]"); } catch (e) { return; }
  if (!q.length) return;
  try { localStorage.removeItem("dp_retry"); } catch (e) {}
  q.forEach(function (p) {
    fetch(WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "text/plain;charset=UTF-8" },
      body: JSON.stringify(Object.assign({}, p, { retried: true })),
      keepalive: true
    }).catch(function () { queueRetry(p); });
  });
}

function showDevNote() {
  if ($("#devNote")) return;
  const n = document.createElement("div");
  n.id = "devNote";
  n.className = "devnote";
  n.innerHTML = "Setup mode: no webhook connected yet. Open the console to see the " +
                "payload, then paste your URL into <code>WEBHOOK_URL</code> in funnel.js.";
  document.body.appendChild(n);
  setTimeout(function () { n.remove(); }, 9000);
}


/* -------------------------------------------------------------- step flow */

function stepEl(i) { return $('.step[data-index="' + (i + 1) + '"]'); }

function showStep(i, opts) {
  const from = stepEl(currentStep);
  const to   = stepEl(i);
  if (!to) return;
  if (from) from.classList.remove("is-active");
  to.classList.add("is-active");
  currentStep = i;
  updateProgress();

  if (!(opts && opts.noScroll)) {
    const anchor = $("#funnel");
    const y = anchor.getBoundingClientRect().top + window.pageYOffset - 8;
    window.scrollTo({ top: y, behavior: prefersReduced() ? "auto" : "smooth" });
  }
  const focusable = to.querySelector("input, select, button:not([data-next])");
  if (focusable && i >= STEPS.indexOf("contact")) {
    setTimeout(function () { focusable.focus({ preventScroll: true }); }, 340);
  }
}

function prefersReduced() {
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function updateProgress() {
  const bar   = $("#progressBar");
  const label = $("#progressLabel");
  const pct   = $("#progressPct");
  const wrap  = $("#progress");

  if (currentStep >= QUESTION_COUNT) {         // estimate / confirmation
    bar.style.width = "100%";
    pct.textContent = "100%";
    label.textContent = currentStep === QUESTION_COUNT ? "Your estimate" : "All done";
    wrap.classList.add("is-done");
    return;
  }
  wrap.classList.remove("is-done");
  const p = Math.round(((currentStep) / QUESTION_COUNT) * 100);
  const shown = Math.max(p, Math.round((1 / QUESTION_COUNT) * 100));
  bar.style.width = shown + "%";
  pct.textContent = shown + "%";
  label.textContent = "Question " + (currentStep + 1) + " of " + QUESTION_COUNT;
}

function completeStep(stepId, value) {
  track("funnel_step_complete", {
    funnel_step_number: STEPS.indexOf(stepId) + 1,
    funnel_step_id: stepId,
    funnel_step_value: value
  });
}

/** Advance from a card step, after a beat so the selection is visible. */
function autoAdvance(nextIndex) {
  setTimeout(function () { showStep(nextIndex); }, prefersReduced() ? 0 : 220);
}


/* ------------------------------------------------------- step 1: space */

$$('.step[data-step="space"] .card').forEach(function (card) {
  card.addEventListener("click", function () {
    selectCard(card);
    answers.space = card.dataset.value;
    completeStep("space", answers.space);
    configureSizeStep();
    autoAdvance(1);
  });
});

function selectCard(card) {
  const siblings = card.closest(".cards").querySelectorAll(".card");
  Array.prototype.forEach.call(siblings, function (c) { c.classList.remove("is-selected"); });
  card.classList.add("is-selected");
}


/* -------------------------------------------------------- step 2: size */

const sizeGarage = $("#sizeGarage");
const sizeArea   = $("#sizeArea");
const sizeStairs = $("#sizeStairs");
const areaRange  = $("#areaRange");
const areaExact  = $("#areaExact");
const areaOut    = $("#areaReadout");
const stepsRange = $("#stepsRange");
const stepsOut   = $("#stepsReadout");

// Sensible starting square footage per space type, so the slider does not
// open on a number nobody would pick.
const AREA_DEFAULTS = {
  "Basement": 800, "Patio / Porch": 300, "Shop / Warehouse": 1500,
  "Commercial / Business": 2000, "Other": 500
};

function configureSizeStep() {
  const space = answers.space;
  sizeGarage.hidden = sizeArea.hidden = sizeStairs.hidden = true;

  if (space === "Garage") {
    sizeGarage.hidden = false;
    $("#sizeQ").textContent = "How big is the garage?";
    $("#sizeHelp").textContent = "Pick the closest size — we measure it properly on site.";
  } else if (space === "Stairs / Steps") {
    sizeStairs.hidden = false;
    $("#sizeQ").textContent = "How many steps?";
    $("#sizeHelp").textContent = "Count the treads. Landings we'll sort out on site.";
    syncSteps();
  } else {
    sizeArea.hidden = false;
    $("#sizeQ").textContent = "Roughly how big is the space?";
    $("#sizeHelp").textContent = "A close guess is fine — we measure it properly at the on-site quote.";
    const d = AREA_DEFAULTS[space] || 500;
    areaRange.value = d; areaExact.value = d;
    syncArea("range");
  }
}

$$('#sizeGarage .card').forEach(function (card) {
  card.addEventListener("click", function () {
    selectCard(card);
    answers.size = card.dataset.value;
    answers.sizeDetail = PRICING.garageSqft[card.dataset.value];
    completeStep("size", answers.size + " (" + answers.sizeDetail + " sq ft)");
    autoAdvance(2);
  });
});

function clampArea(v) {
  v = Math.round(Number(v) || 0);
  return Math.min(5000, Math.max(100, v));
}

function syncArea(source) {
  const v = clampArea(source === "exact" ? areaExact.value : areaRange.value);
  if (source === "exact") areaRange.value = v; else areaExact.value = v;
  areaOut.innerHTML = v.toLocaleString("en-US") + "<span>sq ft</span>";
  answers.size = v.toLocaleString("en-US") + " sq ft";
  answers.sizeDetail = v;
}
areaRange.addEventListener("input", function () { syncArea("range"); });
areaExact.addEventListener("input", function () {
  // Only mirror while the value is already in range, so typing "1" then "200"
  // is not clamped to 100 mid-keystroke.
  const raw = Number(areaExact.value);
  if (raw >= 100 && raw <= 5000) syncArea("exact");
});
areaExact.addEventListener("blur", function () { syncArea("exact"); });

function syncSteps() {
  const v = Math.min(30, Math.max(1, Math.round(Number(stepsRange.value) || 1)));
  stepsOut.innerHTML = v + "<span>" + (v === 1 ? "step" : "steps") + "</span>";
  answers.size = v + (v === 1 ? " step" : " steps");
  answers.sizeDetail = v;
}
stepsRange.addEventListener("input", syncSteps);

$$("[data-next]").forEach(function (b) {
  b.addEventListener("click", function () {
    if (answers.space === "Stairs / Steps") syncSteps(); else syncArea("exact");
    completeStep("size", answers.size);
    showStep(2);
  });
});


/* ------------------------------------ steps 3-5: finish / condition / time */

[["finish", 3], ["condition", 4], ["timeline", 5]].forEach(function (pair) {
  const id = pair[0], nextIndex = pair[1];
  $$('.step[data-step="' + id + '"] .card').forEach(function (card) {
    card.addEventListener("click", function () {
      selectCard(card);
      answers[id] = card.dataset.value;
      completeStep(id, answers[id]);
      autoAdvance(nextIndex);
    });
  });
});


/* ----------------------------------------------------- step 6: contact */

const funnelForm = $("#funnelForm");
const phoneInput = $("#fPhone");

phoneInput.addEventListener("input", function () {
  if (phoneInput.selectionStart !== phoneInput.value.length) return;   // mid-edit
  const d = phoneInput.value.replace(/\D/g, "").slice(0, 10);
  if (d.length > 6)      phoneInput.value = "(" + d.slice(0,3) + ") " + d.slice(3,6) + "-" + d.slice(6);
  else if (d.length > 3) phoneInput.value = "(" + d.slice(0,3) + ") " + d.slice(3);
  else if (d.length > 0) phoneInput.value = "(" + d;
});

function fieldOf(el) { return el.closest(".field"); }

function validateField(el) {
  const wrap = fieldOf(el);
  if (!wrap) return true;
  let ok = el.checkValidity();

  if (ok && el.id === "fPhone") {
    const digits = el.value.replace(/\D/g, "");
    // 10 digits, or 11 starting with a US country code.
    ok = digits.length === 10 || (digits.length === 11 && digits.charAt(0) === "1");
  }
  wrap.classList.toggle("is-invalid", !ok);
  const err = wrap.querySelector(".err");
  if (err && !ok) err.textContent = err.dataset.msg || el.validationMessage;
  return ok;
}

$$("#funnelForm input, #funnelForm select").forEach(function (el) {
  el.addEventListener("blur", function () { if (el.value) validateField(el); });
  el.addEventListener("input", function () {
    const w = fieldOf(el);
    if (w && w.classList.contains("is-invalid")) validateField(el);
  });
});

funnelForm.addEventListener("submit", function (e) {
  e.preventDefault();
  const required = ["#fName", "#fPhone", "#fEmail", "#fCity"].map(function (s) { return $(s); });
  let firstBad = null;
  required.forEach(function (el) { if (!validateField(el) && !firstBad) firstBad = el; });
  if (firstBad) {
    firstBad.focus();
    firstBad.scrollIntoView({ block: "center", behavior: prefersReduced() ? "auto" : "smooth" });
    track("funnel_validation_error", { funnel_step_id: "contact", field: firstBad.name });
    return;
  }

  answers.name        = $("#fName").value.trim();
  answers.phone       = $("#fPhone").value.trim();
  answers.email       = $("#fEmail").value.trim();
  answers.address     = $("#fAddress").value.trim() || null;
  answers.city        = $("#fCity").value;
  answers.sms_opt_in  = $("#fSms").checked;

  completeStep("contact", answers.city);

  renderEstimate();
  track("estimate_shown", {
    estimate_low:  estimate ? estimate.low  : null,
    estimate_high: estimate ? estimate.high : null,
    space: answers.space, finish: answers.finish
  });

  // Fire the lead now, before the booking step. If they bail after seeing the
  // number, you still have a qualified lead with a price attached.
  leadSent = true;
  send("estimate_viewed");
  track("lead_submitted", { value: estimate ? estimate.low : null, currency: "USD" });

  const btn = $("#submitContact");
  btn.disabled = true;
  btn.textContent = "Calculating…";
  setTimeout(function () {
    showStep(QUESTION_COUNT);                 // estimate screen
    btn.disabled = false;
    btn.textContent = "Show My Estimate";
  }, prefersReduced() ? 0 : 450);
});


/* ---------------------------------------------- step 7: booking + submit */

// Build the next six working days (Mon-Sat), skipping Sunday.
(function buildDays() {
  const row = $("#dayRow");
  const DAY = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  const MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  const out = [];
  const d = new Date();
  d.setDate(d.getDate() + 1);                 // start tomorrow
  while (out.length < 6) {
    if (d.getDay() !== 0) {                   // no Sundays
      out.push({
        label: DAY[d.getDay()],
        sub: MON[d.getMonth()] + " " + d.getDate(),
        value: DAY[d.getDay()] + " " + MON[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear()
      });
    }
    d.setDate(d.getDate() + 1);
  }
  row.innerHTML = out.map(function (o, i) {
    return '<label class="dayopt"><input type="radio" name="preferred_day" value="' + o.value + '">' +
           '<span><b>' + o.label + '</b><small>' + o.sub + '</small></span></label>';
  }).join("");
})();

const bookingForm = $("#bookingForm");

bookingForm.addEventListener("change", function (e) {
  if (e.target.name === "preferred_day") $("#dayErr").closest(".daypick").classList.remove("is-invalid");
  if (e.target.name === "time_window")   $("#timeErr").closest(".daypick").classList.remove("is-invalid");
});

bookingForm.addEventListener("submit", function (e) {
  e.preventDefault();
  const day  = bookingForm.querySelector('input[name="preferred_day"]:checked');
  const time = bookingForm.querySelector('input[name="time_window"]:checked');
  let bad = false;
  if (!day)  { $("#dayErr").closest(".daypick").classList.add("is-invalid");  bad = true; }
  if (!time) { $("#timeErr").closest(".daypick").classList.add("is-invalid"); bad = true; }
  if (bad) {
    track("funnel_validation_error", { funnel_step_id: "booking" });
    (day ? $("#timeErr") : $("#dayErr")).scrollIntoView({ block: "center", behavior: prefersReduced() ? "auto" : "smooth" });
    return;
  }

  answers.preferred_day = day.value;
  answers.time_window   = time.value;

  const btn = $("#submitBooking");
  btn.disabled = true;
  btn.textContent = "Locking it in…";

  track("appointment_requested", {
    preferred_day: answers.preferred_day,
    time_window: answers.time_window,
    value: estimate ? estimate.low : null, currency: "USD"
  });

  send("appointment_requested").then(function () {
    $("#doneSummary").textContent =
      answers.name.split(" ")[0] + ", we've got you down for " + answers.preferred_day +
      ", " + answers.time_window.toLowerCase() + ".";
    showStep(QUESTION_COUNT + 1);
    btn.disabled = false;
    btn.textContent = "Lock In My Free Quote";
    $("#stickybar").classList.add("is-hidden");
  });
});


/* --------------------------------------------------- before/after slider */

(function () {
  const ba = $("#beforeAfter");
  if (!ba) return;
  const range = $(".ba__range", ba);
  const paint = function () { ba.style.setProperty("--pos", range.value + "%"); };
  range.addEventListener("input", paint);
  paint();

  const drag = function (e) {
    const r = ba.getBoundingClientRect();
    const x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
    range.value = String(Math.max(0, Math.min(100, (x / r.width) * 100)));
    paint();
  };
  const stop = function () {
    document.removeEventListener("pointermove", drag);
    document.removeEventListener("pointerup", stop);
  };
  ba.addEventListener("pointerdown", function (e) {
    if (e.pointerType === "mouse" && e.button !== 0) return;
    drag(e);
    document.addEventListener("pointermove", drag);
    document.addEventListener("pointerup", stop);
  });
})();


/* ------------------------------------------------- smooth scroll to funnel */

$$("[data-scroll]").forEach(function (a) {
  a.addEventListener("click", function (e) {
    e.preventDefault();
    track("cta_click", { cta: a.dataset.track || "unknown" });
    const y = $("#funnel").getBoundingClientRect().top + window.pageYOffset - 8;
    window.scrollTo({ top: y, behavior: prefersReduced() ? "auto" : "smooth" });
    const focusable = stepEl(currentStep) && stepEl(currentStep).querySelector(".card, input");
    if (focusable) setTimeout(function () { focusable.focus({ preventScroll: true }); }, 420);
  });
});

$$("[data-track]").forEach(function (el) {
  if (el.hasAttribute("data-scroll")) return;
  el.addEventListener("click", function () { track("cta_click", { cta: el.dataset.track }); });
});


/* --------------------------------------------------- exit / back-button catch */

const modal = $("#exitModal");

function openExit(reason) {
  if (exitShown || currentStep >= QUESTION_COUNT) return;   // never after the estimate
  if (currentStep === 0 && !answers.space) return;          // they never engaged
  exitShown = true;
  const left = QUESTION_COUNT - currentStep;
  $("#exitStepsLeft").textContent = left === 1 ? "one question" : left + " questions";
  modal.hidden = false;
  track("exit_intent_shown", { reason: reason, funnel_step_id: STEPS[currentStep] });
}

function closeExit() { modal.hidden = true; }

$$("[data-close-modal]").forEach(function (el) {
  el.addEventListener("click", closeExit);
});
$("#exitResume").addEventListener("click", function () {
  closeExit();
  track("exit_intent_resume", { funnel_step_id: STEPS[currentStep] });
  showStep(currentStep);
});
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && !modal.hidden) closeExit();
});

// Desktop: pointer leaves through the top of the viewport.
document.addEventListener("mouseout", function (e) {
  if (e.relatedTarget || e.clientY > 12) return;
  if (window.matchMedia("(hover: none)").matches) return;
  openExit("mouse_exit");
});

// Mobile: catch the first back press with a pushed history entry.
(function backCatch() {
  if (!window.matchMedia("(hover: none)").matches) return;
  history.pushState({ dpFunnel: true }, "");
  window.addEventListener("popstate", function () {
    if (exitShown) return;                 // let the second press actually leave
    openExit("back_button");
    history.pushState({ dpFunnel: true }, "");
  });
})();


/* ----------------------------------------------- sticky bar visibility */

(function stickyBar() {
  const bar = $("#stickybar");
  const funnel = $("#funnel");
  if (!("IntersectionObserver" in window)) return;
  // Hide the bar while the funnel itself is on screen - the CTA is right there.
  const io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (currentStep > QUESTION_COUNT) { bar.classList.add("is-hidden"); return; }
      bar.classList.toggle("is-hidden", en.isIntersecting && en.intersectionRatio > 0.35);
    });
  }, { threshold: [0, 0.35, 1] });
  io.observe(funnel);
})();


/* ------------------------------------------------------------------ init */

updateProgress();
flushRetries();
track("funnel_start", {
  utm_source: UTMS.utm_source || null,
  utm_campaign: UTMS.utm_campaign || null
});
if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") {
  console.info("%c[DP Funnel] Setup mode", "font-weight:bold",
    "\nWEBHOOK_URL is still the placeholder in funnel.js." +
    "\nThe funnel works end to end; payloads are logged here instead of being sent.");
}

// Small debugging surface, handy when wiring up GHL.
window.DPFunnel = {
  answers: answers,
  pricing: PRICING,
  preview: function () { return buildPayload("preview"); },
  calc: calculateEstimate,
  goTo: showStep
};

})();
