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
  marketing banner (the blue/gray flake garage). Used on the garage service page,
  the gallery, and the garage section of every location page. Note this is
  marketing artwork rather than a photograph of a completed job, so its alt says
  "Modern garage finished with a blue and gray flake epoxy floor" and does not
  place it anywhere.


## AI-generated reference images (added Aug 26 2026)

Thirteen images were generated with **OpenArt (GPT Image 2)** to fill gaps the
stock library could not cover. They are **renderings, not photographs of
completed DP Flooring jobs**, and nothing on the site claims otherwise.

| File | What it shows |
| --- | --- |
| `colors/metallic-ocean-blue.jpg` | Metallic pour, deep blue + teal + pearl |
| `colors/metallic-silver-storm.jpg` | Metallic pour, charcoal through bright silver |
| `colors/metallic-copper-bronze.jpg` | Metallic pour, copper over dark bronze |
| `colors/metallic-black-and-gold.jpg` | Metallic pour, gold veining on a black base |
| `photos/patio-flake-covered-porch.jpg` | Covered porch, grey/white flake, dusk |
| `photos/patio-flake-open-patio.jpg` | Open patio slab, tan/brown flake |
| `photos/stairs-flake-front-steps.jpg` | Front entry steps, dark grey flake |
| `photos/basement-flake-floor.jpg` | Finished basement, light grey flake |
| `photos/shop-flake-epoxy-floor.jpg` | Shop / pole barn, dark grey flake |
| `photos/metallic-epoxy-garage-floor.jpg` | Garage, blue/silver metallic |
| `photos/metallic-epoxy-lobby-floor.jpg` | Office lobby, charcoal/silver metallic |
| `photos/before-bare-garage-slab.jpg` | Two-car garage, cracked bare concrete |
| `photos/after-flake-garage-floor.jpg` | **The same garage**, flake floor installed |

The last two are a genuine matched pair: the "after" was produced image-to-image
from the "before", so the room, camera angle and lighting are unchanged and only
the floor differs. Verified numerically — the upper half of the frame differs by
3.0 mean RGB, the lower half by 25.7.

Each swatch was colour-verified after generation rather than trusted: Ocean Blue
measures blue, Copper Bronze warm, Silver Storm neutral, and Black & Gold shows
warm gold veining (187,153,96) over a black base (6,7,9).

### Client-supplied job photos

`photos/dp-job-garage-floor-1.jpg`, `-2.jpg`, `-3.jpg` are **real completed DP
Flooring jobs**, supplied by the client Aug 26 2026 (originals `2.webp`,
`4.webp`, `10.webp`). They are portrait originals, centre-cropped to the 3:2 the
gallery grid uses with the crop biased low so the floor survives. These are the
only images in the gallery captioned as completed work, and they carry the
"Completed Garage" label for exactly that reason.

### Flake swatches

The 15 files in `colors/flake-*.jpg` are the client's own product swatches
(supplied Aug 26 2026), ordered dark to light in `site.config.json`. Their
descriptions were written from measured centre-crop colour data.

## Stock photography - Pexels

Everything else in `photos/` is from **Pexels**, under the
[Pexels License](https://www.pexels.com/license/): free for commercial use, no
attribution required, no release needed. They are downloaded and served from this
repo rather than hotlinked, and each one is cropped to its slot and re-encoded at
quality 74-86 progressive JPEG.

**These are reference photos of the floor systems, not DP Flooring job photos.**
That distinction is deliberate and it is stated on the gallery page. Nothing on
this site claims a pictured floor was installed by DP Flooring.

### Descriptions must match the photograph

Every `alt` describes **what is actually in the frame**, verified against the
image. Two rules hold, and `tools/audit.py` enforces the second:

1. **No claim the photo does not support.** Earlier drafts said the flake
   close-up was "gray, white and blue" (measured saturation is 5 — it is neutral
   gray, no blue at all), that the basement shot showed a "seamless coated floor"
   (it is warm tan tile), and that the steel shop building had a "freshly coated
   concrete floor" (it is bare concrete). All corrected.
2. **No stock photo asserts a location.** An alt may *relate* an image to a town
   — "the kind of pole barn slab we coat around Mahomet, IL" — because that is
   true. It may never say "Pole barn shop near Mahomet, IL", because the photo
   was not taken there. The audit fails the build on the second form, so the
   city still appears in the alt for SEO without the site claiming something
   untrue.

Four filenames were renamed for the same reason — they described the photo
wrongly (`basement-epoxy-floor-urbana-il` → `finished-basement-lower-level`,
`shop-warehouse-epoxy-floor-central-illinois` →
`shop-building-bare-concrete-floor`, `high-gloss-epoxy-shop-floor` →
`high-gloss-epoxy-hangar-floor` (it is an aircraft hangar),
`polished-epoxy-parking-deck` → `parking-structure-gray-floor`). Three more
dropped a city they could not support (`garage-floor-coating-champaign-il` →
`garage-storage-cabinets-gray-floor`, `commercial-epoxy-floor-coating-bloomington-il`
→ `commercial-epoxy-floor-coating`, `hero-epoxy-floor-champaign-il-*` →
`hero-high-gloss-epoxy-warehouse-*`).

**When you swap in a real job photo, update its alt to match** — and once it is
genuinely your work in a named town, you can say so plainly. Add the town to the
`QUALIFIERS` exemption only if the photo really was taken there. As real jobs are
photographed, drop the new file in over the old one **using the same filename**
and every page that references it updates at once - no HTML edit needed.

### Priority order for swapping in real job photos

1. `photos/hero-high-gloss-epoxy-warehouse-2400.jpg` + `-1280.jpg` (homepage hero)
2. The six before/after pairs on `/gallery/` - these carry the most persuasive
   weight and are the most obviously generic
3. `photos/garage-storage-cabinets-gray-floor.jpg` (used on the Savoy page)
4. `photos/epoxy-crew-installing-warehouse-floor.jpg` - replace with a real photo
   of Drayton and Dylan working; it is the About page's main image

Keep the replacement's aspect ratio the same as the file it replaces (most are
3:2 at 1280x854; the hero is 16:9; `applying-epoxy-floor-coating-roller.jpg` is
3:4 portrait) or the crop will shift.
