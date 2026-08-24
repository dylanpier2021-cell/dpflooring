# DP Flooring Services — Instant Estimate Funnel

A single-page, multi-step lead-qualification funnel for **DP Flooring Services LLC**
(Drayton Potthast & Dylan Pierson, Champaign County, IL).

Built for paid traffic: someone taps a Facebook ad on a phone, answers five
questions, sees a real price range, and books the on-site quote — so you walk
into every appointment already knowing what they want and roughly what it costs.

```
funnel/
├── index.html      markup: hero, 8 funnel screens, FAQ, footer, sticky bar, exit modal
├── styles.css      mobile-first, navy #071229 + electric blue #0050F0
├── funnel.js       webhook constant, pricing engine, step logic, analytics
├── README.md       this file
└── assets/
    ├── logo.png              horizontal lockup, white on transparent
    ├── before.jpg            bare concrete garage floor
    ├── after.jpg             finished blue/gray flake garage floor
    ├── finish-flake.jpg      swatches shown on the finish step
    ├── finish-solid.jpg
    └── finish-metallic.jpg
```

No build step, no dependencies, no framework. Three files and an image folder.

---

## 1. Paste your webhook URL

Open **`funnel.js`**. It is the very first thing in the file:

```js
const WEBHOOK_URL = "PASTE_GHL_WEBHOOK_HERE";
```

To get that URL in GoHighLevel: **Automation → Workflows → Create Workflow →
Add New Trigger → Inbound Webhook.** Copy the URL it generates and paste it
between the quotes.

**Until you paste it, the funnel still runs end to end.** Every payload is
logged to the browser console instead of being sent, and a small amber notice
appears on screen so you never mistake setup mode for a working webhook. Open
DevTools → Console to see exactly what GHL will receive.

### The funnel POSTs twice, on purpose

| When | `event` | Why |
| --- | --- | --- |
| They submit contact details and the estimate appears | `estimate_viewed` | Captures the lead **before** the booking step. If they see the number and bail, you still have a qualified lead with a price attached. |
| They pick a day + time window and hit Lock In | `appointment_requested` | The full record, with the booking preference added. |

Both hit the same URL with the same shape. Branch on the `event` field in your
workflow — most people route `estimate_viewed` into a nurture sequence and
`appointment_requested` straight to the calendar and an SMS.

### Payload

One flat JSON object, 31 fields, no nesting — GHL custom values map straight onto it.

```jsonc
{
  "event": "appointment_requested",
  "submitted_at": "2026-08-24T15:04:11.221Z",
  "page_url": "https://estimate.dpflooring.com/?utm_source=facebook",
  "referrer": "https://l.facebook.com/",
  "business": "DP Flooring Services LLC",

  "name": "Jordan Miller",
  "phone": "(217) 555-0134",
  "email": "jordan@example.com",
  "address": "1200 W Springfield Ave",
  "city": "Champaign",
  "sms_opt_in": true,

  "space": "Garage",
  "size": "2-car",
  "size_detail": 450,
  "size_unit": "sq_ft",          // or "steps" for a stairs job
  "finish": "Flake",
  "condition": "A few cracks or small pits",
  "timeline": "ASAP",

  "estimate_low": 2800,
  "estimate_high": 3800,
  "estimate_display": "$2,800 - $3,800",
  "estimate_at_minimum": false,  // true when the job fell under the $1,500 floor

  "preferred_day": "Tue Aug 25, 2026",
  "time_window": "Afternoon",

  "utm_source": "facebook",
  "utm_medium": "cpc",
  "utm_campaign": "garage_spring",
  "utm_term": null,
  "utm_content": null,
  "fbclid": "IwAR...",
  "gclid": null
}
```

UTMs are read from the query string on landing and kept in `sessionStorage`, so
attribution survives a refresh or a back-and-forward.

**Two implementation details worth knowing.** The request is sent with
`Content-Type: text/plain` — that keeps it a "simple" CORS request so the
browser skips the preflight that GHL inbound webhooks do not answer. GHL parses
the body as JSON regardless. And because the response is opaque, the UI never
waits on it: a lead is never trapped behind a network error. Anything that fails
is queued in `localStorage` and retried automatically on the next page load.

---

## 2. Change the prices

All of it lives in one object near the top of `funnel.js`, under the big
`PRICING ENGINE` banner. Nothing else in the file needs touching.

```js
const PRICING = {
  finishes: {
    "Flake":        { low: 6,  high: 8  },   // per sq ft
    "Solid color":  { low: 5,  high: 7  },
    "Metallic":     { low: 9,  high: 12 },
    "Not sure yet": { low: 5,  high: 12 }    // spans cheapest low to priciest high
  },
  garageSqft: { "1-car": 250, "2-car": 450, "3-car": 650, "4+ car": 850 },
  stairsPerStep: { low: 50, high: 75 },      // per step, not per sq ft
  conditionModifiers: {
    "Like new, no cracks":                   { low: 0.00, high: 0.00 },
    "A few cracks or small pits":            { low: 0.05, high: 0.05 },   // +5%
    "Major cracks, pitting, or old coating": { low: 0.15, high: 0.20 },   // +15-20%
    "Not sure":                              { low: 0.00, high: 0.20 }
  },
  minimumJob: 1500,
  roundTo: 100,
  roundOutward: true
};
```

**How a number is built:** `sq ft × finish rate`, then `× (1 + condition
modifier)`, then rounded, then floored at the minimum job.

**`roundOutward: true`** rounds the low *down* and the high *up* to the nearest
$100, so the displayed floor is never higher than the arithmetic. Set it to
`false` for plain nearest-$100 rounding on both ends.

**Minimum job.** If the *top* of the range lands at or under `minimumJob`, the
screen shows `$1,500+` instead of a range. If only the bottom is under it, the
low is lifted to $1,500 and it stays a range.

Worked examples with the shipped numbers:

| Answers | Shown |
| --- | --- |
| 2-car garage (450 sq ft), Flake, like new | $2,700 – $3,600 |
| 2-car garage, Flake, a few cracks | $2,800 – $3,800 |
| 2-car garage, Flake, major cracks | $3,100 – $4,400 |
| 1-car garage (250 sq ft), Solid, like new | $1,500 – $1,800 |
| 3-car garage (650 sq ft), Metallic, like new | $5,800 – $7,800 |
| Basement 800 sq ft, Flake, a few cracks | $5,000 – $6,800 |
| Warehouse 5,000 sq ft, Solid, like new | $25,000 – $35,000 |
| Stairs, 12 steps, Flake, like new | $1,500+ |
| Patio 100 sq ft, Solid, like new | $1,500+ |

> **One thing to watch.** "Not sure yet" on finish **and** "Not sure" on
> condition stack into a very wide range — a 4-car garage that way shows
> $4,200 – $12,300. That is honest arithmetic, but if it reads as unhelpful in
> your ads, tighten `finishes["Not sure yet"]` to the flake range
> (`{ low: 6, high: 8 }`) and it narrows immediately.

To sanity-check any edit, open the page and run `DPFunnel.calc()` in the
console after clicking through, or `DPFunnel.preview()` to see the full payload.

---

## 3. Deploy

The funnel is fully static, so anything that serves files will host it. Paths
are **relative** (`assets/logo.png`, not `/assets/logo.png`) on purpose — that
way it works identically at a domain root, in a subfolder, or pasted into GHL.

### Netlify

Drag the `funnel/` folder onto <https://app.netlify.com/drop>, and you have a
live URL in about ten seconds. For a git-connected deploy:

- **Base directory:** `funnel`
- **Publish directory:** `funnel`
- **Build command:** leave empty

Then point a subdomain at it — `estimate.yourdomain.com` is the usual choice, so
ad traffic is cleanly separated from the main site in analytics.

### Vercel

```bash
cd funnel
npx vercel --prod
```

Framework preset **Other**, no build command, output directory `.`.

### GoHighLevel custom code block

GHL funnel pages take raw HTML but do not host loose files, so inline the CSS
and JS:

1. Create a funnel step, add a **Custom Code / HTML** element, full width.
2. Paste the body of `index.html` (everything between `<body>` and `</body>`).
3. Paste the whole of `styles.css` inside a `<style>` tag above it.
4. Paste the whole of `funnel.js` inside a `<script>` tag below it —
   **including your webhook URL**.
5. Upload the six images to GHL's Media Library and swap each `assets/...` path
   for the URL GHL gives you.

Set the page background to `#071229` in GHL's own settings so the hero blends
with the page frame.

### GitHub Pages / anything else

Copy the four files and `assets/` to the web root. There is nothing to
configure.

---

## 4. Analytics — wiring it into GTM

Every step pushes to `dataLayer`, so drop-off is measurable without touching
this code again. Events, in the order a completed lead fires them:

| Event | Fires when | Useful fields |
| --- | --- | --- |
| `funnel_start` | Page load | `utm_source`, `utm_campaign` |
| `cta_click` | Any CTA tapped | `cta` (`hero_cta`, `sticky_cta`, `faq_cta`, …) |
| `funnel_step_complete` | Each of the 6 questions answered | `funnel_step_number`, `funnel_step_id`, `funnel_step_value` |
| `funnel_validation_error` | Contact or booking form rejected | `funnel_step_id`, `field` |
| `estimate_shown` | Estimate screen renders | `estimate_low`, `estimate_high`, `space`, `finish` |
| `lead_submitted` | Contact captured (first webhook) | `value`, `currency` |
| `appointment_requested` | Booking submitted (second webhook) | `preferred_day`, `time_window`, `value` |
| `exit_intent_shown` / `exit_intent_resume` | Exit modal opened / dismissed back into the funnel | `reason`, `funnel_step_id` |

In GTM, make a Custom Event trigger on `funnel_step_complete` with a Data Layer
Variable on `funnel_step_id`, and you can see exactly which question loses
people. In practice it is almost always the contact step — that is normal, and
it is why the estimate is withheld until after it.

For the Meta pixel, map `lead_submitted` → **Lead** and `appointment_requested`
→ **Schedule**, passing `value` and `currency` so the ad account can optimise
toward job size rather than raw lead count.

---

## 5. Swapping the images

Replace the file, keep the name, and every reference updates at once.

| File | What it should show | Aspect |
| --- | --- | --- |
| `logo.png` | Your logo, **white/light on transparent** — the header is navy | any, sized to 40–52px tall |
| `before.jpg` | A real bare or damaged slab | 3:2 |
| `after.jpg` | That same floor finished, if you have the pair | 3:2 |
| `finish-flake.jpg` | Close-up of a flake floor | 1:1 |
| `finish-solid.jpg` | Close-up of a solid-color floor | 1:1 |
| `finish-metallic.jpg` | Close-up of a metallic pour | 1:1 |

`before.jpg` and `after.jpg` must be the **same dimensions** or the comparison
slider will not line up. Both ship at 1200×800.

The current images are stock and client artwork, not photographs of completed DP
Flooring jobs — the alt text is written to reflect that. Once you swap in real
job photos, update the `alt` text in `index.html` to describe them, and you can
name the town plainly because it will then be true.

---

## 6. Placeholders to replace before you spend on ads

Two spots are honestly marked and should not go live as-is. Both are commented
`<!-- REPLACE -->` in `index.html`:

- **Star rating** in the hero trust row — currently reads "5.0 Google rating —
  placeholder until reviews are live". Swap in your real rating and review count,
  or delete the block. Do not ship an invented number.
- **"100+ Floors Coated"** badge under the estimate. Put the real figure in.

Everything else — name, owners, phone, email, service area, cities in the
dropdown, FAQ answers — is real and needs no editing.

---

## 7. Notes on how it behaves

- **Auto-advance** on every card step, with a ~220ms pause so the selection is
  visible before the screen moves. Size steps use a Continue button, because a
  slider has no natural "done" moment.
- **Progress bar** covers the six questions. It turns green and reads "Your
  estimate" once they are through.
- **Exit intent** is desktop mouse-leave-through-the-top, and on touch devices a
  pushed history entry that catches the first back press. It never fires before
  they have answered anything, and never after the estimate is on screen —
  interrupting someone who already got what they came for only costs you the
  booking.
- **Phone validation** accepts 10 digits, or 11 starting with a US country code,
  and formats as you type without fighting the caret mid-edit.
- **Sticky bar** hides itself while the funnel is on screen (the CTA is already
  right there) and after the booking is submitted.
- **Reduced motion** is respected throughout — animations and smooth scrolling
  are disabled for anyone who has asked for that.
- The days offered start **tomorrow**, run Monday–Saturday, and skip Sunday.

`window.DPFunnel` is exposed for debugging: `.answers`, `.pricing`, `.calc()`,
`.preview()`, and `.goTo(n)` to jump straight to a step while styling.
