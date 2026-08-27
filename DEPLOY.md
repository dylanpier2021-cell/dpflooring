# Deployment

This site is hosted on **Vercel**, auto-deploying from `main` on this repo.
Live at <https://www.dpflooringservices.com> (apex `308`s to `www`).

## `vercel.json`

Headers only, deliberately.

- **No `cleanUrls` / `trailingSlash`.** The live URLs already resolve correctly
  and those keys change routing — not worth risking on a production site.
- **No `Content-Security-Policy`.** The pages load the LeadConnector chat
  widget, Google Maps embeds and Google Fonts. A CSP written without a browser
  to test in would break one of them. Add one deliberately, tested, if you want.
- **No comments, and no extra top-level keys.** JSON has no comment syntax, and
  Vercel validates `vercel.json` against a strict schema — any key it does not
  recognise fails the build with *"should NOT have additional property"*. When
  that happens Vercel keeps serving the last good deployment, so the site looks
  fine and your change simply never appears. I hit exactly this on 27 Aug 2026
  by putting a `_comment` array in the file. That is why this explanation is in
  a Markdown file instead.

Vercel supplies `Strict-Transport-Security` itself; the four headers here are
the ones it does not.

## `netlify.toml`

**Inert.** It predates the move to Vercel and nothing in it is applied. Kept
only in case the site is ever moved back to Netlify.

## Checking a deploy actually landed

Vercel serves HTML from its edge cache, so a normal refresh can show you a stale
page. Bust it and compare against your local build:

```bash
curl -sS "https://www.dpflooringservices.com/?cb=$RANDOM" | grep -c leadconnectorhq
```

If the site is live but your change is missing, the build failed — check
<https://vercel.com/dashboard> → the project → **Deployments** for a red one.
A failed build is silent from the outside.
