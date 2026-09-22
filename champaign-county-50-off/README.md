# DP Flooring Services — 50% Off for Champaign County funnel (`/champaign-county-50-off/`)

The landing page for Meta (Facebook / Instagram) ads. The visitor designs their
floor in 7 tapped steps, leaves their details, and we call them to book an
in-person quote. **No price is shown anywhere on this page** — that's the point.
(The older `funnel/` page is the one that shows an instant price range.)

Steps, with a progress bar and a Back button (the phone's back button works too):

1. What are we coating (garage, basement, patio, shop, commercial, other)
2. How big (car count for garages, small/medium/large for everything else)
3. Finish: Flake, Metallic, Solid color, or Not sure
4. Colors: up to 3 favorites from the real swatches in `/assets/img/colors/`
   (flake, metallic, or solid chips, depending on step 3; can be skipped)
5. Concrete condition
6. Timeline
7. Contact: name, phone, email, city, best time to call, notes, SMS consent

Then a "You're all set" screen: we call you → we come out → you get your quote.

## Setup (all at the top of `quote.js`)

- `WEBHOOK_URL` — paste the GoHighLevel inbound webhook URL. Until then the
  form still works and logs the payload to the browser console.
- `META_PIXEL_ID` — paste your pixel ID to fire `PageView` on load and `Lead`
  on submit. Leave `""` if the pixel is already installed another way.
- `COLORS` — add/remove/rename swatches. Keep file names in sync with
  `/assets/img/colors/`.

## Webhook payload (one POST, `event: "quote_requested"`)

`name, first_name, last_name, phone, email, address, city, best_time_to_call,
notes, sms_consent_service, sms_consent_marketing, space, size, finish,
colors` (comma-separated, or `"Undecided"`)`, condition, timeline`, plus
`submitted_at, page_url, referrer` and `utm_* / fbclid / gclid` for ad attribution.

## Ad URL

`https://www.dpflooringservices.com/champaign-county-50-off/?utm_source=facebook&utm_medium=paid&utm_campaign=...`

The page is `noindex` so it doesn't compete with the main site in Google, and
`tools/build.py` knows to leave the folder alone.
