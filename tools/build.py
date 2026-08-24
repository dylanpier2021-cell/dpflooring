#!/usr/bin/env python3
"""
Static site generator for DP Flooring Services LLC.

    python3 tools/build.py [outdir]      # outdir defaults to the repo root

Every .html file in the repo is written by this script from site.config.json
plus the content below. Do not hand-edit the generated HTML - rerun this
instead. No third-party dependencies; standard library only.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else ROOT
CFG = json.load(open(os.path.join(ROOT, "site.config.json"), encoding="utf-8"))

BASE = CFG["baseUrl"].rstrip("/")
NAME = CFG["legalName"]
BRAND = CFG["brand"]
PHONE = CFG["phone"]
TEL = CFG["phoneE164"]
EMAIL = CFG["email"]
OWNERS = CFG["owners"]
OWNER_PAIR = " and ".join(OWNERS)
AREA = CFG["serviceArea"]
YEAR = CFG["copyrightYear"]
IMG = "/assets/img/photos"

# --------------------------------------------------------------------- icons
I = {
"check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>',
"check_circle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
"phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
"mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
"pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
"shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>',
"home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 13 15 13 15 22"/></svg>',
"tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.6 13.4 12 22l-9-9V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5" fill="currentColor" stroke="none"/></svg>',
"ruler": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="1.5" y="7" width="21" height="10" rx="2"/><path d="M6 7v4M10 7v3M14 7v4M18 7v3"/></svg>',
"layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 2 9 5-9 5-9-5 9-5z"/><path d="m3 12 9 5 9-5"/><path d="m3 17 9 5 9-5"/></svg>',
"sparkle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 14.2 9 21 11l-6.8 2L12 19.5 9.8 13 3 11l6.8-2z"/></svg>',
"wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a4.5 4.5 0 0 0 5.9 5.9l-8.4 8.4a2.5 2.5 0 0 1-3.5-3.5z"/><path d="M14.7 6.3 18 3"/></svg>',
"truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 3h13v13H1z"/><path d="M14 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="17.5" cy="18.5" r="2"/></svg>',
"clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15.5 14"/></svg>',
"chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.5 9.1 9.1 0 0 1-3.8-.8L3 21l1.9-4.9A8.3 8.3 0 0 1 4 11.5 8.4 8.4 0 0 1 12.5 3 8.4 8.4 0 0 1 21 11.5z"/></svg>',
"grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
"menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
"close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>',
"facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.52 1.5-3.91 3.77-3.91 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.78-1.63 1.57v1.89h2.78l-.45 2.91h-2.33V22c4.78-.79 8.44-4.93 8.44-9.94z"/></svg>',
"googleBusinessProfile": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.6 12.23c0-.71-.06-1.4-.18-2.05H12v3.88h5.38a4.6 4.6 0 0 1-2 3.02v2.5h3.23c1.89-1.74 2.99-4.3 2.99-7.35z"/><path d="M12 22c2.7 0 4.96-.9 6.61-2.42l-3.23-2.5c-.9.6-2.05.95-3.38.95-2.6 0-4.8-1.75-5.59-4.1H3.07v2.58A10 10 0 0 0 12 22z"/><path d="M6.41 13.93a6 6 0 0 1 0-3.83V7.52H3.07a10 10 0 0 0 0 8.96z"/><path d="M12 5.98c1.47 0 2.79.5 3.82 1.5l2.87-2.87A9.6 9.6 0 0 0 12 2a10 10 0 0 0-8.93 5.52l3.34 2.58C7.2 7.73 9.4 5.98 12 5.98z"/></svg>',
"instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1.2" fill="currentColor" stroke="none"/></svg>',
}

LOGO_MARK = ('<img class="brand__mark" src="/assets/img/logo-mark.png" '
             'alt="{alt}" width="520" height="424" fetchpriority="high" decoding="async">')
LOGO_FULL = ('<img class="footer__logo" src="/assets/img/logo-full-ondark.png" '
             'alt="{alt}" width="900" height="965" loading="lazy" decoding="async">')
TAGLINE = "Built to last. Finished to impress."


# ------------------------------------------------------------------- content
NAV = [("Home", "/"), ("Services", "/services/"), ("About", "/about/"),
       ("Service Area", "/service-area/"), ("Gallery", "/gallery/"), ("FAQ", "/faq/")]
NAV_MOBILE = NAV + [("Contact", "/contact/")]

SERVICES = [
 dict(slug="garage-epoxy-floors", name="Garage Epoxy Floors", icon="home", type="Garage",
      img="garage-floor-coating-champaign-il.jpg",
      alt="Clean residential garage with a light gray epoxy floor coating and open overhead doors",
      short="The floor you look at every single day. Ground down to clean concrete, filled, coated and top-sealed so oil, road salt, hot tires and dropped tools stop leaving their mark.",
      long="A garage slab takes more abuse than any other floor in the house: hot tires parking on it, road salt melting off the fenders every February, oil drips, jack stands and whatever you dropped last weekend. Bare concrete soaks all of that up and never lets go. A properly installed epoxy floor seals it out, wipes clean with a mop, and makes the whole garage read as finished space instead of storage.",
      bullets=["Diamond-ground surface prep, so the coating bonds instead of peeling in a year",
               "Hot-tire resistant &mdash; no lifting or delamination where the car parks",
               "Solid color, partial flake or full-broadcast flake, in a blend you pick",
               "Most two- and three-car garages are a one- to two-day install"]),
 dict(slug="basement-floors", name="Basement Floors", icon="layers", type="Basement",
      img="basement-epoxy-floor-urbana-il.jpg",
      alt="Bright finished basement living space with clean seamless flooring and natural light",
      short="Turn a cold, dusty slab into a finished floor that mops clean. A sealed basement stops concrete dust at the source and makes the whole lower level feel like real living space.",
      long="Untreated basement concrete is a dust factory &mdash; it sheds fine powder onto everything you store down there, and it wicks moisture up from the ground underneath. Sealing it with the right epoxy system shuts both of those down. We moisture-test before we quote, because a slab with vapor drive through it needs a different system than a dry one, and putting the wrong coating on it is how basement floors fail.",
      bullets=["Moisture-tested before we quote, so the system actually matches the slab",
               "Seamless surface &mdash; nowhere for dirt, dust or mildew to collect",
               "Light-colored coatings bounce what little natural light a basement gets",
               "Ideal under home gyms, workshops, laundry rooms and finished rec space"]),
 dict(slug="commercial-industrial-coatings", name="Commercial &amp; Industrial Coatings", icon="truck", type="Commercial / industrial",
      img="commercial-epoxy-floor-coating-bloomington-il.jpg",
      alt="Large commercial building interior with a freshly coated high-gloss epoxy floor",
      short="Coatings specified for the traffic the floor actually takes &mdash; forklifts, pallet jacks, wash-downs and chemicals. We schedule around your operation, nights and weekends included.",
      long="A production floor is not a garage floor with more square footage. Forklift wheels, pallet jack casters, hot wash-downs and spilled chemistry all attack a coating differently, and the system has to be specified for whichever of those is happening on your floor. We spec the build thickness and the topcoat around your actual use, then phase the work so you are never shut down completely.",
      bullets=["High-build and chemical-resistant systems for real production environments",
               "Safety line striping, aisle marking, walkways and hazard zones",
               "Phased in sections so the operation keeps running while we work",
               "Off-hours, overnight and weekend scheduling available"]),
 dict(slug="shop-warehouse-floors", name="Shop &amp; Warehouse Floors", icon="wrench", type="Shop or warehouse",
      img="shop-warehouse-epoxy-floor-central-illinois.jpg",
      alt="Empty shop and warehouse building interior with a smooth coated concrete floor",
      short="Big square footage, done right and done on schedule. Pole barns, machine shops, body shops, ag buildings and distribution space all over Central Illinois.",
      long="Shop floors are where epoxy earns its keep. Instead of concrete that drinks up every drop of hydraulic fluid and turns gray-black over a decade, you get a surface that a push broom and a mop actually clean. It reflects your lights, so the shop is brighter without adding a single fixture, and dropped tools and welding spatter stop taking chunks out of the slab.",
      bullets=["Any size &mdash; a single service bay through a full warehouse floor",
               "Stands up to dropped tools, welding spatter, hydraulic fluid and steel wheels",
               "Sweeps and mops clean instead of absorbing every spill",
               "Non-slip aggregate available wherever the floor gets wet"]),
 dict(slug="decorative-flake-and-metallic-epoxy", name="Decorative Flake &amp; Metallic Epoxy", icon="sparkle", type="Decorative / showroom",
      img="decorative-flake-epoxy-floor-finish.jpg",
      alt="Close-up of a gray and white decorative flake epoxy floor finish",
      short="For when the floor is part of the room. Vinyl flake blends in any color mix, or a poured metallic finish with movement and depth you will never get out of a can of paint.",
      long="Flake and metallic are the finishes people stop and look at. Full-broadcast flake gives you a subtle texture underfoot, hides the small imperfections every slab has, and comes in whatever color blend you want. A metallic pour is a different animal entirely &mdash; pigments move through the resin as it levels, so no two floors are ever the same, and the depth in the finished surface looks like polished stone. Both get a clear urethane topcoat over the top.",
      bullets=["Full-broadcast flake hides slab imperfections and adds grip underfoot",
               "Metallic pours &mdash; genuinely one of a kind, every single time",
               "Pick your blend from real samples we bring to the estimate",
               "Clear urethane topcoat for UV stability and scuff resistance"]),
 dict(slug="floor-prep-and-repair", name="Floor Prep &amp; Repair", icon="ruler", type="Repair / not sure",
      img="concrete-floor-prep-and-repair.jpg",
      alt="Cracked and stained bare concrete slab of the kind that needs grinding and repair before coating",
      short="The part nobody sees, and the part everything else depends on. Cracks, pits, spalling, failing old coatings and oil-soaked concrete all get dealt with before a drop of epoxy goes down.",
      long="Almost every failed epoxy floor we get called out to look at failed for the same reason: nobody prepped the concrete. Someone rolled a coating over a sealed, dusty or oily slab and the bond never had a chance. We mechanically profile every floor we touch &mdash; no acid etching and hoping &mdash; then chase and fill the cracks, patch the pits and pull the old coating off if there is one. It is the slowest day of the job and the only one that decides how long the floor lasts.",
      bullets=["Diamond grinding or shot blasting to open up the concrete profile",
               "Crack chasing, pit filling and spall repair with structural patch material",
               "Removal of failed coatings &mdash; old paint, sealers and peeling epoxy",
               "Degreasing so oil-contaminated concrete will actually take a bond"]),
]

TRUST = [
 ("shield", "Locally owned &amp; operated", "Drayton and Dylan run the crew and work your job themselves."),
 ("tag", "Free, itemized quotes", "On-site, in writing, and no pressure to sign anything."),
 ("grid", "Any size, any type", "One-car garage through full warehouse floor."),
 ("check_circle", "Quality guaranteed", "Prepped right, coated right, and we stand behind it."),
]

PROCESS = [
 ("Free on-site quote",
  "Call or send the form and we come out, measure, look hard at the slab and talk through finishes. You get an itemized written number. No charge, no obligation, no trip fee anywhere in our service area."),
 ("Surface prep",
  "We diamond grind the concrete to open its profile, chase and fill every crack, patch the pits and degrease anything oil-soaked. This is the step that decides whether your floor lasts fifteen years or fifteen months."),
 ("Coating &amp; flake",
  "The base coat goes down, flake gets broadcast to refusal if you chose it, then the floor is scraped and vacuumed dead clean before the clear urethane topcoat goes on."),
 ("Cure &amp; hand back",
  "Light foot traffic in about a day, furniture in two to three, vehicles once it has had roughly a week. We give you the exact dates for your floor and a one-page care sheet before we leave."),
]

WHY = [
 ("layers", "Prep is most of the job",
  "We mechanically grind every floor. No acid etch, no rolling a coating over a sealed slab and hoping. It costs us a day and it buys you a decade."),
 ("ruler", "Systems matched to the room",
  "A basement with vapor drive, a shop with forklifts and a garage with hot tires need three different builds. We spec yours after we have seen the slab, not from a price list."),
 ("chat", "Straight answers on price",
  "Itemized quotes in plain English. You see what the prep costs, what the system costs and what the extras cost &mdash; and if epoxy is the wrong call for your floor, we will tell you that too."),
 ("check_circle", "We leave it clean",
  "Grinding is dusty work and we do it with vacuum shrouds. Your driveway, your shop and your basement look better when we pull out than when we pulled in."),
]

FAQS = [
 ("How long does epoxy take to cure?",
  "<p>Most floors are ready for light foot traffic about <strong>12 to 24 hours</strong> after the final coat, furniture and light use at <strong>24 to 72 hours</strong>, and vehicle traffic after roughly <strong>5 to 7 days</strong>. Full chemical cure takes about a week.</p>"
  "<p>Those windows move with temperature and humidity, so we give you the exact dates for your floor before we start. And we would much rather tell you to wait two extra days than watch tire marks press permanently into a coating that was still green.</p>"),
 ("How long does an epoxy floor last?",
  "<p>A properly prepped residential garage or basement floor commonly runs <strong>10 to 20 years</strong>. Commercial and industrial floors under forklifts, steel wheels and constant traffic are usually in the <strong>5 to 10 year</strong> range before they want a recoat &mdash; and a recoat is far cheaper than a new install, because the prep is already done.</p>"
  "<p>The single biggest factor is not the epoxy. It is the surface prep underneath it. That is exactly why we grind every floor instead of acid-etching it and hoping for the best.</p>"),
 ("Can you put epoxy over an existing floor?",
  "<p><strong>Over bare concrete &mdash; yes.</strong> That is the ideal surface, and we grind it first to open the pores so the coating can key into it.</p>"
  "<p><strong>Over an existing coating &mdash; it depends.</strong> If the old coating is sound and well bonded, we can abrade it and go over the top. If it is peeling, chipping, bubbling or flaking, it has to come off first &mdash; and we do that too.</p>"
  "<p><strong>Over tile, wood, vinyl or carpet &mdash; no.</strong> Epoxy needs concrete to bond to, so those have to be removed first. We will tell you which situation you are in at the estimate, before you have committed to anything.</p>"),
 ("How much does epoxy flooring cost?",
  "<p>Epoxy is priced by the square foot, and four things move the number:</p>"
  "<ul><li><strong>Square footage.</strong> Bigger floors cost less per foot &mdash; the setup is the same whether the room is 400 or 4,000 square feet.</li>"
  "<li><strong>Slab condition.</strong> A clean, sound slab needs a grind. One with cracks, spalling, pits or an old failing coating needs repair work first.</li>"
  "<li><strong>The system you pick.</strong> Solid color is the most economical, full flake sits in the middle, and metallic is the premium option.</li>"
  "<li><strong>Extras.</strong> Non-slip aggregate, line striping, cove base and heavier build thicknesses all add to it.</li></ul>"
  "<p>We will not quote a floor we have not seen, because a number pulled over the phone helps nobody. Call <a href=\"tel:{tel}\">{phone}</a> and we will come measure. The estimate is free, itemized and in writing, so you can see exactly what you are paying for.</p>"),
 ("Do you offer free estimates?",
  "<p>Yes &mdash; every estimate is free, on-site and carries no obligation whatsoever.</p>"
  "<p>We measure the space, check the slab for moisture and damage, bring real color and flake samples so you are not picking off a screen, and leave you with an itemized written quote. We cover Champaign-Urbana, Bloomington-Normal and everywhere within 50+ miles, and there is <strong>no trip charge anywhere in that area</strong>.</p>"),
 ("Do I have to empty the garage first?",
  "<p>Yes. The floor has to be completely clear before we can grind it &mdash; cars, shelving, the second fridge, tool boxes, all of it. Anything mounted to the wall can usually stay put.</p>"
  "<p>If you are short on space, plan on a driveway, a trailer or a corner of the yard for a couple of days. We confirm exactly how long at the estimate, so you are not living out of boxes any longer than you have to.</p>"),
 ("Can you install epoxy in the winter?",
  "<p>Often, yes. Epoxy cures by chemical reaction rather than by drying, but that reaction slows right down when it gets cold, and most systems want the <em>slab</em> above roughly 55&deg;F &mdash; not just the air.</p>"
  "<p>In an unheated Central Illinois garage in January, that usually means we bring heat in or we schedule you for a warmer stretch. Heated shops, warehouses and basements run year-round without any of that.</p>"),
 ("Is an epoxy floor slippery?",
  "<p>Clean and dry, it grips about like any smooth polished surface. Wet, it can get slick &mdash; which matters most in a garage in the winter, when you are tracking snow in off the car.</p>"
  "<p>The fix is easy: we broadcast a fine non-slip aggregate into the topcoat wherever you want it. Full flake floors already carry a bit of texture on their own. Just tell us where the floor gets wet and we will spec it that way.</p>"),
 ("How do I take care of it?",
  "<p>Sweep or dust mop it, and wet mop with warm water and a mild cleaner when it needs it. Skip citrus and vinegar-based cleaners, and skip soap-based ones that leave a film and dull the gloss.</p>"
  "<p>Wipe up gasoline, brake fluid and battery acid rather than letting them sit. Put a scrap of plywood down before you set a floor jack or jack stand on it. That is genuinely the entire maintenance list &mdash; we leave a care sheet behind with it all written out.</p>"),
]

PAIRS = [
 ("Warehouse floor", "Bare slab &rarr; high-build coating",
  "before-bare-warehouse-slab.jpg", "Empty warehouse before coating, showing bare gray concrete",
  "commercial-epoxy-floor-coating-bloomington-il.jpg", "The same style of warehouse after a high-gloss epoxy floor coating"),
 ("Shop &amp; hangar bay", "Dusty concrete &rarr; mirror-gloss finish",
  "before-bare-shop-concrete-floor.jpg", "Service shop with dusty untreated concrete floor before coating",
  "high-gloss-epoxy-shop-floor.jpg", "Hangar bay with a mirror-gloss white epoxy floor reflecting the aircraft above it"),
 ("Lower level &amp; basement", "Raw slab &rarr; sealed, bright floor",
  "before-bare-basement-slab.jpg", "Unfinished basement with a raw concrete slab and exposed joists",
  "polished-epoxy-parking-deck.jpg", "Lower level with a smooth, sealed, light gray coated floor"),
 ("Garage &amp; workshop", "Stained concrete &rarr; coated floor",
  "before-worn-garage-concrete.jpg", "Workshop with worn and stained bare concrete floor",
  "epoxy-garage-floor-interior.jpg", "Garage workshop with a clean coated gray floor and storage shelving"),
 ("Cracked &amp; pitted slab", "Repaired &rarr; full flake finish",
  "concrete-floor-prep-and-repair.jpg", "Cracked, pitted and stained concrete slab before repair",
  "decorative-flake-epoxy-floor-finish.jpg", "Gray and white full-broadcast flake epoxy finish"),
 ("Commercial deck", "Stained deck &rarr; coating with safety striping",
  "before-stained-parking-deck.jpg", "Stained and worn commercial parking deck before coating",
  "commercial-floor-coating-line-striping.jpg", "Close-up of a coated commercial floor with painted directional arrows and safety striping"),
]

SHOTS = [
 ("car-showroom-epoxy-floor.jpg", "Showroom floor under a high-gloss clear topcoat",
  "Car showroom with a high-gloss coated floor reflecting the vehicles on display"),
 ("showroom-epoxy-floor-graphics.jpg", "Coated floor with inlaid color graphics and striping",
  "Coated showroom floor with black and red inlaid graphics"),
 ("metallic-epoxy-floor-finish.jpg", "Poured metallic epoxy in an amber blend",
  "Large interior with a poured amber metallic epoxy floor and steel columns"),
]


# ------------------- per-service page metadata (titles, H1s, cost drivers) --
SERVICE_META = {
 "garage-epoxy-floors": dict(
   pair=3,
   title="Garage Floor Coating Champaign IL | Epoxy Garage Floors | DP Flooring",
   desc="Epoxy garage floor coating in Champaign-Urbana, Bloomington-Normal and Central Illinois. "
        "Diamond-ground prep, hot-tire resistant systems, flake and solid color finishes.",
   h1="Epoxy Garage Floors",
   sub_h2="A garage floor that shrugs off hot tires and road salt",
   drivers=["Square footage &mdash; a two-car garage and a four-car outbuilding price very differently per foot",
            "Slab condition &mdash; cracking, pitting and spalling at the apron all add repair time",
            "Finish &mdash; solid color, partial flake or full-broadcast flake",
            "Extras &mdash; non-slip aggregate, cove base at the walls, and a second clear coat"]),
 "basement-floors": dict(
   pair=2,
   title="Basement Floor Epoxy Coating | Champaign &amp; Bloomington IL",
   desc="Basement floor epoxy coating across Central Illinois. Seals concrete dust, resists moisture "
        "and brightens the lower level. Moisture tested before we quote.",
   h1="Basement Floor Coatings",
   sub_h2="Stop the concrete dust and get the lower level back",
   drivers=["Square footage of the finished area",
            "Moisture readings &mdash; a slab with vapor drive needs a different, costlier system",
            "How much crack, joint and patch work the slab needs first",
            "Finish choice and whether you want cove base up the walls"]),
 "commercial-industrial-coatings": dict(
   pair=5,
   title="Commercial &amp; Industrial Epoxy Flooring | Bloomington &amp; Decatur IL",
   desc="Commercial and industrial epoxy floor coatings in Central Illinois. High-build, chemical-"
        "resistant systems, safety line striping and phased off-hours installs.",
   h1="Commercial &amp; Industrial Epoxy Coatings",
   sub_h2="Specified for the traffic your floor actually takes",
   drivers=["Total square footage and how many phases the install has to run in",
            "Build thickness and chemical resistance the operation requires",
            "Prep method &mdash; grinding versus shot blasting on a heavily contaminated slab",
            "Line striping, aisle marking, non-slip aggregate and out-of-hours scheduling"]),
 "shop-warehouse-floors": dict(
   pair=0,
   title="Shop &amp; Warehouse Epoxy Floors | Pole Barn Coating IL",
   desc="Shop, warehouse and pole barn epoxy floor coatings across Central Illinois. Any size, from a "
        "single service bay to a full warehouse. Free on-site quotes - (217) 417-5950.",
   h1="Shop &amp; Warehouse Floors",
   sub_h2="Big square footage, done right and on schedule",
   drivers=["Square footage &mdash; this is where the per-foot rate drops the most",
            "Whether the slab is contaminated with oil, hydraulic fluid or an old coating",
            "Joint and crack treatment across a large floor",
            "Non-slip aggregate, striping and any traffic-marking you need"]),
 "decorative-flake-and-metallic-epoxy": dict(
   pair=4,
   title="Decorative Flake &amp; Metallic Epoxy Floors | Champaign &amp; Bloomington IL",
   desc="Decorative flake and poured metallic epoxy floors in Central Illinois. Custom color blends, "
        "one-of-a-kind metallic finishes and a clear urethane topcoat.",
   h1="Decorative Flake &amp; Metallic Epoxy",
   sub_h2="When the floor is meant to be looked at",
   drivers=["System &mdash; full flake sits mid-range, a metallic pour is the premium option",
            "Square footage and how complex the layout is to cut in",
            "Slab prep and repair before any decorative work starts",
            "Number of clear urethane topcoats over the finish"]),
 "floor-prep-and-repair": dict(
   pair=1,
   title="Concrete Floor Prep &amp; Repair | Central Illinois",
   desc="Concrete floor preparation and repair in Central Illinois: diamond grinding, shot blasting, "
        "crack chasing, spall and pit repair, failed coating removal.",
   h1="Floor Prep &amp; Repair",
   sub_h2="The step that decides how long the floor lasts",
   drivers=["Prep method &mdash; a diamond grind versus shot blasting a contaminated slab",
            "Linear feet of cracking and joints that need chasing and filling",
            "Square footage of spalling, pitting or delaminated surface to patch",
            "Whether a failed coating has to come off before anything else happens"]),
}
for _s in SERVICES:
    _m = SERVICE_META[_s["slug"]]
    _s.update({k: v for k, v in _m.items() if k != "pair"})
    _s["pair"] = PAIRS[_m["pair"]]

FLOOR_TYPES = ["Garage", "Basement", "Shop or warehouse", "Commercial / industrial",
               "Decorative / showroom", "Patio, porch or other concrete", "Repair / not sure"]

# ------------------------------------------------------------------- helpers
def fill(s):
    return s.replace("{tel}", TEL).replace("{phone}", PHONE)

def btn(label, href, kind="", icon=None, extra=""):
    ic = I[icon] if icon else ""
    cls = "btn" + (" " + kind if kind else "")
    return f'<a class="{cls}" href="{href}"{extra}>{ic}{label}</a>'

def quote_btn(kind="", label="Get a Free Quote"):
    return btn(label, "/contact/", kind)

def call_btn(kind="btn--ghostDark"):
    return btn(f"Call {PHONE}", f"tel:{TEL}", kind, "phone")

def head(title, desc, path, image="/assets/img/og-image.jpg", schema=None):
    canon = BASE + path
    ld = ""
    if schema:
        for block in (schema if isinstance(schema, list) else [schema]):
            ld += '\n<script type="application/ld+json">' + json.dumps(block, separators=(",", ":")) + "</script>"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0E1116">
<meta name="format-detection" content="telephone=yes">
<meta name="author" content="{NAME}">
<meta name="robots" content="index, follow, max-image-preview:large">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{NAME} &ndash; epoxy flooring in Champaign County and Bloomington-Normal, Illinois">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}{image}">

<link rel="icon" href="/assets/img/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/css/styles.css">{ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
"""

def header(path):
    def links(items, mobile=False):
        out = []
        for label, href in items:
            cur = ' aria-current="page"' if href == path else ""
            out.append(f'<a href="{href}"{cur}>{label}</a>')
        return "\n      ".join(out)
    logo = LOGO_MARK.format(alt=NAME + " logo")
    return f"""<div class="topbar">
  <div class="wrap">
    <span class="topbar__area">{I['pin']} Serving {AREA['shortPhrase']}</span>
    <span class="topbar__links">
      <a href="mailto:{EMAIL}">{I['mail']} {EMAIL}</a>
      <a href="tel:{TEL}">{I['phone']} {PHONE}</a>
    </span>
  </div>
</div>

<header class="header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="{NAME} &ndash; home">
      {logo}
      <span class="brand__text">
        <span class="brand__name">DP Flooring</span>
        <span class="brand__sub">Services LLC</span>
      </span>
    </a>

    <nav class="nav" aria-label="Main">
      {links(NAV)}
    </nav>
    <a class="btn btn--sm btn--onDark header__cta" href="/contact/">Get a Free Quote</a>

    <a class="header__call" href="tel:{TEL}">{I['phone']}<span>{PHONE}</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
      <span class="icon-open">{I['menu']}</span><span class="icon-close">{I['close']}</span>
    </button>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
      {links(NAV_MOBILE, True)}
      <a class="btn btn--onDark btn--block" href="/contact/">Get a Free Quote</a>
  </nav>
</header>
"""

def cta_band(title="Ready for a floor that holds up?",
             body=None, primary="Get a Free Quote"):
    body = body or (f"Free, itemized, on-site quotes across {AREA['shortPhrase']}. "
                    f"Tell us the room and roughly how big it is &mdash; we&rsquo;ll take it from there.")
    return f"""<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>{title}</h2>
      <p>{body}</p>
    </div>
    <div class="btn-row">
      {btn(primary, "/contact/")}
      {btn(PHONE, "tel:" + TEL, "btn--ghostDark", "phone")}
    </div>
  </div>
</section>
"""

def footer():
    socials = ""
    for net, label in (("facebook", "Facebook"), ("instagram", "Instagram"),
                       ("googleBusinessProfile", "Google")):
        url = CFG["social"].get(net, "")
        if url:
            socials += (f'<a href="{url}" rel="noopener noreferrer nofollow" target="_blank" '
                        f'aria-label="{NAME} on {label}">{I[net]}</a>\n        ')
    socials_block = f'<div class="socials">\n        {socials.strip()}\n      </div>' if socials else ""
    logo = LOGO_FULL.format(alt=NAME + " logo")
    svc = "\n      ".join(f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    towns = ", ".join(AREA["headline"])
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <a href="/" aria-label="{NAME} &ndash; home">{logo}</a>
        <p class="tagline">{TAGLINE}</p>
        <p>Epoxy flooring done right the first time &mdash; garages, basements, shops, warehouses and commercial floors across Central Illinois.</p>
        {socials_block}
      </div>

      <div>
        <h4>Services</h4>
        <ul>
      {svc}
        </ul>
      </div>

      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/about/">About Us</a></li>
          <li><a href="/service-area/">Service Area</a></li>
          <li><a href="/gallery/">Gallery</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/contact/">Free Quote</a></li>
        </ul>
      </div>

      <div>
        <h4>Get in touch</h4>
        <ul class="footer__nap">
          <li>{I['phone']}<a href="tel:{TEL}">{PHONE}</a></li>
          <li>{I['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{I['pin']}<span itemscope itemtype="https://schema.org/PostalAddress"><strong>{NAME}</strong><br>
            <span itemprop="addressLocality">Champaign</span>, <span itemprop="addressRegion">{CFG['basedIn']['region']}</span>
            &ndash; {CFG['basedIn']['county']}<br>Serving {towns} and every town within {AREA['radiusMiles']}+ miles.</span></li>
        </ul>
      </div>
    </div>

    <div class="footer__bar">
      <p>&copy; {YEAR} {NAME}. All rights reserved.</p>
      <p>Owned and operated by {OWNER_PAIR}.</p>
    </div>
  </div>
</footer>

<div class="callbar">
  <a class="btn btn--onDark" href="tel:{TEL}">{I['phone']}Call Now</a>
  <a class="btn btn--ghostDark" href="/contact/">Free Quote</a>
</div>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""

def crumbs(trail):
    """trail: list of (label, href|None)"""
    items = []
    for label, href in trail:
        if href:
            items.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            items.append(f'<li><span aria-current="page">{label}</span></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'

def crumb_schema(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": label.replace("&amp;", "&"),
                 "item": BASE + (href or "")}
                for i, (label, href) in enumerate(trail)]}

def pagehead(h1, sub, trail):
    return f"""<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <h1>{h1}</h1>
      <p class="lede">{sub}</p>
      <div class="btn-row">
        {quote_btn("btn--onDark")}
        {call_btn()}
      </div>
    </div>
  </div>
</section>
"""

def faq_html(items, dark=False):
    out = ['<div class="faq">']
    for q, a in items:
        out.append(f'  <details>\n    <summary>{q}</summary>\n    <div class="faq__a">{fill(a)}</div>\n  </details>')
    out.append("</div>")
    return "\n".join(out)

def ba_html(pair, lazy=True):
    title, sub, bimg, balt, aimg, aalt = pair
    ld = ' loading="lazy" decoding="async"' if lazy else ' decoding="async"'
    return f"""<figure class="ba-item reveal">
  <div class="ba">
    <img src="{IMG}/{bimg}" alt="{balt}" width="1280" height="854"{ld}>
    <img class="ba__after" src="{IMG}/{aimg}" alt="{aalt}" width="1280" height="854"{ld}>
    <span class="ba__label ba__label--before">Before</span>
    <span class="ba__label ba__label--after">After</span>
    <input type="range" min="0" max="100" value="50" step="0.1"
           aria-label="{title.replace('&amp;', 'and')}: drag to compare before and after">
    <span class="ba__handle" aria-hidden="true"></span>
  </div>
  <figcaption class="ba__caption"><b>{title}</b><span>{sub}</span></figcaption>
</figure>"""

def local_business():
    return {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": BASE + "/#business",
        "name": NAME,
        "alternateName": BRAND,
        "url": BASE + "/",
        "telephone": TEL,
        "email": EMAIL,
        "image": BASE + "/assets/img/og-image.jpg",
        "logo": BASE + "/assets/img/favicon-512.png",
        "description": ("Epoxy flooring contractor serving Champaign-Urbana, Bloomington-Normal and "
                        "Central Illinois. Garage floor coatings, basement floors, commercial and "
                        "industrial epoxy, shop and warehouse floors, decorative flake and metallic "
                        "epoxy, plus concrete floor prep and repair."),
        "priceRange": "$$",
        "founder": [{"@type": "Person", "name": o} for o in OWNERS],
        "address": {"@type": "PostalAddress", "addressLocality": "Champaign",
                    "addressRegion": CFG["basedIn"]["region"], "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": t + ", IL"} for t in AREA["headline"]],
        "serviceArea": {"@type": "GeoCircle",
                        "geoMidpoint": {"@type": "GeoCoordinates",
                                        "latitude": CFG["geo"]["lat"], "longitude": CFG["geo"]["lng"]},
                        "geoRadius": str(AREA["radiusMeters"])},
        "sameAs": [u for k, u in CFG["social"].items()
                   if not k.startswith("_") and isinstance(u, str) and u.startswith("http")],
        "knowsAbout": ["Epoxy flooring", "Garage floor coating", "Concrete floor coating",
                       "Metallic epoxy", "Decorative flake flooring", "Concrete surface preparation"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Epoxy flooring services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": s["name"].replace("&amp;", "&"),
                    "description": s["short"].replace("&mdash;", "-").replace("&rsquo;", "'")}}
                for s in SERVICES]},
    }

# --------------------------------------------------------------- text helpers
import html as _html
import re as _re
from urllib.parse import quote as _q

def plain(s):
    """HTML fragment -> plain text, for JSON-LD and alt attributes."""
    s = _re.sub(r"<[^>]+>", " ", fill(s))
    return _re.sub(r"\s+", " ", _html.unescape(s)).strip()

def write(relpath, content):
    dest = os.path.join(OUT, relpath)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(content)
    return dest

# ===================================================================== HOME ==
def page_home():
    path = "/"
    title = "Epoxy Flooring Champaign IL &amp; Bloomington | DP Flooring Services"
    desc = ("Durable, high-gloss epoxy floors in Champaign-Urbana, Bloomington-Normal and Central "
            "Illinois. Garages, basements, shops, commercial. Free quotes - (217) 417-5950.")

    cards = "\n".join(f"""      <article class="card reveal">
        <div class="card__media">
          <img src="{IMG}/{s['img']}" alt="{s['alt']}" width="1280" height="854" loading="lazy" decoding="async">
        </div>
        <div class="card__body">
          <h3>{s['name']}</h3>
          <p>{s['short']}</p>
          <a class="arrow-link" href="/services/{s['slug']}/">Read more <span aria-hidden="true">&rarr;</span></a>
        </div>
      </article>""" for s in SERVICES)

    trust_items = "\n".join(
        f'        <li>{I[i]}<div><b>{t}</b><span>{d}</span></div></li>' for i, t, d in TRUST)

    why_items = "\n".join(
        f'        <li>{I[i]}<div><b>{t}</b><span>{d}</span></div></li>' for i, t, d in WHY)

    steps = "\n".join(f"""        <div class="step reveal">
          <h3>{t}</h3>
          <p>{d}</p>
        </div>""" for t, d in PROCESS)

    chips = "\n".join(f'        <li><span class="chip chip--hot">{t}</span></li>' for t in AREA["headline"])

    teaser = "\n".join(f"""      <figure class="shot reveal">
        <img src="{IMG}/{f}" alt="{a}" width="1280" height="854" loading="lazy" decoding="async">
        <figcaption>{c}</figcaption>
      </figure>""" for f, c, a in SHOTS)

    schema = [local_business(), {
        "@context": "https://schema.org", "@type": "WebSite",
        "name": NAME, "url": BASE + "/",
        "publisher": {"@id": BASE + "/#business"}}]

    return head(title, desc, path, schema=schema) + header(path) + f"""
<main id="main">

<section class="hero">
  <div class="hero__media">
    <img src="{IMG}/hero-epoxy-floor-champaign-il-1280.jpg"
         srcset="{IMG}/hero-epoxy-floor-champaign-il-1280.jpg 1280w, {IMG}/hero-epoxy-floor-champaign-il-2400.jpg 2400w"
         sizes="100vw" width="2400" height="1350" fetchpriority="high" decoding="async"
         alt="Large commercial interior with a freshly installed high-gloss epoxy floor reflecting the overhead lights">
  </div>
  <div class="wrap">
    <div class="hero__inner">
      <p class="hero__badge"><span class="dot"></span> Locally owned in <b>{CFG['basedIn']['county']}, Illinois</b></p>
      <h1>Durable, High-Gloss <span class="hl">Epoxy Floors</span> Built to Last</h1>
      <p class="tagline" style="margin-top:.65rem">{TAGLINE}</p>
      <p class="hero__sub">
        Professional epoxy flooring for garages, basements, shops, warehouses and commercial spaces
        across <strong>Champaign County</strong> and <strong>Bloomington-Normal</strong> &mdash; any size, any type.
      </p>
      <div class="btn-row">
        {quote_btn("btn--onDark btn--lg")}
        {btn("Call " + PHONE, "tel:" + TEL, "btn--ghostDark btn--lg", "phone")}
      </div>
      <div class="hero__trust">
        <ul>
{trust_items}
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="trustbar">
  <div class="wrap">
    <ul>
      <li>{I['pin']}<div><b>50+ mile radius</b>Champaign-Urbana to Bloomington-Normal</div></li>
      <li>{I['ruler']}<div><b>Any square footage</b>Single bay through full warehouse</div></li>
      <li>{I['clock']}<div><b>Most garages: 1&ndash;2 days</b>Cars back in under a week</div></li>
      <li>{I['tag']}<div><b>No trip charge</b>Free on-site estimates, in writing</div></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center">
      <p class="eyebrow">What we do</p>
      <h2>Epoxy flooring, any size and any type</h2>
      <p class="lede">Six services, one standard. Whether it is a one-car garage in Savoy or forty
      thousand square feet outside Bloomington, the prep is the same and so is the finish quality.</p>
    </div>
    <div class="grid grid--3">
{cards}
    </div>
    <div class="btn-row btn-row--center" style="margin-top:2.75rem">
      {btn("See all services", "/services/", "btn--ghost")}
      {quote_btn()}
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="split split--wide-text">
      <div>
        <p class="eyebrow">Why DP Flooring</p>
        <h2>Most epoxy floors don&rsquo;t fail. They were never prepped.</h2>
        <p class="lede">Almost every peeling, lifting, flaking floor we get called out to look at has the
        same story behind it: someone rolled a coating over a sealed or oily slab and the bond never had
        a chance. We do the unglamorous part properly, and the floor takes care of itself after that.</p>
        <ul class="features" style="margin-top:2rem">
{why_items}
        </ul>
        <div class="btn-row" style="margin-top:2.25rem">
          {btn("Meet Drayton &amp; Dylan", "/about/", "btn--onDark")}
        </div>
      </div>
      <div class="split__media">
        <img src="{IMG}/epoxy-crew-installing-warehouse-floor.jpg"
             alt="Crew in high-visibility vests installing an epoxy floor coating across a prepared concrete slab"
             width="1280" height="960" loading="lazy" decoding="async">
        <div class="stat-strip">
          <div><b>50+</b><span>Mile radius</span></div>
          <div><b>1&ndash;2</b><span>Days, most garages</span></div>
          <div><b>100%</b><span>Free quotes</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How it goes</p>
      <h2>Four steps, no surprises</h2>
      <p class="lede">You will know the schedule, the price and the cure dates before we start grinding.</p>
    </div>
    <div class="grid grid--2 steps">
{steps}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center">
      <p class="eyebrow">Gallery</p>
      <h2>What a proper epoxy floor looks like</h2>
      <p class="lede">Solid color, full flake, metallic and high-build commercial systems &mdash;
      and what surface prep turns a tired slab into.</p>
    </div>
    <div class="gallery-grid">
{teaser}
    </div>
    <div class="btn-row btn-row--center" style="margin-top:2.5rem">
      {btn("See before &amp; after comparisons", "/gallery/", "btn--ghost")}
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Service area</p>
      <h2>Central Illinois, 50+ miles in every direction</h2>
      <p class="lede">Based in {CFG['basedIn']['county']} and out on jobs from Danville to Decatur and
      Bloomington-Normal to Tuscola. No trip charge anywhere in the area.</p>
    </div>
    <ul class="chips">
{chips}
      <li><span class="chip">&hellip; and every town in between</span></li>
    </ul>
    <ul class="link-grid link-grid--3" style="margin-top:2rem">
{loc_links(limit=6, dark=True)}
    </ul>
    <div class="btn-row" style="margin-top:2.25rem">
      {btn("See the full service area", "/service-area/", "btn--onDark")}
      {call_btn()}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Common questions</p>
      <h2>Straight answers, before you call</h2>
    </div>
    {faq_html(FAQS[:5])}
    <div class="btn-row btn-row--center" style="margin-top:2.5rem">
      {btn("Read all FAQs", "/faq/", "btn--ghost")}
    </div>
  </div>
</section>

{cta_band()}
</main>
""" + footer()

# ============================================================ SERVICES HUB ==
def page_services():
    path = "/services/"
    trail = [("Home", "/"), ("Services", None)]
    title = "Epoxy Flooring Services | Garage, Basement &amp; Commercial Floors"
    desc = ("Epoxy flooring services in Central Illinois: garage floor coatings, basement floors, "
            "commercial and industrial epoxy, shop and warehouse floors, prep and repair.")

    cards = "\n".join(f"""      <article class="card reveal">
        <div class="card__media">
          <img src="{IMG}/{s['img']}" alt="{s['alt']}" width="1280" height="854" loading="lazy" decoding="async">
        </div>
        <div class="card__body">
          <h3><a href="/services/{s['slug']}/" style="text-decoration:none;color:inherit">{s['name']}</a></h3>
          <p>{s['short']}</p>
          <a class="arrow-link" href="/services/{s['slug']}/">See {plain(s['name']).lower()} <span aria-hidden="true">&rarr;</span></a>
        </div>
      </article>""" for s in SERVICES)

    schema = [crumb_schema(trail), {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": "Epoxy flooring services",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": plain(s["name"]),
             "url": BASE + "/services/" + s["slug"] + "/"}
            for i, s in enumerate(SERVICES)]}]

    return head(title, desc, path, schema=schema) + header(path) + pagehead(
        "Epoxy flooring for every kind of floor",
        "Six services, one standard. Garages, basements, shops, warehouses, commercial and industrial "
        "space &mdash; installed across Champaign-Urbana, Bloomington-Normal and 50+ miles around.",
        trail) + f"""
<main id="main">
<section class="section">
  <div class="wrap">
    <div class="grid grid--3">
{cards}
    </div>
  </div>
</section>

<section class="section section--dark section--tight">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Where we install</p>
      <h2>Pick your town</h2>
      <p class="lede">Every service above is available across the whole {AREA['radiusMiles']}+ mile service area.</p>
    </div>
    <ul class="link-grid link-grid--3">
{loc_links(dark=True)}
    </ul>
  </div>
</section>

{cta_band("Not sure which system your floor needs?",
          "Tell us the room, roughly the square footage and what happens on that floor. "
          "We&rsquo;ll come look at the slab and spec it properly &mdash; free, and in writing.")}
</main>
""" + footer()

# ======================================================= SERVICE PAGE (one) ==
def page_service(s):
    path = f"/services/{s['slug']}/"
    trail = [("Home", "/"), ("Services", "/services/"), (plain(s["name"]), None)]
    title = s["title"]
    desc = s["desc"]

    bullets = "\n".join(f'            <li>{I["check"]}<span>{b}</span></li>' for b in s["bullets"])
    drivers = "\n".join(f'        <li>{I["check"]}<span>{d}</span></li>' for d in s["drivers"])
    pair = ba_html(s["pair"], lazy=False)
    price = CFG.get("pricing", {}).get(s["slug"], "")
    if price:
        price_block = (f'<p class="price-figure">{price}</p>'
                       f'<p class="price-unit">Installed, per square foot. Final number comes from the on-site quote.</p>')
    else:
        price_block = ('<p>Epoxy is priced by the square foot, and we will not quote a floor we have not '
                       'seen &mdash; a number pulled over the phone helps nobody. Here is what actually moves it:</p>')

    schema = [crumb_schema(trail), {
        "@context": "https://schema.org", "@type": "Service",
        "@id": BASE + path + "#service",
        "name": plain(s["name"]), "serviceType": plain(s["name"]),
        "description": plain(s["short"]), "url": BASE + path,
        "provider": {"@id": BASE + "/#business"},
        "areaServed": [{"@type": "City", "name": t + ", IL"} for t in AREA["headline"]],
        "offers": {"@type": "Offer", "priceCurrency": "USD",
                   "availability": "https://schema.org/InStock",
                   "url": BASE + "/contact/"}}]

    return head(title, desc, path, schema=schema) + header("/services/") + f"""
<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <p class="tagline">{TAGLINE}</p>
      <h1>{s['h1']}</h1>
      <p class="lede">{s['short']}</p>
      <div class="btn-row">
        <a class="btn btn--onDark" href="/contact/?type={_q(plain(s['type']))}">Get a Free Quote</a>
        {call_btn()}
      </div>
    </div>
  </div>
</section>

<main id="main">

<section class="section">
  <div class="wrap">
    <div class="split split--wide-text">
      <div>
        <p class="eyebrow">What you get</p>
        <h2>{s['sub_h2']}</h2>
        <p>{s['long']}</p>
        <ul class="checks">
{bullets}
        </ul>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/{s['img']}" alt="{s['alt']}" width="1280" height="854" decoding="async">
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Before &amp; after</p>
      <h2>What prep and a proper system do</h2>
      <p class="lede">Drag the divider. Left is the kind of slab we start with, right is the finish.</p>
    </div>
    <div style="max-width:760px">
{pair}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="price-panel">
        <p class="eyebrow">What it costs</p>
        <h3>Pricing for {plain(s['name']).lower()}</h3>
        {price_block}
        <ul class="price-drivers">
{drivers}
        </ul>
        <div class="btn-row" style="margin-top:1.5rem">
          <a class="btn" href="/contact/?type={_q(plain(s['type']))}">Get my free quote</a>
          {btn(PHONE, "tel:" + TEL, "btn--ghost", "phone")}
        </div>
      </div>
      <div>
        <p class="eyebrow">Where we do it</p>
        <h2 style="font-size:clamp(1.5rem,3vw,2.1rem)">{plain(s['name'])} near you</h2>
        <p>Available everywhere in our {AREA['radiusMiles']}+ mile service area. These are the towns we
        work in most often &mdash; if yours is not listed, call anyway.</p>
        <ul class="link-grid" style="margin-top:1.25rem">
{loc_links(limit=8)}
        </ul>
        <p style="margin-top:1.1rem"><a class="arrow-link" href="/service-area/">Full service area <span aria-hidden="true">&rarr;</span></a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark section--tight">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Related</p>
      <h2 style="font-size:clamp(1.4rem,3vw,2rem)">Other services</h2>
    </div>
    <ul class="link-grid link-grid--3">
{svc_links(exclude=s['slug'], dark=True)}
    </ul>
  </div>
</section>

{cta_band("Ready to quote " + plain(s['name']).lower() + "?",
          "Free, itemized, on-site quotes anywhere in the service area &mdash; and no trip charge to come look.")}
</main>
""" + footer()

# ================================================================ LOCATIONS ==
LOCATIONS = [
 dict(slug="epoxy-flooring-champaign-il", city="Champaign", county="Champaign County",
      service="Epoxy Flooring", kw="epoxy flooring Champaign IL",
      img="hero-epoxy-floor-champaign-il-1280.jpg",
      alt="High-gloss epoxy floor coating installed for a commercial building in Champaign, IL",
      title="Epoxy Flooring Champaign IL | Garage &amp; Commercial Floor Coating",
      desc="Epoxy flooring in Champaign, IL. Garage floor coatings, basement, shop and commercial epoxy from a locally owned Champaign County installer. Free quotes.",
      h1="Epoxy Flooring in Champaign, IL",
      intro="Champaign is home base. {name} is owned and run by {owners}, and most of our jobs are inside a twenty-minute drive of here &mdash; which means when you have a question about your floor six months from now, we are not three hours away.",
      local="Champaign gives us two very different kinds of slab. Near campus and through the older neighborhoods off Church and University, we are usually looking at mid-century concrete with a few decades of cracking, oil and settling in it &mdash; that floor needs chasing, filling and patching before anything gets coated. Out on the newer southwest side, the three-car attached garages are typically clean, sound slabs that need a proper diamond grind and nothing more. Add the commercial and light-industrial space north of I-74 and around the Market Street corridor, and there is very little we have not already had to spec for in this town.",
      nearby=["Urbana", "Savoy", "Mahomet", "Rantoul"]),

 dict(slug="epoxy-flooring-urbana-il", city="Urbana", county="Champaign County",
      service="Epoxy Flooring", kw="epoxy flooring Urbana IL",
      img="epoxy-garage-floor-interior.jpg",
      alt="Coated garage floor in an Urbana, IL detached garage with storage shelving",
      title="Epoxy Flooring Urbana IL | Garage &amp; Basement Floor Coating",
      desc="Epoxy flooring in Urbana, IL. Garage floor coatings, basement floors and commercial epoxy from a locally owned Champaign County installer. Free quotes.",
      h1="Epoxy Flooring in Urbana, IL",
      intro="Urbana is about ten minutes from where we keep the equipment, so it is one of the easiest towns in the county for us to schedule &mdash; including the small jobs a lot of contractors will not drive out for.",
      local="Urbana has an older housing stock than most of the county, and that shows up in the concrete. A lot of what we coat here is a detached garage built in the 1950s or 60s: a thinner slab, some spalling near the door where forty winters of road salt have done their work, and hairline cracking through the middle. None of that rules out epoxy &mdash; it just means the repair stage is real work rather than a formality. On the commercial side, the medical and office buildings around the Carle campus and the businesses downtown tend to want low-odour scheduling and overnight turnarounds, which we can do.",
      nearby=["Champaign", "St. Joseph", "Savoy", "Rantoul"]),

 dict(slug="epoxy-flooring-savoy-il", city="Savoy", county="Champaign County",
      service="Epoxy Flooring", kw="epoxy flooring Savoy IL",
      img="garage-floor-coating-champaign-il.jpg",
      alt="Clean three-car garage in Savoy, IL with a light gray epoxy floor coating",
      title="Epoxy Flooring Savoy IL | Garage Floor Coating &amp; Basement Floors",
      desc="Epoxy flooring in Savoy, IL. Garage floor coatings, basement floors and shop epoxy from locally owned installers based in Champaign County. Free quotes - (217) 417-5950.",
      h1="Epoxy Flooring in Savoy, IL",
      intro="Savoy sits ten minutes south of Champaign, and it is one of our favorite places to work &mdash; largely because of what the concrete under the village looks like.",
      local="Most of Savoy&rsquo;s residential growth is recent, which means the garages here are generally newer, bigger and sitting on sound, well-poured slabs. That is the ideal starting point for epoxy: little to no crack repair, a straightforward diamond grind, and the whole budget goes into the coating rather than into fixing the concrete. Three-car attached garages are common in the subdivisions off Prospect and Dunlap, and a full-flake floor across that much square footage genuinely changes how the space feels. We also cover the commercial and hangar-adjacent buildings out toward Willard Airport.",
      nearby=["Champaign", "Tolono", "Urbana", "Monticello"]),

 dict(slug="epoxy-flooring-mahomet-il", city="Mahomet", county="Champaign County",
      service="Epoxy Flooring", kw="epoxy flooring Mahomet IL",
      img="shop-warehouse-epoxy-floor-central-illinois.jpg",
      alt="Pole barn shop near Mahomet, IL with a coated concrete floor",
      title="Epoxy Flooring Mahomet IL | Garage, Shop &amp; Pole Barn Floors",
      desc="Epoxy flooring in Mahomet, IL. Garage floor coatings, pole barn and shop floors, and basement epoxy from a locally owned Champaign County installer.",
      h1="Epoxy Flooring in Mahomet, IL",
      intro="Mahomet is a straight fifteen-minute run west on I-74 for us, and it has grown fast enough that we are out there most months.",
      local="What sets Mahomet apart is the outbuildings. Lots here run bigger than they do in town, so alongside the attached garages in the newer subdivisions we spend a lot of time in detached shops, pole barns and machine sheds &mdash; and those bring their own considerations. A pole barn slab is often poured later, thinner or without a vapor barrier under it, so moisture testing genuinely matters before we pick a system. Get that right and a coated barn floor is transformative: it stops the concrete dust, it reflects your lights, and you can actually sweep it out.",
      nearby=["Champaign", "Fisher", "Urbana", "Monticello"]),

 dict(slug="epoxy-flooring-rantoul-il", city="Rantoul", county="Champaign County",
      service="Epoxy Flooring", kw="epoxy flooring Rantoul IL",
      img="high-gloss-epoxy-shop-floor.jpg",
      alt="Large hangar-style building in Rantoul, IL with a high-gloss epoxy floor",
      title="Epoxy Flooring Rantoul IL | Hangar, Shop &amp; Garage Floor Coating",
      desc="Epoxy flooring in Rantoul, IL. Hangar and shop floor coatings, commercial epoxy and residential garage floors from a locally owned Champaign County installer. (217) 417-5950.",
      h1="Epoxy Flooring in Rantoul, IL",
      intro="Rantoul is about twenty minutes north of Champaign on I-57, and it has a building stock unlike anywhere else in the county.",
      local="Because of the old Chanute air base, Rantoul carries far more hangar, warehouse and institutional square footage than a town its size normally would &mdash; and a lot of those floors are big, old, and have been sitting under decades of traffic. Those are exactly the slabs where surface prep is not optional: shot blasting or heavy grinding, serious crack and joint work, and a high-build system that can take the abuse. On the residential side, Rantoul&rsquo;s mid-century homes come with the same thinner, salt-worn garage slabs we see in Urbana, and they respond well to a proper repair-and-coat.",
      nearby=["Champaign", "Paxton", "Gibson City", "Urbana"]),

 dict(slug="epoxy-flooring-bloomington-il", city="Bloomington", county="McLean County",
      service="Epoxy Flooring", kw="epoxy flooring Bloomington IL",
      img="commercial-epoxy-floor-coating-bloomington-il.jpg",
      alt="Commercial building in Bloomington, IL with a freshly coated high-gloss epoxy floor",
      title="Epoxy Flooring Bloomington IL | Commercial &amp; Garage Floor Coating",
      desc="Epoxy flooring in Bloomington, IL. Commercial and industrial coatings, warehouse floors and residential garage epoxy across McLean County. Free quotes - (217) 417-5950.",
      h1="Epoxy Flooring in Bloomington, IL",
      intro="Bloomington is our second home market. It is roughly a fifty-minute drive up I-74 from Champaign County, and there is no trip charge for it &mdash; we quote and schedule McLean County exactly the way we do our own back yard.",
      local="Bloomington leans commercial for us. The corporate and office employers here keep a lot of light-industrial, service and back-of-house square footage in play, and those floors almost always need to be coated in phases and outside business hours &mdash; which is how we prefer to run them anyway. Residentially, the established neighborhoods on the east and south sides have the classic mid-century garage slab, while the newer builds toward the edges are usually clean pours that only want a grind. If you are weighing a full flake floor against solid color, this is a market where we bring plenty of samples.",
      nearby=["Normal", "Downs", "Le Roy", "Heyworth"]),

 dict(slug="epoxy-flooring-normal-il", city="Normal", county="McLean County",
      service="Epoxy Flooring", kw="epoxy flooring Normal IL",
      img="polished-epoxy-parking-deck.jpg",
      alt="Coated concrete floor in a Normal, IL commercial lower level",
      title="Epoxy Flooring Normal IL | Garage, Basement &amp; Commercial Floors",
      desc="Epoxy flooring in Normal, IL. Garage floor coatings, basement floors and commercial epoxy across McLean County from a locally owned installer. Free quotes - (217) 417-5950.",
      h1="Epoxy Flooring in Normal, IL",
      intro="Normal sits right next to Bloomington, so we cover it on the same runs &mdash; and like the rest of McLean County, there is no trip charge to come out and quote.",
      local="Normal splits neatly for us. Around Illinois State and Uptown there is a steady stream of rental, retail and small-commercial floors where the priority is a fast turnaround between tenants and a surface that mops clean. Out on the north side, the newer subdivisions bring big attached garages on good concrete, where a full-flake floor is usually the ask. And the manufacturing corridor around town keeps heavier industrial work in the mix &mdash; different system, different build thickness, same prep discipline.",
      nearby=["Bloomington", "Hudson", "Towanda", "Lexington"]),

 dict(slug="epoxy-flooring-decatur-il", city="Decatur", county="Macon County",
      service="Epoxy Flooring", kw="epoxy flooring Decatur IL",
      img="metallic-epoxy-floor-finish.jpg",
      alt="Large industrial interior in Decatur, IL with a poured metallic epoxy floor",
      title="Epoxy Flooring Decatur IL | Industrial, Shop &amp; Garage Floor Coating",
      desc="Epoxy flooring in Decatur, IL. Industrial and warehouse floor coatings, shop floors and residential garage epoxy across Macon County. Free quotes - (217) 417-5950.",
      h1="Epoxy Flooring in Decatur, IL",
      intro="Decatur is about fifty minutes southwest of Champaign, well inside our service area, and it is one of the more industrial markets we work in.",
      local="Decatur&rsquo;s ag-processing and manufacturing base means the floors here are frequently large, hard-used and chemically abused &mdash; the sort of slab where a thin roll-on coating would not last a season. Those jobs get shot blasting or heavy grinding, full joint and crack treatment, and a high-build chemical-resistant system with line striping where the traffic patterns need marking. Alongside that there is a big, established residential base, and a Decatur garage slab from the 60s or 70s benefits from exactly the same repair-first approach we take everywhere else.",
      nearby=["Forsyth", "Mt. Zion", "Argenta", "Cerro Gordo"]),

 dict(slug="epoxy-flooring-danville-il", city="Danville", county="Vermilion County",
      service="Epoxy Flooring", kw="epoxy flooring Danville IL",
      img="before-bare-shop-concrete-floor.jpg",
      alt="Shop building in Danville, IL with bare concrete ready for epoxy floor coating",
      title="Epoxy Flooring Danville IL | Shop, Warehouse &amp; Garage Floor Coating",
      desc="Epoxy flooring in Danville, IL. Shop and warehouse floor coatings, commercial epoxy and residential garage floors across Vermilion County. Free quotes - (217) 417-5950.",
      h1="Epoxy Flooring in Danville, IL",
      intro="Danville is a straight thirty-five-minute shot east on I-74, which puts the whole of Vermilion County comfortably inside our range.",
      local="Danville&rsquo;s industrial history left it with a lot of older shop and warehouse space, and those floors tend to arrive with the full set of problems: oil-soaked concrete, spalling at the dock doors, joints that have opened up, and often an old coating that is already letting go. That is fine &mdash; it just means the prep day is a real day. Degrease it, strip what is failing, blast or grind the profile open, fix the joints, and then it will take a coating that holds. The residential side is mostly older detached garages, where the same logic applies at a smaller scale.",
      nearby=["Tilton", "Westville", "Georgetown", "Hoopeston"]),

 dict(slug="epoxy-flooring-monticello-il", city="Monticello", county="Piatt County",
      service="Epoxy Flooring", kw="epoxy flooring Monticello IL",
      img="blue-flake-epoxy-garage-floor.jpg",
      alt="Residential garage near Monticello, IL finished with a blue and gray flake epoxy floor",
      title="Epoxy Flooring Monticello IL | Garage, Pole Barn &amp; Shop Floors",
      desc="Epoxy flooring in Monticello, IL. Garage floor coatings, pole barn and machine shed floors, and basement epoxy across Piatt County. Free quotes - (217) 417-5950.",
      h1="Epoxy Flooring in Monticello, IL",
      intro="Monticello is twenty-five minutes west of Champaign, and Piatt County is well inside the area we cover without a trip charge.",
      local="Work in Monticello skews rural. Between the acreages outside town and the farms around them, a lot of what we coat is a detached shop, a machine shed or a pole barn rather than an attached two-car garage &mdash; and those slabs almost always need moisture testing first, because plenty were poured without a vapor barrier underneath. When the numbers come back right, a coated shop floor pays for itself in how much easier it is to keep clean. In town, the older homes near downtown and Allerton bring the usual mid-century garage concrete.",
      nearby=["Bement", "Cerro Gordo", "Mahomet", "Champaign"]),

 dict(slug="epoxy-flooring-tuscola-il", city="Tuscola", county="Douglas County",
      service="Epoxy Flooring", kw="epoxy flooring Tuscola IL",
      img="showroom-epoxy-floor-graphics.jpg",
      alt="Retail floor in Tuscola, IL finished with a coated epoxy surface and inlaid graphics",
      title="Epoxy Flooring Tuscola IL | Garage, Retail &amp; Shop Floor Coating",
      desc="Epoxy flooring in Tuscola, IL. Garage floor coatings, retail and commercial epoxy, and shop floors across Douglas County. Free on-site quotes - (217) 417-5950.",
      h1="Epoxy Flooring in Tuscola, IL",
      intro="Tuscola sits about half an hour south of Champaign where I-57 meets US-36, and that crossroads position is a big part of what we get called out for.",
      local="Because of the interstate junction, Tuscola punches above its size on the commercial side &mdash; retail, service bays and light industrial that all need floors which look presentable and still take a beating. Those jobs usually want a hard-wearing solid color or flake system plus a clear urethane topcoat, and often line striping to mark out walkways. Away from the junction it is ag country, so machine sheds and shop buildings make up a good share of the rest, and those get the same moisture-test-first treatment we give every rural slab.",
      nearby=["Arcola", "Villa Grove", "Arthur", "Champaign"]),

 dict(slug="garage-floor-coating-champaign-il", city="Champaign", county="Champaign County",
      service="Garage Floor Coating", kw="garage floor coating Champaign IL",
      img="blue-flake-epoxy-garage-floor.jpg",
      alt="Champaign, IL residential garage finished with a blue and gray flake epoxy floor coating",
      title="Garage Floor Coating Champaign IL | Epoxy Garage Floors",
      desc="Garage floor coating in Champaign, IL. Diamond-ground prep, hot-tire resistant epoxy, solid color and full flake finishes. Locally owned, free quotes - (217) 417-5950.",
      h1="Garage Floor Coating in Champaign, IL",
      intro="If you have been looking at your garage slab all winter thinking it deserves better, this is the page. We coat garage floors right here in Champaign, and we are usually able to get out and quote within a few days.",
      local="A Champaign garage floor takes a specific beating: hot tires pulling in off the interstate in August, and road salt melting off the fenders from December through March. Both of those are what kill a cheap floor. Hot tires lift any coating that was not mechanically bonded to the concrete, and salt works its way into every pore of an uncoated slab and spalls the surface off. So we grind, we fix the concrete, and we use a system rated for hot-tire pickup. Most two- and three-car garages here are a one- to two-day install, and you are parking on it again inside a week.",
      nearby=["Urbana", "Savoy", "Mahomet", "Rantoul"]),

 dict(slug="garage-floor-coating-bloomington-il", city="Bloomington", county="McLean County",
      service="Garage Floor Coating", kw="garage floor coating Bloomington IL",
      img="garage-floor-coating-champaign-il.jpg",
      alt="Bloomington, IL garage with a freshly installed light gray epoxy floor coating",
      title="Garage Floor Coating Bloomington IL | Epoxy Garage Floors",
      desc="Garage floor coating in Bloomington, IL. Diamond-ground prep, hot-tire resistant epoxy, flake and solid color finishes across McLean County. Free quotes - (217) 417-5950.",
      h1="Garage Floor Coating in Bloomington, IL",
      intro="We coat garage floors right across Bloomington and McLean County, and there is no trip charge to come out and quote &mdash; we treat this market exactly like our home one.",
      local="Bloomington garages divide into two jobs. In the established neighborhoods, the slab is usually mid-century: sound underneath, but with hairline cracking, some pitting, and spalling along the apron where the salt collects. That gets chased, filled and patched before anything else happens. In the newer subdivisions the concrete is generally clean and flat, so the work is a straight diamond grind and the budget goes into the finish instead. Either way you get a hot-tire rated system, because a coating that lifts where the car parks is not a floor, it is a callback.",
      nearby=["Normal", "Downs", "Le Roy", "Heyworth"]),
]

LOC_BY_SLUG = {l["slug"]: l for l in LOCATIONS}

def loc_links(limit=None, dark=False, exclude=None):
    items = [l for l in LOCATIONS if l["slug"] != exclude]
    if limit: items = items[:limit]
    return "\n".join(
        f'      <li><a class="link-card" href="/{l["slug"]}/">{I["pin"]}'
        f'<span>{l["service"]} in {l["city"]}, IL</span>'
        f'<span class="go" aria-hidden="true">&rarr;</span></a></li>' for l in items)

def svc_links(exclude=None, dark=False):
    return "\n".join(
        f'      <li><a class="link-card" href="/services/{s["slug"]}/">{I[s["icon"]]}'
        f'<span>{s["name"]}</span><span class="go" aria-hidden="true">&rarr;</span></a></li>'
        for s in SERVICES if s["slug"] != exclude)

def map_embed(query, label):
    src = "https://www.google.com/maps?q=" + _q(query) + "&z=11&output=embed"
    return f"""<div class="map-embed">
        <iframe src="{src}" title="Map of the {label} service area"
                loading="lazy" referrerpolicy="no-referrer-when-downgrade"
                allowfullscreen></iframe>
      </div>"""

def page_location(l):
    path = f"/{l['slug']}/"
    trail = [("Home", "/"), ("Service Area", "/service-area/"), (f"{l['service']} in {l['city']}", None)]
    intro = l["intro"].format(name=NAME, owners=OWNER_PAIR)
    nearby = ", ".join(l["nearby"])

    schema = [crumb_schema(trail), {
        "@context": "https://schema.org", "@type": "Service",
        "@id": BASE + path + "#service",
        "name": f"{l['service']} in {l['city']}, IL",
        "serviceType": l["service"],
        "description": plain(l["desc"]),
        "url": BASE + path,
        "provider": {"@id": BASE + "/#business"},
        "areaServed": {"@type": "City", "name": f"{l['city']}, IL",
                       "containedInPlace": {"@type": "AdministrativeArea",
                                            "name": f"{l['county']}, Illinois"}},
        "offers": {"@type": "Offer", "priceCurrency": "USD", "url": BASE + "/contact/",
                   "availability": "https://schema.org/InStock"}},
        local_business()]

    return head(l["title"], l["desc"], path, schema=schema) + header("") + f"""
<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <p class="tagline">{TAGLINE}</p>
      <h1>{l['h1']}</h1>
      <p class="lede">{intro}</p>
      <div class="btn-row">
        {quote_btn("btn--onDark")}
        {call_btn()}
      </div>
    </div>
  </div>
</section>

<main id="main">

<section class="section">
  <div class="wrap">
    <div class="split split--wide-text">
      <div>
        <p class="eyebrow">{l['city']}, {CFG['basedIn']['region']}</p>
        <h2>What we run into on {l['city']} floors</h2>
        <p>{l['local']}</p>
        <div class="local-note">
          <strong>Serving {l['city']} and {nearby}.</strong> {l['county']} is inside our
          {AREA['radiusMiles']}+ mile radius, so there is no trip charge to come out and quote your floor.
        </div>
        <div class="btn-row">
          {quote_btn()}
          {btn(PHONE, "tel:" + TEL, "btn--ghost", "phone")}
        </div>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/{l['img']}" alt="{l['alt']}" width="1280" height="854" loading="lazy" decoding="async">
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Service area</p>
        <h2>Where {l['city']} sits in our range</h2>
        <p>We are based in {CFG['basedIn']['county']} and work {AREA['radiusMiles']}+ miles in every
        direction. {l['city']} and the rest of {l['county']} are well inside that, along with
        {nearby}.</p>
        <p>Call <a href="tel:{TEL}"><strong>{PHONE}</strong></a> and we will tell you straight away
        when we can get out to look at it.</p>
        <p class="map-note">Map shows the {l['city']}, {CFG['basedIn']['region']} area we cover.</p>
      </div>
      {map_embed(l['city'] + ", IL", l['city'] + ", IL")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Services</p>
      <h2>What we install in {l['city']}</h2>
      <p class="lede">Every service below is available across {l['county']} and the surrounding towns.</p>
    </div>
    <ul class="link-grid link-grid--3">
{svc_links()}
    </ul>
  </div>
</section>

<section class="section section--dark section--tight">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Nearby</p>
      <h2 style="font-size:clamp(1.4rem,3vw,2rem)">Other towns we cover</h2>
    </div>
    <ul class="link-grid link-grid--3">
{loc_links(exclude=l['slug'], limit=9, dark=True)}
    </ul>
    <p style="margin-top:1.5rem"><a class="arrow-link" href="/service-area/">See the full service area <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Questions</p>
      <h2>Before you book a {l['city']} quote</h2>
    </div>
    {faq_html(FAQS[:4])}
    <p style="margin-top:1.5rem;text-align:center"><a class="arrow-link" href="/faq/">All FAQs <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>

{cta_band(f"Get a free {l['city']} quote",
          f"On-site, itemized and in writing &mdash; with no trip charge anywhere in {l['county']}.")}
</main>
""" + footer()

# ==================================================================== ABOUT ==
def page_about():
    path = "/about/"
    trail = [("Home", "/"), ("About", None)]
    title = "About DP Flooring Services | Epoxy Contractors, Champaign IL"
    desc = (f"{NAME} is {OWNER_PAIR} - locally owned epoxy flooring contractors "
            "serving Champaign County and Central Illinois. Free, itemized quotes.")

    values = [
        ("check_circle", "Do it right the first time",
         "No shortcuts on prep, no thin coats to stretch material, no &ldquo;that will probably hold.&rdquo; If the floor needs another step, it gets another step."),
        ("sparkle", "Attention to detail",
         "Clean edges, tight cut-ins, even flake coverage and a topcoat with no roller marks in it. On a floor, the details <em>are</em> the job."),
        ("shield", "Hard work, no excuses",
         "We show up when we said we would, we work the hours it takes to hit the cure window, and we clean up behind ourselves before we leave."),
        ("chat", "Straight answers",
         "Honest pricing, realiztic timelines, and a plain-English explanation of what we are doing and why. If epoxy is wrong for your floor, we will say so."),
    ]
    vhtml = "\n".join(f'        <li>{I[i]}<div><b>{t}</b><span>{d}</span></div></li>' for i, t, d in values)

    schema = [crumb_schema(trail), {
        "@context": "https://schema.org", "@type": "AboutPage",
        "name": "About " + NAME, "url": BASE + path,
        "mainEntity": {"@id": BASE + "/#business"}}]

    return head(title, desc, path, schema=schema) + header(path) + pagehead(
        "Locally owned. Personally installed.",
        f"{NAME} is {OWNER_PAIR} &mdash; two {CFG['basedIn']['county']} guys who decided that if a floor "
        "was going to have our name on it, it was going to be done right the first time.",
        trail) + f"""
<main id="main">

<section class="section">
  <div class="wrap">
    <div class="split split--wide-text">
      <div>
        <p class="eyebrow">Our story</p>
        <h2>We got tired of watching good floors fail</h2>
        <p>We started {NAME} because we kept running into the same thing: epoxy floors that looked
        incredible for one season and started lifting by the next winter. Almost every time, the coating
        was not the problem. <strong>The prep was.</strong> Somebody skipped the grinder, rolled a
        product over a sealed or oil-soaked slab, and the bond never had a chance to form.</p>
        <p>So that is the part we refuse to rush. Every floor we take on gets mechanically profiled,
        every crack gets chased and filled, every pit gets patched, and every slab gets checked for
        moisture <em>before</em> we quote it rather than after. It is slower. It is also the whole
        difference between a floor you forget about for fifteen years and one you are calling somebody
        about next spring.</p>
        <p>When you hire us, <strong>you get us</strong>. Drayton and Dylan are the ones who come out to
        measure, the ones running the grinder, and the ones who answer the phone when you call. There is
        no salesperson working a commission and no crew you have never met pulling up in an unmarked van.</p>
        <p>We live here and we work here. The garages, basements, shops and warehouses we coat belong to
        our neighbors across Champaign-Urbana, Bloomington-Normal and the towns in between. Word travels
        fast in Central Illinois, and we would rather earn the next job than close this one.</p>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/epoxy-crew-installing-warehouse-floor.jpg"
             alt="Installers laying an epoxy floor coating over a freshly prepared concrete slab"
             width="1280" height="960" loading="lazy" decoding="async">
      </div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How we work</p>
      <h2>Four things we will not compromise on</h2>
    </div>
    <ul class="features">
{vhtml}
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--flip">
      <div>
        <p class="eyebrow">The owners</p>
        <h2>{OWNER_PAIR}</h2>
        <p class="lede">Two owners, one crew, and both names on the truck.</p>
        <p>Between us we handle everything from the first phone call to the final walkthrough: measuring
        your slab, moisture testing it, quoting it honestly, grinding it, coating it and handing it back
        to you with a care sheet. Nothing gets subcontracted out to whoever was available that week.</p>
        <p>That is deliberate. It means when we tell you a floor will be ready Thursday, it is the person
        who will actually be standing on it Thursday telling you &mdash; and it means there is nobody to
        point at but us if something is not right.</p>
        <div class="btn-row" style="margin-top:1.75rem">
          {quote_btn()}
          {btn(PHONE, "tel:" + TEL, "btn--ghost", "phone")}
        </div>
      </div>
      <div class="split__media split__media--tall reveal">
        <img src="{IMG}/applying-epoxy-floor-coating-roller.jpg"
             alt="Installer pulling a fresh floor coating across a prepared slab with a long-handled squeegee"
             width="900" height="1200" loading="lazy" decoding="async">
      </div>
    </div>
  </div>
</section>

{cta_band("Want it done right the first time?",
          "Free, itemized, on-site quotes anywhere in our service area. "
          "We will tell you exactly what your slab needs &mdash; and what it does not.")}
</main>
""" + footer()

# ============================================================= SERVICE AREA ==
def page_area():
    path = "/service-area/"
    trail = [("Home", "/"), ("Service Area", None)]
    title = "Service Area | Epoxy Flooring Across Central Illinois"
    desc = ("We install epoxy floors in Champaign, Urbana, Savoy, Mahomet, Rantoul, Bloomington, Normal, "
            "Decatur, Danville, Monticello, Tuscola and every surrounding town within 50+ miles.")

    icons = ["home", "truck", "pin", "grid"]
    groups = []
    for n, g in enumerate(AREA["groups"]):
        chips = "\n".join(f'        <li><span class="chip">{t}</span></li>' for t in g["towns"])
        groups.append(f"""      <div class="area-group reveal">
        <h3>{I[icons[n % len(icons)]]} {g['name']}</h3>
        <ul class="chips">
{chips}
        </ul>
      </div>""")

    schema = [crumb_schema(trail), local_business(), {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": "Locations served",
        "itemListElement": [{"@type": "ListItem", "position": i + 1,
                             "name": f"{l['service']} in {l['city']}, IL",
                             "url": BASE + "/" + l["slug"] + "/"}
                            for i, l in enumerate(LOCATIONS)]}]

    all_towns = sum(len(g["towns"]) for g in AREA["groups"])
    return head(title, desc, path, schema=schema) + header(path) + pagehead(
        "Epoxy floors across Central Illinois",
        f"Based in {CFG['basedIn']['county']} and working {AREA['radiusMiles']}+ miles in every direction "
        "&mdash; Champaign-Urbana, Bloomington-Normal, Decatur, Danville and every town in between. "
        "No trip charge anywhere in the area.",
        trail) + f"""
<main id="main">

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Local pages</p>
      <h2>Find your town</h2>
      <p class="lede">Each page below covers what we actually run into on floors in that town &mdash;
      the slabs, the buildings and the scheduling.</p>
    </div>
    <ul class="link-grid link-grid--3">
{loc_links()}
    </ul>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">The radius</p>
        <h2>{AREA['radiusMiles']}+ miles from {CFG['basedIn']['county']}</h2>
        <p>Roughly speaking: if you are within about a {AREA['radiusMiles']}-mile drive of Champaign, we
        cover you, and we do not add a trip charge to get there.</p>
        <p>That circle takes in all of Champaign County, McLean County and Piatt County, plus Decatur,
        Danville, Tuscola, Arcola, Paxton, Gibson City and a long list of smaller towns either side.</p>
        <p class="map-note">Map centerd on Champaign, Illinois &mdash; our service radius runs outward
        from here in every direction.</p>
      </div>
      {map_embed("Champaign, IL", "Central Illinois")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Every town</p>
      <h2>{all_towns} towns and counting</h2>
      <p class="lede">This list is not exhaustive. If your town is not on it, call anyway &mdash;
      we say yes far more often than we say no.</p>
    </div>
{chr(10).join(groups)}
    <div class="btn-row" style="margin-top:2.5rem">
      {quote_btn()}
      {btn("Don&rsquo;t see your town? Call " + PHONE, "tel:" + TEL, "btn--ghost", "phone")}
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Local, not regional</p>
        <h2>Close enough to come back</h2>
        <p class="lede">There is a practical reason we drew the line at {AREA['radiusMiles']} miles.</p>
        <p>A contractor three hours away can sell you a floor, but they cannot easily swing by when you
        have a question about a spot near the overhead door two months later. We can, and we do.</p>
        <p>Working close to home also means we schedule honestly. We are not stacking jobs across half the
        state and hoping the weather cooperates &mdash; if we tell you Tuesday, we mean Tuesday.</p>
        <div class="btn-row" style="margin-top:1.75rem">
          {btn("Get a Free Quote", "/contact/", "btn--onDark")}
        </div>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/high-gloss-epoxy-shop-floor.jpg"
             alt="Large shop bay with a mirror-gloss epoxy floor"
             width="1280" height="854" loading="lazy" decoding="async">
      </div>
    </div>
  </div>
</section>

{cta_band("We&rsquo;re probably already working near you.",
          f"Free, itemized quotes anywhere in the {AREA['radiusMiles']}+ mile service area &mdash; "
          "and no trip charge to come out and look.")}
</main>
""" + footer()

# ================================================================== GALLERY ==
def page_gallery():
    path = "/gallery/"
    trail = [("Home", "/"), ("Gallery", None)]
    title = "Epoxy Floor Gallery | Before &amp; After Projects | Central Illinois"
    desc = ("Before-and-after epoxy floor comparisons from Central Illinois - garage, basement, shop, "
            "warehouse and commercial floors, before prep and after coating.")

    pairs = "\n".join(ba_html(p) for p in PAIRS)
    shots = "\n".join(f"""      <figure class="shot reveal">
        <img src="{IMG}/{f}" alt="{a}" width="1280" height="854" loading="lazy" decoding="async">
        <figcaption>{c}</figcaption>
      </figure>""" for f, c, a in SHOTS)

    schema = [crumb_schema(trail)]

    return head(title, desc, path, schema=schema) + header(path) + pagehead(
        "Before and after: what prep actually does",
        "Drag the slider on any floor below. The left half is bare, worn or damaged concrete. "
        "The right half is what the same kind of slab looks like once it has been ground, repaired and coated.",
        trail) + f"""
<main id="main">

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Before &amp; after</p>
      <h2>Six floors, six problems, one process</h2>
      <p class="lede">Every one of these starts the same way: grind the slab, fix what is broken, then coat it.
      Drag each divider left and right to compare.</p>
    </div>
    <div class="gallery-grid">
{pairs}
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Finishes</p>
      <h2>Systems we install</h2>
      <p class="lede">Solid color, full-broadcast flake, poured metallic and high-build commercial
      coatings &mdash; with line striping and non-slip aggregate wherever the floor needs it.</p>
    </div>
    <div class="gallery-grid">
{shots}
    </div>
    <p class="form-note" style="margin-top:2rem;max-width:70ch">
      These are reference photographs of the floor systems and finishes we install. As jobs wrap up
      around Champaign-Urbana and Bloomington-Normal, real {BRAND} before-and-afters go up in their place.
    </p>
  </div>
</section>

{cta_band("Want your floor in this gallery?",
          "Book a free on-site quote and we will show you samples of every finish above &mdash; "
          "flake blends, metallic pours and solid colors, in person rather than on a screen.")}
</main>
""" + footer()

# ====================================================================== FAQ ==
def page_faq():
    path = "/faq/"
    trail = [("Home", "/"), ("FAQ", None)]
    title = "Epoxy Flooring FAQ | Cure Time, Cost &amp; Lifespan | DP Flooring Services"
    desc = ("How long epoxy takes to cure, how long it lasts, going over an existing floor, what it "
            "costs and whether estimates are free. Answers from Central Illinois installers.")

    schema = [crumb_schema(trail), {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": plain(q),
                        "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                       for q, a in FAQS]}]

    return head(title, desc, path, schema=schema) + header(path) + pagehead(
        "Epoxy flooring, answered honestly",
        "Cure times, lifespan, cost drivers, going over an old floor, winter installs and how to look "
        "after it. If your question is not here, call &mdash; we are happy to talk it through.",
        trail) + f"""
<main id="main">

<section class="section">
  <div class="wrap wrap--narrow">
    {faq_html(FAQS)}
  </div>
</section>

<section class="section section--dark section--tight">
  <div class="wrap wrap--narrow" style="text-align:center">
    <h2 style="font-size:clamp(1.5rem,3vw,2.1rem)">Still have a question?</h2>
    <p class="lede">Call and ask. We would rather spend ten minutes on the phone than have you guess.</p>
    <div class="btn-row btn-row--center" style="margin-top:1.75rem">
      {btn("Call " + PHONE, "tel:" + TEL, "btn--onDark", "phone")}
      {btn("Email us", "mailto:" + EMAIL, "btn--ghostDark", "mail")}
    </div>
  </div>
</section>

{cta_band()}
</main>
""" + footer()

# ================================================================== CONTACT ==
def page_contact():
    path = "/contact/"
    trail = [("Home", "/"), ("Free Quote", None)]
    title = "Free Epoxy Flooring Quote | Champaign &amp; Bloomington IL"
    desc = ("Get a free, itemized epoxy flooring quote. Call (217) 417-5950 or send the form - garages, "
            "basements, shops, warehouses and commercial floors across Central Illinois.")

    options = "\n".join(f'              <option value="{t}">{t}</option>' for t in FLOOR_TYPES)
    netlify = CFG["form"]["provider"] == "netlify"
    form_attrs = ' data-netlify="true" netlify-honeypot="bot-field"' if netlify else ""
    form_name = '\n        <input type="hidden" name="form-name" value="quote">' if netlify else ""

    schema = [crumb_schema(trail), {
        "@context": "https://schema.org", "@type": "ContactPage",
        "name": "Free epoxy flooring quote", "url": BASE + path,
        "mainEntity": {"@id": BASE + "/#business"}}]

    return head(title, desc, path, schema=schema) + header(path) + pagehead(
        "Get a free quote",
        "Tell us the room and roughly how big it is. We will come out, look at the slab and leave you "
        "with an itemized written number &mdash; no charge, no obligation, no trip fee.",
        trail) + f"""
<main id="main">

<section class="section">
  <div class="wrap">
    <div class="quote-layout">

      <div class="form-card">
        <h2 style="font-size:clamp(1.45rem,3vw,1.9rem)">Request your free estimate</h2>
        <p class="lede" style="font-size:1.02rem;margin-bottom:1.9rem">
          Everything marked required helps us quote accurately the first time. Rough numbers are fine
          &mdash; we measure on site anyway.
        </p>

        <form name="quote" method="POST" action="/contact/thank-you/" data-validate{form_attrs}>{form_name}
          <p class="hp" aria-hidden="true">
            <label>Leave this field empty: <input name="bot-field" tabindex="-1" autocomplete="off"></label>
          </p>

          <div class="field-grid">
            <div class="field">
              <label for="name">Your name <span aria-hidden="true">*</span></label>
              <input id="name" name="name" type="text" autocomplete="name" required
                     placeholder="Drayton Potthast">
              <span class="err" data-msg="Please tell us your name."></span>
            </div>

            <div class="field">
              <label for="phone">Phone <span aria-hidden="true">*</span></label>
              <input id="phone" name="phone" type="tel" autocomplete="tel" required
                     inputmode="tel" placeholder="(217) 555-0134"
                     pattern="[\\(\\)0-9\\s\\-\\+\\.]{{10,20}}">
              <span class="err" data-msg="Please enter a phone number we can reach you on."></span>
            </div>

            <div class="field field--full">
              <label for="email">Email <span aria-hidden="true">*</span></label>
              <input id="email" name="email" type="email" autocomplete="email" required
                     placeholder="you@example.com">
              <span class="err" data-msg="Please enter a valid email address."></span>
            </div>

            <div class="field field--full">
              <label for="address">Job address <span class="opt">&mdash; street, city or just the town</span></label>
              <input id="address" name="address" type="text" autocomplete="street-address"
                     placeholder="1200 W Springfield Ave, Champaign, IL">
              <span class="err"></span>
            </div>

            <div class="field">
              <label for="floor-type">Floor type <span aria-hidden="true">*</span></label>
              <select id="floor-type" name="floor_type" required>
                <option value="" selected disabled>Choose one&hellip;</option>
{options}
              </select>
              <span class="err" data-msg="Pick the closest match &mdash; &ldquo;not sure&rdquo; is fine."></span>
            </div>

            <div class="field">
              <label for="sqft">Approx. square footage <span class="opt">&mdash; a guess is fine</span></label>
              <input id="sqft" name="square_footage" type="text" inputmode="numeric"
                     placeholder="e.g. 480 (2-car garage)">
              <span class="err"></span>
            </div>

            <div class="field field--full">
              <label for="message">Tell us about the floor <span class="opt">&mdash; optional</span></label>
              <textarea id="message" name="message"
                        placeholder="Condition of the concrete, any cracks or oil stains, an existing coating, the finish you have in mind, and when you'd like it done."></textarea>
              <span class="err"></span>
            </div>
          </div>

          <div class="form-foot">
            <button class="btn btn--lg btn--block" type="submit">Send my free quote request</button>
            <p class="form-note">
              We reply to every request. Prefer to talk it through? Call
              <a href="tel:{TEL}"><strong>{PHONE}</strong></a>. We use your details to quote your floor
              and nothing else &mdash; no lists, no sharing.
            </p>
          </div>
        </form>
      </div>

      <div>
        <div class="contact-cards">
          <a class="contact-card" href="tel:{TEL}">
            <span class="contact-card__icon">{I['phone']}</span>
            <span>
              <small>Call or text</small>
              <b>{PHONE}</b>
              <p>Fastest way to reach us. Tap to call from your phone.</p>
            </span>
          </a>

          <a class="contact-card" href="mailto:{EMAIL}?subject=Epoxy%20flooring%20quote%20request">
            <span class="contact-card__icon">{I['mail']}</span>
            <span>
              <small>Email</small>
              <b>{EMAIL}</b>
              <p>Send photos of the slab and we can get a head start.</p>
            </span>
          </a>

          <div class="contact-card">
            <span class="contact-card__icon">{I['pin']}</span>
            <span>
              <small>Service area</small>
              <b>{CFG['basedIn']['county']}, IL</b>
              <p>{AREA['phrase']}. No trip charge anywhere in the area.</p>
            </span>
          </div>

          <div class="contact-card">
            <span class="contact-card__icon">{I['shield']}</span>
            <span>
              <small>Owners</small>
              <b>{OWNERS[0]}<br>{OWNERS[1]}</b>
              <p>You deal with us directly, start to finish.</p>
            </span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="section section--paper2 section--tight">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center" style="margin-bottom:1.5rem">
      <h2 style="font-size:clamp(1.45rem,3vw,2rem)">What happens next</h2>
    </div>
    <div class="grid grid--3 steps">
      <div class="step"><h3>We call you back</h3><p>Usually the same day, to ask a couple of questions and find a time that works.</p></div>
      <div class="step"><h3>We come look</h3><p>Measure the space, check the slab for moisture and damage, and show you real finish samples.</p></div>
      <div class="step"><h3>You get it in writing</h3><p>An itemized quote covering prep, materials, install and any extras. Then it is entirely your call.</p></div>
    </div>
  </div>
</section>
</main>
""" + footer()

# =============================================================== THANK YOU ===
def page_thanks():
    path = "/contact/thank-you/"
    html = head("Thanks &ndash; we&rsquo;ve got your request | " + NAME,
                "Your epoxy flooring quote request has been sent to DP Flooring Services LLC in "
                "Champaign County. One of the owners will be in touch shortly, usually the same day.", path)
    html = html.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                        '<meta name="robots" content="noindex, follow">')
    return html + header("/contact/") + f"""
<main id="main">
<section class="section">
  <div class="wrap">
    <div class="thanks">
      <div class="thanks__tick">{I['check']}</div>
      <h1 style="font-size:clamp(2rem,5vw,3rem)">Request received</h1>
      <p class="lede">Thanks &mdash; your quote request is with us. One of us (Drayton or Dylan, not a
      call center) will get back to you shortly, usually the same day.</p>
      <p>In a hurry, or thought of something you forgot to mention? Call
      <a href="tel:{TEL}"><strong>{PHONE}</strong></a> any time.</p>
      <div class="btn-row btn-row--center" style="margin-top:2rem">
        {btn("Call " + PHONE, "tel:" + TEL, "", "phone")}
        {btn("Back to home", "/", "btn--ghost")}
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2 section--tight">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">While you wait</p>
      <h2 style="font-size:clamp(1.4rem,3vw,2rem)">Worth a read before we come out</h2>
    </div>
    {faq_html(FAQS[:3])}
  </div>
</section>
</main>
""" + footer()

# ====================================================================== 404 ==
def page_404():
    path = "/404.html"
    html = head("Page not found | " + NAME,
                "That page does not exist. Head back to the DP Flooring Services home page, or call "
                "(217) 417-5950 for a free epoxy flooring quote.", path)
    html = html.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                        '<meta name="robots" content="noindex, follow">')
    links = "\n".join(f'        <li><a href="{h}">{l}</a></li>' for l, h in NAV_MOBILE)
    return html + header("") + f"""
<main id="main">
<section class="section">
  <div class="wrap">
    <div class="thanks">
      <p class="eyebrow" style="justify-content:center">Error 404</p>
      <h1 style="font-size:clamp(2rem,5vw,3rem)">That page has been ground off</h1>
      <p class="lede">The link you followed does not lead anywhere on this site any more. Everything
      that <em>does</em> exist is below.</p>
      <ul class="chips" style="justify-content:center;margin:2rem 0">
{links}
      </ul>
      <div class="btn-row btn-row--center">
        {quote_btn()}
        {btn("Call " + PHONE, "tel:" + TEL, "btn--ghost", "phone")}
      </div>
    </div>
  </div>
</section>
</main>
""" + footer()


# ====================================================== SITEMAP / MAIN LOOP ==
from datetime import date as _date

# (url path, output file, priority, changefreq, include-in-sitemap)
def build_pages():
    pages = [
        ("/",              "index.html",                   page_home,    "1.0", "weekly",  True),
        ("/services/",     "services/index.html",          page_services,"0.9", "monthly", True),
        ("/about/",        "about/index.html",             page_about,   "0.6", "yearly",  True),
        ("/service-area/", "service-area/index.html",      page_area,    "0.8", "monthly", True),
        ("/gallery/",      "gallery/index.html",           page_gallery, "0.7", "monthly", True),
        ("/faq/",          "faq/index.html",               page_faq,     "0.7", "monthly", True),
        ("/contact/",      "contact/index.html",           page_contact, "0.9", "monthly", True),
        ("/contact/thank-you/", "contact/thank-you/index.html", page_thanks, None, None, False),
        ("/404.html",      "404.html",                     page_404,     None, None, False),
    ]
    for svc in SERVICES:
        pages.append((f"/services/{svc['slug']}/", f"services/{svc['slug']}/index.html",
                      (lambda x=svc: page_service(x)), "0.9", "monthly", True))
    for loc in LOCATIONS:
        pages.append((f"/{loc['slug']}/", f"{loc['slug']}/index.html",
                      (lambda x=loc: page_location(x)), "0.8", "monthly", True))
    return pages

def sitemap(entries):
    today = _date.today().isoformat()
    urls = "\n".join(
        f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        for u, pr, cf in entries)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + urls + "\n</urlset>\n")

def robots():
    return f"""# {NAME}
User-agent: *
Allow: /
Disallow: /contact/thank-you/

Sitemap: {BASE}/sitemap.xml
"""

def webmanifest():
    return json.dumps({
        "name": NAME, "short_name": CFG["shortBrand"],
        "description": CFG["tagline"] if "tagline" in CFG else TAGLINE,
        "start_url": "/", "display": "standalone",
        "background_color": "#071229", "theme_color": "#071229",
        "icons": [
            {"src": "/assets/img/favicon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/img/favicon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
        ],
    }, indent=2) + "\n"

def main():
    pages = build_pages()
    sm = []
    for url, rel, fn, pr, cf, in_sitemap in pages:
        write(rel, fn())
        if in_sitemap:
            sm.append((url, pr, cf))
    write("sitemap.xml", sitemap(sm))
    write("robots.txt", robots())
    write("site.webmanifest", webmanifest())

    print(f"Built {len(pages)} pages into {OUT}")
    print(f"  {len(SERVICES)} service pages, {len(LOCATIONS)} location pages")
    print(f"  sitemap.xml lists {len(sm)} indexable URLs")
    print(f"  base URL: {BASE}")
    orphan = [u for u, p, c in sm if u not in open(os.path.join(OUT, "sitemap.xml"), encoding="utf-8").read()]
    if orphan:
        print("  !! missing from sitemap:", orphan)

if __name__ == "__main__":
    main()
