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
NAV = [("Home", "/"), ("Services", "/services/"), ("About", "/about/"),
       ("Service Area", "/service-area/"), ("Gallery", "/gallery/"), ("FAQ", "/faq/")]
NAV_MOBILE = NAV + [("Contact", "/contact/")]

SERVICES = [
 dict(slug="garage-floor-epoxy", name="Garage Floor Epoxy", icon="home", type="Garage", pair_idx=3,
      img="blue-flake-epoxy-garage-floor.jpg",
      alt="Residential garage in Champaign County, IL finished with a blue and gray flake epoxy floor",
      title="Garage Floor Epoxy Champaign IL | Garage Floor Coating | DP Flooring",
      desc="Epoxy garage floor coating in Champaign-Urbana, Bloomington-Normal and Central Illinois. "
           "Diamond-ground prep, hot-tire resistant systems, flake and solid color finishes.",
      h1="Garage Floor Epoxy",
      sub_h2="A garage floor that shrugs off hot tires and road salt",
      short="The floor you look at every single day. Ground down to clean concrete, filled, coated and "
            "top-sealed so oil, road salt, hot tires and dropped tools stop leaving their mark.",
      long="A garage slab takes more abuse than any other floor on the property. Hot tires park on it all "
           "summer, road salt melts off the fenders every February, oil drips, and sooner or later "
           "something heavy gets dropped on it. Bare concrete absorbs every bit of that and never gives it "
           "back &mdash; which is why an uncoated garage floor goes gray-black around the parking spots and "
           "starts flaking apart along the apron by the door. A properly installed epoxy system seals the "
           "concrete completely. Spills sit on the surface until you wipe them up, the whole floor mops "
           "clean, and the garage stops reading as storage and starts reading as finished space.",
      body2="The failure everybody has heard about is <strong>hot-tire pickup</strong>: you pull the car in "
            "on a hot day, the tires soften slightly, and when you back out a week later the coating comes "
            "up with them in dinner-plate sized sheets. That is what happens to every big-box DIY kit and to "
            "any installer who acid-etched the slab instead of grinding it. Etching leaves a residue and "
            "barely opens the surface; the coating sits on top of the concrete rather than keying into it, "
            "and warm rubber beats that bond every time. We diamond grind every garage down to clean, open "
            "concrete, vacuum it, repair the cracks and pits, and install a system rated for hot-tire "
            "exposure. It is one extra day of work and it is the entire difference. Most two- and three-car "
            "garages run one to two days on site: prep and repair on day one, base coat, flake broadcast and "
            "topcoat on day two. You can walk on it the next morning, move shelving back in after two or "
            "three days, and park on it after about a week.",
      bullets=["Diamond-ground surface prep, so the coating bonds instead of peeling in a year",
               "Hot-tire resistant &mdash; no lifting or delamination where the car parks",
               "Solid color, partial flake or full-broadcast flake, in a blend you pick",
               "Crack, pit and apron-spall repair included before anything is coated",
               "Most two- and three-car garages are a one- to two-day install"],
      drivers=["Square footage &mdash; a two-car garage and a four-car outbuilding price very differently per foot",
               "Slab condition &mdash; cracking, pitting and spalling at the apron all add repair time",
               "Finish &mdash; solid color, partial flake or full-broadcast flake",
               "Extras &mdash; non-slip aggregate, cove base at the walls, and a second clear coat"]),

 dict(slug="basement-floor-epoxy", name="Basement Floor Epoxy", icon="layers", type="Basement", pair_idx=2,
      img="basement-epoxy-floor-urbana-il.jpg",
      alt="Bright finished basement in Urbana, IL with a clean, seamless coated floor",
      title="Basement Floor Epoxy | Champaign &amp; Bloomington IL | DP Flooring",
      desc="Basement floor epoxy coating across Central Illinois. Seals concrete dust, resists moisture "
           "and brightens the lower level. Moisture tested before we quote.",
      h1="Basement Floor Epoxy",
      sub_h2="Stop the concrete dust and get the lower level back",
      short="Turn a cold, dusty slab into a finished floor that mops clean. A sealed basement stops "
            "concrete dust at the source and makes the whole lower level feel like real living space.",
      long="Untreated basement concrete is a dust factory. It sheds a fine gray powder onto every box, "
           "bike and storage tote down there, and it wicks moisture up out of the ground underneath, which "
           "is where the musty smell in most Central Illinois basements actually comes from. Sealing the "
           "slab with the right epoxy system shuts both of those down at once. You get a seamless, "
           "light-reflecting surface with nowhere for dirt or mildew to collect, and a floor you can damp "
           "mop instead of sweep and re-sweep.",
      body2="The part that matters most on a basement is the part you cannot see, which is why we "
            "<strong>moisture test before we quote</strong> rather than after. Concrete below grade is in "
            "constant contact with damp soil, and if water vapor is driving up through the slab it will "
            "push a standard coating right back off &mdash; you get blisters and bubbles within months, and "
            "no amount of surface prep prevents it. We run calcium chloride or relative-humidity testing on "
            "the slab, and if the numbers come back high we spec a moisture-mitigating primer or a "
            "vapor-tolerant system built for exactly that condition. It costs more than a plain coating, so "
            "we would rather show you the readings and let you decide than quote you cheap and come back "
            "next spring. Beyond the technical side, a light-colored basement floor genuinely changes the "
            "room. Lower levels are short on natural light, and a reflective floor throws what little there "
            "is back up into the space. It is the single cheapest thing you can do to make a basement feel "
            "finished, and it works just as well under a home gym, a workshop, a laundry room or a "
            "full rec room build-out.",
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
      icon="truck", type="Commercial / industrial", pair_idx=6,
      img="commercial-epoxy-floor-coating-bloomington-il.jpg",
      alt="Commercial building interior in Bloomington, IL with a freshly coated high-gloss epoxy floor",
      title="Commercial &amp; Industrial Floor Coating | Bloomington &amp; Decatur IL",
      desc="Commercial and industrial epoxy floor coatings in Central Illinois. Warehouses, shops, pole "
           "barns and production floors. High-build systems, line striping, off-hours installs.",
      h1="Commercial &amp; Industrial Floor Coating",
      sub_h2="Specified for the traffic your floor actually takes",
      short="Coatings specified for what really happens on the floor &mdash; forklifts, pallet jacks, "
            "wash-downs and chemicals. Warehouses, shops, pole barns and production space, any size, "
            "scheduled around your operation.",
      long="A production floor is not a garage floor with more square footage. Forklift wheels, pallet jack "
           "casters, hot wash-downs, dropped tooling and spilled chemistry each attack a coating in a "
           "different way, and the system has to be specified around whichever of those is actually "
           "happening on your floor. We spec the build thickness, the resin chemistry and the topcoat from "
           "what we see during the walkthrough, then phase the install so you are never shut down "
           "completely. This is also where we handle shop, warehouse and pole barn floors of any size &mdash; "
           "from a single service bay up to a full distribution floor.",
      body2="Two things separate a commercial floor that lasts from one that does not. The first is "
            "<strong>prep method</strong>. On a slab with years of oil and hydraulic fluid soaked into it, "
            "grinding alone will not get you a bond &mdash; we degrease first, then shot blast to drive a "
            "deep mechanical profile into the concrete. Joints and cracks get chased out and filled with a "
            "semi-rigid filler that can take a wheel load without collapsing at the edge. The second is "
            "<strong>scheduling</strong>. Almost nobody can hand us an empty building for a week, so we work "
            "in sections, overnight and on weekends, and we sequence it so there is always a route through "
            "for your people and your equipment. Once the floor is down, the practical wins show up fast: "
            "a coated floor reflects your existing lights, so the building is measurably brighter without "
            "adding a single fixture; spills stop soaking in and become a mop job; and line striping, aisle "
            "marking and hazard zones can be built directly into the system rather than painted on top to "
            "wear off again. Where the floor gets wet, we broadcast non-slip aggregate into the topcoat.",
      bullets=["High-build and chemical-resistant systems for real production environments",
               "Shop, warehouse and pole barn floors &mdash; single bay through full distribution floor",
               "Safety line striping, aisle marking, walkways and hazard zones",
               "Shot blasting and degreasing for oil-contaminated slabs",
               "Phased, overnight and weekend installs so the operation keeps running"],
      drivers=["Total square footage and how many phases the install has to run in",
               "Build thickness and chemical resistance the operation requires",
               "Prep method &mdash; grinding versus shot blasting on a heavily contaminated slab",
               "Line striping, aisle marking, non-slip aggregate and out-of-hours scheduling"]),

 dict(slug="flake-epoxy-flooring", name="Flake Epoxy Flooring", icon="grid", type="Flake epoxy", pair_idx=4,
      img="decorative-flake-epoxy-floor-finish.jpg",
      alt="Close-up of a gray, white and blue full-broadcast flake epoxy floor finish",
      title="Flake Epoxy Flooring | Garage &amp; Basement Floors | Illinois",
      desc="Full-broadcast flake epoxy flooring in Central Illinois. Custom color blends, built-in grip, "
           "hides slab imperfections, finished with a clear urethane topcoat.",
      h1="Flake Epoxy Flooring",
      sub_h2="The finish most people picture when they picture an epoxy floor",
      short="Vinyl flake broadcast into the base coat until the floor will not take another chip, then "
            "scraped, vacuumed and sealed under clear urethane. Custom color blends, built-in grip, and "
            "it hides everything a slab has been through.",
      long="Flake is the most popular floor we install, and for good reason: it looks sharp, it is the "
           "most forgiving finish there is, and it costs less than metallic. Colored vinyl chips are "
           "broadcast by hand into the wet base coat until the surface reaches refusal &mdash; the point "
           "where it physically will not hold another flake. The floor is then scraped back, vacuumed, and "
           "sealed under one or two coats of clear urethane. The result is a subtle texture underfoot, a "
           "surface that hides dust and tire marks between cleanings, and a look you can tune to the room.",
      body2="The practical advantage of flake is <strong>what it forgives</strong>. A solid-color floor is a "
            "mirror: every trowel mark, every patched crack and every low spot in the slab shows through it "
            "in raking light. Flake breaks the surface up visually, so an older garage or basement slab that "
            "has been repaired reads as a finished floor rather than as a repair job. It also builds grip "
            "in, because the chip edges leave a fine texture that is noticeably less slick underfoot when "
            "wet than a smooth coating &mdash; worth knowing in a garage where you track snow in from "
            "December to March. Blends are yours to choose. We bring physical sample boards to the estimate "
            "rather than asking you to pick off a screen, because flake never looks the same on a monitor as "
            "it does on a floor. You can go subtle with grays and whites, pull your blend toward the blues "
            "in our own logo, or run school or team colors through a rec room. Coverage is a choice too: a "
            "full broadcast gives you the classic dense look, while a lighter partial broadcast leaves the "
            "base color visible and costs less.",
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
      type="Metallic epoxy", pair_idx=5,
      img="metallic-epoxy-floor-finish.jpg",
      alt="Large interior with a poured metallic epoxy floor in an amber blend and steel columns",
      title="Metallic Epoxy Flooring | Showroom &amp; Garage Floors | Central Illinois",
      desc="Poured metallic epoxy floors in Central Illinois. Pigments move through the resin as it "
           "levels, so no two floors are alike. Showrooms, retail, basements and feature garages.",
      h1="Metallic Epoxy Flooring",
      sub_h2="A floor with depth and movement you cannot get from paint",
      short="Metallic pigments suspended in clear resin, worked while it levels so the color moves. Every "
            "floor is genuinely one of a kind &mdash; and it is the finish people stop walking to look at.",
      long="Metallic is the premium end of what we install. Reflective pigments are dispersed into a clear "
           "resin, poured over a pigmented base, and then worked with rollers, brushes and air while the "
           "material is still moving. The pigments travel as it levels and self-heals, which produces the "
           "depth, veining and cloud movement people associate with polished stone. Nobody &mdash; including "
           "us &mdash; can reproduce a metallic floor exactly twice, and that is the point of it.",
      body2="Because the finish is created live, on the floor, <strong>a metallic pour is the least "
            "forgiving thing we do</strong> and the most dependent on the person doing it. The working "
            "window is short, the pour has to stay wet edge to wet edge across the whole room, and once the "
            "resin starts to gel the pattern is locked in for good. That is a large part of why we handle "
            "these ourselves rather than sending a crew: there is no touching one up afterward. It also "
            "means the slab underneath has to be genuinely flat and genuinely sound before we start, so "
            "metallic jobs usually carry more prep than a flake floor on the same square footage. Where it "
            "earns its keep is anywhere the floor is part of the room &mdash; a showroom or retail space, a "
            "restaurant, an office lobby, a finished basement, or a garage that has stopped being just a "
            "garage. We will show you sample panels of the blends we run at the estimate, and we are honest "
            "about the trade-off: metallic costs more and takes longer, and if what you actually want is a "
            "hard-working, forgiving floor, flake is the better buy.",
      bullets=["Poured and worked by hand &mdash; genuinely one of a kind, every time",
               "Depth, veining and movement that reads like polished stone",
               "Blends shown as physical sample panels at the estimate",
               "Flatter, sounder slab prep than a flake floor of the same size",
               "Finished with clear urethane for UV stability and scuff resistance"],
      drivers=["Square footage and how many people it takes to keep a wet edge across the room",
               "Extra slab flatness and repair work a metallic pour demands",
               "Number of pigment colors and the complexity of the blend",
               "Clear urethane topcoats over the finished pour"]),

 dict(slug="concrete-floor-prep-and-repair", name="Concrete Floor Prep &amp; Repair", icon="ruler",
      type="Prep / repair", pair_idx=1,
      img="concrete-floor-prep-and-repair.jpg",
      alt="Cracked, pitted and stained concrete slab in Central Illinois before grinding and repair",
      title="Concrete Floor Prep &amp; Repair | Crack Repair | Central Illinois",
      desc="Concrete floor preparation and repair in Central Illinois: diamond grinding, shot blasting, "
           "crack chasing, spall and pit repair, and failed coating removal.",
      h1="Concrete Floor Prep &amp; Repair",
      sub_h2="The step that decides how long the floor lasts",
      short="The part nobody sees, and the part everything else depends on. Cracks, pits, spalling, "
            "failing old coatings and oil-soaked concrete all get dealt with before a drop of epoxy "
            "goes down.",
      long="Almost every failed epoxy floor we get called out to look at failed for the same reason: "
           "nobody prepped the concrete. Someone rolled a coating over a sealed, dusty or oily slab and the "
           "bond never had a chance to form. We mechanically profile every floor we touch &mdash; no acid "
           "etching and hoping &mdash; then chase and fill the cracks, patch the pits and pull the old "
           "coating off if there is one. It is the slowest day of the job and the only one that decides how "
           "long the floor lasts.",
      body2="Concrete has to be <strong>opened up</strong> before anything will stick to it. A troweled or "
            "sealed slab is effectively closed at the surface, so we run diamond grinders with vacuum "
            "shrouds until the profile is right, or shot blast where the contamination runs deeper. Cracks "
            "get chased out into a V with a crack saw and filled with a structural repair resin rather than "
            "smeared over &mdash; a crack that is only skimmed will telegraph straight back through the "
            "finished floor within a season. Spalled and pitted areas get patched and re-leveled. Oil and "
            "grease are their own problem: they wick down into the slab, and heat or foot traffic pulls them "
            "back up through a fresh coating, so contaminated concrete gets degreased and tested before "
            "anything else happens. Old failing coatings come off entirely. We also take this work on its "
            "own, without a coating attached. If you have a slab that just needs the cracks stabilized "
            "before you put down tile, racking or equipment &mdash; or you inherited a building with a "
            "peeling floor and want it stripped back to bare concrete &mdash; call us for that too.",
      bullets=["Diamond grinding and shot blasting with vacuum dust control",
               "Crack chasing and structural filling, not a skim coat over the top",
               "Spall, pit and edge repair with re-leveling where the slab needs it",
               "Removal of failed coatings &mdash; old paint, sealers and peeling epoxy",
               "Degreasing and testing so oil-contaminated concrete will take a bond",
               "Available as standalone work, with or without a new coating after it"],
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
 ("Showroom &amp; feature floor", "Bare slab &rarr; poured metallic",
  "before-bare-warehouse-slab.jpg", "Bare concrete slab in a large interior before a metallic epoxy pour",
  "metallic-epoxy-floor-finish.jpg", "Poured metallic epoxy floor in an amber blend with visible movement and depth"),
 ("Commercial deck", "Stained deck &rarr; coating with safety striping",
  "before-stained-parking-deck.jpg", "Stained and worn commercial parking deck before coating",
  "commercial-floor-coating-line-striping.jpg", "Close-up of a coated commercial floor with painted directional arrows and safety striping"),
]

SHOTS = [
 ("blue-flake-epoxy-garage-floor.jpg", "Blue and gray flake epoxy in a residential garage",
  "Residential garage in Champaign County, IL with a blue and gray flake epoxy floor"),
 ("car-showroom-epoxy-floor.jpg", "Showroom floor under a high-gloss clear topcoat",
  "Car showroom with a high-gloss coated floor reflecting the vehicles on display"),
 ("showroom-epoxy-floor-graphics.jpg", "Coated floor with inlaid color graphics and striping",
  "Coated showroom floor with black and red inlaid graphics"),
 ("metallic-epoxy-floor-finish.jpg", "Poured metallic epoxy in an amber blend",
  "Large interior with a poured amber metallic epoxy floor and steel columns"),
]


for _s in SERVICES:
    _s["pair"] = PAIRS[_s["pair_idx"]]

FLOOR_TYPES = ["Garage", "Basement", "Commercial / industrial", "Shop, warehouse or pole barn",
               "Flake epoxy", "Metallic epoxy", "Prep / repair", "Not sure yet"]

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
                   "url": BASE + "/contact/"}},
        local_business()]

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
{loc_links()}
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
      img="hero-epoxy-floor-champaign-il-1280.jpg",
      alt="High-gloss epoxy floor coating installed in a commercial building in Champaign, IL",
      intro="Champaign is home base. {name} is owned and run by {owners}, and most of our jobs are inside "
            "a twenty-minute drive of here &mdash; which means when you have a question about your floor "
            "six months from now, we are not three hours away.",
      local="Champaign hands us two very different kinds of slab, and which one you have decides most of "
            "the quote. Through Old Town, the Clark Park and Beardsley Park blocks and the streets running "
            "off West Church and University, the housing is early-1900s foursquares and bungalows, and the "
            "garages are detached, sat off the alley, and poured somewhere between the 1940s and the 1970s. "
            "Those slabs are usually sound underneath but carry real cracking, some settlement, and heavy "
            "spalling at the apron where seventy Illinois winters of road salt have chewed the surface off. "
            "Garden Hills and the mid-century ranch neighborhoods sit in a similar bracket. Out on the "
            "southwest side it flips completely: Trails at Brittany, Ironwood, Cherry Hills, Boulder Ridge "
            "and Sawgrass were built from the 1990s onward with attached three-car garages on clean, flat, "
            "well-poured concrete that needs a diamond grind and essentially nothing else. Then there is the "
            "commercial and light-industrial stock north of I-74 along North Market Street, Apollo Drive and "
            "Interstate Drive, plus the service and retail buildings along Neil Street &mdash; bigger floors, "
            "heavier traffic, and usually a phased overnight install.",
      garage="A Champaign garage floor takes a specific beating: hot tires pulling in off I-57 and I-74 in "
             "August, and road salt melting off the fenders from December through March. Both of those are "
             "what kill a cheap floor. Hot tires lift any coating that was not mechanically bonded to the "
             "concrete, and salt works into every pore of an uncoated slab and spalls the surface off it. So "
             "we grind, we repair the concrete properly, and we install a system rated for hot-tire pickup. "
             "In the older neighborhoods that means budgeting for crack and apron repair before the coating; "
             "in the newer subdivisions it usually means the whole budget goes into the finish instead. "
             "Either way most two- and three-car garages here are a one- to two-day install, and you are "
             "parking on it again inside a week.",
      area="We are ten minutes from Memorial Stadium and the State Farm Center, so scheduling in Champaign "
           "is genuinely easy &mdash; including the small single-bay jobs a lot of contractors will not "
           "drive out for.",
      nearby=["Urbana", "Savoy", "Tolono", "Mahomet"]),

 dict(slug="epoxy-flooring-urbana-il", city="Urbana", county="Champaign County",
      img="epoxy-garage-floor-interior.jpg",
      alt="Detached garage in Urbana, IL with a clean coated gray epoxy floor and storage shelving",
      intro="Urbana is about ten minutes from where we keep the equipment, which makes it one of the "
            "easiest towns in the county for us to schedule &mdash; small jobs included.",
      local="Urbana has an older housing stock than most of Champaign County, and that shows up in the "
            "concrete. Around Leal, the Historic East Urbana blocks and the streets near downtown and "
            "Crystal Lake Park, you are mostly looking at pre-1940 homes with detached garages set back off "
            "the alley. Those slabs tend to be thinner than a modern pour, with hairline cracking through "
            "the middle, some settlement toward the door, and spalling along the apron. None of that rules "
            "out epoxy &mdash; it just means the repair stage is genuine work rather than a formality, and "
            "we say so in the quote instead of discovering it on the day. The 1950s and 60s ranches out "
            "toward Ambucs and Crystal Lake are a step up in slab quality, and Stone Creek on the southeast "
            "side is a different world again: newer construction, attached three-car garages, flat sound "
            "concrete. On the commercial side, the medical and office buildings around the Carle Foundation "
            "Hospital campus and the businesses around Lincoln Square and the Market at the Square district "
            "usually want low-odor products and an overnight turnaround, which we can schedule.",
      garage="Most garage floor coating we do in Urbana is on a detached garage that has been standing for "
             "sixty or seventy years, and the honest answer is that those floors need more prep than a new "
             "build does. We chase and fill the cracks, patch the spalled apron by the door, grind the whole "
             "slab to open concrete and then coat it. Done that way an Urbana garage floor looks as good as "
             "anything in a new subdivision and lasts just as long. Skipped, the coating peels off the "
             "patched areas first and the whole thing looks worse than bare concrete did. Flake is the "
             "popular choice here for exactly that reason &mdash; it hides repaired areas far better than a "
             "solid color ever will.",
      area="Urbana sits right next to our base, so there is no trip charge, and we can usually get out to "
           "look at a floor within a few days of the call.",
      nearby=["Champaign", "St. Joseph", "Savoy", "Rantoul"]),

 dict(slug="epoxy-flooring-savoy-il", city="Savoy", county="Champaign County",
      img="garage-floor-coating-champaign-il.jpg",
      alt="Newer three-car garage in Savoy, IL finished with a light gray epoxy floor coating",
      intro="Savoy sits ten minutes south of Champaign on Neil Street, and it is one of our favorite "
            "villages to work in &mdash; largely because of what the concrete under it looks like.",
      local="Savoy grew late and it grew fast, and almost all of that growth is post-1995. Prairie Fields, "
            "the subdivisions off Curtis Road and Burwash Avenue, and the newer streets around Windsor and "
            "Church were built to modern standards, which means the garage slabs here are generally "
            "thicker, flatter, better cured and far less cracked than anything in the older parts of the "
            "county. For an epoxy floor that is close to the ideal starting point: minimal crack and spall "
            "repair, a straightforward diamond grind, and the entire budget goes into the coating system "
            "rather than into fixing concrete. Three-car attached garages are common through these "
            "subdivisions, and a full-broadcast flake floor across that much square footage genuinely "
            "changes how the space works &mdash; people stop using it purely for cars and start using it. "
            "Beyond the residential side, we cover the commercial buildings along the Route 45 corridor, the "
            "retail around Savoy Plaza and the 16 IMAX, and the hangar-adjacent and institutional space out "
            "toward University of Illinois Willard Airport.",
      garage="Garage floor coating in Savoy is usually the cleanest version of this job. A slab poured in "
             "the last twenty-five years typically needs joint treatment and a grind rather than structural "
             "repair, so the install runs fast and the finish comes out flawless. That also means solid "
             "color is genuinely on the table here, which it often is not on an older slab &mdash; a "
             "solid-color floor is a mirror and shows every imperfection, so it only works over concrete "
             "that is actually flat. If you want the classic dense flake look instead, this is the kind of "
             "slab where it goes down beautifully. Either way, expect one to two days on site and vehicles "
             "back on it after about a week.",
      area="Ten minutes from our base, well inside the radius, no trip charge, and easy to schedule around "
           "Willard Airport traffic.",
      nearby=["Champaign", "Tolono", "Urbana", "Monticello"]),

 dict(slug="epoxy-flooring-mahomet-il", city="Mahomet", county="Champaign County",
      img="shop-warehouse-epoxy-floor-central-illinois.jpg",
      alt="Pole barn shop near Mahomet, IL with a freshly coated concrete floor",
      intro="Mahomet is a straight fifteen-minute run west on I-74, and it has grown fast enough that we "
            "are out there most months of the year.",
      local="What sets Mahomet apart is the outbuildings. Lots here run considerably bigger than they do in "
            "Champaign or Urbana, so alongside the attached garages in Timberline, Thornewood, Prairieview "
            "and the newer streets north of the interstate, we spend a lot of time in detached shops, pole "
            "barns and machine sheds &mdash; and those bring their own considerations. A pole barn slab is "
            "frequently poured later than the building, thinner than a house garage, and often without a "
            "vapor barrier underneath it, so moisture testing genuinely matters before we pick a system. "
            "Coat a slab with vapor driving up through it and you will have blisters by the following "
            "summer. When the readings come back clean, a coated shop or barn floor is transformative: it "
            "stops the concrete dust that gets into everything, it throws your existing lights back up into "
            "the building, and you can push a broom across it instead of fighting it. Around the village "
            "itself, the older homes near the Sangamon River and toward Lake of the Woods sit on typical "
            "mid-century garage concrete that wants the usual crack and apron work first.",
      garage="Garage floor coating in Mahomet splits between two jobs. In the newer subdivisions it is a "
             "clean modern slab and a straightforward grind-and-coat. Out on the acreages it is often a "
             "detached shop or a barn floor of two, three or four times the square footage, where the "
             "per-foot rate drops but the moisture question comes first. We test either way. And because "
             "these buildings usually double as workshops rather than just parking, we tend to steer people "
             "toward a full-broadcast flake with a non-slip aggregate in the topcoat &mdash; it hides "
             "everything, it grips when there is snowmelt or a spilled drink on it, and dropped tools do not "
             "mark it the way they mark bare concrete.",
      area="Fifteen minutes from base, right past Lake of the Woods Forest Preserve and the Museum of the "
           "Grand Prairie. No trip charge anywhere in the village or the surrounding acreages.",
      nearby=["Champaign", "Fisher", "Urbana", "Monticello"]),

 dict(slug="epoxy-flooring-rantoul-il", city="Rantoul", county="Champaign County",
      img="high-gloss-epoxy-shop-floor.jpg",
      alt="Large hangar-style building in Rantoul, IL with a high-gloss epoxy floor",
      intro="Rantoul is about twenty minutes north of Champaign on I-57, and it has a building stock unlike "
            "anywhere else in the county.",
      local="Because of the old Chanute Air Force Base, Rantoul carries far more hangar, warehouse and "
            "institutional square footage than a town its size would normally have. The Rantoul National "
            "Aviation Center and the surrounding former base buildings hold floors that are large, old, and "
            "have been under traffic for decades &mdash; and those are exactly the slabs where prep is not "
            "optional. They get shot blasting rather than grinding, serious crack and joint treatment, and a "
            "high-build system that can take forklifts and steel wheels rather than a thin residential-grade "
            "coating. On the residential side, a large share of Rantoul housing dates from the base era, "
            "1950s and 60s, and those garage slabs come with the same thinner concrete and salt-worn aprons "
            "we see across older Urbana. They respond very well to a proper repair-and-coat. Around downtown "
            "and out toward Wabash & Erie Park the housing runs older still, with detached garages that are "
            "worth quoting individually rather than off a per-foot rate.",
      garage="Garage floor coating in Rantoul is mostly work on mid-century slabs, and we approach it the "
             "same way we do in Urbana: fix the concrete first, then coat it. The apron by the overhead door "
             "is nearly always the worst area, because that is where the snow and the salt collect, and it "
             "needs patching and re-leveling before anything goes over it. Once that is done, flake is the "
             "sensible finish &mdash; it is forgiving over repaired areas and it builds in grip. We also get "
             "a fair number of calls here for larger detached garages and shop buildings, which price better "
             "per square foot than a standard two-car does.",
      area="Twenty minutes up I-57, comfortably inside the service radius, no trip charge.",
      nearby=["Paxton", "Champaign", "Gibson City", "Urbana"]),

 dict(slug="epoxy-flooring-bloomington-il", city="Bloomington", county="McLean County",
      img="commercial-epoxy-floor-coating-bloomington-il.jpg",
      alt="Commercial building in Bloomington, IL with a freshly coated high-gloss epoxy floor",
      intro="Bloomington is our second home market. It is roughly a fifty-minute drive up I-74 from "
            "Champaign County, and there is no trip charge for it &mdash; we quote and schedule McLean "
            "County exactly the way we do our own back yard.",
      local="Bloomington has more architectural range than most Central Illinois cities, and it changes what "
            "we quote block to block. Dimmitt's Grove and Founders' Grove are full of Victorians, "
            "foursquares and early-1900s homes with detached carriage-style garages sitting on old, thin, "
            "much-repaired concrete. The east side and the streets around Miller Park run to 1950s through "
            "70s ranches with attached two-car garages &mdash; sound slabs, but usually with settlement "
            "cracking and a spalled apron. Then Fox Creek, Eagle Crest, Tipton Trails and the Grove at "
            "Kickapoo Creek are modern subdivisions with big attached three-car garages on clean concrete "
            "that needs little more than a grind. Commercially, Bloomington keeps a lot of office, service "
            "and back-of-house square footage in play thanks to the insurance and corporate employers here, "
            "and those floors almost always need to be coated in phases and outside business hours &mdash; "
            "which is how we prefer to run them anyway.",
      garage="Garage floor coating in Bloomington divides cleanly into those same two jobs. In the "
             "established neighborhoods the slab is mid-century: sound underneath, but with hairline "
             "cracking, some pitting, and spalling along the apron where the salt collects, all of which "
             "gets chased, filled and patched before anything else happens. In the newer subdivisions the "
             "concrete is generally clean and flat, so the work is a straight diamond grind and the budget "
             "goes into the finish instead. Either way you get a system rated for hot-tire pickup, because a "
             "coating that lifts where the car parks is not a floor, it is a callback &mdash; and driving "
             "back up I-74 to redo somebody's garage is not a business model.",
      area="Fifty minutes up I-74, past Downs and Le Roy. We treat McLean County as a home market: same "
           "pricing, same scheduling, no trip charge.",
      nearby=["Normal", "Downs", "Le Roy", "Clinton"]),

 dict(slug="epoxy-flooring-normal-il", city="Normal", county="McLean County",
      img="polished-epoxy-parking-deck.jpg",
      alt="Coated concrete floor in a commercial lower level in Normal, IL",
      intro="Normal sits right against Bloomington, so we cover it on the same runs &mdash; and like the "
            "rest of McLean County, there is no trip charge to come out and quote.",
      local="Normal splits three ways for us. Around Illinois State University and Uptown, there is a steady "
            "stream of rental, retail and small-commercial floors where the priority is a fast turnaround "
            "between tenants and a surface that mops clean rather than one that looks like a showpiece. Old "
            "North Normal and the streets around Fairview Park run to older homes with detached garages on "
            "aging concrete. Out on the north side, Blackstone Trails, Savannah Green and the newer "
            "subdivisions off Raab Road bring large attached three-car garages on modern slabs, and those are "
            "where most of our residential flake work in Normal happens. There is also real industrial "
            "square footage in and around town &mdash; the manufacturing corridor here keeps heavier work in "
            "the mix, which means a different system, a heavier build thickness and shot blasting rather "
            "than grinding, but the same prep discipline underneath it.",
      garage="Garage floor coating in Normal is mostly newer-subdivision work, and on a clean modern slab "
             "the install is quick: grind, treat the joints, base coat, broadcast flake, scrape and vacuum, "
             "clear topcoat. One to two days on site. Around Old North Normal and the older streets it is "
             "the familiar mid-century slab that needs crack and apron repair first. One thing worth knowing "
             "if you are near campus: we can schedule around the university calendar, which matters if you "
             "are coating a rental garage or a small commercial floor and need it done between tenants "
             "rather than during a move-in week.",
      area="Same run as Bloomington, straight up I-74. Uptown Normal, ISU, Constitution Trail and the north "
           "side are all inside the no-trip-charge area.",
      nearby=["Bloomington", "Hudson", "Towanda", "Le Roy"]),

 dict(slug="epoxy-flooring-decatur-il", city="Decatur", county="Macon County",
      img="metallic-epoxy-floor-finish.jpg",
      alt="Large industrial interior in Decatur, IL with a poured metallic epoxy floor",
      intro="Decatur is about fifty minutes southwest of Champaign, well inside our service area, and it is "
            "the most industrial market we work in.",
      local="Decatur's ag-processing and manufacturing base means the floors here are frequently large, "
            "hard-used and chemically abused &mdash; the sort of slab where a thin roll-on coating would not "
            "survive a season. Those jobs get shot blasting or heavy grinding, full joint and crack "
            "treatment, and a high-build chemical-resistant system, usually with line striping where the "
            "traffic patterns need marking out. Residentially, Decatur has some of the best older housing "
            "stock in Central Illinois. The West End Historic District and the streets around Millikin "
            "University hold grand early-1900s homes, many with detached carriage-house garages on original "
            "concrete that has been patched more than once. The mid-century ranches out toward Mound Road "
            "and the neighborhoods around Fairview Park are more straightforward. South Shores, on Lake "
            "Decatur, is a different case again &mdash; lakefront properties, plenty of detached shops and "
            "boat storage, and slabs that see a lot of wet traffic and so usually want non-slip aggregate "
            "worked into the topcoat.",
      garage="Garage floor coating in Decatur ranges from a standard attached two-car to a detached "
             "carriage house that has been standing for a century. On the older properties the concrete is "
             "the deciding factor, and we will tell you honestly at the estimate whether a slab is worth "
             "coating or whether the money is better spent replacing it &mdash; occasionally it is, and we "
             "would rather say so than take the job. Where the slab is sound, the process is the same one we "
             "run everywhere: grind, chase and fill, patch the spalling, coat, flake, seal. Around the lake "
             "we normally recommend non-slip aggregate as standard.",
      area="Fifty minutes southwest via Route 121 or I-72. Decatur, Forsyth, Mt. Zion and Argenta are all "
           "inside the radius with no trip charge.",
      nearby=["Forsyth", "Mt. Zion", "Cerro Gordo", "Clinton"]),

 dict(slug="epoxy-flooring-danville-il", city="Danville", county="Vermilion County",
      img="before-bare-shop-concrete-floor.jpg",
      alt="Shop building in Danville, IL with bare concrete ready for an epoxy floor coating",
      intro="Danville is a straight thirty-five-minute shot east on I-74, which puts the whole of Vermilion "
            "County comfortably inside our range.",
      local="Danville's industrial history left it with a lot of older shop and warehouse space, and those "
            "floors tend to arrive with the full set of problems at once: oil-soaked concrete, spalling at "
            "the dock doors, joints that have opened up under years of wheel traffic, and often an old "
            "coating that is already letting go in sheets. That is fine &mdash; it just means the prep day is "
            "a real day. Degrease it, strip whatever is failing, blast the profile open, fix the joints, and "
            "then it will take a coating that holds. On the residential side, the North Street Historic "
            "District and the older streets around Lincoln Park run to pre-1930 homes with detached garages "
            "off the alley, on thin original slabs. Vermilion Heights and the mid-century neighborhoods are "
            "a more typical ranch-and-attached-garage proposition. We also cover the smaller towns around "
            "Danville &mdash; Tilton, Westville, Georgetown and out toward Kickapoo State Recreation Area.",
      garage="Garage floor coating in Danville is mostly older-slab work, and the apron is nearly always the "
             "problem area. Decades of freeze-thaw and salt take the top layer off the concrete right where "
             "the overhead door sits, and if that is coated over without being repaired it will fail there "
             "first and take the surrounding floor with it. We patch and re-level the apron, chase and fill "
             "the cracks, grind the whole slab, then coat. Flake is the default recommendation here because "
             "it hides repaired areas so much better than solid color does, and on a garage that has been "
             "standing since the 1920s there will be repaired areas.",
      area="Thirty-five minutes east on I-74. Danville, Tilton, Westville, Georgetown and Hoopeston are all "
           "inside the service radius.",
      nearby=["Tilton", "Westville", "Georgetown", "Hoopeston"]),

 dict(slug="epoxy-flooring-monticello-il", city="Monticello", county="Piatt County",
      img="blue-flake-epoxy-garage-floor.jpg",
      alt="Residential garage near Monticello, IL finished with a blue and gray flake epoxy floor",
      intro="Monticello is twenty-five minutes west of Champaign on I-72, and Piatt County is well inside "
            "the area we cover without a trip charge.",
      local="Work in Monticello skews rural, and that shapes what we quote. Between the acreages outside "
            "town and the farms around them, a large share of what we coat is a detached shop, a machine "
            "shed or a pole barn rather than an attached two-car garage. Those slabs almost always need "
            "moisture testing first, because plenty of them were poured without a vapor barrier underneath "
            "and will push a standard coating straight back off. When the readings come back right, a coated "
            "shop floor pays for itself in how much easier the building is to keep clean and how much "
            "brighter it gets. In town, the older homes around the courthouse square and the streets running "
            "toward Allerton Park sit on typical mid-century garage concrete that needs the usual crack and "
            "apron work, while the newer subdivisions on the edges of the village are clean modern pours. We "
            "also pick up commercial work along the Route 105 corridor and around the Monticello Railway "
            "Museum end of town.",
      garage="Garage floor coating in Monticello often is not a garage at all &mdash; it is a thirty by "
             "forty shop with a workbench down one side. Those price better per square foot than a standard "
             "two-car and they benefit more from being coated, because that is a building you actually spend "
             "time in. For a working shop we recommend full flake with non-slip aggregate: it hides the "
             "concrete repairs, it grips when there is snow melting off a truck, and it does not show every "
             "mark the way a solid color does. For an attached garage in one of the newer village "
             "subdivisions, it is a straightforward grind-and-coat.",
      area="Twenty-five minutes west on I-72, past Allerton Park and Lodge Park. All of Piatt County is "
           "inside the radius.",
      nearby=["Bement", "Cerro Gordo", "Mahomet", "Clinton"]),

 dict(slug="epoxy-flooring-tuscola-il", city="Tuscola", county="Douglas County",
      img="showroom-epoxy-floor-graphics.jpg",
      alt="Retail floor in Tuscola, IL finished with a coated epoxy surface and inlaid graphics",
      intro="Tuscola sits about half an hour south of Champaign where I-57 meets US-36, and that crossroads "
            "position is a big part of what we get called out for.",
      local="Because of the interstate junction and Tanger Outlets, Tuscola punches well above its size on "
            "the commercial side. Retail units, service bays and light industrial along the Route 36 "
            "corridor all need floors that look presentable to customers and still take a beating from carts "
            "and foot traffic, and those jobs usually want a hard-wearing solid color or flake system with a "
            "clear urethane topcoat over it, plus line striping to mark walkways and back-of-house routes. "
            "Away from the junction, Tuscola is a small county-seat town: older homes around the Douglas "
            "County courthouse and Ervin Park with detached garages on original concrete, a scattering of "
            "newer builds on the edges, and then ag country in every direction. That last part matters most "
            "by volume &mdash; machine sheds, grain-operation shops and equipment buildings make up a good "
            "share of the square footage we coat down here, and every one of those rural slabs gets moisture "
            "tested before we spec anything.",
      garage="Garage floor coating in Tuscola runs the full spread, from a two-car attached in a newer "
             "subdivision to a farm shop big enough to pull a combine into. The small end is a "
             "grind-and-coat over sound concrete. The large end is about square footage and moisture: the "
             "per-foot rate drops as the floor gets bigger, but a barn or shed slab poured without a vapor "
             "barrier needs a system that can tolerate it. On the older in-town garages it is the familiar "
             "story of a thin slab, a cracked middle and a spalled apron, all of which we repair before "
             "coating rather than after.",
      area="Half an hour south at the I-57 and US-36 junction. Tuscola, Arcola, Villa Grove and Arthur are "
           "all inside the service radius.",
      nearby=["Arcola", "Villa Grove", "Arthur", "Tolono"]),

 dict(slug="epoxy-flooring-paxton-il", city="Paxton", county="Ford County",
      img="shop-warehouse-epoxy-floor-central-illinois.jpg",
      alt="Farm shop building near Paxton, IL with a coated concrete floor",
      intro="Paxton is around thirty-five minutes north of Champaign on I-57, and Ford County sits "
            "comfortably inside the fifty-mile radius we work.",
      local="Paxton is a county seat in the middle of some of the most productive farmland in Illinois, and "
            "the floors follow from that. Grain operation shops, equipment sheds and ag service buildings "
            "make up most of the larger square footage we coat here, and those are almost always slabs that "
            "went in without a vapor barrier and have spent years taking dirt, chemical and steel-wheel "
            "traffic. They get moisture tested, degreased where needed, blasted or ground hard, and then a "
            "build heavy enough to survive equipment rather than cars. In town, the housing around the Ford "
            "County courthouse and Pells Park is mostly older &mdash; pre-war and mid-century homes with "
            "detached garages on original concrete that will need crack and apron repair. There is also a "
            "steady run of small commercial work along the US-45 corridor. Paxton is a small town, and we "
            "quote the single-bay jobs here the same way we quote the big ones.",
      garage="Garage floor coating in Paxton is usually one of two things: an older detached garage in town "
             "that needs its concrete fixed before anything is coated, or a farm shop several times that "
             "size where the moisture reading decides the system. For the in-town garages we recommend flake "
             "&mdash; it is the most forgiving finish over repaired concrete and it adds grip for the "
             "winter. For a working shop, flake with a non-slip aggregate in the topcoat, because those "
             "floors get wet and get walked on in boots. Either way, there is no trip charge to come out and "
             "look at it.",
      area="Thirty-five minutes north on I-57, past Rantoul and Gibson City. All of Ford County is inside "
           "the radius.",
      nearby=["Rantoul", "Gibson City", "Champaign", "Hoopeston"]),

 dict(slug="epoxy-flooring-clinton-il", city="Clinton", county="DeWitt County",
      img="polished-epoxy-parking-deck.jpg",
      alt="Coated concrete floor in a large building in Clinton, IL",
      intro="Clinton is about forty-five minutes west of Champaign, roughly halfway between us and "
            "Bloomington, and DeWitt County is inside our service radius with no trip charge.",
      local="Clinton is a small county seat with a mix we do not see everywhere. There is the older housing "
            "around the DeWitt County courthouse square and the C.H. Moore Homestead &mdash; pre-war and "
            "mid-century homes, detached garages, original concrete with the usual cracking and apron "
            "spalling. There is genuine industrial and institutional square footage in the area, including "
            "the buildings supporting the Clinton Power Station, where floors need real build thickness and "
            "chemical resistance rather than a residential-grade coating. And then there is Clinton Lake and "
            "Weldon Springs, which brings a surprising number of detached shops, boat and RV storage "
            "buildings and lakeside outbuildings into the mix. Those lake-adjacent floors see a lot of wet "
            "traffic, so we normally spec non-slip aggregate into the topcoat as standard rather than as an "
            "upgrade. Rural shops and machine sheds across the rest of DeWitt County round it out, and every "
            "one of those gets moisture tested first.",
      garage="Garage floor coating in Clinton is a good example of why we quote on site rather than over "
             "the phone. A detached garage near the square and a forty-foot storage building out by the lake "
             "are the same service on paper and completely different jobs in practice &mdash; different "
             "prep, different system, different per-foot rate. What does not change is the order of "
             "operations: test the slab, fix the concrete, grind it open, then coat. For storage buildings "
             "and anything near the water we push hard for non-slip aggregate, because a smooth coated floor "
             "with lake water and a trailer on it is genuinely slick.",
      area="Forty-five minutes west, an easy run out Route 54. Clinton, Farmer City and the Clinton Lake "
           "area are all inside the radius.",
      nearby=["Farmer City", "Bloomington", "Decatur", "Monticello"]),

 dict(slug="epoxy-flooring-tolono-il", city="Tolono", county="Champaign County",
      img="epoxy-garage-floor-interior.jpg",
      alt="Garage in Tolono, IL with a clean coated concrete floor and workbench",
      intro="Tolono is fifteen minutes south of Champaign on US-45, which makes it one of the closest towns "
            "on this list and one of the easiest for us to fit into a week.",
      local="Tolono is a village of a few thousand surrounded immediately by farmland, and that combination "
            "gives us a nice split of work. In the village itself, the older homes around the historic rail "
            "crossing and toward Tolono Community Park have detached garages on mid-century concrete &mdash; "
            "thin slabs, cracking through the middle, spalled aprons, all of it repairable and all of it "
            "worth repairing properly. The newer subdivisions on the edges of the village, and the homes out "
            "toward the Unity school campus, are modern pours with attached two- and three-car garages that "
            "need little more than a diamond grind. Step outside the village limits and it becomes machine "
            "sheds, grain shops and equipment buildings, which is where the bigger square footage is. Those "
            "rural slabs get moisture tested without exception, because a barn floor poured straight onto "
            "grade will drive vapor up through a coating that was not specified for it.",
      garage="Garage floor coating in Tolono is genuinely quick for us to schedule &mdash; it is fifteen "
             "minutes from base, so we can drop in to look at a floor almost any day and there is obviously "
             "no trip charge. On the newer subdivision slabs it is a straight grind-and-coat, one to two "
             "days on site, and solid color is a real option because the concrete is flat enough to carry "
             "it. On the older village garages we repair first and then recommend flake, which hides the "
             "patched areas and adds grip. For the farm shops out of town, expect a moisture test, a heavier "
             "build and non-slip aggregate in the topcoat.",
      area="Fifteen minutes south on US-45, closer than most of the towns we cover. Tolono, Philo, Sidney "
           "and Pesotum are all a short run from base.",
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

<section class="section section--dark">
  <div class="wrap">
    <div class="split split--flip">
      <div>
        <p class="eyebrow">Garages</p>
        <h2>{l['h2_garage']}</h2>
        <p>{l['garage']}</p>
        <div class="btn-row" style="margin-top:1.75rem">
          <a class="btn btn--onDark" href="/contact/?type=Garage">Quote my garage floor</a>
          <a class="btn btn--ghostDark" href="/services/garage-floor-epoxy/">Garage floor epoxy</a>
        </div>
      </div>
      <div class="split__media reveal">
        <img src="{IMG}/blue-flake-epoxy-garage-floor.jpg"
             alt="Garage floor coating of the kind we install in {l['city']}, IL &ndash; blue and gray flake epoxy"
             width="1280" height="854" loading="lazy" decoding="async">
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
        <p>{l['area']}</p>
        <p>We are based in {CFG['basedIn']['county']} and work {AREA['radiusMiles']}+ miles in every
        direction, so {l['city']} and the rest of {l['county']} are well inside it, along with
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

    # Renaming a slug leaves the old directory behind, still crawlable and still
    # competing with its replacement. Report those; --prune deletes them.
    wanted = {os.path.normpath(os.path.join(OUT, rel)) for _, rel, _, _, _, _ in pages}
    stale = []
    for base in [OUT, os.path.join(OUT, "services")]:
        if not os.path.isdir(base): continue
        for name in sorted(os.listdir(base)):
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
