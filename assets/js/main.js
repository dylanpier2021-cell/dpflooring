/* DP Flooring Services LLC - site behavior.
   Everything here is progressive enhancement: with JS off the nav links still
   work, the FAQ still opens (native <details>), the before/after sliders still
   show the "after" image, and the quote form still submits. */
(function () {
  "use strict";

  var doc = document;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------ mobile navigation */
  var toggle = doc.querySelector(".nav-toggle");
  var mobileNav = doc.getElementById("mobile-nav");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      mobileNav.classList.toggle("is-open", !open);
    });
    // Close when a link is tapped or Escape is pressed.
    mobileNav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("is-open");
      }
    });
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("is-open");
        toggle.focus();
      }
    });
  }

  /* ------------------------------------------------- header shadow on scroll */
  var header = doc.querySelector(".header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ------------------------------------------------ before / after comparers */
  Array.prototype.forEach.call(doc.querySelectorAll(".ba"), function (ba) {
    var range = ba.querySelector('input[type="range"]');
    if (!range) return;
    var paint = function () { ba.style.setProperty("--pos", range.value + "%"); };
    range.addEventListener("input", paint);
    paint();

    // Dragging anywhere on the image moves the divider, not just the thumb.
    var drag = function (e) {
      var r = ba.getBoundingClientRect();
      var x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
      range.value = String(Math.max(0, Math.min(100, (x / r.width) * 100)));
      paint();
    };
    var stop = function () {
      doc.removeEventListener("pointermove", drag);
      doc.removeEventListener("pointerup", stop);
    };
    ba.addEventListener("pointerdown", function (e) {
      if (e.pointerType === "mouse" && e.button !== 0) return;
      drag(e);
      doc.addEventListener("pointermove", drag);
      doc.addEventListener("pointerup", stop);
    });
  });

  /* --------------------------------------------------------- reveal on scroll */
  // The class goes on <html> only once we know the observer exists, so the
  // hiding rule can never apply without something to un-hide it.
  var revealables = doc.querySelectorAll(".reveal");
  if (revealables.length && !reduceMotion && "IntersectionObserver" in window) {
    doc.documentElement.classList.add("js-reveal");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
    Array.prototype.forEach.call(revealables, function (el, i) {
      el.style.transitionDelay = Math.min(i % 4, 3) * 70 + "ms";
      io.observe(el);
    });
    // Belt and braces: if anything is still hidden after 3s, show it.
    window.setTimeout(function () {
      Array.prototype.forEach.call(doc.querySelectorAll(".reveal:not(.is-in)"), function (el) {
        var box = el.getBoundingClientRect();
        if (box.top < window.innerHeight) el.classList.add("is-in");
      });
    }, 3000);
  }

  /* ------------------------------------------------------- quote form helper */
  var form = doc.querySelector("form[data-validate]");
  if (form) {
    var phone = form.querySelector('input[type="tel"]');
    if (phone) {
      // Format US numbers as they are typed, but never fight the user's caret
      // when they are editing mid-string.
      phone.addEventListener("input", function () {
        if (phone.selectionStart !== phone.value.length) return;
        var d = phone.value.replace(/\D/g, "").slice(0, 10);
        if (d.length > 6)      phone.value = "(" + d.slice(0, 3) + ") " + d.slice(3, 6) + "-" + d.slice(6);
        else if (d.length > 3) phone.value = "(" + d.slice(0, 3) + ") " + d.slice(3);
        else if (d.length > 0) phone.value = "(" + d;
      });
    }

    var fieldOf = function (input) { return input.closest(".field"); };

    var check = function (input) {
      var wrap = fieldOf(input);
      if (!wrap) return true;
      var ok = input.checkValidity();
      wrap.classList.toggle("is-invalid", !ok);
      var err = wrap.querySelector(".err");
      if (err && !ok) err.textContent = err.dataset.msg || input.validationMessage;
      return ok;
    };

    form.addEventListener("submit", function (e) {
      var bad = null;
      Array.prototype.forEach.call(form.querySelectorAll("input, select, textarea"), function (input) {
        if (input.type === "hidden" || input.name === "bot-field") return;
        if (!check(input) && !bad) bad = input;
      });
      if (bad) {
        e.preventDefault();
        bad.focus();
        bad.scrollIntoView({ block: "center", behavior: reduceMotion ? "auto" : "smooth" });
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
    });

    form.addEventListener("blur", function (e) {
      if (e.target.matches("input, select, textarea") && e.target.value) check(e.target);
    }, true);

    form.addEventListener("input", function (e) {
      var wrap = fieldOf(e.target);
      if (wrap && wrap.classList.contains("is-invalid")) check(e.target);
    });
  }

  /* --------------------------------------------- deep link into the quote form */
  // /contact/?type=garage preselects the floor type from a service card link.
  var typeSelect = doc.getElementById("floor-type");
  if (typeSelect) {
    var want = new URLSearchParams(window.location.search).get("type");
    if (want) {
      Array.prototype.forEach.call(typeSelect.options, function (opt) {
        if (opt.value.toLowerCase() === want.toLowerCase()) typeSelect.value = opt.value;
      });
    }
  }
})();
