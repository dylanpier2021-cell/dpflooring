// Vercel serverless function: receives the 50% off funnel submission from the
// browser (same origin, plain JSON) and forwards it to the GoHighLevel inbound
// webhook server-to-server. Doing it here avoids the browser's cross-origin
// limits, so GHL always gets a real application/json body it can map.
const GHL_WEBHOOK_URL = process.env.GHL_WEBHOOK_URL ||
  "https://services.leadconnectorhq.com/hooks/mjRUsuYleLiad81XISnz/webhook-trigger/dca357a9-50d0-4467-9beb-9242697fb160";

module.exports = async function handler(req, res) {
  if (req.method === "GET") {
    res.status(200).json({ ok: true, service: "dp-lead-forwarder" });
    return;
  }
  if (req.method !== "POST") {
    res.setHeader("Allow", "GET, POST");
    res.status(405).json({ ok: false, error: "method_not_allowed" });
    return;
  }

  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch (e) { body = null; }
  }
  if (!body || typeof body !== "object" || !body.phone || !body.email) {
    res.status(400).json({ ok: false, error: "missing_fields" });
    return;
  }

  // Flat object of short strings/booleans only - nothing else is forwarded.
  const clean = {};
  Object.keys(body).slice(0, 60).forEach(function (k) {
    const v = body[k];
    if (v === null || typeof v === "boolean" || typeof v === "number") clean[k] = v;
    else if (typeof v === "string") clean[k] = v.slice(0, 2000);
  });
  clean.forwarded_by = "dpflooringservices.com/api/lead";

  try {
    const r = await fetch(GHL_WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(clean)
    });
    res.status(r.ok ? 200 : 502).json({ ok: r.ok, ghl_status: r.status });
  } catch (err) {
    res.status(502).json({ ok: false, error: "forward_failed" });
  }
};
