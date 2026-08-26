# Review funnel — `/review` and `/feedback`

Two standalone pages for QR codes, review cards and text-to-review campaigns.
Both are `noindex` and excluded from `sitemap.xml` on purpose — they are for
customers you send there directly, not for search traffic.

| Page | What it does |
| --- | --- |
| `/review/` | Five tap-friendly stars, one screen, no scrolling. 4–5 → your Google review page. 1–3 → `/feedback/?rating=N`. |
| `/feedback/` | Private form: name, phone, what happened, how to make it right. POSTs to your webhook and shows a thank-you. |

Files: `tools/build.py` (both page builders), `assets/js/review.js` (all the
logic), and the `.util` / `.star` / `.ufield` blocks at the end of
`assets/css/styles.css`. Both pages are generated — run
`python3 tools/build.py . --prune` after any edit.

---

## 1. Paste your webhook URL

Open **`assets/js/review.js`**. It is the first thing in the file:

```js
const WEBHOOK_URL = "PASTE_GHL_WEBHOOK_HERE";
```

GHL: **Automation → Workflows → Create Workflow → Add New Trigger → Inbound
Webhook**, copy the URL, paste it between the quotes, rebuild.

Until you do, `/feedback` still works end to end — it logs the payload to the
browser console instead of sending it, so you can see exactly what GHL will get.

### Payload

```jsonc
{
  "event": "negative_feedback",
  "submitted_at": "2026-08-26T18:22:04.113Z",
  "page_url": "https://.../feedback/?rating=2&src=qr-truck",
  "business": "DP Flooring Services LLC",
  "rating": 2,                       // null if they landed without a star
  "name": "Jordan Miller",
  "phone": "(217) 555-0134",
  "what_happened": "…",
  "how_to_fix": "…",                 // null if left blank
  "utm_source": null,
  "utm_medium": null,
  "utm_campaign": null,
  "source": "qr-truck"               // from ?src= — see §3
}
```

The request goes out as `Content-Type: text/plain` so the browser skips the CORS
preflight GHL does not answer; GHL parses it as JSON regardless. The UI never
waits on the response — somebody who already had a bad experience must not then
hit an error screen. Failures queue in `localStorage` and retry next load.

**Set up a notification the moment you paste the URL.** A 1-star submission
sitting unseen in a dashboard is worse than no form at all. In GHL, add an
SMS-to-owner action on that workflow.

---

## 2. Before you print anything — read this

As built, this sends 4–5 stars to Google and 1–3 stars to a private form. That
is **review gating**, and it is against
[Google's prohibited-content policy](https://support.google.com/contributionpolicy/answer/7400114)
on discouraging or selectively soliciting reviews. It is common in the trades
and it is not illegal, but the risk is real: Google can strip reviews or
penalise the Business Profile, and the funnel is trivially visible to anyone who
taps 2 stars and watches where they land.

**The compliant version is a one-line change.** In `assets/js/review.js`:

```js
const GOOGLE_THRESHOLD = 1;   // was 4 — now everyone goes to Google
```

A middle path that keeps most of the benefit: leave the threshold at 4, but on
`/feedback` add a visible "You can also leave a public review" link to the same
Google URL. Nobody is blocked, you still catch the unhappy ones first, and the
gating claim goes away. Say the word and I'll add it.

Your call either way — I've built what you asked for and flagged the trade-off.

---

## 3. Linking a QR code or text campaign

The review URL is `https://yourdomain.com/review/`. Add `?src=` to any campaign
so you can tell where each submission came from — it flows through the star tap
into the webhook payload as `source`.

```
https://yourdomain.com/review/?src=qr-truck
https://yourdomain.com/review/?src=qr-leavebehind
https://yourdomain.com/review/?src=sms-followup
https://yourdomain.com/review/?src=invoice
```

### QR codes

Generate at [qr.io](https://qr.io) or [qrcode-monkey.com](https://www.qrcode-monkey.com)
— any generator works, the URL is plain.

- **Minimum printed size 1 inch / 25mm.** Smaller and phone cameras struggle.
- Leave a clear white margin (the "quiet zone") of about 4 modules around it.
- Test the actual print, not the screen — matte vinyl on a truck door scans very
  differently from a glossy card.
- Put readable text under it. "Scan to rate us" outperforms a bare code.

Good placements: a leave-behind card handed over at the final walkthrough, the
truck door, the back of the invoice, and a sticker inside the garage door.

### Text-to-review

Send it the day after the job, once they've parked on the floor. Short, one
link, no preamble:

> Hey [name] — Drayton at DP Flooring. Hope the new floor is treating you well.
> Mind rating us? Takes 5 seconds: https://yourdomain.com/review/?src=sms-followup

In GHL, trigger it from the job being marked complete with a 24-hour delay.
Avoid sending on a Sunday and avoid sending twice.

### What good looks like

Roughly 10–25% of texted customers tap a star. Of those, most land on 5. If more
than about 1 in 5 is landing on `/feedback`, the problem is upstream of this
page and no funnel will fix it.

---

## 4. Two things to check before launch

1. **The phone number.** Your brief for these pages said `(217) 417-5950`, but
   the live site has used `(217) 372-7770` everywhere since Aug 24, when you
   asked me to change it. I used the live one so all 32 pages match. If
   417-5950 is actually correct, change `phone` and `phoneE164` in
   `site.config.json` and rebuild — that fixes the whole site in one edit.
2. **The Google link.** `googleReviewUrl` in `site.config.json` is the URL you
   supplied and is used as-is. `googleBusinessProfile` is **inferred** from it
   by dropping `/review`, and now appears in the footer and the LocalBusiness
   `sameAs`. Open it once to confirm it lands on your profile.
