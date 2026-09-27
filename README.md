# SkillBridge Automation Architecture

This document is the map for the n8n automation layer described in the
Step 13 spec. Read the **Scope and honesty note** first — it explains
exactly what's fully built, what's designed-but-untested, and what
genuinely cannot be built without your own credentials and an n8n
instance to test against.

---

## Scope and honesty note (read this first)

**Fully built, in this repo, matching the rest of the project's pattern:**
- The complete Supabase schema for this system (migration
  `20260921115719_multiclient_automation_schema.sql`) — tables, RLS,
  indexes, the `client_id` generator, dedupe protection.

**Designed in full node-by-node detail, with an importable n8n JSON
skeleton, but NOT executed or tested:**
- `SB — MASTER — Opportunity Research` (partial — the parts that
  don't require a paid API key)
- `SB — MASTER — Client Daily Delivery`

I have no n8n instance, no Google Places/Meta/email credentials, and
no network access in this environment to actually run these. They're
built to the real node types and real Supabase REST calls n8n would
use, but "designed correctly" and "verified working" are different
claims — only you can do the second one, in your own n8n.

**Specified (workflow purpose, trigger, inputs/outputs, stop
conditions) but not built as JSON:** the remaining 11 workflows
below. Building all 13 as fake-tested JSON would look complete while
being unverifiable noise — I'd rather hand you 2 done right and 11
precisely specified than 13 I can't stand behind.

**Cannot be built at all without your accounts/keys, regardless of
effort:** Google Places API key, Meta Marketing API app + access
token, an email-sending provider (Resend, etc.) with a verified
domain, and — if you want it — Canva Connect API access. These are
credentials only you can create; I can wire the workflow around them
once you have them.

---

## 1. System architecture

```
CLIENT
  down
SkillBridge Web App  (this repo -- Vite + vanilla JS)
  down
Supabase Auth
  down
Supabase Database (RLS-protected)
  down
n8n Automation Layer  (separate hosted service -- not in this repo)
  down
External APIs (Google Places, Meta Marketing API, email provider)
  down
Supabase (results written back)
  down
Client Dashboard (reads the same RLS-protected tables)
```

n8n never talks to the browser directly. It talks to Supabase using
the **service-role key**, stored only as an n8n credential (Settings ->
Credentials -> HTTP Header Auth or Supabase node), never in this
repo, never in any frontend file. That key bypasses RLS by design --
which is exactly why it must never leave n8n's server-side credential
store.

SkillBridge and ZYRVON stay architecturally separate: SkillBridge
owns `opportunities`, `campaigns`, `outreach_*`, `ads_campaigns`; a
ZYRVON engagement for a client would be its own n8n workflow
(`[CLIENT_ID] -- ZYRVON <purpose>`) reading/writing its own tables (or
none in this database at all) -- it should reference `clients.id` to
stay linked to the same person, not duplicate their profile.

---

## 2. client_id

Format: `<first-initial>.<second-initial>.<3-digit sequence>` --
e.g. `V.K.001` for "Vikash Kumar". Generated once, in
`public.generate_client_id()`, called from the (updated)
`handle_new_user()` trigger at signup. It's copied onto both
`profiles.client_id` and `clients.client_id` for convenience in n8n
executions and logs.

**It is a label, not a credential.** Every RLS policy in the new
migration keys off `auth.uid()` / `clients.user_id`, never off
`client_id` -- so even if a `client_id` value leaked (e.g. in a log or
a PDF filename), it grants no access to anything.

---

## 3. Workflow map (all 13, exact names)

| # | Workflow name | Status here |
|---|---|---|
| 1 | `SB — MASTER — Client Onboarding` | Specified below (S5) |
| 2 | `SB — MASTER — Opportunity Research` | Built (S6) -- non-API-key portion |
| 3 | `SB — MASTER — Opportunity Intelligence` | Specified (S5) |
| 4 | `SB — MASTER — Opportunity Report` | Specified (S5) |
| 5 | `SB — MASTER — Client Daily Delivery` | Built (S7) |
| 6 | `SB — MASTER — Outreach Preparation` | Specified (S5) |
| 7 | `SB — MASTER — Outreach Send` | Specified (S5) |
| 8 | `SB — MASTER — Follow-Up` | Specified (S5) |
| 9 | `SB — MASTER — Reply Classification` | Specified (S5) |
| 10 | `SB — MASTER — Ads Reporting` | Specified (S5) |
| 11 | `SB — MASTER — Dashboard Sync` | Specified (S5) |
| 12 | `SB — MASTER — Notifications` | Specified (S5) |
| 13 | `SB — MASTER — Error Handler` | Specified (S5) |

Client-specific exception workflows (rare, only when genuinely
needed): `[CLIENT_ID] — <Workflow Type>`, e.g.
`V.K.001 — Custom CRM Automation` for a ZYRVON engagement.

---

## 4. Shared conventions (apply to every workflow)

- **Trigger validation first, always.** Every workflow's first real
  step after the trigger is "does this `client_id` / `opportunity_id`
  / `campaign_id` actually exist and belong to who it claims?" -- a
  Supabase lookup, not an assumption from the trigger payload.
- **Error branch on every workflow**, wired to
  `SB — MASTER — Error Handler`: catches the failure, writes/updates
  an `automation_jobs` row with `status='FAILED'` and
  `error_message`, and creates a `notifications` row with
  `type='automation_error'` for the admin (not the client, unless the
  failure is something the client needs to act on).
- **One failed item never kills the batch.** Loop over items with
  n8n's "Continue on Fail" per item, log the specific failure, move
  on.
- **Idempotency.** Before inserting an opportunity, check the unique
  index on `(client_id, company_website, lower(company_name))` (see
  migration). Before sending a message, check
  `outreach_messages.status <> 'SENT'` for that contact +
  `message_type` combination first.
- **Rate limiting.** Every HTTP Request node calling an external API
  needs n8n's built-in batching (Split In Batches node) + a Wait
  node between batches, tuned to that API's documented rate limit --
  I can't tune this for you without knowing which plan/quota you're
  on.

---

## 5. Specified workflows (design-level; build once you have the underlying credential)

### `SB — MASTER — Client Onboarding`
**Trigger:** Supabase Webhook (Database Webhook on `clients` INSERT,
or called directly from the signup flow).
**Flow:** validate client -- nothing to do, `handle_new_user()`
already created `profiles` + `clients` + `client_id` atomically in
Postgres (see migration) -- this workflow's only job is to create a
`client_requirements` row once the client fills the onboarding form
in the app, and to write a `notifications` row ("Welcome") + an
`automation_jobs` row (`workflow_type='ONBOARDING'`).
**Needs no external API key** -- buildable immediately once you're
ready to wire the onboarding form's submit to a webhook.

### `SB — MASTER — Opportunity Intelligence`
**Trigger:** called by Opportunity Research (S6) once candidate
businesses are collected, one execution per candidate.
**Flow:** take the raw scraped/API fields -- an LLM node (your choice
of provider, kept as a swappable credential) writes `potential_need`,
`why_relevant`, `recommended_service`, `suggested_solution`,
`suggested_approach`, and an `opportunity_score` (0-100) **strictly
as a prioritization heuristic** -- the prompt must explicitly forbid
the model from claiming conversion probability, and the workflow
must reject/blank any output that violates the disclaimer rules in
S8 of the original spec.
**Needs:** an LLM API key (not specified which provider -- pick one
and I'll write the exact prompt + validation node once you tell me).

### `SB — MASTER — Opportunity Report`
**Trigger:** `client_id` + `opportunity_id`, called after an
opportunity is saved.
**Flow:** fetch opportunity row -- render into the HTML/CSS report
template (build this as a reusable HTML file, since "the workflow
must continue to function without Canva" per spec) -- convert to PDF
(n8n has no native HTML-to-PDF node; use an HTTP Request to a
PDF-rendering service, or self-host gotenberg/weasyprint -- pick
one, it needs a real endpoint) -- upload to Supabase Storage -- insert
`opportunity_reports` row with `report_url` + `generation_status='READY'`.
**Needs:** a chosen PDF-rendering approach -- flagging rather than
guessing which one you'll actually run.

### `SB — MASTER — Outreach Preparation`
**Trigger:** client approves a campaign + opportunity selection in
the app (webhook).
**Flow:** for each approved opportunity, generate a personalized
draft (LLM node, same provider as above) -- insert
`outreach_messages` row with `status='DRAFT'`. **Never** auto-advance
to `SENT` -- that only happens when the client clicks Approve in the
app (which flips the row through the RLS policy already restricting
clients to `DRAFT`/`APPROVED`) and the *next* workflow picks it up.

### `SB — MASTER — Outreach Send`
**Trigger:** scheduled poll for `outreach_messages.status='APPROVED'`.
**Flow:** for each, send via the client's **OAuth-authorized** email
connection (Gmail/Outlook OAuth node in n8n -- never a stored
password) -- on success, set `status='SENT'`, `sent_at=now()`, and
update the matching `outreach_contacts.status`/`last_contacted_at` --
schedule the Day-3 follow-up row in `follow_ups`.
**Needs:** each client to complete an OAuth connection -- this is a
per-client setup step in the app, not something n8n can do for them.

### `SB — MASTER — Follow-Up`
**Trigger:** scheduled (e.g. hourly), queries `follow_ups` where
`scheduled_at <= now()` and `status='SCHEDULED'`.
**Flow:** for each, check stop conditions first -- replied?
unsubscribed? bounced? campaign paused? -- query
`outreach_contacts.status` and `reply_received_at`. If any stop
condition is true, set this follow-up `status='CANCELLED'` and do
**not** send. Otherwise send via `SB — MASTER — Outreach Send`'s send
logic (call it as a sub-workflow rather than duplicating the send
node) and schedule the next follow-up in the sequence (Day 3 -> 7 ->
14 -> stop).

### `SB — MASTER — Reply Classification`
**Trigger:** inbound email webhook from the client's authorized
email provider (Gmail push notification / IMAP poll -- depends on
which OAuth integration you actually connect).
**Flow:** LLM node classifies into the exact enum from S15 of the
spec -- update `outreach_contacts.status` and `reply_received_at` --
branch: `INTERESTED`/`MEETING_REQUEST` -> insert `notifications` row
for the client; `NOT_INTERESTED`/`UNSUBSCRIBE`/`BOUNCE` -> cancel any
`SCHEDULED` follow-ups for that contact; `UNKNOWN` -> flag for human
review (a `notifications` row to the admin, not an auto-decision).

### `SB — MASTER — Ads Reporting`
**Trigger:** scheduled (daily).
**Flow:** for each client with a connected Meta Ads account, call
the Meta Marketing API's Insights endpoint -- upsert into
`ads_campaigns` (impressions, reach, clicks, leads, spend). If no
Meta connection exists for that client, write nothing and make sure
the dashboard shows "Meta Ads integration not connected" (this is a
frontend concern -- the table simply has no rows for that client,
which the UI should treat as the not-connected state, not as "zero
performance").
**Needs:** a Meta App with Marketing API access + each client's
ad-account authorization (Meta's own OAuth flow) -- this is a real
Meta App Review process for anything beyond your own ad accounts.

### `SB — MASTER — Dashboard Sync`
This one doesn't need to exist as a separate n8n workflow -- every
other workflow already writes directly to the tables the dashboard
reads via RLS-protected Supabase queries. Real-time UI updates can
use Supabase Realtime subscriptions in the frontend instead of an
n8n polling loop. Flagging so you don't build redundant automation.

### `SB — MASTER — Notifications`
Also not a separate workflow -- every workflow above inserts its own
`notifications` row at the relevant point (see the "Needs" callouts
above). Centralizing it as one more workflow would just add an extra
hop; each workflow already knows exactly which notification it
needs to create.

### `SB — MASTER — Error Handler`
**Trigger:** called via n8n's "Error Trigger" node, attached to every
other workflow.
**Flow:** receives the failing workflow's name + error + execution
ID -- updates the matching `automation_jobs` row (`status='FAILED'`,
`error_message`) -- inserts a `notifications` row for the **admin**
(`type='automation_error'`) -- does not surface raw error text to the
client-facing notification, only to the admin one.

---

## 6. Built: `SB — MASTER — Opportunity Research`

File: `automation/n8n-workflows/SB-MASTER-Opportunity-Research.json`

This covers steps 1-9 and 15-19 of the spec's flow (get requirements,
validate, determine target, query Google Places, dedupe, save,
notify, log) using real node types and real Supabase REST calls.
Steps 10-14 (deep research into "potential need" / relevance /
priority) are left as a placeholder **Code node** with a clear
`// TODO: call your chosen LLM here` comment, because that step
needs an LLM credential decision I can't make for you, and I'd
rather leave an honest gap than fabricate a prompt against a
provider you may not even use.

**To import:** n8n -> Workflows -> Import from File. You'll need to:
1. Create an HTTP Header Auth credential named `Supabase Service Role`
   with header `apikey: <your service role key>` and
   `Authorization: Bearer <your service role key>` (Settings ->
   Credentials -- never paste this into the frontend project).
2. Create a Google Places API key (Google Cloud Console) and add it
   as an HTTP Query Auth credential.
3. Fill in the Code node where marked.

## 7. Built: `SB — MASTER — Client Daily Delivery`

File: `automation/n8n-workflows/SB-MASTER-Client-Daily-Delivery.json`

Scheduled trigger -> for each active client, queries opportunities
created since the last run -> if none, skips that client entirely
(never sends an empty/fabricated summary) -> builds the email body
from real row data only -> sends via whichever email node credential
you set up (SMTP, Resend, SendGrid -- the node is a generic HTTP
Request to Resend's API by default since that's what the rest of
this project already uses; swap the node if you prefer another
provider) -> updates `automation_jobs`.

---

## 8. Environment variables

See `.env.n8n.example` in the project root. As with the app's own
`.env.example`, never commit real values -- these are n8n
**credentials**, configured in n8n's own credential store, not files
your frontend ever reads.
