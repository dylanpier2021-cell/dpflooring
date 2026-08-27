# Getting the site indexed — Search Console & Bing

Status as of **27 Aug 2026**, checked live:

| | |
| --- | --- |
| Domain | `dpflooringservices.com` — registered, resolving |
| DNS host | **Vercel** (`ns1.vercel-dns.com` / `ns2.vercel-dns.com`) |
| Site | Live at `https://www.dpflooringservices.com`, auto-deploying from this repo |
| Canonical host | Apex `308`s to `www` — correct, one host |
| `sitemap.xml` | Live, 28 URLs, all returning `200` |
| `robots.txt` | Live, points at the sitemap |
| Verified in Search Console | **No — this is the only thing left** |

---

## 1. The DNS TXT record — you have to add this, I can't

```
google-site-verification=PVEuODtcJr65iMmLelE3F4t1rHAK1OfUMTJRlECTk1A
```

DNS lives at your registrar/DNS host, not in this repo, so nothing I commit can
create it. Your nameservers are Vercel's, so **add it in Vercel**, not at
GoDaddy/Namecheap/wherever you bought the domain — records added at the
registrar are ignored while Vercel holds the nameservers.

1. <https://vercel.com/dashboard> → your project → **Settings → Domains**
   (or **Domains** in the sidebar) → `dpflooringservices.com` → **DNS Records**
2. **Add**:
   - **Type:** `TXT`
   - **Name:** `@` (leave blank if Vercel won't accept `@` — it means the root)
   - **Value:** `google-site-verification=PVEuODtcJr65iMmLelE3F4t1rHAK1OfUMTJRlECTk1A`
   - **TTL:** default (60 is fine)
3. Save, wait ~5 minutes, then check it took:
   ```bash
   dig +short TXT dpflooringservices.com
   ```
   You want the string above in the output. Right now that command returns
   nothing — that's how I know it isn't added yet.
4. Back in Search Console, click **Verify**.

Paste the value **exactly**, including the `google-site-verification=` prefix.
Some panels add the domain to the Name field for you — if you end up with
`@.dpflooringservices.com`, clear it back to `@` or blank.

> That token is for a **Domain property**, which is the better choice: it covers
> `http`, `https`, `www` and non-`www` in one, so you never have to re-verify.
> The token is stored in `site.config.json` under `verification.googleDnsTxt`
> purely so it doesn't get lost.

### If DNS is a hassle, there's a second route

Search Console → **HTML tag** method → it gives you a *different* token. Paste
just the content string into `site.config.json`:

```json
"verification": { "googleSiteVerification": "the-token-from-google" }
```

Rebuild (`python3 tools/build.py . --prune`), push, and it renders into the
`<head>` of all 32 pages. Verified working — with a token set it emits
`<meta name="google-site-verification" content="…">` on every page; empty, it
emits nothing.

**Do not paste the DNS token there.** Google issues a separate token per method
and the DNS one will not verify as a meta tag.

---

## 2. Submit the sitemap

Once verification goes green:

1. Search Console → **Sitemaps** (left sidebar)
2. Enter `sitemap.xml` — just that, not the full URL
3. **Submit**

Expect "Success" and 28 discovered URLs. If it says "Couldn't fetch", wait an
hour and hit refresh — it's almost always Google being slow, not a broken file.

You submit once. Google re-reads it on its own afterwards, so pushing new pages
needs no further action.

### Then force the important pages in

Sitemaps get a brand-new domain crawled, but slowly. To jump the queue, use
**URL Inspection** (top search bar) → paste the URL → **Request indexing**. It's
roughly 10 a day, so spend them on:

```
https://www.dpflooringservices.com/
https://www.dpflooringservices.com/services/
https://www.dpflooringservices.com/contact/
https://www.dpflooringservices.com/epoxy-flooring-champaign-il/
https://www.dpflooringservices.com/epoxy-flooring-urbana-il/
https://www.dpflooringservices.com/epoxy-flooring-bloomington-il/
https://www.dpflooringservices.com/services/garage-floor-epoxy/
https://www.dpflooringservices.com/colors-and-finishes/
```

## 3. Bing

Bing sends less traffic but it's ten minutes of work and it feeds ChatGPT search.

<https://www.bing.com/webmasters> → **Import from Google Search Console**. That
carries the verification *and* the sitemap across in one click, so do Google
first. Failing that, add the site manually and submit
`https://www.dpflooringservices.com/sitemap.xml`. There's a
`verification.bingSiteVerification` slot in the config if you'd rather verify by
meta tag — same mechanism as Google's.

---

## 4. What's already handled

You don't need to do anything about these — they're built and live:

- `sitemap.xml` regenerates from the same registry that writes the pages, so a
  new page can't be added and forgotten. Validated: well-formed XML, 28 URLs, no
  duplicates, all absolute `https`, all one host, valid `lastmod`, priorities in
  range, every URL returns `200`, and no `noindex` page leaks in.
- `robots.txt` allows everything except `/contact/thank-you/` and points at the
  sitemap.
- `/review/` and `/feedback/` are `noindex` but deliberately **not** blocked in
  robots.txt — a page has to be crawlable for `noindex` to be seen at all.
- Canonical tags on all 32 pages; apex already redirects to `www`.
- `LocalBusiness`, `Service`, `FAQPage` and `BreadcrumbList` JSON-LD.

## 5. What to expect

A new domain takes **2–6 weeks** to show meaningful impressions and often
longer to rank for anything competitive. The location pages usually surface
first because they're the least contested. Don't judge it before week four.

The highest-leverage thing left is not on this list: **create the Google
Business Profile** and get the NAP matching `site.config.json` character for
character. For a local contractor that outranks everything technical here.
See §3 of `README.md`.
