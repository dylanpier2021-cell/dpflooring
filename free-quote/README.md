# DP Flooring Services — Free Quote funnel (`/champaign-county-50-off/` and `/free-quote/`)

The landing page for Meta ads, rebuilt Nov 15 2026. One self-contained `index.html`
(the same file lives in `/free-quote/` and is pasted into the GHL funnel
"DP Free Quote - Book Now" as a Custom Code element).

No scrolling on phone or desktop. Header (logo + tap-to-call), trust bar, footer.
One simple question per screen (radio + NEXT bar, Coat Goats style), then the GHL calendar:

0. Within 30 miles of Champaign-Urbana? (No -> call/text screen)
1. What are we coating (Garage, Basement, Shop / Commercial, Patio / Other)
2. Size (cars for garages, small/medium/large otherwise)
3. Finish (Flake, Metallic, Solid color, Not sure yet)
4. Name + mobile -> sent to GHL right away (team gets the "call ASAP" text even if they never book)
5. GHL calendar "Free Epoxy Floor Quote" (id qvy8BDBIJjOh1Rq3LEJS) — only the next 4 open days are bookable

Photos are real DP jobs only, hosted in GHL Media Storage. No stock or AI images on this page.

Lead path: `/api/lead` (same origin) -> GHL inbound webhook, falling back to a direct
post if the function is unreachable. Config values sit at the top of the `<script>`.

The previous 7-step page is kept at `/champaign-county-50-off-old/` for reference.
