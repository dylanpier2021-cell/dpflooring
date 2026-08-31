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
_args = [a for a in sys.argv[1:] if not a.startswith("-")]
OUT = os.path.abspath(_args[0]) if _args else ROOT
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
LEGAL = CFG["legal"]
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
             'alt="{alt}" width="260" height="214" fetchpriority="high" decoding="async">')
LOGO_FULL = ('<img class="footer__logo" src="/assets/img/logo-full-ondark.png" '
             'alt="{alt}" width="420" height="450" loading="lazy" decoding="async">')
TAGLINE = "Built to last. Finished to impress."


# ------------------------------------------------------------------- content
NAV = [("Home", "/"), ("Services", "/services/"), ("Colors", "/colors-and-finishes/"),
       ("Gallery", "/gallery/"), ("Service Area", "/service-area/"), ("About", "/about/"),
       ("FAQ", "/faq/")]
NAV_MOBILE = NAV + [("Contact", "/contact/")]

SERVICES = [
 dict(slug="garage-floor-epoxy", name="Garage Floor Epoxy", icon="home", type="Garage", pair_idx=0,
      img="blue-flake-epoxy-garage-floor.jpg",
      alt="Modern garage finished with a blue and gray flake epoxy floor",
      title="Garage Floor Epoxy Champaign IL | Garage Floor Coating | DP Flooring",
      desc="Epoxy garage floor coating in Champaign-Urbana, Bloomington-Normal and Central Illinois. "
           "Diamond-ground prep, hot-tire resistant systems, flake and solid color finishes.",
      h1="Garage Floor Epoxy",
      sub_h2="A garage floor that shrugs off hot tires and road salt",
      short="The floor you look at every single day. Ground down to clean concrete, filled, coated and "
            "top-sealed so oil, road salt, hot tires and dropped tools stop leaving their mark.",
      long="A garage slab takes more abuse than any floor on the property &mdash; hot tires, road salt, oil, dropped tools &mdash; and bare concrete absorbs all of it. A proper epoxy system seals the slab completely: spills wipe up, the whole floor mops clean, and the garage starts reading as finished space instead of storage.",
      body2="<strong>Hot-tire pickup</strong> is what kills DIY kits and acid-etched installs: the coating sits on top of the concrete instead of keying into it, and warm rubber peels it up in sheets. We diamond grind to open concrete, repair the cracks and pits, and install a system rated for hot-tire exposure. Most garages: two days on site, parking after about a week.",
      bullets=["Diamond-ground surface prep, so the coating bonds instead of peeling in a year",
               "Hot-tire resistant &mdash; no lifting or delamination where the car parks",
               "Solid color, partial flake or full-broadcast flake, in a blend you pick",
               "Crack, pit and apron-spall repair included before anything is coated",
               "Most two- and three-car garages are a one- to two-day install"],
      drivers=["Square footage &mdash; a two-car garage and a four-car outbuilding price very differently per foot",
               "Slab condition &mdash; cracking, pitting and spalling at the apron all add repair time",
               "Finish &mdash; solid color, partial flake or full-broadcast flake",
               "Extras &mdash; non-slip aggregate, cove base at the walls, and a second clear coat"]),

 dict(slug="basement-floor-epoxy", name="Basement Floor Epoxy", icon="layers", type="Basement", pair_idx=1,
      img="basement-flake-floor.jpg",
      alt="Finished residential basement with a light gray and white flake epoxy floor",
      title="Basement Floor Epoxy | Champaign &amp; Bloomington IL | DP Flooring",
      desc="Basement floor epoxy coating across Central Illinois. Seals concrete dust, resists moisture "
           "and brightens the lower level. Moisture tested before we quote.",
      h1="Basement Floor Epoxy",
      sub_h2="Stop the concrete dust and get the lower level back",
      short="Turn a cold, dusty slab into a finished floor that mops clean. A sealed basement stops "
            "concrete dust at the source and makes the whole lower level feel like real living space.",
      long="Untreated basement concrete is a dust factory, and it wicks ground moisture &mdash; that is where the musty smell comes from. Sealing the slab shuts both down at once: a seamless, light-reflecting floor you damp mop instead of sweep and re-sweep.",
      body2="We <strong>moisture test before we quote</strong>. Below-grade concrete can drive vapor up through the slab and blister a standard coating off within months &mdash; if the readings are high, we spec a vapor-tolerant system and show you the numbers first. Then a light, reflective floor does the rest: it is the cheapest single thing that makes a basement feel finished.",
      bullets=["Moisture-tested before we quote, so the system actually matches the slab",
               "Seamless surface &mdash; nowhere for dirt, dust or mildew to collect",
               "Light-colored coatings bounce what little natural light a basement gets",
               "Vapor-tolerant systems available where the slab readings call for one",
               "Ideal under home gyms, workshops, laundry rooms and finished rec space"],
      drivers=["Square footage of the finished area",
               "Moisture readings &mdash; a slab with vapor drive needs a different, costlier system",
               "How much crack, joint and patch work the slab needs first",
               "Finish choice and whether you want cove base up the walls"]),

 dict(slug="commercial-industrial-floor-coating", name="Commercial &amp; Industrial Floor Coating",
      icon="truck", type="Commercial / industrial", pair_idx=3,
      img="commercial-epoxy-floor-coating.jpg",
      alt="Warehouse interior with a freshly installed high-gloss epoxy floor",
      title="Commercial &amp; Industrial Floor Coating | Bloomington &amp; Decatur IL",
      desc="Commercial and industrial epoxy floor coatings in Central Illinois. Warehouses, shops, pole "
           "barns and production floors. High-build systems, line striping, off-hours installs.",
      h1="Commercial &amp; Industrial Floor Coating",
      sub_h2="Specified for the traffic your floor actually takes",
      short="Coatings specified for what really happens on the floor &mdash; forklifts, pallet jacks, "
            "wash-downs and chemicals. Warehouses, shops, pole barns and production space, any size, "
            "scheduled around your operation.",
      long="A production floor is not a big garage. Forklifts, hot wash-downs and spilled chemistry each attack a coating differently, so we spec thickness, resin and topcoat from what actually happens on your floor &mdash; then phase the install so you are never shut down completely. Single service bay to full distribution floor.",
      body2="Two things separate a commercial floor that lasts: <strong>prep</strong> &mdash; degrease, shot blast, and fill joints with semi-rigid filler that takes wheel loads &mdash; and <strong>scheduling</strong>. We work in sections, overnight and weekends, so your operation keeps moving. The payoff: a brighter building, spills that become a mop job, and striping built into the system instead of painted on top.",
      bullets=["High-build and chemical-resistant systems for real production environments",
               "Shop, warehouse and pole barn floors &mdash; single bay through full distribution floor",
               "Safety line striping, aisle marking, walkways and hazard zones",
               "Shot blasting and degreasing for oil-contaminated slabs",
               "Phased, overnight and weekend installs so the operation keeps running"],
      drivers=["Total square footage and how many phases the install has to run in",
               "Build thickness and chemical resistance the operation requires",
               "Prep method &mdash; grinding versus shot blasting on a heavily contaminated slab",
               "Line striping, aisle marking, non-slip aggregate and out-of-hours scheduling"]),

 dict(slug="flake-epoxy-flooring", name="Flake Epoxy Flooring", icon="grid", type="Flake epoxy", pair_idx=2,
      img="decorative-flake-epoxy-floor-finish.jpg",
      alt="Close-up of a gray and white speckled floor finish, the look a full-broadcast flake system gives",
      title="Flake Epoxy Flooring | Garage &amp; Basement Floors | Illinois",
      desc="Full-broadcast flake epoxy flooring in Central Illinois. Custom color blends, built-in grip, "
           "hides slab imperfections, finished with a clear urethane topcoat.",
      h1="Flake Epoxy Flooring",
      sub_h2="The finish most people picture when they picture an epoxy floor",
      short="Vinyl flake broadcast into the base coat until the floor will not take another chip, then "
            "scraped, vacuumed and sealed under clear urethane. Custom color blends, built-in grip, and "
            "it hides everything a slab has been through.",
      long="Our most popular floor: colored vinyl chips broadcast by hand into the wet base until the surface will not hold another flake, then scraped, vacuumed and sealed under clear urethane. Subtle texture underfoot, hides dust and tire marks between cleanings, and the look is yours to tune.",
      body2="Flake <strong>forgives</strong>. A solid-color floor mirrors every patch and trowel mark; flake breaks the surface up so a repaired slab reads as a finished floor &mdash; and the chip texture adds real grip when you track snow in. We bring physical sample boards to the estimate: subtle grays, our logo blues, or your team colors, in full or partial broadcast.",
      bullets=["Broadcast to refusal &mdash; full coverage, not a light scatter",
               "Hides slab imperfections and repaired cracks better than any solid color",
               "Chip edges build in grip, which matters on a wet winter garage floor",
               "Custom blends chosen from physical samples at the estimate",
               "Sealed under one or two coats of clear urethane for UV and scuff resistance"],
      drivers=["Square footage and how complex the layout is to cut in",
               "Full broadcast versus a lighter partial broadcast",
               "Slab prep and repair needed before the decorative work starts",
               "Number of clear urethane topcoats and whether you add non-slip aggregate"]),

 dict(slug="metallic-epoxy-flooring", name="Metallic Epoxy Flooring", icon="sparkle",
      type="Metallic epoxy", pair_idx=4,
      img="metallic-epoxy-floor-finish.jpg",
      alt="Large interior with a poured amber metallic floor finish and dark steel columns",
      title="Metallic Epoxy Flooring | Showroom &amp; Garage Floors | Central Illinois",
      desc="Poured metallic epoxy floors in Central Illinois. Pigments move through the resin as it "
           "levels, so no two floors are alike. Showrooms, retail, basements and feature garages.",
      h1="Metallic Epoxy Flooring",
      sub_h2="A floor with depth and movement you cannot get from paint",
      short="Metallic pigments suspended in clear resin, worked while it levels so the color moves. Every "
            "floor is genuinely one of a kind &mdash; and it is the finish people stop walking to look at.",
      long="The premium end of what we install. Reflective pigments poured over a colored base and worked while the resin still moves &mdash; that is what produces the depth and veining of polished stone. Nobody, including us, can pour the same floor twice. That is the point of it.",
      body2="A metallic pour is created live on the floor &mdash; <strong>the least forgiving thing we do</strong>. The working window is minutes and there is no touching it up after, which is why we pour these ourselves. It earns its keep anywhere the floor is part of the room: showrooms, lobbies, finished basements. And we are honest about the trade-off &mdash; if you want a hard-working, forgiving floor, flake is the better buy.",
      bullets=["Poured and worked by hand &mdash; genuinely one of a kind, every time",
               "Depth, veining and movement that reads like polished stone",
               "Blends shown as physical sample panels at the estimate",
               "Flatter, sounder slab prep than a flake floor of the same size",
               "Finished with clear urethane for UV stability and scuff resistance"],
      drivers=["Square footage and how many people it takes to keep a wet edge across the room",
               "Extra slab flatness and repair work a metallic pour demands",
               "Number of pigment colors and the complexity of the blend",
               "Clear urethane topcoats over the finished pour"]),

 dict(slug="epoxy-floor-prep-and-repair", name="Epoxy Floor Prep &amp; Repair", icon="ruler",
      type="Existing epoxy floor that is failing", pair_idx=7,
      img="concrete-floor-prep-and-repair.jpg",
      alt="Cracked, pitted and stained concrete slab of the kind we grind and repair before coating",
      title="Epoxy Floor Prep &amp; Repair | Slab Prep | Central Illinois",
      desc="Slab prep and repair before an epoxy floor in Central Illinois: diamond grinding, shot "
           "blasting, crack chasing, spall repair and failed coating removal.",
      h1="Epoxy Floor Prep &amp; Repair",
      sub_h2="The step that decides how long your epoxy floor lasts",
      short="The part nobody sees, and the part your epoxy floor depends on entirely. Cracks, pits, "
            "spalling, failing old coatings and oil-soaked concrete all get dealt with before a drop of "
            "epoxy goes down.",
      long="Almost every failed epoxy floor failed the same way: nobody prepped the concrete. We mechanically profile every floor &mdash; no acid etching and hoping &mdash; then chase the cracks, patch the pits and strip any old coating. The slowest day of the job, and the only one that decides how long the floor lasts.",
      body2="Concrete has to be <strong>opened up</strong> before anything sticks. We diamond grind or shot blast to profile, chase cracks out and fill them structurally, patch the spalling, degrease oil-soaked areas and strip failing coatings entirely. Every prep job leads into one of our epoxy systems &mdash; this is the day that decides whether your floor lasts fifteen years or fifteen months.",
      bullets=["Diamond grinding and shot blasting with vacuum dust control",
               "Crack chasing and structural filling, not a skim coat over the top",
               "Spall, pit and edge repair with re-leveling where the slab needs it",
               "Removal of failed coatings &mdash; old paint, sealers and peeling epoxy",
               "Degreasing and testing so oil-contaminated concrete will take a bond",
               "Included in every epoxy floor we install &mdash; never quoted as an optional extra"],
      drivers=["Prep method &mdash; a diamond grind versus shot blasting a contaminated slab",
               "Linear feet of cracking and joints that need chasing and filling",
               "Square footage of spalling, pitting or delaminated surface to patch",
               "Whether a failed coating has to come off before anything else happens"]),
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
 # Answers are deliberately short. These render on /faq/, on all 14 location
 # pages (FAQS[:4]) and on the thank-you page, so every extra sentence here is
 # paid for ~16 times over. Lead with the number, then one line of why.
 ("How long does epoxy take to cure?",
  "<p>Foot traffic in <strong>12&ndash;24 hours</strong>, furniture in <strong>24&ndash;72</strong>, "
  "vehicles after <strong>5&ndash;7 days</strong>.</p>"
  "<p>Temperature shifts those windows, so you get exact dates for your floor before we start.</p>"),

 ("How long does an epoxy floor last?",
  "<p><strong>10&ndash;20 years</strong> in a home garage or basement. <strong>5&ndash;10</strong> under "
  "forklifts and steel wheels, then a recoat &mdash; which is cheap, because the prep is already done.</p>"
  "<p>Prep decides this, not the epoxy. We grind every floor rather than acid-etch it.</p>"),

 ("Can you put epoxy over an existing floor?",
  "<ul><li><strong>Bare concrete &mdash; yes.</strong> The ideal surface. We grind it first so the coating keys in.</li>"
  "<li><strong>An existing coating &mdash; maybe.</strong> Sound and bonded, we abrade and go over it. "
  "Peeling or bubbling, it comes off first &mdash; we do that too.</li>"
  "<li><strong>Tile, wood, vinyl or carpet &mdash; no.</strong> Epoxy needs concrete. Those come out first.</li></ul>"
  "<p>We tell you which you have at the estimate, before you have committed to anything.</p>"),

 ("How much does epoxy flooring cost?",
  "<p>Priced by the square foot. Four things move it:</p>"
  "<ul><li><strong>Size.</strong> Bigger floors cost less per foot.</li>"
  "<li><strong>Slab condition.</strong> Cracks, spalling and old coatings add repair time.</li>"
  "<li><strong>System.</strong> Solid color is cheapest, flake mid, metallic premium.</li>"
  "<li><strong>Extras.</strong> Non-slip, striping, cove base, heavier build.</li></ul>"
  "<p>We will not quote a floor we have not seen. Call <a href=\"tel:{tel}\">{phone}</a> &mdash; the "
  "estimate is free, itemized and in writing.</p>"),

 ("Do you offer free estimates?",
  "<p>Yes &mdash; free, on-site, no obligation. We measure, check the slab for moisture and damage, bring "
  "real color and flake samples, and leave an itemized written quote.</p>"
  "<p><strong>No trip charge</strong> anywhere in our 50+ mile area.</p>"),

 ("Do I have to empty the garage first?",
  "<p>Yes &mdash; completely clear, so we can grind it. Anything mounted to the wall can stay.</p>"
  "<p>Short on space? Plan on the driveway or a trailer for a couple of days. We confirm exactly how long "
  "at the estimate.</p>"),

 ("Can you install epoxy in the winter?",
  "<p>Usually. Epoxy cures by reaction, not drying, but most systems want the <em>slab</em> above about "
  "<strong>55&deg;F</strong>.</p>"
  "<p>In an unheated January garage that means we bring heat or book a warmer stretch. Heated shops, "
  "warehouses and basements run year-round.</p>"),

 ("Is an epoxy floor slippery?",
  "<p>Dry, it grips like any smooth surface. Wet, it can get slick &mdash; which matters in a garage in "
  "winter.</p>"
  "<p>Fix: we broadcast fine non-slip aggregate into the topcoat wherever you want it. Flake floors "
  "already carry some texture. Tell us where it gets wet.</p>"),

 ("What is the difference between epoxy and polyaspartic?",
  "<p>Two resins, and most good floors use both.</p>"
  "<ul><li><strong>Epoxy</strong> builds thickness and bonds hard to prepared concrete. Ambers slightly in "
  "strong UV, cures slowly in cold.</li>"
  "<li><strong>Polyaspartic</strong> cures in hours, stays clear in UV, tolerates cold &mdash; but it is "
  "thin, pricey, and has a working window of minutes.</li></ul>"
  "<p>So: epoxy base for build and bond, polyaspartic or urethane clear on top. &ldquo;One-day "
  "polyaspartic&rdquo; trades film build for speed &mdash; a real trade-off, not a free upgrade.</p>"),

 ("How soon can you start?",
  "<p>Spring through fall we book <strong>two to four weeks</strong> out. Winter is often quicker for "
  "heated spaces.</p>"
  "<p>We can almost always look sooner &mdash; estimates usually within a few days, free, no trip charge. "
  "Call <a href=\"tel:{tel}\">{phone}</a> and we will tell you honestly where the calendar stands.</p>"),

 ("How do I take care of it?",
  "<ul><li>Sweep or dust mop; wet mop with warm water and a mild cleaner.</li>"
  "<li>Skip citrus and vinegar cleaners, and soaps that leave a film.</li>"
  "<li>Wipe up gas, brake fluid and battery acid rather than letting them sit.</li>"
  "<li>Put a scrap of plywood under a floor jack or jack stand.</li></ul>"
  "<p>That is the whole list &mdash; we leave a care sheet behind with it written out.</p>"),
]

PAIRS = [
 # These render as a drag-to-wipe slider, so the two frames have to sit in the
 # SAME kind of space at a SIMILAR camera height - otherwise dragging the handle
 # morphs a basement into a parking garage and the widget just looks broken.
 # Index 0 is the only genuine same-room pair we own (identical camera position,
 # before and after the flake went down). The rest are like-for-like space
 # pairings, which is exactly what the gallery copy says they are: "the kind of
 # slab we start from" next to "the finish the same kind of slab takes".
 # Order matters twice over: the gallery shows PAIRS[:4], and each service page
 # picks one by pair_idx - so a pair must match the service that points at it.

 # 0 - garage-floor-epoxy. The real before/after.
 ("Two-car garage", "Cracked bare slab &rarr; flake epoxy floor",
  "before-bare-garage-slab.jpg", "Empty two-car garage with a cracked, stained bare concrete floor before coating",
  "after-flake-garage-floor.jpg", "The same two-car garage after a gray and white flake epoxy floor was installed"),

 # 1 - basement-floor-epoxy
 ("Finished basement", "Raw block-wall slab &rarr; flake epoxy floor",
  "before-bare-basement-slab.jpg", "Unfinished basement with a raw concrete slab, block walls and exposed floor joists",
  "basement-flake-floor.jpg", "Finished residential basement with a light gray and white flake epoxy floor"),

 # 2 - flake-epoxy-flooring
 ("Shop &amp; pole barn", "Dusty bare slab &rarr; full flake broadcast",
  "shop-building-bare-concrete-floor.jpg", "Steel shop building with a dusty, untreated bare concrete floor",
  "shop-flake-epoxy-floor.jpg", "Steel shop building with a dark gray flake epoxy floor running the length of the span"),

 # 3 - commercial-industrial-floor-coating
 ("Warehouse floor", "Bare industrial slab &rarr; high-build coating",
  "before-bare-warehouse-slab.jpg", "Empty warehouse with bare gray concrete and roof skylights, before coating",
  "commercial-epoxy-floor-coating.jpg", "Wide warehouse interior with a high-gloss light gray epoxy floor coating"),

 # 4 - metallic-epoxy-flooring
 ("Garage &amp; workshop", "Worn concrete &rarr; poured metallic",
  "before-worn-garage-concrete.jpg", "Bright workshop garage with a bare, worn concrete floor before coating",
  "metallic-epoxy-garage-floor.jpg", "Garage finished with a deep blue and silver poured metallic epoxy floor"),

 # 5
 ("Service bay", "Stained shop floor &rarr; mirror-gloss finish",
  "before-bare-shop-concrete-floor.jpg", "Vehicle service shop with a dusty, stained floor before coating",
  "high-gloss-epoxy-hangar-floor.jpg", "Large-span service interior with a mirror-gloss white epoxy floor"),

 # 6
 ("Commercial deck", "Stained deck &rarr; sealed, striped floor",
  "before-stained-parking-deck.jpg", "Dark, stained commercial parking deck before coating",
  "parking-structure-gray-floor.jpg", "Bright parking structure with a smooth light gray coated floor and striped columns"),

 # 7 - epoxy-floor-prep-and-repair. Both frames are close-ups, so they wipe cleanly.
 ("Cracked &amp; pitted slab", "Damaged concrete &rarr; full flake finish",
  "concrete-floor-prep-and-repair.jpg", "Cracked, pitted and stained concrete slab before repair",
  "decorative-flake-epoxy-floor-finish.jpg", "Close-up of a gray and white speckled full-broadcast flake finish"),
]

SHOTS = [
 ("blue-flake-epoxy-garage-floor.jpg", "Blue and gray flake epoxy in a modern garage",
  "Modern garage lit with blue accent lighting, finished with a blue and gray flake epoxy floor"),
 ("car-showroom-epoxy-floor.jpg", "Showroom floor under a high-gloss clear topcoat",
  "Car showroom with a high-gloss coated floor reflecting the vehicles on display"),
 ("showroom-epoxy-floor-graphics.jpg", "Coated floor with inlaid color graphics and striping",
  "Coated floor with black and red inlaid graphics running beside a ribbed metal wall"),
 ("metallic-epoxy-floor-finish.jpg", "Poured metallic epoxy in an amber blend",
  "Large interior with a poured amber metallic floor finish and dark steel columns"),
]

# ---- per-service extra sections: why epoxy here, how the install runs, FAQs --
# Kept deliberately short: one or two sentences per item. The bold lead carries
# the point; the reader is scanning, not reading.
SERVICE_EXTRA = {
"garage-floor-epoxy": dict(
  why_h="Why epoxy beats paint, tiles and roll-out mats",
  why=["<strong>Garage floor paint</strong> sits on the surface and hot tires lift it inside a season. "
       "Epoxy cures into a film several times thicker, bonded into ground concrete.",
       "<strong>Tiles and roll-out mats</strong> do not bond &mdash; water, salt and oil run into the "
       "seams and sit against the slab, which is exactly what causes spalling.",
       "<strong>Sealers</strong> are thin, fill nothing, and need redoing every few years. Only an epoxy "
       "system repairs the slab first and then covers it seamlessly."],
  steps=[("Free on-site quote",
          "We measure, check the slab, and bring physical flake and color samples. Itemized written "
          "number before we leave; no trip charge."),
         ("Grind and repair",
          "Garage empty, we diamond grind with vacuum shrouds, fill every crack, patch the pits and "
          "rebuild the spalled apron. This day decides the floor's lifespan."),
         ("Base coat and flake",
          "Pigmented base down, chips broadcast by hand to refusal, left overnight, then scraped flat "
          "and vacuumed clean."),
         ("Clear topcoat and cure",
          "Urethane clear seals it &mdash; non-slip aggregate if you want it. Walk on it next morning, "
          "shelving in 2&ndash;3 days, park after about a week.")],
  faqs=[("How long will my garage be out of action?",
         "<p>About a week, and completely empty for the first two to three days. Walk on it the next "
         "morning, shelving back in two or three days, drive on it after roughly seven &mdash; exact "
         "dates in writing before we start.</p>"),
        ("Do you coat the apron and the area under the door?",
         "<p>Yes, up to the inside edge of the door seal. The outdoor apron lives with UV, standing water "
         "and freeze-thaw, so an interior system does not belong out there. The strip just inside the "
         "door is usually the worst-damaged concrete, and it gets rebuilt during prep.</p>"),
        ("Can you match a color to the house or my cabinets?",
         "<p>Within reason, yes. Flake blends mix from stock chip colors, and we bring sample boards to "
         "the estimate so you can hold them against what you have. Solid-color bases come in a standard "
         "range. Want something exact? Ask &mdash; we will be straight about whether we can hit it.</p>")]),

"basement-floor-epoxy": dict(
  why_h="Why a basement slab is not a garage slab",
  why=["The difference is <strong>water you cannot see</strong>. A basement slab sits against damp soil, "
       "and ground moisture moves up through concrete as vapor whether or not you have ever had a leak.",
       "Seal that with a standard coating and the vapor collects underneath, builds pressure, and pushes "
       "the floor off in blisters &mdash; usually within a year.",
       "So we <strong>test rather than guess</strong>. Low readings: a standard system at garage prices. "
       "High readings: a vapor-tolerant build that costs more and actually survives. You see the numbers "
       "before the price."],
  steps=[("Quote and moisture test",
          "We measure and moisture test before quoting &mdash; the reading changes which system you "
          "need, and what it costs."),
         ("Clear, grind and repair",
          "Diamond grinding with vacuum shrouds &mdash; it matters most in a basement, where dust has "
          "nowhere to go. Cracks filled, joints treated, pits leveled."),
         ("Prime and base coat",
          "Mitigating primer where readings call for it, then the base coat and flake. Light colors are "
          "the usual pick &mdash; basements are short on daylight."),
         ("Topcoat, cove base and cure",
          "Clear urethane seals it; cove base turns the coating up the wall for a mop-proof junction. "
          "Foot traffic next day, furniture after two or three.")],
  faqs=[("My basement floods occasionally. Can it still be coated?",
         "<p>Fix the water first &mdash; a coating survives getting wet but will not stop water coming "
         "in. Once drainage is handled, a sealed slab is actually easier to dry out and clean up after "
         "an event than bare concrete.</p>"),
        ("Will it stop the musty smell?",
         "<p>Usually a real difference: much of that smell is moisture evaporating out of the slab and "
         "feeding mildew. Sealing the concrete cuts it off at the source. If the smell is from walls or "
         "a crawl space, the floor alone will not fix it &mdash; and we will say so when we look.</p>"),
        ("Can you coat around a finished basement?",
         "<p>The floor has to be completely clear &mdash; furniture out, usually baseboard off &mdash; "
         "and we cannot coat under built-ins or partition walls. Planning a build-out? Coat the slab "
         "first and frame over it. Easier and cheaper.</p>")]),

"commercial-industrial-floor-coating": dict(
  why_h="What actually destroys a commercial epoxy floor",
  why=["<strong>Point loading.</strong> A forklift concentrates thousands of pounds onto four small "
       "patches and turns them. We spec build thickness from your equipment, and fill joints with "
       "semi-rigid filler that supports the edge.",
       "<strong>Thermal shock.</strong> Hot wash-downs expand the floor faster than the slab beneath it. "
       "Standard epoxy will not take that for long; a urethane mortar will. Tell us if you wash down "
       "&mdash; it changes the spec.",
       "<strong>Old contamination.</strong> Oil wicks deep into concrete; grinding makes it look clean, "
       "then heat pulls it back up and the coating releases. That slab needs degreasing and shot "
       "blasting, not a grind."],
  steps=[("Walkthrough and spec",
          "We walk the floor and ask what actually happens on it &mdash; what drives, what spills, how "
          "hot the wash-down &mdash; then spec and quote around that, phasing plan included."),
         ("Phasing and scheduling",
          "The floor gets sectioned so there is always a route through for your people and equipment. "
          "Overnight and weekend work where needed."),
         ("Degrease, blast and repair",
          "Contamination degreased and tested, deep profile shot blasted in, joints rebuilt with "
          "semi-rigid filler that carries a wheel load."),
         ("Build coats, striping and topcoat",
          "System down to spec thickness. Striping and hazard zones sealed into the floor, non-slip "
          "aggregate wherever it gets wet.")],
  faqs=[("Can you work without shutting us down?",
         "<p>Yes &mdash; that is how most of our commercial work runs. Sectioned floor, one area at a "
         "time, a route always open, nights and weekends where the operation needs it. Slower than an "
         "empty building, priced honestly, and it beats losing a week of production.</p>"),
        ("How long before forklifts can run on it?",
         "<p>Foot traffic in 24 hours, light wheeled traffic in two to three days, full forklift loading "
         "after about seven, at full cure. Steel wheels on a green floor leave permanent tracking, so "
         "you get the dates in writing.</p>"),
        ("Do you do line striping and safety marking?",
         "<p>Yes &mdash; built into the floor, not painted on top. Aisles, walkways, hazard hatching and "
         "keep-clear zones go in between base and topcoat, sealed under the clear so they do not wear "
         "off under traffic.</p>")]),

"flake-epoxy-flooring": dict(
  why_h="Full broadcast, partial broadcast, and why it matters",
  why=["<strong>Full broadcast</strong> means chips thrown into the wet base until the floor will not "
       "take another one &mdash; refusal. Dense, granite-like, real texture underfoot, and the most "
       "forgiving surface we install.",
       "<strong>Partial broadcast</strong> leaves base color showing between chips. Less flake, lower "
       "cost, and on a clean modern slab it looks intentional. On a repaired slab it shows every patch.",
       "The honest rule: <strong>repaired concrete gets full broadcast.</strong> Clean modern pour and "
       "you like the lighter look? Partial is a real option. We will tell you which your floor is at "
       "the estimate."],
  steps=[("Pick the blend in person",
          "Physical sample boards at the quote &mdash; flake never looks the same on a screen as on a "
          "floor."),
         ("Grind and repair the slab",
          "Diamond grinding with dust control, then crack chasing, pit filling and spall repair. Flake "
          "hides repairs because the repairs were done properly."),
         ("Base coat and broadcast",
          "Base down, chips broadcast by hand to refusal &mdash; hand work is what keeps the coverage "
          "even into corners and along walls."),
         ("Scrape, vacuum, seal",
          "Scraped flat next morning, vacuumed clean, then one or two coats of clear urethane &mdash; "
          "with non-slip aggregate if the floor gets wet.")],
  faqs=[("Does flake feel rough underfoot?",
         "<p>Fine orange-peel texture, not rough &mdash; comfortable barefoot, easy to mop, and "
         "noticeably more grip than a smooth coating when wet. Want more? We broadcast fine aggregate "
         "into the topcoat.</p>"),
        ("Can I mix my own colors?",
         "<p>Yes &mdash; blends mix from stock chips: subtle grays, our logo blues, or team colors in a "
         "rec room. We mix samples and bring them out. One tip: judge a blend flat on the floor in the "
         "room's own light. Vertical boards under shop lights lie.</p>"),
        ("How does flake compare to metallic on price?",
         "<p>The middle: more than solid color, less than metallic &mdash; and the better buy for most "
         "working floors. Metallic is the right call when the floor is meant to be looked at; flake when "
         "it is meant to be used.</p>")]),

"metallic-epoxy-flooring": dict(
  why_h="What you are actually buying with a metallic floor",
  why=["A metallic floor is <strong>an outcome created live on your slab</strong> &mdash; pigment moved "
       "through self-leveling resin with rollers, brushes and air. The travel is what makes it read as "
       "stone.",
       "So <strong>nobody can promise a specific pattern</strong>, including us. The finished floor will "
       "be recognizably the blend on the sample panel &mdash; not identical to it. An installer who says "
       "otherwise is being loose with you.",
       "And it is unforgiving: a short working window, wet edge to wet edge across the whole room, no "
       "touch-ups ever. That is why we pour these ourselves &mdash; and why flake is the better buy for "
       "a hard-working floor."],
  steps=[("Sample panels and honest expectations",
          "Physical panels of the blends we run, how each behaves, and a plain statement of what cannot "
          "be guaranteed."),
         ("Extra slab preparation",
          "Self-leveling resin finds every low spot, so metallic carries more grinding and patching than "
          "flake on the same footage."),
         ("Base coat",
          "The pigmented base cures first. Its color shows through the metallic layer, so it is part of "
          "the design, not just a primer."),
         ("The pour",
          "One continuous session, wet edge kept across the whole room. Once it gels, it is finished. "
          "Two coats of urethane clear go over it after cure.")],
  faqs=[("Is metallic slippery?",
         "<p>Smooth plus wet is slick &mdash; more so than flake. Fine for a showroom, lobby or finished "
         "basement; for an entry that gets rain and snow, we broadcast fine non-slip aggregate into the "
         "topcoat. It slightly softens the gloss and it is worth it.</p>"),
        ("Can you repair a metallic floor if it gets damaged?",
         "<p>Not invisibly &mdash; the pattern cannot be reproduced, so a patch reads as a patch. Gouges "
         "can be filled and recoated, and scuffed urethane can take a fresh clear coat across the whole "
         "floor. It is a feature finish: put it where it will be looked at, not dropped on.</p>"),
        ("How much longer does metallic take than flake?",
         "<p>A day or two, mostly in prep: extra flattening, a cured base coat before the pour, and two "
         "urethane coats each needing their own window. Budget on cure dates &mdash; you get both in "
         "writing.</p>")]),

"epoxy-floor-prep-and-repair": dict(
  why_h="Why nearly every failed epoxy floor failed here",
  why=["<strong>Acid etching instead of grinding.</strong> Every DIY kit sells it. It barely opens the "
       "surface, leaves salt residue, and does nothing to a hard-troweled or sealed slab.",
       "<strong>Coating over contamination.</strong> Oil wicks deep into concrete; a grind makes the "
       "surface look clean, and the first warm week pulls it back up through the new coating.",
       "<strong>Skimming cracks</strong> instead of chasing them &mdash; they telegraph back through "
       "inside a season. And <strong>coating a wet slab</strong>: no moisture test, blisters by summer. "
       "All four are prep failures. None are the epoxy's fault."],
  steps=[("Assess and test",
          "What is on the slab &mdash; sealer, failing coating, oil &mdash; plus a moisture test. On a "
          "failed floor we want to know why, because the cause is still there."),
         ("Strip and decontaminate",
          "Failed coatings come off entirely; oil-soaked areas get degreased and re-tested. This is the "
          "step people skip, and the reason they call somebody like us twice."),
         ("Profile the concrete",
          "Diamond grinding with vacuum shrouds, shot blasting where contamination or traffic runs "
          "deeper &mdash; opening the pores so the epoxy keys in mechanically."),
         ("Repair, then coat",
          "Cracks chased into a V and filled structurally, spalls patched and leveled, joints treated. "
          "Only then does the system go down.")],
  faqs=[("My epoxy floor is peeling. Can you fix it or does it all come off?",
         "<p>Depends how much has let go and why. A small failure on a well-bonded floor can be cut "
         "back, re-profiled and blended in (visibly, on a solid color). Widespread failure or bad "
         "original prep means it all comes off &mdash; anything over a releasing coating comes up with "
         "it. We will tell you which you have, straight.</p>"),
        ("Is a DIY kit ever worth it?",
         "<p>On a brand-new, bone-dry slab in a heated garage, a good kit applied carefully looks decent "
         "for a few years &mdash; which describes very few real garages here. The kits are thin, rely on "
         "acid etching, and include nothing for repair. Stripping a failed DIY floor costs more than "
         "doing it properly would have.</p>"),
        ("How dusty is the grinding?",
         "<p>Far less than you would expect &mdash; vacuum shrouds with HEPA extraction capture most of "
         "it at the head. A fine film remains and we clean that up ourselves before we leave. In a "
         "basement this matters most, and it is why we will not work without proper extraction.</p>")]),
}
for _s in SERVICES:
    _s.update(SERVICE_EXTRA[_s["slug"]])

for _s in SERVICES:
    _s["pair"] = PAIRS[_s["pair_idx"]]

FLOOR_TYPES = ["Garage epoxy floor", "Basement epoxy floor",
               "Commercial / industrial epoxy", "Shop, warehouse or pole barn epoxy",
               "Flake epoxy", "Metallic epoxy",
               "Existing epoxy floor that is failing", "Not sure yet"]

# ------------------------------------------------------------------- helpers
def fill(s):
    return s.replace("{tel}", TEL).replace("{phone}", PHONE)

def btn(label, href, kind="", icon=None, extra=""):
    ic = I[icon] if icon else ""
    cls = "btn" + (" " + kind if kind else "")
    return f'<a class="{cls}" href="{href}"{extra}>{ic}{label}</a>'

def quote_btn(kind="", label="Get a Free Quote"):
    return btn(label, "/contact/", kind)

def call_btn(kind="btn--ghostDark", label=None):
    return btn(label or f"Call {PHONE}", f"tel:{TEL}", kind, "phone")

def call_primary(kind="btn--call"):
    """The main call-to-action. Filled brand blue, oversized, number spelled out."""
    return (f'<a class="btn {kind}" href="tel:{TEL}">{I["phone"]}'
            f'<span class="num">{PHONE}</span></a>')

def phone_cta(label="Talk to Drayton or Dylan"):
    """Big tappable number block for hero and page headers."""
    return (f'<a class="phone-cta" href="tel:{TEL}">'
            f'<span class="phone-cta__icon">{I["phone"]}</span>'
            f'<span><small>{label}</small><b>{PHONE}</b></span></a>')

def call_strip(kicker="Fastest way to get a number", sub=None, note=None):
    """Full-width call band. Goes on every page."""
    sub = sub or ("Tell us the room and roughly how big it is. Most quotes get scheduled "
                  "on the same call.")
    note = note or ('Prefer to type it out? <a href="/contact/">Send the quote form instead</a> '
                    f'or email <a href="mailto:{EMAIL}">{EMAIL}</a>.')
    return f"""<section class="callstrip">
  <div class="wrap">
    <p class="kicker">{kicker}</p>
    <a class="big" href="tel:{TEL}">{PHONE}</a>
    <p class="sub">{sub}</p>
    <p class="or">{note}</p>
  </div>
</section>
"""

def head(title, desc, path, image="/assets/img/og-image.jpg", schema=None):
    canon = BASE + path
    _v = CFG.get("verification", {})
    verify = ""
    if _v.get("googleSiteVerification"):
        verify += f'\n<meta name="google-site-verification" content="{_v["googleSiteVerification"]}">'
    if _v.get("bingSiteVerification"):
        verify += f'\n<meta name="msvalidate.01" content="{_v["bingSiteVerification"]}">' 
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
<meta name="robots" content="index, follow, max-image-preview:large">{verify}

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
      <a href="tel:{TEL}" style="color:#fff;font-weight:700">{I['phone']} {PHONE}</a>
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

    <a class="header__call" href="tel:{TEL}" aria-label="Call {NAME} on {PHONE}">{I['phone']}<span>{PHONE}</span></a>
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
      {call_primary("btn--call")}
      {btn(primary, "/contact/", "btn--ghostDark")}
    </div>
  </div>
</section>
"""


def lc_widget():
    """LeadConnector (GoHighLevel) chat widget.

    Kept verbatim as the vendor supplied it - no async/defer added, because a
    third-party loader is not worth second-guessing. Sitting last in <body>
    means the document is already parsed by the time it runs.
    Returns "" when the id is blank, so one config edit removes it everywhere.
    """
    wid = CFG.get("integrations", {}).get("leadConnectorWidgetId", "")
    if not wid:
        return ""
    return ('<script src="https://widgets.leadconnectorhq.com/loader.js" '
            'data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" '
            f'data-widget-id="{wid}" data-source="WEB_USER"></script>\n')

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
          <li><a href="/privacy-policy/">Privacy Policy</a></li>
          <li><a href="/terms-and-conditions/">Terms and Conditions</a></li>
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
  <a class="btn btn--onDark" href="tel:{TEL}" aria-label="Call {PHONE}">{I['phone']}<span class="num">{PHONE}</span></a>
  <a class="btn btn--ghostDark" href="/contact/">Free Quote</a>
</div>

<script src="/assets/js/main.js" defer></script>
{lc_widget()}</body>
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
        {call_primary()}
        {quote_btn("btn--ghostDark")}
      </div>
      <p class="form-note" style="color:#9FADBF;margin:1rem 0 0;font-size:.92rem">
        Free, on-site and itemized &mdash; and no trip charge anywhere we work.
      </p>
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
            f"Illinois. Garages, basements, shops, commercial. Free quotes - {PHONE}.")

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
    <img src="{IMG}/hero-high-gloss-epoxy-warehouse-1280.jpg"
         srcset="{IMG}/hero-high-gloss-epoxy-warehouse-1280.jpg 1280w, {IMG}/hero-high-gloss-epoxy-warehouse-2400.jpg 2400w"
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
        {phone_cta("Call us now &mdash; free quote")}
        {quote_btn("btn--ghostDark btn--lg", "Or request a quote")}
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
      {quote_btn("btn--ghost")}
    </div>
  </div>
</section>

{call_strip()}

<section class="section section--dark">
  <div class="wrap">
    <div class="split split--wide-text">
      <div>
        <p class="eyebrow">Why DP Flooring</p>
        <h2>Most epoxy floors don&rsquo;t fail. They were never prepped.</h2>
        <p class="lede">Every peeling floor we get called to has the same story: a coating rolled over
        a sealed or oily slab. We do the unglamorous part properly &mdash; the floor takes care of
        itself after that.</p>
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

{call_strip("Not sure which one you need?",
            "Describe the room and what happens in it. We can usually narrow it to one system on the "
            "phone and give you a ballpark before we ever come out.")}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Choosing a system</p>
      <h2>Solid color, flake or metallic?</h2>
      <p class="lede">Three finishes, three different jobs. The room usually decides it for you.</p>
    </div>
    <div class="grid grid--3 steps">
      <div class="step reveal">
        <h3>Solid color</h3>
        <p>Cheapest and least forgiving &mdash; it mirrors every patch and trowel mark. Sharp on a
        clean modern pour; on a repaired slab it advertises every repair you just paid for.</p>
      </div>
      <div class="step reveal">
        <h3>Flake</h3>
        <p>Mid-price and right for most floors. Chips hide imperfections and repairs, add real grip
        when wet, and the blend is yours. Repaired slab? Pick this.</p>
      </div>
      <div class="step reveal">
        <h3>Metallic</h3>
        <p>The premium feature finish &mdash; depth and veining like polished stone, no two alike.
        Needs a flatter slab, costs more, cannot be invisibly repaired. Put it where the floor gets
        looked at.</p>
      </div>
    </div>
    <div class="wrap--narrow" style="padding:0;margin:1.6rem 0 0">
      <p>And the option nobody sells you: <strong>sometimes the answer is not to coat it at all.</strong>
      A slab that is structurally failing is not a candidate for epoxy, and we will say so at the
      estimate rather than after. Not sure which yours is?
      Call <a href="tel:{TEL}"><strong>{PHONE}</strong></a> or <a href="/contact/">request a free
      quote</a> &mdash; we bring real samples and tell you straight.</p>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Every job, no exceptions</p>
      <h2>What is included as standard</h2>
      <p class="lede">These are not line items you have to ask for. They are the job.</p>
    </div>
    <ul class="features">
      <li>{I['check_circle']}<div><b>Mechanical surface prep</b><span>Diamond grinding or shot blasting
        with vacuum dust extraction. Never acid etching, on any floor, at any price.</span></div></li>
      <li>{I['check_circle']}<div><b>Moisture testing before the quote</b><span>So the system matches
        your slab, and so a number you have been given cannot change after we start.</span></div></li>
      <li>{I['check_circle']}<div><b>Crack, pit and spall repair</b><span>Cracks chased out and filled
        with structural resin, not skimmed. Pitted and spalled areas patched and re-leveled.</span></div></li>
      <li>{I['check_circle']}<div><b>An itemized written quote</b><span>Prep, materials, install and
        extras broken out separately, so you can see exactly what you are paying for.</span></div></li>
      <li>{I['check_circle']}<div><b>Written cure dates</b><span>When you can walk on it, when furniture
        can go back, and when you can park on it &mdash; for your floor, not from a brochure.</span></div></li>
      <li>{I['check_circle']}<div><b>Clean-up and a care sheet</b><span>We leave the space cleaner than we
        found it, with a one-page sheet on how to look after the floor.</span></div></li>
    </ul>
    <div class="btn-row btn-row--center" style="margin-top:2.75rem">
      {call_primary()}
      {quote_btn("btn--ghost")}
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
    why_ps = "\n        ".join(f"<p>{x}</p>" for x in s["why"])
    steps = "\n".join(f"""        <div class="step reveal">
          <h3>{t}</h3>
          <p>{d}</p>
        </div>""" for t, d in s["steps"])
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
                   "url": BASE + "/contact/"}},
        local_business(),
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": plain(q),
                         "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                        for q, a in s["faqs"]]}]

    return head(title, desc, path, schema=schema) + header("/services/") + f"""
<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <p class="tagline">{TAGLINE}</p>
      <h1>{s['h1']}</h1>
      <p class="lede">{s['short']}</p>
      <div class="btn-row">
        {call_primary()}
        <a class="btn btn--ghostDark" href="/contact/?type={_q(plain(s['type']))}">Or request a quote</a>
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
        <p>{s['body2']}</p>
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

{call_strip(f"Questions about {plain(s['name']).lower()}?",
            "One call and we can usually tell you what your slab needs, roughly what it costs, "
            "and when we could get to it.")}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Straight talk</p>
      <h2>{s['why_h']}</h2>
    </div>
    <div class="wrap--narrow" style="padding:0;margin:0">
        {why_ps}
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How the install runs</p>
      <h2>Four steps, no surprises</h2>
      <p class="lede">You will know the schedule, the price and the cure dates before we start grinding.</p>
    </div>
    <div class="grid grid--2 steps">
{steps}
    </div>
    <div class="btn-row" style="margin-top:2.5rem">
      {call_primary()}
      <a class="btn btn--ghostDark" href="/contact/?type={_q(plain(s['type']))}">Request a quote</a>
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
          {call_primary()}
          <a class="btn btn--ghost" href="/contact/?type={_q(plain(s['type']))}">Get my free quote</a>
        </div>
      </div>
      <div>
        <p class="eyebrow">Where we do it</p>
        <h2 style="font-size:clamp(1.5rem,3vw,2.1rem)">{plain(s['name'])} near you</h2>
        <p>Available everywhere in our {AREA['radiusMiles']}+ mile service area. These are the towns we
        work in most often &mdash; if yours is not listed, call anyway.</p>
        <ul class="link-grid" style="margin-top:1.25rem">
{loc_links()}
        </ul>
        <p style="margin-top:1.1rem"><a class="arrow-link" href="/service-area/">Full service area <span aria-hidden="true">&rarr;</span></a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Questions</p>
      <h2>{plain(s['name'])} FAQs</h2>
    </div>
    {faq_html(s['faqs'])}
    <p style="margin-top:1.5rem;text-align:center">
      <a class="arrow-link" href="/faq/">All epoxy flooring FAQs <span aria-hidden="true">&rarr;</span></a>
    </p>
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
      img="hero-high-gloss-epoxy-warehouse-1280.jpg",
      alt="Large commercial interior with a high-gloss epoxy floor &mdash; the finish we install on Champaign, IL floors",
      intro="Champaign is home base &mdash; owned and run by {owners}, with most jobs inside a twenty-minute drive.",
      local="<p>Two kinds of slab in this town, and which one you have decides most of the quote.</p><ul><li><strong>Old Town, Clark Park, Beardsley Park, West Church &amp; University</strong> &mdash; 1940s&ndash;70s detached garages. Real cracking and salt-spalled aprons. Repair first.</li><li><strong>Trails at Brittany, Ironwood, Cherry Hills, Boulder Ridge, Sawgrass</strong> &mdash; 1990s-on three-car slabs. Flat and sound; grind and coat.</li><li><strong>North Market St, Apollo Dr, Interstate Dr, Neil St</strong> &mdash; commercial floors, heavier traffic, phased overnight installs.</li></ul>",
      garage="<p>Hot tires off I-57 and I-74, then road salt December to March. Both kill a cheap floor.</p><ul><li>We grind, repair the concrete, and use a system rated for hot-tire pickup.</li><li>Older neighborhoods: budget for crack and apron repair. Newer: budget goes into the finish.</li><li>Most two- and three-car garages are a one- to two-day install.</li></ul>",
      area="Ten minutes from Memorial Stadium &mdash; easy to schedule, single-bay jobs included.",
      nearby=["Urbana", "Savoy", "Tolono", "Mahomet"]),

 dict(slug="epoxy-flooring-urbana-il", city="Urbana", county="Champaign County",
      img="epoxy-garage-floor-interior.jpg",
      alt="Garage interior with a smooth gray floor and storage shelving, like the detached garages we coat in Urbana, IL",
      intro="Urbana is ten minutes from where we keep the equipment &mdash; one of the easiest towns to schedule, small jobs included.",
      local="<p>Older housing stock than most of the county, and it shows up in the concrete.</p><ul><li><strong>Leal, Historic East Urbana, downtown, Crystal Lake Park</strong> &mdash; pre-1940 detached garages. Thin slabs, hairline cracks, spalled aprons. All repairable.</li><li><strong>Ambucs, Crystal Lake ranches, Stone Creek</strong> &mdash; better concrete, up to flat modern three-car slabs.</li><li><strong>Carle campus, Lincoln Square, Market at the Square</strong> &mdash; low-odor products and overnight turnarounds.</li></ul>",
      garage="<p>Mostly detached garages that have stood sixty or seventy years. They need more prep than a new build.</p><ul><li>Chase and fill cracks, patch the spalled apron, grind the slab, then coat.</li><li>Skip that and the coating peels off the patches first.</li><li>Flake is popular here &mdash; it hides repaired areas far better than solid color.</li></ul>",
      area="Right next to base, so no trip charge and usually a look within a few days.",
      nearby=["Champaign", "St. Joseph", "Savoy", "Rantoul"]),

 dict(slug="epoxy-flooring-savoy-il", city="Savoy", county="Champaign County",
      img="garage-storage-cabinets-gray-floor.jpg",
      alt="Empty residential garage with storage cabinets and a smooth gray floor, like the newer slabs we coat in Savoy, IL",
      intro="Savoy is ten minutes south of Champaign on Neil Street, and the concrete under it is some of the best we work on.",
      local="<p>Savoy grew late and fast &mdash; almost all of it post-1995, which is close to the ideal starting point.</p><ul><li><strong>Prairie Fields, Curtis Road, Burwash Ave, Windsor &amp; Church</strong> &mdash; thicker, flatter, better-cured slabs. Minimal repair.</li><li>Three-car attached garages are common, and full flake across that footage changes how the space gets used.</li><li><strong>Route 45 corridor, Savoy Plaza, Willard Airport</strong> &mdash; commercial, retail and hangar-adjacent floors.</li></ul>",
      garage="<p>The cleanest version of this job. A slab poured in the last twenty-five years wants joint treatment and a grind, not structural repair.</p><ul><li>Solid color is genuinely on the table here &mdash; it mirrors every imperfection, so it needs flat concrete.</li><li>Dense flake goes down beautifully on this kind of slab too.</li><li>One to two days on site; vehicles back after about a week.</li></ul>",
      area="Ten minutes from base, well inside the radius, no trip charge.",
      nearby=["Champaign", "Tolono", "Urbana", "Monticello"]),

 dict(slug="epoxy-flooring-mahomet-il", city="Mahomet", county="Champaign County",
      img="shop-building-bare-concrete-floor.jpg",
      alt="Steel-sided shop building with a bare concrete floor &mdash; the kind of pole barn slab we coat around Mahomet, IL",
      intro="Mahomet is a fifteen-minute run west on I-74, and it has grown fast enough that we are out there most months.",
      local="<p>What sets Mahomet apart is the outbuildings &mdash; lots run bigger here than in Champaign or Urbana.</p><ul><li><strong>Timberline, Thornewood, Prairieview</strong> and the streets north of I-74 &mdash; modern attached garages, straightforward grind and coat.</li><li><strong>Shops, pole barns and machine sheds</strong> &mdash; often poured after the building and without a vapor barrier. Moisture testing decides the system.</li><li><strong>Near the Sangamon River and Lake of the Woods</strong> &mdash; mid-century garage concrete wanting the usual crack and apron work.</li></ul>",
      garage="<p>Two different jobs here. Newer subdivisions are a clean grind-and-coat; the acreages are shops and barns at two to four times the footage.</p><ul><li>Bigger floor, lower per-foot rate &mdash; but the moisture question comes first. We test either way.</li><li>These buildings double as workshops, so we steer people to full flake with non-slip aggregate.</li><li>It hides everything, grips in snowmelt, and dropped tools do not mark it.</li></ul>",
      area="Fifteen minutes from base, past Lake of the Woods. No trip charge in the village or the acreages.",
      nearby=["Champaign", "Fisher", "Urbana", "Monticello"]),

 dict(slug="epoxy-flooring-rantoul-il", city="Rantoul", county="Champaign County",
      img="high-gloss-epoxy-hangar-floor.jpg",
      alt="Aircraft hangar with a mirror-gloss white epoxy floor, the kind of large-span floor we coat in Rantoul, IL",
      intro="Rantoul is twenty minutes north on I-57, with a building stock unlike anywhere else in the county.",
      local="<p>Chanute Air Force Base left Rantoul far more hangar and warehouse square footage than a town its size would normally have.</p><ul><li><strong>Rantoul National Aviation Center</strong> and the former base buildings &mdash; large, old, decades under traffic. Shot blasting and a high-build system, not a residential coating.</li><li><strong>Base-era 1950s and 60s housing</strong> &mdash; thinner concrete and salt-worn aprons, same as older Urbana. Responds well to repair-and-coat.</li><li><strong>Downtown and Wabash &amp; Erie Park</strong> &mdash; older detached garages, worth quoting individually.</li></ul>",
      garage="<p>Mostly mid-century slabs: fix the concrete first, then coat it.</p><ul><li>The apron by the overhead door is nearly always worst &mdash; it needs patching and re-leveling before anything goes over it.</li><li>Flake is the sensible finish: forgiving over repairs, and it builds in grip.</li><li>Larger detached garages and shop buildings price better per square foot.</li></ul>",
      area="Twenty minutes up I-57, comfortably inside the radius, no trip charge.",
      nearby=["Paxton", "Champaign", "Gibson City", "Urbana"]),

 dict(slug="epoxy-flooring-bloomington-il", city="Bloomington", county="McLean County",
      img="commercial-epoxy-floor-coating.jpg",
      alt="Warehouse interior with a high-gloss epoxy floor, the kind of commercial coating we install in Bloomington, IL",
      intro="Bloomington is our second home market &mdash; fifty minutes up I-74, quoted and scheduled exactly like our own back yard, with no trip charge.",
      local="<p>More architectural range than most Central Illinois cities, and it changes the quote block to block.</p><ul><li><strong>Dimmitt&rsquo;s Grove, Founders&rsquo; Grove</strong> &mdash; Victorians and foursquares with detached carriage garages on old, much-repaired concrete.</li><li><strong>Miller Park and the east side</strong> &mdash; 1950s&ndash;70s ranches. Sound slabs with settlement cracking and spalled aprons.</li><li><strong>Fox Creek, Eagle Crest, Tipton Trails, Grove at Kickapoo Creek</strong> &mdash; big modern three-car garages needing little more than a grind.</li><li><strong>Office and back-of-house floors</strong> &mdash; coated in phases, outside business hours.</li></ul>",
      garage="<p>The same two jobs. Established neighborhoods get the concrete chased, filled and patched first; newer subdivisions get a straight diamond grind.</p><ul><li>Either way you get a system rated for hot-tire pickup.</li><li>A coating that lifts where the car parks is not a floor, it is a callback.</li></ul>",
      area="Fifty minutes up I-74, past Downs and Le Roy. McLean County is a home market: same pricing, no trip charge.",
      nearby=["Normal", "Downs", "Le Roy", "Clinton"]),

 dict(slug="epoxy-flooring-normal-il", city="Normal", county="McLean County",
      img="parking-structure-gray-floor.jpg",
      alt="Smooth, light gray floor running through a large parking structure, like the big floors we coat in Normal, IL",
      intro="Normal sits against Bloomington, so we cover it on the same runs &mdash; and there is no trip charge to come quote.",
      local="<p>Normal splits three ways for us.</p><ul><li><strong>ISU and Uptown</strong> &mdash; rental, retail and small-commercial floors. Fast turnaround between tenants, mops clean.</li><li><strong>Old North Normal, Fairview Park</strong> &mdash; older homes, detached garages, aging concrete.</li><li><strong>Blackstone Trails, Savannah Green, off Raab Road</strong> &mdash; large attached three-car garages on modern slabs. Most of our flake work here.</li><li><strong>The manufacturing corridor</strong> &mdash; heavier build, shot blasting rather than grinding.</li></ul>",
      garage="<p>Mostly newer-subdivision work, and on a clean modern slab the install is quick.</p><ul><li>Grind, treat joints, base coat, broadcast flake, scrape and vacuum, clear topcoat. One to two days.</li><li>Around Old North Normal it is the familiar mid-century slab &mdash; crack and apron repair first.</li><li>Near campus we can schedule around the university calendar, between tenants.</li></ul>",
      area="Same run as Bloomington, straight up I-74. Uptown, ISU and the north side are all no-trip-charge.",
      nearby=["Bloomington", "Hudson", "Towanda", "Le Roy"]),

 dict(slug="epoxy-flooring-decatur-il", city="Decatur", county="Macon County",
      img="metallic-epoxy-floor-finish.jpg",
      alt="Poured amber metallic floor finish in a large interior, the kind of feature floor we install in Decatur, IL",
      intro="Decatur is fifty minutes southwest, well inside our area, and the most industrial market we work in.",
      local="<p>Ag processing and manufacturing means large, hard-used, chemically abused floors &mdash; the sort a thin roll-on coating would not survive a season.</p><ul><li><strong>Industrial slabs</strong> &mdash; shot blasting, full joint and crack treatment, high-build chemical-resistant systems, line striping where traffic needs marking.</li><li><strong>West End Historic District, Millikin University</strong> &mdash; grand early-1900s homes, detached carriage garages, concrete patched more than once.</li><li><strong>Mound Road and Fairview Park ranches</strong> &mdash; more straightforward mid-century slabs.</li><li><strong>South Shores, Lake Decatur</strong> &mdash; detached shops and boat storage. Wet traffic, so non-slip aggregate in the topcoat.</li></ul>",
      garage="<p>Anything from a standard attached two-car to a century-old carriage house.</p><ul><li>On older properties the concrete decides it. We will tell you honestly if a slab is better replaced than coated.</li><li>Where it is sound: grind, chase and fill, patch the spalling, coat, flake, seal.</li><li>Around the lake we recommend non-slip aggregate as standard.</li></ul>",
      area="Fifty minutes southwest via Route 121 or I-72. Decatur, Forsyth, Mt. Zion and Argenta &mdash; no trip charge.",
      nearby=["Forsyth", "Mt. Zion", "Cerro Gordo", "Clinton"]),

 dict(slug="epoxy-flooring-danville-il", city="Danville", county="Vermilion County",
      img="before-bare-shop-concrete-floor.jpg",
      alt="Vehicle service shop with a bare, untreated concrete floor &mdash; the condition we usually start from in Danville, IL",
      intro="Danville is a thirty-five-minute shot east on I-74, putting all of Vermilion County inside our range.",
      local="<p>An industrial history left a lot of older shop and warehouse space, and those floors arrive with every problem at once.</p><ul><li><strong>Shops and warehouses</strong> &mdash; oil-soaked concrete, spalled dock doors, opened joints, old coatings letting go in sheets. Degrease, strip, blast, fix joints, then coat.</li><li><strong>North Street Historic District, Lincoln Park</strong> &mdash; pre-1930 homes, detached alley garages on thin original slabs.</li><li><strong>Vermilion Heights</strong> &mdash; mid-century ranches and attached garages.</li><li>We also cover Tilton, Westville, Georgetown and out toward Kickapoo State Recreation Area.</li></ul>",
      garage="<p>Mostly older-slab work, and the apron is nearly always the problem.</p><ul><li>Freeze-thaw and salt take the top layer off right where the door sits. Coated over unrepaired, it fails there first.</li><li>We patch and re-level the apron, chase and fill cracks, grind, then coat.</li><li>Flake by default &mdash; on a garage standing since the 1920s, there will be repaired areas.</li></ul>",
      area="Thirty-five minutes east on I-74. Danville, Tilton, Westville, Georgetown and Hoopeston are all inside the radius.",
      nearby=["Tilton", "Westville", "Georgetown", "Hoopeston"]),

 dict(slug="epoxy-flooring-monticello-il", city="Monticello", county="Piatt County",
      img="blue-flake-epoxy-garage-floor.jpg",
      alt="Modern garage with a blue and gray flake epoxy floor, the finish we install on shops and garages around Monticello, IL",
      intro="Monticello is twenty-five minutes west on I-72, and Piatt County is well inside the no-trip-charge area.",
      local="<p>Work here skews rural, and that shapes what we quote.</p><ul><li><strong>Acreages and farms</strong> &mdash; detached shops, machine sheds and pole barns. Many poured without a vapor barrier, so moisture testing comes first.</li><li>A coated shop floor pays for itself in how much easier and brighter the building gets.</li><li><strong>Courthouse square, toward Allerton Park</strong> &mdash; mid-century garage concrete wanting the usual crack and apron work.</li><li><strong>Route 105 corridor and the Railway Museum end</strong> &mdash; commercial floors.</li></ul>",
      garage="<p>Often not a garage at all &mdash; it is a thirty-by-forty shop with a workbench down one side.</p><ul><li>Those price better per square foot, and benefit more, because you actually spend time in them.</li><li>For a working shop: full flake with non-slip aggregate. Hides repairs, grips in snowmelt, does not show every mark.</li><li>For an attached garage in a newer village subdivision, a straightforward grind-and-coat.</li></ul>",
      area="Twenty-five minutes west on I-72, past Allerton Park. All of Piatt County is inside the radius.",
      nearby=["Bement", "Cerro Gordo", "Mahomet", "Clinton"]),

 dict(slug="epoxy-flooring-tuscola-il", city="Tuscola", county="Douglas County",
      img="showroom-epoxy-floor-graphics.jpg",
      alt="Coated floor with black and red inlaid graphics, the kind of retail finish we install in Tuscola, IL",
      intro="Tuscola sits half an hour south where I-57 meets US-36, and that crossroads is a big part of what we get called out for.",
      local="<p>Between the interstate junction and Tanger Outlets, Tuscola punches well above its size commercially.</p><ul><li><strong>Route 36 corridor</strong> &mdash; retail units, service bays and light industrial. Hard-wearing solid color or flake, clear urethane topcoat, line striping.</li><li><strong>Douglas County courthouse, Ervin Park</strong> &mdash; older homes, detached garages on original concrete.</li><li><strong>Ag country in every direction</strong> &mdash; machine sheds, grain shops and equipment buildings. Every rural slab gets moisture tested.</li></ul>",
      garage="<p>The full spread, from a two-car attached to a farm shop big enough to pull a combine into.</p><ul><li>Small end: grind-and-coat over sound concrete.</li><li>Large end: the per-foot rate drops, but a slab without a vapor barrier needs a system that tolerates it.</li><li>Older in-town garages: thin slab, cracked middle, spalled apron &mdash; repaired before coating, not after.</li></ul>",
      area="Half an hour south at the I-57 and US-36 junction. Tuscola, Arcola, Villa Grove and Arthur are all inside the radius.",
      nearby=["Arcola", "Villa Grove", "Arthur", "Tolono"]),

 dict(slug="epoxy-flooring-paxton-il", city="Paxton", county="Ford County",
      img="shop-building-bare-concrete-floor.jpg",
      alt="Steel-sided farm shop with a bare concrete floor &mdash; the kind of slab we prepare and coat around Paxton, IL",
      intro="Paxton is thirty-five minutes north on I-57, and Ford County sits comfortably inside the fifty-mile radius.",
      local="<p>A county seat in the middle of some of the most productive farmland in Illinois, and the floors follow from that.</p><ul><li><strong>Grain shops, equipment sheds and ag service buildings</strong> &mdash; most of the larger footage. Usually no vapor barrier, years of dirt, chemical and steel-wheel traffic.</li><li>Those get moisture tested, degreased, blasted or ground hard, then a build heavy enough for equipment rather than cars.</li><li><strong>Ford County courthouse, Pells Park</strong> &mdash; pre-war and mid-century homes, detached garages needing crack and apron repair.</li><li><strong>US-45 corridor</strong> &mdash; a steady run of small commercial work.</li></ul>",
      garage="<p>Usually one of two things: an older detached garage in town, or a farm shop several times the size.</p><ul><li>In-town garages: fix the concrete first, then flake &mdash; the most forgiving finish over repairs, and it adds winter grip.</li><li>Working shops: flake with non-slip aggregate, because those floors get wet and get walked on in boots.</li><li>No trip charge to come out and look either way.</li></ul>",
      area="Thirty-five minutes north on I-57, past Rantoul and Gibson City. All of Ford County is inside the radius.",
      nearby=["Rantoul", "Gibson City", "Champaign", "Hoopeston"]),

 dict(slug="epoxy-flooring-clinton-il", city="Clinton", county="DeWitt County",
      img="parking-structure-gray-floor.jpg",
      alt="Smooth, light gray floor in a large parking structure, like the storage and shop buildings we coat around Clinton, IL",
      intro="Clinton is forty-five minutes west, halfway to Bloomington, and DeWitt County is inside our radius with no trip charge.",
      local="<p>A small county seat with a mix we do not see everywhere.</p><ul><li><strong>Courthouse square, C.H. Moore Homestead</strong> &mdash; pre-war and mid-century detached garages, original concrete, the usual cracking and apron spalling.</li><li><strong>Clinton Power Station and area industry</strong> &mdash; real build thickness and chemical resistance, not a residential-grade coating.</li><li><strong>Clinton Lake and Weldon Springs</strong> &mdash; detached shops, boat and RV storage. Wet traffic, so non-slip aggregate as standard.</li><li>Rural shops and machine sheds across DeWitt County &mdash; every one moisture tested first.</li></ul>",
      garage="<p>A good example of why we quote on site. A garage near the square and a forty-foot storage building by the lake are the same service on paper and different jobs in practice.</p><ul><li>What does not change: test the slab, fix the concrete, grind it open, then coat.</li><li>Near the water we push hard for non-slip aggregate &mdash; lake water and a trailer on smooth coating is genuinely slick.</li></ul>",
      area="Forty-five minutes west, an easy run out Route 54. Clinton, Farmer City and Clinton Lake are inside the radius.",
      nearby=["Farmer City", "Bloomington", "Decatur", "Monticello"]),

 dict(slug="epoxy-flooring-tolono-il", city="Tolono", county="Champaign County",
      img="epoxy-garage-floor-interior.jpg",
      alt="Garage interior with a smooth gray floor and storage shelving, like the village garages we coat in Tolono, IL",
      intro="Tolono is fifteen minutes south on US-45 &mdash; one of the closest towns on this list and one of the easiest to fit into a week.",
      local="<p>A village of a few thousand surrounded immediately by farmland, which gives us a nice split of work.</p><ul><li><strong>The historic rail crossing and Tolono Community Park</strong> &mdash; detached garages on mid-century concrete. Thin slabs, cracked middles, spalled aprons, all worth repairing properly.</li><li><strong>Newer subdivisions and the Unity school campus</strong> &mdash; modern pours needing little more than a diamond grind.</li><li><strong>Outside the village</strong> &mdash; machine sheds, grain shops and equipment buildings, where the bigger footage is. Moisture tested without exception.</li></ul>",
      garage="<p>Quick for us to schedule &mdash; fifteen minutes from base, so we can look almost any day, and obviously no trip charge.</p><ul><li>Newer subdivision slabs: straight grind-and-coat, one to two days, and solid color is a real option.</li><li>Older village garages: repair first, then flake to hide the patches and add grip.</li><li>Farm shops: moisture test, heavier build, non-slip aggregate in the topcoat.</li></ul>",
      area="Fifteen minutes south on US-45. Tolono, Philo, Sidney and Pesotum are all a short run from base.",
      nearby=["Champaign", "Savoy", "Philo", "Tuscola"]),
]

for _l in LOCATIONS:
    _c, _co = _l["city"], _l["county"]
    _l["service"] = "Epoxy Flooring"
    _l["h1"] = f"Epoxy Flooring in {_c}, IL"
    _l["h2_garage"] = f"Garage Floor Coating in {_c}, IL"
    _l["title"] = f"Epoxy Flooring {_c} IL | Garage Floor Coating {_c} IL"
    _l["desc"] = (f"Epoxy flooring and garage floor coating in {_c}, IL. Garage, basement, flake, "
                  f"metallic and commercial epoxy across {_co}. Free quotes.")

LOC_BY_SLUG = {l["slug"]: l for l in LOCATIONS}

def loc_links(limit=None, dark=False, exclude=None):
    items = [l for l in LOCATIONS if l["slug"] != exclude]
    if limit: items = items[:limit]
    return "\n".join(
        f'      <li><a class="link-card" href="/{l["slug"]}/">{I["pin"]}'
        f'<span>Epoxy Flooring in {l["city"]}, IL</span>'
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
    trail = [("Home", "/"), ("Service Area", "/service-area/"), (f"Epoxy Flooring in {l['city']}", None)]
    intro = l["intro"].format(name=NAME, owners=OWNER_PAIR)
    nearby = ", ".join(l["nearby"])

    schema = [crumb_schema(trail), local_business(), {
        "@context": "https://schema.org", "@type": "Service",
        "@id": BASE + path + "#service",
        "name": f"Epoxy Flooring in {l['city']}, IL",
        "serviceType": "Epoxy flooring",
        "description": plain(l["desc"]),
        "url": BASE + path,
        "provider": {"@id": BASE + "/#business"},
        "areaServed": {"@type": "City", "name": f"{l['city']}, IL",
                       "containedInPlace": {"@type": "AdministrativeArea",
                                            "name": f"{l['county']}, Illinois"}},
        "hasOfferCatalog": {"@type": "OfferCatalog",
                            "name": f"Epoxy flooring services in {l['city']}, IL",
                            "itemListElement": [
                                {"@type": "Offer", "itemOffered": {
                                    "@type": "Service", "name": plain(sv["name"]),
                                    "url": BASE + "/services/" + sv["slug"] + "/"}}
                                for sv in SERVICES]},
        "offers": {"@type": "Offer", "priceCurrency": "USD", "url": BASE + "/contact/",
                   "availability": "https://schema.org/InStock"}}]

    return head(l["title"], l["desc"], path, schema=schema) + header("") + f"""
<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <p class="tagline">{TAGLINE}</p>
      <h1>{l['h1']}</h1>
      <p class="lede">{intro}</p>
      <div class="btn-row">
        {call_primary()}
        {quote_btn("btn--ghostDark")}
      </div>
      <p class="form-note" style="color:#9FADBF;margin:1rem 0 0;font-size:.92rem">
        Free, on-site and itemized &mdash; and no trip charge anywhere we work.
      </p>
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
        {l['local']}
        <div class="local-note">
          <strong>Serving {l['city']} and {nearby}.</strong> {l['county']} is inside our
          {AREA['radiusMiles']}+ mile radius, so there is no trip charge to come out and quote your floor.
        </div>
        <div class="btn-row">
          {call_primary()}
          {quote_btn("btn--ghost")}
        </div>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/{l['img']}" alt="{l['alt']}" width="1280" height="854" loading="lazy" decoding="async">
      </div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="split split--flip">
      <div>
        <p class="eyebrow">Garages</p>
        <h2>{l['h2_garage']}</h2>
        {l['garage']}
        <div class="btn-row" style="margin-top:1.75rem">
          <a class="btn btn--onDark" href="/contact/?type=Garage">Quote my garage floor</a>
          <a class="btn btn--ghostDark" href="/services/garage-floor-epoxy/">Garage floor epoxy</a>
        </div>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/blue-flake-epoxy-garage-floor.jpg"
             alt="Blue and gray flake epoxy garage floor, the finish we install on garages in {l['city']}, IL"
             width="1280" height="854" loading="lazy" decoding="async">
      </div>
    </div>
  </div>
</section>

{call_strip(f"Epoxy floor quote in {l['city']}?",
            f"Call and tell us the room. We cover {l['county']} with no trip charge, and we can "
            "usually say on the phone roughly what your slab will need.")}

<section class="section section--paper2">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Service area</p>
        <h2>Where {l['city']} sits in our range</h2>
        <p>{l['area']}</p>
        <p>{l['city']}, {nearby} and the rest of {l['county']} are inside our
        {AREA['radiusMiles']}-mile radius &mdash; no trip charge. Call
        <a href="tel:{TEL}"><strong>{PHONE}</strong></a> for a date.</p>
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
      <p class="lede">All six services are available across {l['county']} and the surrounding towns.</p>
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
{loc_links(exclude=l['slug'], dark=True)}
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
         "Honest pricing, realistic timelines, and a plain-English explanation of what we are doing and why. If epoxy is wrong for your floor, we will say so."),
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
        <p>We started {NAME} because we kept seeing epoxy floors that looked incredible for one
        season and lifted by the next winter. The coating was almost never the problem.
        <strong>The prep was.</strong></p>
        <p>So that is the part we refuse to rush: every floor mechanically profiled, every crack
        chased and filled, every slab moisture-checked <em>before</em> we quote it. Slower &mdash; and
        the whole difference between fifteen years and next spring.</p>
        <p>When you hire us, <strong>you get us</strong>. Drayton and Dylan measure, run the grinder and
        answer the phone. No commissioned salesperson, no crew you have never met.</p>
        <p>We live and work here. Word travels fast in Central Illinois, and we would rather earn the
        next job than close this one.</p>
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

{call_strip("Talk to an owner, not a call center",
            "When you ring this number, one of the two people whose faces are on the truck picks it up.")}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Epoxy, and only epoxy</p>
      <h2>We do one thing on purpose</h2>
    </div>
    <div class="wrap--narrow" style="padding:0;margin:0">
      <p><strong>{NAME} installs epoxy floors.</strong> Not general flooring, not concrete work with
      a sideline &mdash; one trade, on purpose.</p>
      <p>Epoxy is unforgiving: everything that decides whether a floor lasts fifteen years or fifteen
      months happens before the coating goes down &mdash; the profile, the moisture test, the crack
      work, the recoat window. Get one wrong and the floor looks perfect on handover and fails a year
      later.</p>
      <p>Doing one job over and over is where the judgement comes from &mdash; how a 1950s Urbana slab
      differs from a 2010 Savoy pour, what a Mahomet pole barn floor does without a vapor barrier under
      it.</p>
      <p>It also means we will tell you when epoxy is the <em>wrong</em> answer &mdash; a slab too far
      gone, a water problem that needs solving first. We would rather lose a job than install one we
      know will not hold. In a market this size, our floors are the advertising.</p>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">What it is like to work with us</p>
      <h2>No surprises, start to finish</h2>
    </div>
    <div class="grid grid--3 steps">
      <div class="step reveal"><h3>You get a real number</h3>
        <p>Itemized and in writing, broken out so you can see what the prep costs, what the system costs
        and what any extras cost. Not a range, not a per-square-foot rate multiplied out on a phone
        &mdash; an actual quote for your actual floor, after we have stood on it.</p></div>
      <div class="step reveal"><h3>You get real dates</h3>
        <p>Install days and cure dates, written down before we start. Cure times move with temperature and
        humidity, so we would rather tell you to wait two extra days than watch tire marks press
        permanently into a floor that was still green.</p></div>
      <div class="step reveal"><h3>You get the space back clean</h3>
        <p>Grinding is dusty and we run vacuum shrouds and HEPA extraction to keep it contained. Whatever
        film is left, we clean up ourselves. Your driveway, shop or basement should look better when we
        pull out than it did when we pulled in.</p></div>
    </div>
    <div class="btn-row btn-row--center" style="margin-top:2.5rem">
      {call_primary()}
      {quote_btn("btn--ghost")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--flip">
      <div>
        <p class="eyebrow">The owners</p>
        <h2>{OWNER_PAIR}</h2>
        <p class="lede">Two owners, one crew, and both names on the truck.</p>
        <p>We handle everything from first call to final walkthrough &mdash; measure, moisture test,
        quote, grind, coat, care sheet. Nothing subcontracted.</p>
        <p>So when we say the floor is ready Thursday, it is the person standing on it Thursday saying
        so &mdash; and nobody to point at but us if something is not right.</p>
        <div class="btn-row" style="margin-top:1.75rem">
          {call_primary()}
          {quote_btn("btn--ghost")}
        </div>
      </div>
      <div class="split__media split__media--tall reveal">
        <img src="{IMG}/applying-epoxy-floor-coating-roller.jpg"
             alt="Applicator spreading a fresh yellow floor coating with a long-handled squeegee"
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
      {call_primary()}
      {quote_btn("btn--ghost", "Don&rsquo;t see your town? Ask us")}
    </div>
  </div>
</section>

{call_strip("Not sure if you are in range?",
            "Call and ask. The radius is a guideline, not a fence &mdash; we say yes far more often "
            "than we say no.")}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Around the region</p>
      <h2>What changes from one county to the next</h2>
    </div>
    <div class="wrap--narrow" style="padding:0;margin:0">
      <ul>
        <li><strong>Champaign County</strong> &mdash; home, and the widest spread of slabs we see.
        Older Urbana and pre-war Champaign need real crack and apron repair; Savoy, Tolono and southwest
        Champaign mostly want a grind; Mahomet adds pole barns (and the moisture question); Rantoul adds
        hangar-scale floors.</li>
        <li><strong>McLean County</strong> &mdash; Bloomington-Normal, fifty minutes up I-74, treated as
        a home market: same pricing, same scheduling, no trip charge. Skews commercial.</li>
        <li><strong>Piatt, Douglas, Ford &amp; DeWitt</strong> &mdash; the rural belt: Monticello,
        Tuscola, Paxton, Clinton. Mostly machine sheds and grain-operation shops, often poured without a
        vapor barrier &mdash; moisture testing decides the system. Per-foot rates drop as floors grow.</li>
        <li><strong>Macon &amp; Vermilion</strong> &mdash; Decatur and Danville, our most industrial
        markets: heavier builds, shot blasting, degreasing decades of oil, line striping &mdash; plus
        excellent older housing with detached garages that reward proper prep.</li>
      </ul>
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
        <ul>
          <li>If we tell you Tuesday, we mean Tuesday &mdash; we are not stacking jobs across half the
          state and hoping the weather holds.</li>
          <li>Epoxy has cure windows, and cure windows do not care about traffic. If the topcoat is due
          eighteen hours after the base, somebody has to be standing on it eighteen hours later. We are
          twenty minutes from most of our jobs.</li>
          <li>And months later, when you have a question about a mark near the door &mdash; or a second
          building to do &mdash; swinging by is not a half-day expedition. That is how a job becomes a
          customer.</li>
        </ul>
        <div class="btn-row" style="margin-top:1.75rem">
          {btn("Get a Free Quote", "/contact/", "btn--onDark")}
        </div>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/high-gloss-epoxy-hangar-floor.jpg"
             alt="Aircraft hangar with a mirror-gloss white epoxy floor"
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


# ========================================================= COLORS & FINISHES ==
def page_colors():
    path = "/colors-and-finishes/"
    trail = [("Home", "/"), ("Colors &amp; Finishes", None)]
    title = "Epoxy Colors &amp; Finishes | Flake &amp; Metallic Blends | Central Illinois"
    desc = ("Flake and metallic epoxy colors from DP Flooring Services. Storm Grey, Onyx Black, "
            "Ocean Blue and more, with typical per-square-foot pricing. Samples at every free quote.")

    fin = "\n".join(f"""      <article class="fincard reveal">
        <div class="fincard__media">
          <img src="{IMG}/{f['img']}" alt="{f['alt']}" width="1280" height="854" loading="lazy" decoding="async">
        </div>
        <div class="fincard__body">
          <h3>{f['name']}</h3>
          <p>{f['blurb']}</p>
          <p class="fincard__price"><b>{f['price']}</b><span>typical / sq&nbsp;ft</span></p>
          <a class="arrow-link" href="/contact/">Quote this finish <span aria-hidden="true">&rarr;</span></a>
        </div>
      </article>""" for f in CFG["finishes"])

    def swatches(kind):
        return "\n".join(f"""      <figure class="swatch reveal">
        <div class="swatch__media">
          <img src="/assets/img/colors/{c['file']}" alt="{c['name']} &ndash; {kind} epoxy colour swatch"
               width="560" height="560" loading="lazy" decoding="async">
        </div>
        <figcaption><b>{c['name']}</b><span>{c['note']}</span></figcaption>
      </figure>""" for c in CFG["colors"][kind])

    schema = [crumb_schema(trail), local_business(), {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": "Epoxy floor colors and finishes",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": c["name"], "description": c["note"]}
            for i, c in enumerate(CFG["colors"]["flake"] + CFG["colors"]["metallic"])]}]

    return head(title, desc, path, schema=schema) + header(path) + f"""
<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <p class="tagline">{TAGLINE}</p>
      <h1>Explore Our Colors &amp; Finishes</h1>
      <p class="lede">Custom epoxy floors for garages, shops and patios across Champaign County
      &mdash; pick a blend, we bring the samples.</p>
      <div class="btn-row">
        {btn("Get My Free Quote", "/contact/", "btn--onDark")}
        {call_btn()}
      </div>
    </div>
  </div>
</section>

<main id="main">

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Finish types</p>
      <h2>Three systems. Same prep underneath.</h2>
      <p class="lede">Every floor is diamond ground, repaired and sealed the same way. What changes
      is the coat that goes on top, and what it costs per square foot.</p>
    </div>
    <div class="fincards">
{fin}
    </div>
    <p class="pricenote">Typical installed pricing per square foot. The number on your floor moves with
    square footage, slab condition and how much repair it needs first &mdash; every quote is free,
    on site and itemized.</p>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Flake blends</p>
      <h2>Flake colors</h2>
      <p class="lede">Vinyl chips broadcast into the base coat to refusal, then scraped, vacuumed and
      sealed under clear urethane. Any blend below, or bring us one of your own.</p>
    </div>
    <div class="swatches">
{swatches("flake")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Metallic pours</p>
      <h2>Metallic colors</h2>
      <p class="lede">Pigment moves through the resin as it levels, so the pattern is created live on
      your floor. Nobody can reproduce one exactly twice &mdash; including us.</p>
    </div>
    <div class="swatches swatches--4">
{swatches("metallic")}
    </div>
    <p class="pricenote"><b>Metallic swatches are rendered colour references, not photographs of
    installed floors.</b> A metallic pour never looks the same twice and screens shift colour either
    way, so treat these as the palette rather than the exact result. We bring real sample boards to
    every estimate so you are choosing off the actual product.</p>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Choosing</p>
      <h2>How to pick the right one</h2>
    </div>
    <ul class="features">
      <li>{I['grid']}<div><b>Match the mess, not the mood board</b><span>Darker blends and busier
      flake hide tire marks, salt and sawdust between cleanings. A near-white solid floor looks
      incredible on day one and shows every footprint on day two. Think about what actually lands on
      your floor before you pick.</span></div></li>
      <li>{I['sparkle']}<div><b>Flake forgives, solid does not</b><span>A solid color is a mirror: every
      trowel mark and repaired crack telegraphs through it in raking light. If your slab has history,
      flake breaks the surface up visually and the repairs disappear.</span></div></li>
      <li>{I['home']}<div><b>Look at it under your own lights</b><span>Storm Grey under a cool LED shop
      fixture and Storm Grey under a warm garage bulb are two different floors. This is exactly why we
      leave sample boards with you rather than asking you to decide off a screen.</span></div></li>
      <li>{I['shield']}<div><b>Add grip where it gets wet</b><span>Flake carries a little texture on its
      own. On a patio, a walkout basement or a garage that sees winter slush, we broadcast a fine
      non-slip aggregate into the topcoat &mdash; it costs very little and it changes how the floor
      behaves underfoot.</span></div></li>
    </ul>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Every floor, every color</p>
      <h2>What the price includes</h2>
    </div>
    <ul class="checks checks--dark">
      <li>{I['check']}<span>Diamond grinding to open the concrete profile &mdash; never an acid etch</span></li>
      <li>{I['check']}<span>Crack chasing, pit filling and spall repair before any color goes down</span></li>
      <li>{I['check']}<span>Moisture testing, with the base coat specified to match the readings</span></li>
      <li>{I['check']}<span>Full-broadcast flake or a hand-worked metallic pour, depending on your pick</span></li>
      <li>{I['check']}<span>Clear polyaspartic or urethane topcoat for UV and scuff resistance</span></li>
      <li>{I['check']}<span>Cleanup, a written care sheet, and exact cure dates before we leave</span></li>
    </ul>
  </div>
</section>

{call_strip("Not sure which blend suits your slab?",
            "Tell us the room and what happens on that floor. We will tell you straight away which "
            "finishes make sense and which ones we would talk you out of.")}

<section class="section">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Color questions</p>
      <h2>Asked before every install</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Can I get a custom blend?</summary>
        <div class="faq__a"><p>Yes. The fifteen flake blends here are the ones we keep in stock, but chips
        come in dozens of colors and we mix to order &mdash; team colors, a match to your cabinets, or
        a tweak to one of ours. Bring a photo or a paint chip to the estimate and we will get close.
        Custom blends can add a few days of lead time.</p></div>
      </details>
      <details>
        <summary>Will the color fade?</summary>
        <div class="faq__a"><p>Not under the topcoat we use. Bare epoxy ambers in sunlight, which is why
        every floor we install is sealed with a UV-stable polyaspartic or urethane clear. In a garage or
        basement it is a non-issue. On a patio or anywhere with direct sun, the topcoat is doing real
        work &mdash; and it is one of the reasons we do not skip it to save a few dollars.</p></div>
      </details>
      <details>
        <summary>How closely will my floor match the sample?</summary>
        <div class="faq__a"><p>Flake matches closely, because the chips are a manufactured product and
        the blend is measured. Metallic is different by nature: the pigment moves as the resin levels,
        so your floor will share the sample's palette and character but the pattern will be its own.
        If you need predictability, flake is the safer pick.</p></div>
      </details>
    </div>
  </div>
</section>

{cta_band("Want to see it in person?",
          "We bring samples to every free estimate &mdash; real boards, in your space, under your "
          "own lighting. No charge, no obligation, and no trip fee anywhere in our service area.",
          "Get My Free Quote")}
</main>
""" + footer()

# ================================================================== GALLERY ==
# (file, label, [categories]) - label is what shows under the tile.
# Categories drive the filter tabs. Anything named "placeholder-*" is a slot
# waiting on a real project photo.
GALLERY_ITEMS = [
 # --- the client's own completed jobs -------------------------------------
 ("dp-job-garage-floor-1.jpg",           "Flake &mdash; Completed Garage",    ["flake","garage"],
  "Completed residential garage floor installed by DP Flooring Services"),
 ("dp-job-garage-floor-2.jpg",           "Flake &mdash; Completed Garage",    ["flake","garage"],
  "Finished garage floor with a flake epoxy coating, installed by DP Flooring Services"),
 ("dp-job-garage-floor-3.jpg",           "Flake &mdash; Completed Garage",    ["flake","garage"],
  "Coated garage floor on a completed DP Flooring Services job"),
 # --- garages ---------------------------------------------------------------
 ("blue-flake-epoxy-garage-floor.jpg",   "Flake &mdash; 2-Car Garage",        ["flake","garage"],
  "Modern garage finished with a blue and gray flake epoxy floor"),
 ("metallic-epoxy-garage-floor.jpg",     "Metallic &mdash; Feature Garage",   ["metallic","garage"],
  "Residential garage with a deep blue and silver metallic epoxy floor under accent lighting"),
 # Plain coated slab, no flake in the photo - so it is not filed under "flake".
 ("epoxy-garage-floor-interior.jpg",     "Solid &mdash; Garage Workshop",     ["garage"],
  "Garage interior with a smooth gray coated floor and open storage shelving"),
 ("garage-storage-cabinets-gray-floor.jpg","Solid &mdash; Garage &amp; Storage", ["garage"],
  "Empty residential garage with storage cabinets and a smooth gray floor"),
 # --- patios & steps --------------------------------------------------------
 ("patio-flake-covered-porch.jpg",       "Flake &mdash; Covered Porch",       ["flake","patio"],
  "Covered back porch at dusk with a gray and white flake epoxy floor"),
 ("patio-flake-open-patio.jpg",          "Flake &mdash; Backyard Patio",      ["flake","patio"],
  "Open backyard patio slab coated in tan and brown flake epoxy"),
 ("stairs-flake-front-steps.jpg",        "Flake &mdash; Front Entry Steps",   ["flake","patio"],
  "Exterior concrete front entry steps coated in dark gray flake epoxy"),
 # --- interiors -------------------------------------------------------------
 ("basement-flake-floor.jpg",            "Flake &mdash; Finished Basement",   ["flake"],
  "Finished residential basement with a light gray and white flake epoxy floor"),
 ("shop-flake-epoxy-floor.jpg",          "Flake &mdash; Shop &amp; Pole Barn",["flake","commercial"],
  "Workshop interior with a dark gray flake epoxy floor running the length of the building"),
 ("decorative-flake-epoxy-floor-finish.jpg","Flake &mdash; Full Broadcast",   ["flake"],
  "Close-up of a gray and white speckled full-broadcast flake finish"),
 # --- commercial ------------------------------------------------------------
 ("metallic-epoxy-lobby-floor.jpg",      "Metallic &mdash; Office Lobby",     ["metallic","commercial"],
  "Commercial office lobby with a charcoal and silver metallic epoxy floor"),
 ("metallic-epoxy-floor-finish.jpg",     "Metallic &mdash; Feature Floor",    ["metallic","commercial"],
  "Large interior with a poured amber metallic floor finish and dark steel columns"),
 ("showroom-epoxy-floor-graphics.jpg",   "Solid &mdash; Showroom Graphics",   ["commercial"],
  "Coated floor with black and red inlaid graphics beside a ribbed metal wall"),
 ("car-showroom-epoxy-floor.jpg",        "Solid &mdash; Dealership Showroom", ["commercial"],
  "Car showroom with a high-gloss coated floor reflecting the vehicles on display"),
 ("commercial-epoxy-floor-coating.jpg",  "Solid &mdash; Warehouse Floor",     ["commercial"],
  "Warehouse interior with a freshly installed high-gloss epoxy floor"),
 ("high-gloss-epoxy-hangar-floor.jpg",   "Solid &mdash; Hangar Bay",          ["commercial"],
  "Aircraft hangar with a mirror-gloss white epoxy floor"),
 ("commercial-floor-coating-line-striping.jpg","Solid &mdash; Safety Striping",["commercial"],
  "Close-up of a coated commercial floor with painted directional arrows and a red safety stripe"),
 ("parking-structure-gray-floor.jpg",    "Solid &mdash; Parking Structure",   ["commercial"],
  "Smooth, light gray floor running through a large parking structure"),
]

GALLERY_FILTERS = [("all","All"), ("flake","Flake"), ("metallic","Metallic"),
                   ("garage","Garage"), ("patio","Patio"), ("commercial","Commercial")]

def page_gallery():
    path = "/gallery/"
    trail = [("Home", "/"), ("Gallery", None)]
    title = "Epoxy Floor Gallery | Before &amp; After Projects | Central Illinois"
    desc = ("Epoxy floor gallery from DP Flooring Services - garage, patio, commercial and metallic "
            "floors, plus before-and-after comparisons showing what surface prep does.")

    tabs = "\n".join(
        f'        <button class="ftab{" is-active" if k == "all" else ""}" type="button" '
        f'data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{lab}</button>'
        for k, lab in GALLERY_FILTERS)

    tiles = "\n".join(f"""      <figure class="gtile reveal" data-cats="{' '.join(cats)}">
        <button class="gtile__btn" type="button" data-full="{IMG}/{f}" data-caption="{lab}">
          <img src="{IMG}/{f}" alt="{alt}" width="1280" height="854" loading="lazy" decoding="async">
          <span class="gtile__zoom" aria-hidden="true">{I['grid']}</span>
        </button>
        <figcaption>{lab}</figcaption>
      </figure>""" for f, lab, cats, alt in GALLERY_ITEMS)

    pairs = "\n".join(ba_html(pr) for pr in PAIRS[:4])

    schema = [crumb_schema(trail), local_business(), {
        "@context": "https://schema.org", "@type": "ImageGallery",
        "name": "DP Flooring Services epoxy floor gallery", "url": BASE + path}]

    return head(title, desc, path, schema=schema) + header(path) + f"""
<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <p class="tagline">{TAGLINE}</p>
      <h1>See the Transformation</h1>
      <p class="lede">Real floors installed across Champaign County &mdash; garages, patios,
      shops and commercial space, in flake, solid color and poured metallic.</p>
      <div class="btn-row">
        {btn("Get My Free Quote", "/contact/", "btn--onDark")}
        {call_btn()}
      </div>
    </div>
  </div>
</section>

<main id="main">

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">The work</p>
      <h2>Browse by floor type</h2>
    </div>

    <div class="ftabs" role="group" aria-label="Filter the gallery by floor type">
{tabs}
    </div>

    <div class="gallery" id="galleryGrid">
{tiles}
    </div>
    <p class="gempty" id="galleryEmpty" hidden>Nothing in that category yet &mdash; call
      <a href="tel:{TEL}">{PHONE}</a> and we&rsquo;ll send recent photos straight to your phone.</p>

    <p class="pricenote" style="margin-top:1.75rem">Tiles labelled <b>Completed Garage</b> are our own
    finished jobs. The rest are reference images of the systems and finishes we install, captioned by
    floor type &mdash; we swap them for real project photography as each job is shot.</p>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Before &amp; after</p>
      <h2>What prep actually does</h2>
      <p class="lede">Drag any divider. Left is the kind of slab we start from, right is the finish
      the same kind of slab takes once it has been ground, repaired and coated.</p>
    </div>
    <div class="gallery-grid">
{pairs}
    </div>
  </div>
</section>


<section class="section section--paper2">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">By floor type</p>
      <h2>What you&rsquo;re looking at</h2>
      <p class="lede">Same prep on every floor above. What changes is the system on top and what
      that space has to put up with.</p>
    </div>
    <div class="grid grid--3 steps">
      <div class="step reveal">
        <h3>Garage floors</h3>
        <p>Hot tires, road salt and dropped tools. These get a system rated for hot-tire pickup
        and, nine times out of ten, a full flake broadcast &mdash; it hides the repairs an older
        Champaign County slab always needs and adds grip for winter slush.</p>
      </div>
      <div class="step reveal">
        <h3>Patios &amp; porches</h3>
        <p>Outdoor concrete lives with UV and freeze-thaw, so the topcoat is doing real work. We
        spec a UV-stable clear and broadcast non-slip aggregate into it as standard &mdash; a smooth
        coated patio in the rain is not something we&rsquo;ll hand over.</p>
      </div>
      <div class="step reveal">
        <h3>Commercial &amp; warehouse</h3>
        <p>Forklifts, pallet jacks and wash-downs. Higher build thickness, chemical-resistant resin,
        and joints filled with a semi-rigid filler that takes a wheel load without breaking down at
        the edge. Striping and aisle marking go into the system, not on top of it.</p>
      </div>
      <div class="step reveal">
        <h3>Flake finishes</h3>
        <p>Vinyl chips broadcast to refusal, scraped back, vacuumed and sealed. The most forgiving
        finish we install and the one most people picture. Fifteen stock blends, or we&rsquo;ll mix
        to match something you bring us.</p>
      </div>
      <div class="step reveal">
        <h3>Metallic pours</h3>
        <p>Pigment worked through clear resin while it levels, so the pattern forms live on your
        floor. Showrooms, lobbies and feature garages. Costs more, takes longer, and no two ever
        come out the same.</p>
      </div>
      <div class="step reveal">
        <h3>Solid color</h3>
        <p>Clean, uniform and the most economical way to seal a slab. It is also a mirror &mdash;
        every trowel mark and patched crack shows in raking light, so we only recommend it over
        concrete that is genuinely flat.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Before you ask</p>
      <h2>Two things people always want to know</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Can I see one of these floors in person?</summary>
        <div class="faq__a"><p>Usually, yes. We keep a short list of past customers around
        Champaign, Urbana and Bloomington who are happy to let someone stand on their floor before
        committing. Tell us which finish you are weighing up and we will see who is nearby. Failing
        that, we bring full sample boards to every estimate &mdash; real product, in your space,
        under your own lighting.</p></div>
      </details>
      <details>
        <summary>How long does a floor like this take?</summary>
        <div class="faq__a"><p>Most residential garages and basements are a one- to two-day install:
        grind and repair on day one, coat and broadcast on day two. Commercial floors run longer and
        we phase them in sections so you are never fully shut down. Either way you get exact cure
        dates before we start &mdash; light foot traffic in about a day, vehicles after roughly a
        week.</p></div>
      </details>
    </div>
  </div>
</section>


<section class="section section--dark section--tight">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Where we work</p>
      <h2>Floors like these, across Central Illinois</h2>
      <p class="lede">We are based in Champaign County and install within a 50-mile radius, so the
      floors above are the same ones going into garages, shops and commercial space right across the
      area &mdash; with no trip charge to come out and quote yours.</p>
    </div>
    <ul>
      <li><strong>Urbana, Danville, Decatur</strong> &mdash; mid-century garages, cracked and
      salt-spalled. Repair first, and flake is the popular pick because it hides the repairs.</li>
      <li><strong>Savoy, Mahomet, north Normal</strong> &mdash; clean modern pours where solid color or
      a metallic is realistic.</li>
      <li><strong>Monticello, Tuscola, Paxton, Tolono</strong> &mdash; pole barns and machine sheds,
      every one moisture tested before we spec anything.</li>
    </ul>
    <p>Your town's page covers what we run into on floors there and what it means for the quote.</p>
    <ul class="link-grid link-grid--3" style="margin-top:1.5rem">
{loc_links(limit=9, dark=True)}
    </ul>
    <p style="margin-top:1.5rem"><a class="arrow-link" href="/service-area/">See the full service area <span aria-hidden="true">&rarr;</span></a></p>
  </div>
</section>

{call_strip("Seen one you like?",
            "Tell us which floor caught your eye and roughly how big your space is. "
            "We will tell you what that finish costs on your slab.")}

{cta_band("Ready for your floor?",
          "Free, itemized, on-site quotes anywhere within 50 miles &mdash; with real samples in hand "
          "so you can see the finish in your own space before you commit.",
          "Get My Free Quote")}
</main>

<div class="lightbox" id="lightbox" hidden>
  <button class="lightbox__close" type="button" data-lb-close aria-label="Close image viewer">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>
  </button>
  <button class="lightbox__nav lightbox__nav--prev" type="button" data-lb-prev aria-label="Previous image">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>
  </button>
  <figure class="lightbox__fig">
    <img id="lightboxImg" src="" alt="" width="1280" height="854" data-template>
    <figcaption id="lightboxCap"></figcaption>
  </figure>
  <button class="lightbox__nav lightbox__nav--next" type="button" data-lb-next aria-label="Next image">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>
  </button>
</div>
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

{call_strip("Still have a question?",
            "Call and ask. We would far rather spend ten minutes on the phone than have you guess "
            "&mdash; and there is no obligation attached to a phone call.")}

{cta_band()}
</main>
""" + footer()

# ================================================================== CONTACT ==
def page_contact():
    path = "/contact/"
    trail = [("Home", "/"), ("Free Quote", None)]
    title = "Free Epoxy Flooring Quote | Champaign &amp; Bloomington IL"
    desc = (f"Get a free, itemized epoxy flooring quote. Call {PHONE} or send the form - garages, "
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

          <div class="consent">
            <label class="consent__row">
              <input type="checkbox" name="sms_consent_service" value="Yes">
              <span>I consent to receive non-marketing text messages from <strong>{NAME}</strong>
              about my quote request, scheduling and job updates. Message frequency varies,
              message &amp; data rates may apply. Reply HELP for assistance, reply STOP to opt out.</span>
            </label>

            <label class="consent__row">
              <input type="checkbox" name="sms_consent_marketing" value="Yes">
              <span>I consent to receive marketing text messages from <strong>{NAME}</strong>
              about seasonal offers, promotions and new services. Message frequency varies,
              message &amp; data rates may apply. Reply HELP for assistance, reply STOP to opt out.</span>
            </label>
          </div>

          <div class="form-foot">
            <button class="btn btn--lg btn--block" type="submit">Send my free quote request</button>
            <p class="form-note">
              We reply to every request. Prefer to talk it through? Call
              <a href="tel:{TEL}"><strong>{PHONE}</strong></a>. We use your details to quote your floor
              and nothing else &mdash; no lists, no sharing.
            </p>
            <p class="form-legal">
              <a href="/privacy-policy/">Privacy Policy</a> <span aria-hidden="true">|</span>
              <a href="/terms-and-conditions/">Terms and Conditions</a>
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

{call_strip("Rather just talk it through?",
            "Most people find it faster. Two minutes on the phone usually tells us more than a form "
            "does, and we can often give you a ballpark on the spot.")}

<section class="section">
  <div class="wrap">
    <div class="split split--wide-text">
      <div>
        <p class="eyebrow">Before you call</p>
        <h2>Four things that make the quote faster</h2>
        <p>None of these are required &mdash; call us with none of them and we will still come out. But
        if you have them to hand, we can usually give you a realistic ballpark before we ever get in the
        truck.</p>
        <ul class="checks">
          <li>{I['check']}<span><strong>Rough dimensions.</strong> Length and width in feet is plenty.
          A standard two-car garage is around 400&ndash;500 square feet, a three-car around
          650&ndash;750. Pacing it out is close enough for a ballpark.</span></li>
          <li>{I['check']}<span><strong>The age of the slab, roughly.</strong> Even &ldquo;it is the
          original garage from when the house was built in the sixties&rdquo; tells us a great deal about
          what prep to expect.</span></li>
          <li>{I['check']}<span><strong>A photo or two of the concrete.</strong> Text or email them.
          Cracking, spalling near the door, dark oil staining and any existing coating are the four
          things that move a price, and all four show up in a phone picture.</span></li>
          <li>{I['check']}<span><strong>Whether anything has been put on it before.</strong> Paint, a
          sealer, a DIY kit, or a previous epoxy job that is now letting go. An existing coating changes
          the prep entirely, and it is far better to know now than on the morning.</span></li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">What it costs to find out</p>
        <h2>Nothing, anywhere we work</h2>
        <p>Every estimate is free, on-site and carries no obligation. There is <strong>no trip
        charge</strong> anywhere in the {AREA['radiusMiles']}+ mile service area &mdash; not to Danville,
        not to Decatur, not to Bloomington-Normal. If you are inside roughly a
        {AREA['radiusMiles']}-mile drive of Champaign, coming out to look costs you nothing.</p>
        <p>On the visit: we measure, moisture-test the slab, and bring physical flake and metallic
        samples. You get an itemized written quote &mdash; prep, materials, install and extras broken
        out &mdash; that you can compare honestly against anyone else.</p>
        <p>Then it is your call. No pressure, no &ldquo;today-only&rdquo; pricing, no repeated calls
        afterward. If the number works, call us back.</p>
        <div class="local-note">
          <strong>One straight answer up front:</strong> we will not quote a floor over the phone.
          A number given without seeing the slab is a guess, and the only way it can go is up once we
          arrive &mdash; which helps nobody. The visit is free precisely so that the number can be real.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow">Questions</p>
      <h2>Asked on most first calls</h2>
    </div>
    {faq_html(FAQS[:3])}
    <p style="margin-top:1.5rem;text-align:center">
      <a class="arrow-link" href="/faq/">All epoxy flooring FAQs <span aria-hidden="true">&rarr;</span></a>
    </p>
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

{call_strip("In a hurry?",
            "If you would rather not wait for the callback, ring us directly &mdash; one of the owners "
            "picks up.")}

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
                f"{PHONE} for a free epoxy flooring quote.", path)
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
        {call_primary()}
        {quote_btn("btn--ghost")}
      </div>
    </div>
  </div>
</section>

{call_strip("Looking for an epoxy floor quote?",
            "That is what this site is for. Call and we will get you a real number.")}
</main>
""" + footer()



# =========================================================== REVIEW / FEEDBACK ==
# Two standalone utility pages for QR codes and text-to-review campaigns.
# Deliberately noindex and deliberately outside the normal page shell: /review
# has to fit one screen with no scrolling, which the site header, footer and
# call strip would make impossible.

def util_head(title, desc, path, extra_css=""):
    """Minimal <head> for the utility pages - same tokens and fonts, no chrome."""
    h = head(title, desc, path)
    h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                  '<meta name="robots" content="noindex, nofollow">')
    return h

def util_footer():
    return f"""  <footer class="util__foot">
    <p><b>{NAME}</b></p>
    <p>
      <a href="tel:{TEL}">{PHONE}</a>
      <span aria-hidden="true">&middot;</span>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </p>
    <p>{CFG['basedIn']['county']}, {CFG['basedIn']['regionName']}</p>
  </footer>
"""

def star_svg(i):
    return (f'<button class="star" type="button" data-rating="{i}" '
            f'aria-label="{i} star{"s" if i > 1 else ""} out of 5">'
            '<svg viewBox="0 0 24 24" aria-hidden="true">'
            '<path d="M12 2.6l2.95 5.98 6.6.96-4.77 4.65 1.12 6.57L12 17.66l-5.9 3.1 1.13-6.57L2.46 9.54l6.6-.96z"/>'
            '</svg></button>')

def page_review():
    path = "/review/"
    stars = "\n        ".join(star_svg(i) for i in range(1, 6))
    return util_head("How was your experience? | " + NAME,
                     "Tell DP Flooring Services how your epoxy floor install went.",
                     path) + f"""
<main class="util util--center" id="main">
  <div class="util__card">
    <img class="util__logo" src="/assets/img/logo-full-ondark.png"
         alt="{NAME}" width="420" height="450">

    <h1>How Was Your Experience?</h1>
    <p class="util__sub">Tap a star to let us know.</p>

    <div class="stars" id="stars" role="group" aria-label="Rate your experience from 1 to 5 stars">
        {stars}
    </div>

    <p class="util__hint" id="starHint">1 = poor &middot; 5 = excellent</p>
  </div>
{util_footer()}
</main>

<script>
  window.DP_REVIEW_URL = "{CFG['social']['googleReviewUrl']}";
</script>
<script src="/assets/js/review.js" defer></script>
</body>
</html>
"""

def page_feedback():
    path = "/feedback/"
    return util_head("We&rsquo;d love to make this right | " + NAME,
                     "Tell DP Flooring Services what went wrong. Goes straight to the owners.",
                     path) + f"""
<main class="util" id="main">
  <div class="util__card util__card--form">
    <img class="util__logo" src="/assets/img/logo-full-ondark.png"
         alt="{NAME}" width="420" height="450">

    <p class="ratingpill" id="ratingPill" hidden></p>

    <h1>We&rsquo;d Love to Make This Right</h1>
    <p class="util__sub">Your feedback goes straight to our team, not posted publicly.
    Tell us what happened.</p>

    <form id="feedbackForm" novalidate>
      <div class="ufield">
        <label for="fbName">Your name <span class="req">*</span></label>
        <input id="fbName" name="name" type="text" autocomplete="name" required placeholder="First and last">
        <span class="uerr" data-msg="Please tell us your name."></span>
      </div>

      <div class="ufield">
        <label for="fbPhone">Phone <span class="req">*</span></label>
        <input id="fbPhone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required
               placeholder="(217) 555-0134">
        <span class="uerr" data-msg="Enter a 10-digit US phone number so we can reach you."></span>
      </div>

      <div class="ufield">
        <label for="fbWhat">What happened? <span class="req">*</span></label>
        <textarea id="fbWhat" name="what_happened" required
                  placeholder="Tell us what went wrong, in as much or as little detail as you want."></textarea>
        <span class="uerr" data-msg="Please tell us what happened."></span>
      </div>

      <div class="ufield">
        <label for="fbFix">How can we make it right? <span class="opt">optional</span></label>
        <textarea id="fbFix" name="how_to_fix"
                  placeholder="If there is something specific that would fix this, tell us and we will try."></textarea>
        <span class="uerr"></span>
      </div>

      <button class="ubtn" type="submit" id="fbSubmit">Send Feedback</button>
      <p class="util__hint">Goes to Drayton and Dylan directly. Never posted publicly.</p>
    </form>

    <div class="thanks" id="fbThanks" hidden>
      <div class="thanks__tick" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"
             stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
      </div>
      <h2>Thank you</h2>
      <p>We take this seriously and someone will reach out to you personally within 24 hours.</p>
      <p class="util__hint">Need us sooner? Call <a href="tel:{TEL}">{PHONE}</a>.</p>
    </div>
  </div>
{util_footer()}
</main>

<script src="/assets/js/review.js" defer></script>
</body>
</html>
"""


# ==================================================== PRIVACY / TERMS (legal) ==
# These two pages exist for a hard external reason as well as the obvious one:
# carriers reviewing an A2P 10DLC SMS campaign check that the page collecting the
# phone number links to a reachable privacy policy and terms page, that the
# privacy policy carries the mobile-information non-sharing clause verbatim, and
# that the terms spell out STOP/HELP, rates and frequency. Do not soften or
# reword the clause in privacy_sms_clause() - it is quoted language.

def legal_head(h1, sub, trail):
    """Slimmer page header for the legal pages - no quote/call CTA row, which
    would sit oddly on top of a policy document."""
    return f"""<section class="pagehead">
  <div class="wrap">
    {crumbs(trail)}
    <div class="pagehead__inner">
      <h1>{h1}</h1>
      <p class="lede">{sub}</p>
    </div>
  </div>
</section>
"""

def privacy_sms_clause():
    """Verbatim carrier-required wording. Do not edit."""
    return ("No mobile information will be shared with third parties/affiliates for "
            "marketing/promotional purposes. Information sharing to subcontractors in support "
            "services, such as customer service, is permitted. All other use case categories "
            "exclude text messaging originator opt-in data and consent; this information will "
            "not be shared with any third parties.")

def page_privacy():
    path = "/privacy-policy/"
    trail = [("Home", "/"), ("Privacy Policy", None)]
    title = f"Privacy Policy | {BRAND}"
    desc = (f"How {NAME} collects, uses and protects the information you give us, including "
            "mobile phone numbers and SMS opt-in consent, which we never share.")
    schema = [crumb_schema(trail)]

    return head(title, desc, path, schema=schema) + header(path) + legal_head(
        "Privacy Policy",
        f"What {BRAND} does with the information you give us &mdash; in plain English, "
        "and short enough to actually read.",
        trail) + f"""
<main id="main">

<section class="section">
  <div class="wrap wrap--narrow">
    <div class="legal">
      <p class="legal__updated"><strong>Last updated:</strong> {LEGAL['lastUpdated']}</p>

      <p>{NAME} (&ldquo;{BRAND}&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;) is an epoxy flooring
      contractor based in {CFG['basedIn']['county']}, {CFG['basedIn']['regionName']}. This policy
      explains what we collect when you contact us or use this website, why we collect it, and
      what we do &mdash; and do not do &mdash; with it.</p>

      <p>The short version: we collect what we need to quote and complete your floor, we use it
      for that, and we do not sell it or hand it to anyone for marketing.</p>

      <h2>Information we collect</h2>
      <p>We only ever collect information you choose to give us, plus basic technical data your
      browser sends to any website.</p>
      <ul>
        <li><strong>Information you give us directly.</strong> Your name, phone number, email
        address, job address, floor type, approximate square footage, and anything you write in
        the message box on our quote form &mdash; or tell us by phone, text or email.</li>
        <li><strong>Photos and job details.</strong> If you send us pictures of your slab or
        details about the space, we keep them with your quote so we can price the job accurately.</li>
        <li><strong>SMS consent records.</strong> If you tick either consent box on our form, we
        record that you did, along with the date and the wording you agreed to. We are required
        to keep this record.</li>
        <li><strong>Basic website data.</strong> Standard server and analytics data such as pages
        visited, approximate location by city, referring site, and device or browser type. This is
        aggregate and is not used to identify you personally.</li>
      </ul>

      <h2>How we use it</h2>
      <ul>
        <li>To prepare and send you a written, itemized quote.</li>
        <li>To schedule a site visit and the installation itself, and to keep you updated while
        the work is underway.</li>
        <li>To answer questions you send us, by whichever channel you used.</li>
        <li>To follow up on a quote you asked for, and &mdash; only if you ticked the marketing
        consent box &mdash; to tell you about {LEGAL['smsMarketingDescription']}.</li>
        <li>To invoice you, keep our own records, and meet our legal and tax obligations.</li>
        <li>To keep the website working and secure.</li>
      </ul>

      <h2>Text messages and your mobile number</h2>
      <p>Ticking a consent box on our form is optional. You will get your quote either way &mdash;
      we will never make an SMS opt-in a condition of quoting or doing your floor.</p>
      <p>If you do opt in, you can expect {LEGAL['smsDescription']}. Message frequency varies.
      Message and data rates may apply. Reply <strong>STOP</strong> to any message to opt out, or
      <strong>HELP</strong> for help. Full details are in our
      <a href="/terms-and-conditions/">Terms and Conditions</a>.</p>

      <div class="legal__callout">
        <p><strong>Mobile information &mdash; non-sharing.</strong> {privacy_sms_clause()}</p>
      </div>

      <h2>Who we share information with</h2>
      <p><strong>We do not sell your information, and we do not rent, trade or otherwise pass it
      to anyone for their own marketing.</strong></p>
      <p>We share the minimum necessary with the service providers who help us run the business,
      and only so they can perform that service for us:</p>
      <ul>
        <li>Our website host and form provider, which delivers your quote request to our inbox.</li>
        <li>Our scheduling, messaging and customer-service tools, which we use to reply to you
        and keep track of your job.</li>
        <li>Our payment processor and accountant, for invoicing and bookkeeping.</li>
        <li>Where a job calls for it, a subcontractor or supplier working on your floor &mdash;
        given only the details needed to do that work, such as the job address and scope.</li>
      </ul>
      <p>These providers are bound to use your information only to provide their service to us.
      As stated above, mobile numbers and SMS consent are excluded from any sharing outside
      support services performed on our behalf.</p>
      <p>We may also disclose information if the law requires it, or to establish or defend a
      legal claim.</p>

      <h2>How long we keep it</h2>
      <p>We keep quote requests and job records for as long as we need them to serve you and to
      satisfy tax, warranty and legal requirements &mdash; generally seven years for completed
      work. SMS consent and opt-out records are kept for as long as we operate the messaging
      program. You can ask us to delete anything we are not required to keep.</p>

      <h2>Your choices</h2>
      <ul>
        <li><strong>Stop texts.</strong> Reply STOP to any message from us.</li>
        <li><strong>Stop emails.</strong> Use the unsubscribe link, or just reply and tell us.</li>
        <li><strong>See, correct or delete your information.</strong> Call or email us and we will
        take care of it.</li>
      </ul>
      <p>To make any of these requests, contact us using the details below.</p>

      <h2>Security</h2>
      <p>This site is served over HTTPS, and we use reputable providers for our forms, messaging
      and payments. No system is perfect, but we take reasonable steps to protect what you give
      us and we limit access to the people who need it.</p>

      <h2>Children</h2>
      <p>This website and our services are for adults. We do not knowingly collect information
      from anyone under 18. If you believe a child has given us information, contact us and we
      will delete it.</p>

      <h2>Cookies</h2>
      <p>We use a small number of cookies to keep the site working and to understand, in aggregate,
      how it is used. You can block or delete cookies in your browser settings; the site will still
      work, though some conveniences may not.</p>

      <h2>Changes to this policy</h2>
      <p>If we change this policy we will update the date at the top of this page. Material changes
      to how we handle your information will be reflected here before they take effect.</p>

      <h2>Contact us</h2>
      <p>Questions about this policy, or about information we hold on you:</p>
      <ul>
        <li><strong>{NAME}</strong></li>
        <li>Phone or text: <a href="tel:{TEL}">{PHONE}</a></li>
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{CFG['basedIn']['county']}, {CFG['basedIn']['regionName']}</li>
      </ul>
    </div>
  </div>
</section>

{cta_band()}
</main>
""" + footer()

def page_terms():
    path = "/terms-and-conditions/"
    trail = [("Home", "/"), ("Terms and Conditions", None)]
    title = f"Terms and Conditions | {BRAND}"
    desc = (f"Terms for using the {BRAND} website and our SMS messaging program, including how to "
            "opt out with STOP and get help with HELP.")
    schema = [crumb_schema(trail)]

    return head(title, desc, path, schema=schema) + header(path) + legal_head(
        "Terms and Conditions",
        "The terms that apply to this website and to our text messaging program.",
        trail) + f"""
<main id="main">

<section class="section">
  <div class="wrap wrap--narrow">
    <div class="legal">
      <p class="legal__updated"><strong>Last updated:</strong> {LEGAL['lastUpdated']}</p>

      <p>These terms apply to your use of this website and to the SMS messaging program operated
      by <strong>{NAME}</strong> (&ldquo;{BRAND}&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;). By
      using this site or opting in to our messages, you agree to them.</p>

      <h2>SMS Terms of Service</h2>
      <h3>{NAME}</h3>

      <ul>
        <li>When you opt in to the {NAME} messaging program, you can expect to receive
        {LEGAL['smsDescription']}. If you also tick the marketing consent box, you may receive
        messages about {LEGAL['smsMarketingDescription']}. Opting in is optional, and it is never
        a condition of getting a quote or having us do your floor.</li>

        <li>You can cancel the SMS service at any time. Just text &ldquo;<strong>STOP</strong>&rdquo;
        to <a href="tel:{TEL}">{PHONE}</a>. After you send the SMS message
        &ldquo;STOP&rdquo; to us, we will send you an SMS message to confirm that you have been
        unsubscribed. After this, you will no longer receive SMS messages from us. If you want to
        join again, just sign up as you did the first time and we will start sending SMS messages
        to you again.</li>

        <li>If you are experiencing issues with the messaging program you can reply with the
        keyword <strong>HELP</strong> for more assistance, or you can get help directly at
        <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{TEL}">{PHONE}</a>.</li>

        <li>Carriers are not liable for delayed or undelivered messages.</li>

        <li>As always, message and data rates may apply for any messages sent to you from us and
        to us from you. You will receive messages as needed for your quote and job, and
        {LEGAL['messageFrequency']}. If you have any questions about your text plan or data plan,
        it is best to contact your wireless provider.</li>

        <li>If you have any questions regarding privacy, please read our privacy policy:
        <a href="/privacy-policy/">{BASE}/privacy-policy/</a></li>
      </ul>

      <h2>Quotes and estimates</h2>
      <p>Quotes are free, given in writing, and based on what we see at the site visit. A quote is
      valid for 30 days unless it says otherwise. If we uncover something once the coating is
      ground off &mdash; failed slab, moisture, an old coating that has to come up &mdash; we will
      stop, tell you what we found and what it changes, and get your approval before carrying on.
      Nothing gets added to your bill without you agreeing to it first.</p>

      <h2>Scheduling and access</h2>
      <p>We will agree a start date with you in advance. You are responsible for clearing the
      space and giving us access, water and power on the day. Weather, cure times and conditions
      in the space can move a schedule; we will keep you posted if that happens.</p>

      <h2>Payment</h2>
      <p>Payment terms are set out on your quote or invoice. Unless agreed otherwise, the balance
      is due on completion.</p>

      <h2>Workmanship</h2>
      <p>We stand behind our work. Any warranty on materials or workmanship is set out on your
      quote and invoice, and that document governs. A warranty does not cover damage from misuse,
      impact, chemicals the floor was not specified for, or structural movement in the slab.</p>

      <h2>Website content</h2>
      <p>We keep this site accurate, but it is provided for general information. Prices, finishes,
      colors and availability can change, and photographs and color swatches are representative
      &mdash; the color of a finished floor depends on lighting and on your slab. Nothing on this
      site is a binding offer; your written quote is.</p>
      <p>The content, photographs, logos and design of this site belong to {NAME} and may not be
      copied or reused without our permission.</p>

      <h2>Limitation of liability</h2>
      <p>To the fullest extent the law allows, our liability arising out of this website or our
      services is limited to the amount you paid us for the work in question. We are not liable
      for indirect or consequential losses.</p>

      <h2>Governing law</h2>
      <p>These terms are governed by the laws of the State of {CFG['basedIn']['regionName']}.</p>

      <h2>Changes</h2>
      <p>We may update these terms; the date at the top of this page shows when we last did.
      Continued use of the site or the messaging program after a change means you accept it.</p>

      <h2>Contact us</h2>
      <ul>
        <li><strong>{NAME}</strong></li>
        <li>Phone or text: <a href="tel:{TEL}">{PHONE}</a></li>
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{CFG['basedIn']['county']}, {CFG['basedIn']['regionName']}</li>
      </ul>
    </div>
  </div>
</section>

{cta_band()}
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
        ("/colors-and-finishes/", "colors-and-finishes/index.html", page_colors, "0.8", "monthly", True),
        ("/gallery/",      "gallery/index.html",           page_gallery, "0.7", "monthly", True),
        ("/faq/",          "faq/index.html",               page_faq,     "0.7", "monthly", True),
        ("/contact/",      "contact/index.html",           page_contact, "0.9", "monthly", True),
        ("/contact/thank-you/", "contact/thank-you/index.html", page_thanks, None, None, False),
        ("/privacy-policy/", "privacy-policy/index.html",   page_privacy, "0.3", "yearly", True),
        ("/terms-and-conditions/", "terms-and-conditions/index.html", page_terms, "0.3", "yearly", True),
        ("/404.html",      "404.html",                     page_404,     None, None, False),
        ("/review/",       "review/index.html",            page_review,   None, None, False),
        ("/feedback/",     "feedback/index.html",          page_feedback, None, None, False),
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

    # Renaming a slug leaves the old directory behind, still crawlable and still
    # competing with its replacement. Report those; --prune deletes them.
    wanted = {os.path.normpath(os.path.join(OUT, rel)) for _, rel, _, _, _, _ in pages}
    # Hand-authored directories that live in this repo but are NOT generated by
    # this script. Without this guard --prune would delete them, because they
    # contain an index.html that is not in the page registry.
    NOT_GENERATED = {"funnel", "assets", "tools", ".git", "node_modules"}
    stale = []
    for base in [OUT, os.path.join(OUT, "services")]:
        if not os.path.isdir(base): continue
        for name in sorted(os.listdir(base)):
            if name in NOT_GENERATED: continue
            d = os.path.join(base, name)
            idx = os.path.join(d, "index.html")
            if os.path.isdir(d) and os.path.isfile(idx) and idx not in wanted:
                stale.append(d)
    if stale:
        prune = "--prune" in sys.argv
        for d in stale:
            print(("  pruned stale page: " if prune else "  !! STALE PAGE (rerun with --prune): ")
                  + os.path.relpath(d, OUT))
            if prune:
                os.remove(os.path.join(d, "index.html"))
                if not os.listdir(d): os.rmdir(d)

    print(f"Built {len(pages)} pages into {OUT}")
    print(f"  {len(SERVICES)} service pages, {len(LOCATIONS)} location pages")
    print(f"  sitemap.xml lists {len(sm)} indexable URLs")
    print(f"  base URL: {BASE}")
    orphan = [u for u, p, c in sm if u not in open(os.path.join(OUT, "sitemap.xml"), encoding="utf-8").read()]
    if orphan:
        print("  !! missing from sitemap:", orphan)

if __name__ == "__main__":
    main()
