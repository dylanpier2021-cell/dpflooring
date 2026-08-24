# Image credits and provenance

## Brand marks - client-owned

Source artwork: `DP-Flooring-Services-Transparent-Logo.png`, supplied by the client
Aug 23 2026. Everything below is derived from that one file, so re-export from it
rather than from any of the derivatives.

| File | What it is | Used by |
| --- | --- | --- |
| `logo-mark.png` | Faces + "DP" shield only, transparent. The lower "FLOORING SERVICES" wordmark is cropped off because it is unreadable at header size. | Site header |
| `logo-full.png` | Whole trimmed lockup, transparent. Dark navy wordmark - **only readable on a light ground.** | Reserved for light-background use |
| `logo-full-ondark.png` | Same lockup with the near-black "FLOORING" recolored white, matching how the client's own banner treats it. | Footer, OG card |
| `favicon.ico` (16/32/48), `favicon-32.png`, `favicon-192.png`, `favicon-512.png`, `apple-touch-icon.png` | The "DP" shield alone on a `#071229` navy rounded square. The shield is the only part of the mark that survives 16px. | Browser tabs, home screen |
| `og-image.jpg` | 1200x630 social card: the client's banner garage photo, the navy wedge from their banner, the lockup, the tagline and the phone number. | `og:image` / `twitter:image` on every page |

Brand colors sampled from the logo artwork: navy `#001030` (used as `#071229`
for large fields) and blue `#0050F0`. White on `#0050F0` measures 6.2:1, so the
brand blue is safe for button fills and for body-size text on white.

## Client-owned photography

- `photos/blue-flake-epoxy-garage-floor.jpg` - cropped from the client's own
  marketing banner (the blue/gray flake garage). Used on the Monticello and
  Champaign garage-coating pages.

## Stock photography - Pexels

Everything else in `photos/` is from **Pexels**, under the
[Pexels License](https://www.pexels.com/license/): free for commercial use, no
attribution required, no release needed. They are downloaded and served from this
repo rather than hotlinked, and each one is cropped to its slot and re-encoded at
quality 74-86 progressive JPEG.

**These are reference photos of the floor systems, not DP Flooring job photos.**
That distinction is deliberate and it is stated on the gallery page. Nothing on
this site claims a pictured floor was installed by DP Flooring. As real jobs are
photographed, drop the new file in over the old one **using the same filename**
and every page that references it updates at once - no HTML edit needed.

### Priority order for swapping in real job photos

1. `photos/hero-epoxy-floor-champaign-il-2400.jpg` + `-1280.jpg` (homepage hero)
2. The six before/after pairs on `/gallery/` - these carry the most persuasive
   weight and are the most obviously generic
3. `photos/garage-floor-coating-champaign-il.jpg` (garage service page)
4. `photos/epoxy-crew-installing-warehouse-floor.jpg` - replace with a real photo
   of Drayton and Dylan working; it is the About page's main image

Keep the replacement's aspect ratio the same as the file it replaces (most are
3:2 at 1280x854; the hero is 16:9; `applying-epoxy-floor-coating-roller.jpg` is
3:4 portrait) or the crop will shift.
