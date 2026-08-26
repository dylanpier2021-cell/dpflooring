/* ==========================================================================
   DP Flooring Services - /review and /feedback
   One file serves both pages; each block no-ops if its markup is absent.
   ========================================================================== */
(function () {
"use strict";

/* ==========================================================================
   PASTE YOUR GOHIGHLEVEL INBOUND WEBHOOK URL HERE
   --------------------------------------------------------------------------
   GHL: Automation > Workflows > new workflow > trigger "Inbound Webhook",
   copy the URL and paste it between the quotes below.
   Until you do, /feedback still works end to end and logs the payload to the
   browser console instead of sending it.
   ========================================================================== */
const WEBHOOK_URL = "PASTE_GHL_WEBHOOK_HERE";

/* Ratings at or above this go to Google; below it go to /feedback.
   Set to 1 to send EVERYONE to Google - see README-REVIEW-FUNNEL.md on why
   you might want to. */
const GOOGLE_THRESHOLD = 4;

const $  = function (s, r) { return (r || document).querySelector(s); };
const $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ------------------------------------------------------------ /review page */
const starWrap = $("#stars");
if (starWrap) {
  const stars = $$(".star", starWrap);
  const hint  = $("#starHint");
  const GOOGLE = window.DP_REVIEW_URL || "";
  let locked = false;

  function light(n) {
    starWrap.classList.toggle("is-lit", n > 0);
    stars.forEach(function (s) {
      s.classList.toggle("is-on", Number(s.dataset.rating) <= n);
    });
  }

  stars.forEach(function (s) {
    const n = Number(s.dataset.rating);
    // hover / focus preview
    s.addEventListener("mouseenter", function () { if (!locked) light(n); });
    s.addEventListener("focus",      function () { if (!locked) light(n); });
    s.addEventListener("click", function () { choose(n); });
  });

  starWrap.addEventListener("mouseleave", function () { if (!locked) light(0); });

  // Arrow keys move between stars, matching normal rating-widget behaviour.
  starWrap.addEventListener("keydown", function (e) {
    const i = stars.indexOf(document.activeElement);
    if (i === -1) return;
    if (e.key === "ArrowRight" || e.key === "ArrowUp") {
      e.preventDefault(); stars[Math.min(i + 1, stars.length - 1)].focus();
    } else if (e.key === "ArrowLeft" || e.key === "ArrowDown") {
      e.preventDefault(); stars[Math.max(i - 1, 0)].focus();
    }
  });

  function choose(n) {
    if (locked) return;
    locked = true;
    light(n);
    starWrap.classList.add("is-sent");
    if (hint) hint.textContent = n >= GOOGLE_THRESHOLD ? "Thank you! Taking you to Google…"
                                                       : "Thank you — tell us more…";

    // Carry any tracking params through to the next page.
    const q = new URLSearchParams(window.location.search);
    q.set("rating", String(n));

    const dest = n >= GOOGLE_THRESHOLD ? GOOGLE : "/feedback/?" + q.toString();

    if (window.dataLayer) {
      window.dataLayer.push({ event: "review_star_click", rating: n,
                              destination: n >= GOOGLE_THRESHOLD ? "google" : "feedback" });
    }
    // A short beat so the star visibly fills before the page changes.
    window.setTimeout(function () { window.location.href = dest; }, reduce ? 0 : 260);
  }
}

/* ---------------------------------------------------------- /feedback page */
const form = $("#feedbackForm");
if (form) {
  const params = new URLSearchParams(window.location.search);
  const rating = params.get("rating");
  const pill   = $("#ratingPill");

  if (pill && rating && /^[1-5]$/.test(rating)) {
    pill.innerHTML = "You rated us <b>" + rating + "/5</b>";
    pill.hidden = false;
  }

  const phone = $("#fbPhone");
  phone.addEventListener("input", function () {
    if (phone.selectionStart !== phone.value.length) return;   // don't fight mid-edit
    const d = phone.value.replace(/\D/g, "").slice(0, 10);
    if (d.length > 6)      phone.value = "(" + d.slice(0,3) + ") " + d.slice(3,6) + "-" + d.slice(6);
    else if (d.length > 3) phone.value = "(" + d.slice(0,3) + ") " + d.slice(3);
    else if (d.length > 0) phone.value = "(" + d;
  });

  function check(el) {
    const wrap = el.closest(".ufield");
    if (!wrap) return true;
    let ok = el.checkValidity() && el.value.trim() !== "";
    if (ok && el === phone) {
      const d = el.value.replace(/\D/g, "");
      ok = d.length === 10 || (d.length === 11 && d.charAt(0) === "1");
    }
    wrap.classList.toggle("is-invalid", !ok);
    const err = wrap.querySelector(".uerr");
    if (err && !ok) err.textContent = err.dataset.msg || el.validationMessage;
    return ok;
  }

  $$("#feedbackForm input, #feedbackForm textarea").forEach(function (el) {
    el.addEventListener("blur", function () { if (el.value) check(el); });
    el.addEventListener("input", function () {
      const w = el.closest(".ufield");
      if (w && w.classList.contains("is-invalid")) check(el);
    });
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    let bad = null;
    [$("#fbName"), phone, $("#fbWhat")].forEach(function (el) {
      if (!check(el) && !bad) bad = el;
    });
    if (bad) {
      bad.focus();
      bad.scrollIntoView({ block: "center", behavior: reduce ? "auto" : "smooth" });
      return;
    }

    const payload = {
      event: "negative_feedback",
      submitted_at: new Date().toISOString(),
      page_url: window.location.href,
      business: "DP Flooring Services LLC",
      rating: rating && /^[1-5]$/.test(rating) ? Number(rating) : null,
      name: $("#fbName").value.trim(),
      phone: phone.value.trim(),
      what_happened: $("#fbWhat").value.trim(),
      how_to_fix: $("#fbFix").value.trim() || null,
      utm_source:   params.get("utm_source")   || null,
      utm_medium:   params.get("utm_medium")   || null,
      utm_campaign: params.get("utm_campaign") || null,
      source: params.get("src") || null          // e.g. ?src=qr-truck, ?src=sms
    };

    const btn = $("#fbSubmit");
    btn.disabled = true;
    btn.textContent = "Sending…";

    send(payload).then(function () {
      form.hidden = true;
      $("#fbThanks").hidden = false;
      $("#fbThanks").scrollIntoView({ block: "center", behavior: reduce ? "auto" : "smooth" });
      if (window.dataLayer) window.dataLayer.push({ event: "feedback_submitted", rating: payload.rating });
    });
  });
}

/**
 * Fire-and-forget POST. Never rejects and never blocks the UI - somebody who
 * has already had a bad experience must not then hit an error screen.
 *
 * text/plain keeps this a "simple" CORS request, so the browser skips the
 * preflight that GHL inbound webhooks do not answer. GHL parses it as JSON.
 * The response is opaque, so failures are queued and retried on the next load.
 */
function send(payload) {
  if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") {
    console.warn("[DP Feedback] WEBHOOK_URL is still the placeholder. Payload that " +
                 "WOULD have been sent:", payload);
    return Promise.resolve(false);
  }
  return fetch(WEBHOOK_URL, {
    method: "POST",
    headers: { "Content-Type": "text/plain;charset=UTF-8" },
    body: JSON.stringify(payload),
    keepalive: true
  }).then(function () { return true; })
    .catch(function (err) {
      console.error("[DP Feedback] webhook failed, queued for retry:", err);
      try {
        const q = JSON.parse(localStorage.getItem("dp_fb_retry") || "[]");
        q.push(payload);
        localStorage.setItem("dp_fb_retry", JSON.stringify(q.slice(-10)));
      } catch (e) { /* storage unavailable */ }
      return false;
    });
}

// Retry anything that failed on a previous visit.
(function flush() {
  if (WEBHOOK_URL === "PASTE_GHL_WEBHOOK_HERE") return;
  let q;
  try { q = JSON.parse(localStorage.getItem("dp_fb_retry") || "[]"); } catch (e) { return; }
  if (!q.length) return;
  try { localStorage.removeItem("dp_fb_retry"); } catch (e) {}
  q.forEach(function (p) {
    fetch(WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "text/plain;charset=UTF-8" },
      body: JSON.stringify(Object.assign({}, p, { retried: true })),
      keepalive: true
    }).catch(function () {});
  });
})();

})();
