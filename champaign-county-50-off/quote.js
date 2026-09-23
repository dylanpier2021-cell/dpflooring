/* ==========================================================================
   DP Flooring Services - free quote funnel
   No dependencies, no build step. The visitor designs their floor, leaves
   their details, and we call them to book an in-person quote. No price is
   ever shown on this page, on purpose.
   ========================================================================== */
(function () {
"use strict";

/* ==========================================================================
   1. SETTINGS - the only things you should need to edit
   ========================================================================== */

// GoHighLevel: Automation > Workflows > new workflow > trigger "Inbound
// Webhook". Paste the URL it gives you between the quotes. Until you do, the
// form still works end to end and logs what it WOULD send to the console.
const WEBHOOK_URL = "https://services.leadconnectorhq.com/hooks/mjRUsuYleLiad81XISnz/webhook-trigger/0ccc4f13-4968-4900-850d-7b59c3b7571c";

// Meta Pixel ID (Events Manager > Data sources). Leave "" to skip loading it.
// When set: PageView on load, Lead when the form is submitted.
const META_PIXEL_ID = "2277309869728746";

// How many colors someone may favorite.
const MAX_COLORS = 3;

// Swatches shown on the color step. Files live in /assets/img/colors/, the
// same images the /colors-and-finishes/ page uses. Solid colors have no photo,
// so they are drawn from the hex value.
const COLORS = {
  flake: [
    { name: "Carbon",      file: "flake-carbon.jpg" },
    { name: "Obsidian",    file: "flake-obsidian.jpg" },
    { name: "Nightfall",   file: "flake-nightfall.jpg" },
    { name: "Denim",       file: "flake-denim.jpg" },
    { name: "Slate Blue",  file: "flake-slate-blue.jpg" },
    { name: "Evergreen",   file: "flake-evergreen.jpg" },
    { name: "Wombat",      file: "flake-wombat.jpg" },
    { name: "Domino",      file: "flake-domino.jpg" },
    { name: "Pumice",      file: "flake-pumice.jpg" },
    { name: "Saddle Tan",  file: "flake-saddle-tan.jpg" },
    { name: "Gravel",      file: "flake-gravel.jpg" },
    { name: "Creekbed",    file: "flake-creekbed.jpg" },
    { name: "Cabin Fever", file: "flake-cabin-fever.jpg" },
    { name: "Tidal Wave",  file: "flake-tidal-wave.jpg" },
    { name: "Claystone",   file: "flake-claystone.jpg" },
    { name: "Schist",      file: "flake-schist.jpg" },
    { name: "Desert",      file: "flake-desert.jpg" }
  ],
  metallic: [
    { name: "Silver Storm",   file: "metallic-silver-storm.jpg" },
    { name: "Black & Gold",   file: "metallic-black-and-gold.jpg" },
    { name: "Ocean Blue",     file: "metallic-ocean-blue.jpg" },
    { name: "Copper Bronze",  file: "metallic-copper-bronze.jpg" },
    { name: "Bourbon",        file: "metallic-bourbon.jpg" },
    { name: "Champagne",      file: "metallic-champagne.jpg" },
    { name: "Titanium Pearl", file: "metallic-titanium-pearl.jpg" },
    { name: "Emerald Isle",   file: "metallic-emerald-isle.jpg" },
    { name: "Crimson Ember",  file: "metallic-crimson-ember.jpg" },
    { name: "Amethyst",       file: "metallic-amethyst.jpg" }
  ],
  solid: [
    { name: "Light Gray",  hex: "#B9BFC7" },
    { name: "Medium Gray", hex: "#8A929C" },
    { name: "Charcoal",    hex: "#44494F" },
    { name: "Black",       hex: "#1C1E22" },
    { name: "Tan",         hex: "#C9B79A" },
    { name: "Tile Red",    hex: "#8E3B2E" },
    { name: "Navy Blue",   hex: "#22324F" },
    { name: "Hunter Green",hex: "#2F4A3A" }
  ]
};
const COLOR_IMG_BASE = "/assets/img/colors/";


/* ==========================================================================
   2. Funnel machinery
   ========================================================================== */

const STEPS = ["space", "size", "finish", "color", "condition", "timeline", "contact"];
const TOTAL = STEPS.length;

const answers = {
  space: null, size: null, finish: null, colors: [],
  condition: null, timeline: null
};

let current = 0;
let submitted = false;

const $  = (s, r) => (r || document).querySelector(s);
const $$ = (s, r) => Array.prototype.slice.call((r || document).querySelectorAll(s));
const stepEl = (name) => $('.step[data-step="' + name + '"]');


/* --------------------------------------------------------------- tracking */

window.dataLayer = window.dataLayer || [];
function track(event, data) {
  window.dataLayer.push(Object.assign({ event: event }, data || {}));
}

function loadPixel() {
  if (!META_PIXEL_ID) return;
  /* eslint-disable */
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','https://connect.facebook.net/en_US/fbevents.js');
  /* eslint-enable */
  window.fbq("init", META_PIXEL_ID);
  window.fbq("track", "PageView");
}
function pixel(event, data) {
  if (typeof window.fbq === "function") window.fbq("track", event, data || {});
}

function getUTMs() {
  const keys = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "gclid"];
  const qs = new URLSearchParams(window.location.search);
  const out = {};
  let found = false;
  keys.forEach(function (k) { if (qs.get(k)) { out[k] = qs.get(k); found = true; } });
  try {
    if (found) sessionStorage.setItem("dpq_utms", JSON.stringify(out));
    else return JSON.parse(sessionStorage.getItem("dpq_utms") || "{}");
  } catch (e) { /* storage blocked - attribution is best effort */ }
  return out;
}
const UTMS = getUTMs();


/* ---------------------------------------------------------------- webhook */

function buildPayload(contact) {
  return Object.assign({
    event: "quote_requested",
    submitted_at: new Date().toISOString(),
    page_url: window.location.href,
    referrer: document.referrer || null,
    business: "DP Flooring Services LLC",

    space: answers.space,
    size: answers.size,
    finish: answers.finish,
    colors: answers.colors.length ? answers.colors.join(", ") : "Undecided",
    condition: answers.condition,
    timeline: answers.timeline,

    utm_source:   UTMS.utm_source   || null,
    utm_medium:   UTMS.utm_medium   || null,
    utm_campaign: UTMS.utm_campaign || null,
    utm_term:     UTMS.utm_term     || null,
    utm_content:  UTMS.utm_content  || null,
    fbclid:       UTMS.fbclid       || null,
    gclid:        UTMS.gclid        || null
  }, contact);
}

// Fire-and-forget. text/plain keeps it a "simple" CORS request so the browser
// skips the preflight GHL does not answer; GHL still parses the JSON body.
function send(payload) {
  if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") {
    console.warn("[DP Quote] WEBHOOK_URL is still the placeholder. Payload that WOULD have been sent:", payload);
    showDevNote();
    return;
  }
  fetch(WEBHOOK_URL, {
    method: "POST",
    headers: { "Content-Type": "text/plain;charset=UTF-8" },
    body: JSON.stringify(payload),
    keepalive: true
  }).catch(function (err) {
    console.error("[DP Quote] webhook failed, queued for retry:", err);
    queueRetry(payload);
  });
}

function queueRetry(payload) {
  try {
    const q = JSON.parse(localStorage.getItem("dpq_retry") || "[]");
    q.push(payload);
    localStorage.setItem("dpq_retry", JSON.stringify(q.slice(-20)));
  } catch (e) { /* nothing more we can do */ }
}

function flushRetries() {
  if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") return;
  let q;
  try { q = JSON.parse(localStorage.getItem("dpq_retry") || "[]"); } catch (e) { return; }
  if (!q.length) return;
  try { localStorage.removeItem("dpq_retry"); } catch (e) {}
  q.forEach(function (p) { send(Object.assign({}, p, { retried: true })); });
}

function showDevNote() {
  if ($("#devNote")) return;
  const n = document.createElement("div");
  n.id = "devNote";
  n.className = "devnote";
  n.innerHTML = "Setup mode: no webhook connected yet. Open the console to see the payload, " +
                "then paste your URL into <code>WEBHOOK_URL</code> in quote.js.";
  document.body.appendChild(n);
  setTimeout(function () { n.remove(); }, 9000);
}


/* -------------------------------------------------------------- step flow */

function setProgress(i) {
  const done = i >= TOTAL;
  const pct = done ? 100 : Math.round(((i + 1) / TOTAL) * 100);
  $("#progressBar").style.width = pct + "%";
  $("#progressTrack").setAttribute("aria-valuenow", pct);
  $("#progressPct").textContent = pct + "%";
  $("#progressLabel").textContent = done ? "Request sent" : "Step " + (i + 1) + " of " + TOTAL;
  $("#progress").classList.toggle("is-done", done);
  $("#backBtn").hidden = i === 0 || done;
}

function show(i, dir) {
  const name = i >= TOTAL ? "done" : STEPS[i];
  if (name === "size") prepareSize();
  if (name === "color") prepareColors();
  if (name === "contact") renderSummary($("#pickedSummary"));

  $$(".step").forEach(function (s) { s.classList.remove("is-active", "is-back"); });
  const el = stepEl(name);
  if (dir === "back") el.classList.add("is-back");
  el.classList.add("is-active");
  current = i;
  setProgress(i);

  // Keep the top of the panel in view on phones without jumping if it already is.
  const top = $("#quote").getBoundingClientRect().top;
  if (top < -10 || top > window.innerHeight * 0.4) $("#quote").scrollIntoView({ block: "start" });

  const heading = $(".step__q", el);
  if (heading && dir) { heading.setAttribute("tabindex", "-1"); heading.focus({ preventScroll: true }); }
}

function next() {
  const i = current + 1;
  track("quote_step_complete", { step_number: current + 1, step_id: STEPS[current] });
  try { history.pushState({ step: i }, ""); } catch (e) {}
  show(i, "forward");
}

function back() {
  if (current === 0 || submitted) return;
  history.back();
}

window.addEventListener("popstate", function (e) {
  if (submitted) { show(TOTAL); return; }
  const i = e.state && typeof e.state.step === "number" ? e.state.step : 0;
  show(Math.min(i, TOTAL - 1), "back");
});


/* ------------------------------------------------------ single-pick cards */

$$(".cards[data-field]").forEach(function (group) {
  group.addEventListener("click", function (e) {
    const card = e.target.closest(".card");
    if (!card) return;
    const field = group.getAttribute("data-field");
    $$(".card", group).forEach(function (c) { c.classList.remove("is-selected"); });
    card.classList.add("is-selected");

    const value = card.getAttribute("data-value");
    if (field === "finish" && answers.finish !== value) answers.colors = [];
    if (field === "space" && answers.space !== value) answers.size = null;
    answers[field] = value;

    // Short pause so the tap registers visually before the screen moves.
    setTimeout(next, 230);
  });
});

function prepareSize() {
  const garage = answers.space === "Garage";
  $("#sizeGarage").hidden = !garage;
  $("#sizeArea").hidden = garage;
  $("#sizeQ").textContent = garage ? "How many cars does it fit?" : "About how big is it?";
  $$("#sizeGarage .card, #sizeArea .card").forEach(function (c) {
    c.classList.toggle("is-selected", c.getAttribute("data-value") === answers.size);
  });
}


/* ------------------------------------------------------------ color step */

function groupsFor(finish) {
  if (finish === "Flake")       return [["flake", "Flake colors", ""]];
  if (finish === "Metallic")    return [["metallic", "Metallic colors", ""]];
  if (finish === "Solid color") return [["solid", "Solid colors", "Close match shown. We bring real chips."]];
  return [["flake", "Flake", "Most popular"], ["metallic", "Metallic", "Premium"]];
}

function prepareColors() {
  const wrap = $("#colorGroups");
  const finish = answers.finish;
  if (wrap.getAttribute("data-for") !== finish) {
    wrap.setAttribute("data-for", finish);
    wrap.innerHTML = "";
    groupsFor(finish).forEach(function (g) {
      const kind = g[0];
      const sec = document.createElement("div");
      sec.className = "cgroup";
      sec.innerHTML = '<h3 class="cgroup__title">' + g[1] + (g[2] ? " <small>" + g[2] + "</small>" : "") + "</h3>";
      const grid = document.createElement("div");
      grid.className = "swatches";
      COLORS[kind].forEach(function (c) {
        const b = document.createElement("button");
        b.type = "button";
        b.className = "swatch";
        const value = (finish === "Not sure yet" ? g[1] + ": " : "") + c.name;
        b.setAttribute("data-value", value);
        b.setAttribute("aria-pressed", "false");
        b.innerHTML =
          (c.file
            ? '<img src="' + COLOR_IMG_BASE + c.file + '" alt="" width="560" height="560" loading="lazy" decoding="async">'
            : '<span class="swatch__chip" style="background:' + c.hex + '"></span>') +
          '<span class="swatch__name">' + c.name + "</span>" +
          '<span class="swatch__check" aria-hidden="true"></span>';
        grid.appendChild(b);
      });
      sec.appendChild(grid);
      wrap.appendChild(sec);
    });
    if (finish === "Metallic" || finish === "Not sure yet") {
      const note = document.createElement("p");
      note.className = "cnote";
      note.textContent = "Metallic swatches are color renderings. Every pour is one of a kind, so we bring real samples to your quote.";
      wrap.appendChild(note);
    }
  }

  const q = { "Flake": "Pick your flake colors", "Metallic": "Pick your metallic colors",
              "Solid color": "Pick your color", "Not sure yet": "Anything catch your eye?" };
  $("#colorQ").textContent = q[finish] || "Pick your colors";
  $("#colorHelp").textContent = "Tap up to " + MAX_COLORS + " favorites. We'll bring those samples when we come out.";
  syncColors();
}

function syncColors() {
  const full = answers.colors.length >= MAX_COLORS;
  $$("#colorGroups .swatch").forEach(function (s) {
    const on = answers.colors.indexOf(s.getAttribute("data-value")) !== -1;
    s.classList.toggle("is-selected", on);
    s.classList.toggle("is-maxed", full);
    s.setAttribute("aria-pressed", on ? "true" : "false");
  });
  const btn = $("#colorNext");
  const n = answers.colors.length;
  btn.disabled = n === 0;
  btn.textContent = n === 0 ? "Tap a color to continue"
                  : "Continue with " + n + " color" + (n > 1 ? "s" : "");
}

$("#colorGroups").addEventListener("click", function (e) {
  const s = e.target.closest(".swatch");
  if (!s) return;
  const v = s.getAttribute("data-value");
  const at = answers.colors.indexOf(v);
  if (at !== -1) answers.colors.splice(at, 1);
  else if (answers.colors.length < MAX_COLORS) answers.colors.push(v);
  else { answers.colors.shift(); answers.colors.push(v); }   // swap out the oldest pick
  syncColors();
});

$("#colorNext").addEventListener("click", function () { if (answers.colors.length) next(); });
$("#colorSkip").addEventListener("click", function () { answers.colors = []; syncColors(); next(); });


/* ------------------------------------------------------------- summaries */

function summaryItems() {
  return [answers.space, answers.size, answers.finish === "Not sure yet" ? "Finish: undecided" : answers.finish]
    .concat(answers.colors.length ? answers.colors : ["Colors: pick in person"])
    .filter(Boolean);
}

function renderSummary(target) {
  target.innerHTML = "";
  summaryItems().forEach(function (t) {
    const s = document.createElement("span");
    s.textContent = t;
    target.appendChild(s);
  });
}


/* --------------------------------------------------------------- contact */

const phone = $("#fPhone");
phone.addEventListener("input", function () {
  // Format as (217) 555-0134 once there are enough digits; don't fight the caret before that.
  let d = phone.value.replace(/\D/g, "");
  if (d.length === 11 && d[0] === "1") d = d.slice(1);
  if (d.length === 10) phone.value = "(" + d.slice(0, 3) + ") " + d.slice(3, 6) + "-" + d.slice(6);
});

function phoneDigits(v) {
  let d = String(v || "").replace(/\D/g, "");
  if (d.length === 11 && d[0] === "1") d = d.slice(1);
  return d;
}

function setError(input, bad) {
  const field = input.closest(".field");
  const err = $(".err", field);
  field.classList.toggle("has-error", bad);
  err.textContent = bad ? err.getAttribute("data-msg") : "";
  input.setAttribute("aria-invalid", bad ? "true" : "false");
}

function validate() {
  const checks = [
    [$("#fFirst"), function (v) { return v.trim().length > 0; }],
    [phone,        function (v) { return phoneDigits(v).length === 10; }],
    [$("#fEmail"), function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); }],
    [$("#fCity"),  function (v) { return v.trim().length > 1; }]
  ];
  let first = null;
  checks.forEach(function (c) {
    const bad = !c[1](c[0].value);
    setError(c[0], bad);
    if (bad && !first) first = c[0];
  });
  if (first) {
    first.focus();
    track("quote_validation_error", { field: first.name });
  }
  return !first;
}

$$(".fields input").forEach(function (el) {
  el.addEventListener("input", function () {
    if (el.closest(".field") && el.closest(".field").classList.contains("has-error")) setError(el, false);
  });
});

$("#quoteForm").addEventListener("submit", function (e) {
  e.preventDefault();
  if (current !== STEPS.indexOf("contact") || submitted) return;
  if (!validate()) return;

  const first = $("#fFirst").value.trim();
  const last = $("#fLast").value.trim();
  const d = phoneDigits(phone.value);
  const bestTime = $('input[name="best_time"]:checked');

  send(buildPayload({
    name: (first + " " + last).trim(),
    first_name: first,
    last_name: last || null,
    phone: "(" + d.slice(0, 3) + ") " + d.slice(3, 6) + "-" + d.slice(6),
    email: $("#fEmail").value.trim(),
    address: $("#fAddress").value.trim() || null,
    city: $("#fCity").value.trim(),
    best_time_to_call: bestTime ? bestTime.value : "Anytime",
    notes: $("#fNotes").value.trim() || null,
    sms_consent_service: $("#fSmsService").checked,
    sms_consent_marketing: $("#fSmsMarketing").checked
  }));

  submitted = true;
  track("quote_step_complete", { step_number: TOTAL, step_id: "contact" });
  track("lead_submitted", { space: answers.space, finish: answers.finish });
  pixel("Lead", { content_name: "Free quote request", content_category: answers.finish || "" });

  $("#doneTitle").textContent = "You're all set, " + first + "!";
  renderSummary($("#doneSummary"));
  try { history.replaceState({ step: TOTAL }, ""); } catch (err) {}
  show(TOTAL, "forward");
});

$("#backBtn").addEventListener("click", back);

$$("[data-track]").forEach(function (a) {
  a.addEventListener("click", function () { track("cta_click", { cta: a.getAttribute("data-track") }); });
});


/* ------------------------------------------------------------------ boot */

try { history.replaceState({ step: 0 }, ""); } catch (e) {}
loadPixel();
flushRetries();
setProgress(0);
track("quote_start", { utm_source: UTMS.utm_source || null, utm_campaign: UTMS.utm_campaign || null });

// Debug handle: DPQuote.answers, DPQuote.goTo(n)
window.DPQuote = { answers: answers, goTo: function (n) { show(n, "forward"); } };

})();
