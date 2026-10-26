"""Generates every SkillBridge policy page as a standalone HTML file.
Run:  python3 build_policies.py
Edit the POLICIES list below, then re-run. All text is a DRAFT until a qualified
Indian legal professional has reviewed it. Items in [square brackets] are for the
owner to confirm; they are never filled in by guesswork."""
import html, os

UPDATED = "23 October 2026"
EMAIL = "hello.manavlab@gmail.com"
WHATSAPP = "+91 7350259870"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SHOW_DRAFT_NOTICE = True

def P(*a): return ("p", " ".join(a))
def L(*items): return ("ul", list(items))

COMMON_OWNER_ITEMS = [
    "Registered legal name and business status of the entity that operates SkillBridge (for example sole proprietorship or company)",
    "Registered business address, if it is to be published",
    "Governing law and courts with jurisdiction for disputes",
    "Name and contact of the person handling privacy and grievance requests (and the response time you commit to)",
]

POLICIES = [
 ("privacy-policy", "Privacy Policy",
  "How SkillBridge protects customer data, who processes it, and how we keep it.", [
  ("1. Who we are", [P("SkillBridge is a project powered by ManavLab. For every privacy question or request, write to", EMAIL + ".")]),
  ("2. Our privacy commitments", [L(
    "We never sell or rent customer personal information.",
    "We do not share customer information with unrelated websites, companies, data brokers or other third parties for their own use.",
    "We do not submit customer personal data to AI tools for model training.",
    "We do not disclose one customer's order, requirements, contact details or business information to another customer.",
    "We collect and use only the information needed to provide the service you asked for.",
    "Where we use a service provider to run SkillBridge, we name it in this policy and explain what it processes.")]),
  ("3. Why we collect your information", [P("We collect information only to:"), L(
    "reply to your inquiry and understand what you need;",
    "check whether our lead generation, collaboration or expert services suit you;",
    "prepare your order, quote and invoice, and confirm your payment;",
    "deliver the research or service you ordered;",
    "contact you about your own request;",
    "keep the website and accounts secure, and meet legal and accounting obligations.")]),
  ("4. What we collect and how it moves", [
    L("Inquiries and order details you choose to give: name, business name, email, WhatsApp or phone number, website or social link, country, city, target industry or audience, number of leads, service, and notes.",
      "Collaboration requests and expert applications: the details you enter on those forms.",
      "Account information, only if you create or sign in to a SkillBridge account: name, email and profile details.",
      "Basic technical data sent automatically when you visit any website, such as your IP address and browser type."),
    P("The order and lead forms on this website do not send your details to our server automatically. Your details leave your device only when you press Send in WhatsApp or your email app, or when you submit a Google Form."),
  ]),
  ("5. Service providers that process your data", [
    P("These providers are technically necessary to run SkillBridge. Each processes data under its own terms and privacy policy, and we name them so you know where your data may go:"),
    L("Google (Google Forms): stores the responses you submit to our inquiry, collaboration and expert forms.",
      "Google (Google Fonts): when a page loads its fonts, your browser contacts Google, which can receive your IP address.",
      "Google (Gmail, for hello.manavlab@gmail.com): stores emails you send to us.",
      "Meta (WhatsApp): carries the messages you send to us when you press Send in WhatsApp.",
      "Supabase: hosts the SkillBridge database and sign-in for accounts. It holds account and dashboard records only for people who create or sign in to an account.",
      "Website hosting provider [Vercel, to be confirmed by the owner]: serves the website and keeps standard server logs, which can include your IP address.",
      "Automation tools (not active yet): SkillBridge's planned research and reporting workflows may use a research data service, an AI language model and an email-sending service. They will be used only after the owner has configured and reviewed them, and this policy will be updated before they handle any customer data.")]),
  ("6. AI tools and model training", [
    P("We do not enter your personal data into AI tools to train their models, and we do not enter confidential customer information into any AI tool for that purpose. If an AI service is ever used to process your information, we will: use only a service whose terms and settings say it does not use customer inputs for training; send only the minimum fields needed for the task; and update this policy before doing so.")]),
  ("7. Sale, sharing and disclosure", [
    P("We do not sell or rent personal information. We share it only in these cases:"),
    L("with the service providers listed in section 5, only as needed to run SkillBridge;",
      "with a specialist or partner, only for a project or introduction you have approved and only with your permission;",
      "with public authorities, only when the law requires it.")]),
  ("8. Lead research and customer separation", [P("Prospect information in our research comes from publicly available sources. Each customer's requirements, orders and contact details are kept separate, and we never disclose one customer's private information to another. We do not sell prospect lists.")]),
  ("9. Payments", [P("We do not store card numbers, bank passwords or one-time codes on this website. Payment details are shared privately by us only after your order is confirmed. Never send payment details or one-time codes to anyone claiming to be SkillBridge without first checking with us on the contact details above.")]),
  ("10. Security", [P("We protect data with access controls. Database tables enforce row-level security, so a signed-in user can read only their own records. Administrative access is restricted to authorised accounts. Secret keys are kept on the server side and are never placed in the website's code. No system is completely secure, so we cannot guarantee absolute security. If we become aware of a personal data breach, we will act as the law requires.")]),
  ("11. How long we keep your information", [
    P("In simple words: we keep records for as long as they are needed. We do not delete everything after a fixed period, and we do not keep personal information forever for no reason."),
    L("Active accounts: we keep your account information for as long as your account stays active.",
      "Orders, invoices and business records: we keep these for as long as needed for our legitimate business purposes, such as delivering and supporting your order, answering questions about past work, and handling disputes, and for as long as applicable law requires, including accounting and tax records.",
      "Inquiries, collaboration requests and expert applications that did not lead to an order or project: we review them periodically and delete or anonymise them when they are no longer needed.",
      "Periodic review: we review inactive records and other personal information on a regular schedule [review frequency to be confirmed by the owner].",
      "Deletion requests: when you ask us to delete your information, we do so, unless the law requires us to keep certain records (for example, invoices and tax records). In that case we keep only what the law requires and tell you why."),
    P("We cannot promise to keep every personal detail forever. Storage must always be balanced against data-protection principles such as purpose limitation and data minimisation, and against applicable law."),
  ]),
  ("12. Your choices and rights", [P("You can ask us to see, correct or delete your information, to stop using it for a request you made, and to change your cookie choice at any time from the Cookie preferences link in the footer. For all privacy requests, write to", EMAIL + ". Indian data-protection law, including the Digital Personal Data Protection Act, 2023, may apply. The exact rights and response times are [to be confirmed by a qualified legal professional].")]),
  ("13. Cookies, children and changes", [P("We use only essential browser storage, and optional cookies only if you accept them (see the Cookie Policy). This website is not directed at children under 18. We may update this policy; the date at the top shows the latest version.")]),
 ], ["Name of the website hosting provider you actually use (the policy names Vercel as a placeholder)", "Whether your hosting and database regions are confirmed, and whether data-processing agreements are signed with Google, Meta, Supabase and your host", "Final decision on AI tools, and whether any AI provider will process customer data", "Review frequency for inactive records", "Response time you commit to for privacy requests"]),

 ("terms-of-service", "Terms and Conditions",
  "The terms that apply when you use the SkillBridge website and services.", [
  ("1. Agreement to these terms", [P("By using this website, submitting an inquiry, or requesting a collaboration, you agree to these terms. SkillBridge is a project powered by ManavLab.")]),
  ("2. Services", [P("SkillBridge offers the following services. Availability, scope and price are confirmed with you before any work begins:"),
    L("Lead generation: researched potential business opportunities, including the Premium Lead Generation package (50 researched potential opportunities with outreach guidance and templates, priced at ₹499 per package), and custom lead plans quoted on request.",
      "Business collaboration: research and introductions to explore potential collaborations.",
      "Expert network: project-based collaboration with independent specialists.")]),
  ("3. No guarantees", [P("SkillBridge does not guarantee customers, prospect replies, meetings, projects, sales, partnerships, revenue, search rankings or business growth. Research is based on the information available at the time.")]),
  ("4. Inquiries are not orders", [P("Submitting a form, sending a WhatsApp message, or sending an email starts an inquiry only. It does not create a payment or project obligation. Opening WhatsApp does not mean you have paid or purchased a package.")]),
  ("5. Agreements before work starts", [P("Work starts only after we confirm the scope, deliverables, price, timeline, responsibilities and payment terms in writing, for example by email or a proposal. Where a written agreement is required, we will tell you before any payment is due.")]),
  ("6. Your responsibilities", [L("Give accurate and lawful information.", "Do not misuse the website, attempt to access other people's data, or interfere with its operation.", "Use prospect information and any outreach only in a lawful way, as described in the Lead and Opportunity Policy.", "Make your own decisions about business matters. Our research and recommendations are inputs, not guarantees.")]),
  ("7. Third-party services", [P("The website and our services rely on third parties, such as Google Forms, WhatsApp, Supabase and email providers. Their own terms and privacy policies apply to their services.")]),
  ("8. Intellectual property", [P("The website content, branding and the SkillBridge and ManavLab names belong to their respective owners. Ownership of project deliverables is set out in the written agreement for that project.")]),
  ("9. Suspension", [P("We may refuse or end an inquiry, or suspend access to the website, if these terms are breached or misuse is reasonably suspected.")]),
  ("10. Limitation of liability", [P("To the extent permitted by law, SkillBridge is not liable for indirect or consequential losses arising from use of the website, or from reliance on research, recommendations or prospect information. [Liability cap, if any, to be confirmed by a qualified legal professional.]")]),
  ("11. Governing law and changes", [P("These terms are governed by the laws of India. [Governing law details and courts with jurisdiction to be confirmed.] We may update these terms; the date above shows the latest version.")]),
 ], ["Governing law, courts with jurisdiction and the dispute process", "Liability cap, if any"]),

 ("cookie-policy", "Cookie Policy",
  "What browser storage this website uses and how to change your choice.", [
  ("1. What we use", [L(
    "Essential storage: if you sign in to a SkillBridge account, your session is kept in your browser's local storage so you stay signed in. Your cookie choice is also stored locally (key: sb_cookie_consent). These are needed for the site to work and are always on.",
    "Third-party requests: the site loads fonts from Google Fonts. Google may receive your IP address and browser details when fonts are requested.",
    "Optional analytics or advertising cookies: none are active at the time of writing.")]),
  ("2. Your choice", [P("When you first visit, a banner lets you accept or reject optional cookies. Rejecting does not affect essential storage. Clicking the Cookie Policy link on the banner is not treated as consent.")]),
  ("3. Changing your preference", [P("Use the \"Cookie preferences\" link in the footer of any page to review or change your choice at any time.")]),
  ("4. If we add optional tools", [P("If we add optional analytics or advertising tools, they will stay switched off until you accept optional cookies. We will also ask for your choice again if this policy changes materially.")]),
  ("5. Contact", [P("Questions about this policy:", EMAIL + ".")]),
 ], ["Whether fonts will be hosted by SkillBridge instead of Google Fonts", "Any analytics or advertising tools planned for the future (this policy and the consent version must be updated first)"]),

 ("refund-cancellation-policy", "Refund and Cancellation Policy",
  "How cancellations and refunds are handled for SkillBridge services.", [
  ("1. Inquiries", [P("Submitting an inquiry, a collaboration request or an expert application is free and creates no payment obligation.")]),
  ("2. Premium Lead Generation package (₹499)", [
    P("The refund position for this package is set out below. It is a draft that the owner must confirm before publication:"),
    L("Cancellation before research starts: [refund amount or window to be confirmed by the owner].",
      "Cancellation after research has started: [to be confirmed]. Research already done cannot be returned, so the amount payable is normally based on work delivered.",
      "Delivery problems: if a delivered spreadsheet or document does not match the agreed scope, tell us within [number] days and we will correct it or agree a remedy.")]),
  ("3. Custom lead plans and collaboration projects", [P("Cancellation and refund terms are set out in the written quote or project agreement. These are agreed before payment is due.")]),
  ("4. Third-party spend", [P("Amounts paid to third parties, such as advertising platforms, API or hosting providers, are paid to those providers and are generally not refundable by SkillBridge.")]),
  ("5. How to request", [P("Write to", EMAIL, "or message", WHATSAPP, "on WhatsApp with your name, the service concerned, and the reason for your request. We will reply within [time frame to be confirmed].")]),
 ], ["Refund amount or window before research starts", "Whether any part of a payment is non-refundable once work begins", "Refund method and processing time"]),

 ("service-policy", "Service Policy",
  "How SkillBridge services are scoped, delivered, reviewed and limited.", [
  ("1. Scope", [P("Each service is confirmed individually. For the Premium Lead Generation package, the scope is 50 researched potential business opportunities, business details and available contact information, research-based relevance, suggested services where research supports them, outreach guidance and email templates, call scripts, and a structured spreadsheet. Custom plans are scoped in the quote.")]),
  ("2. What we do and do not do under the lead generation package", [L("We research and organise potential prospects and provide guidance and templates.", "We do not send messages on your behalf under this package, unless a separate written agreement says so.", "We do not promise a number of replies, meetings, buyers or projects.")]),
  ("3. Reports and findings", [P("Reports distinguish verified observations, evidence and sources, potential problems, possible causes, recommendations, priorities, and information that remains unverified. We do not state that a problem exists unless the evidence supports it.")]),
  ("4. Your responsibilities", [P("You provide accurate information, timely feedback, and any access needed for the agreed work. Delays caused by missing information may change the timeline.")]),
  ("5. Delivery and review", [P("Deliverables are provided as agreed. [Number of review or correction rounds included to be confirmed.]")]),
  ("6. Refusing or pausing work", [P("We may decline or pause a request that we cannot deliver properly, that breaches the law or platform rules, or that is unsuitable. We will explain why and refund any amount due under the Refund and Cancellation Policy.")]),
  ("7. No guarantees", [P("Our services support your decisions. They do not guarantee customers, sales, revenue, rankings or growth.")]),
 ], ["Standard delivery timeline for the ₹499 package", "Number of review rounds included"]),

 ("opportunity-policy", "Lead and Opportunity Policy",
  "What researched potential opportunities are, what they are not, and how prospect information is handled.", [
  ("1. What a researched opportunity is", [P("A researched opportunity is a business that may be relevant to a client's service or target market, based on publicly available information and our analysis.")]),
  ("2. What it is not", [L("It is not a verified buyer or an active customer.", "It is not a promise that the business will reply, meet, buy or become a client.", "It is not a guarantee that contact details are current, correct or complete.")]),
  ("3. Scores and priority", [P("Where we show a score or priority, it is a research-based prioritisation indicator. It is not a probability of conversion or a sales forecast.")]),
  ("4. Sources and accuracy", [P("We use publicly available and permitted sources. If an opportunity cannot be researched sufficiently, we leave it out rather than invent details. Information can change, so you should verify it before relying on it.")]),
  ("5. Your outreach must be lawful", [P("If you contact prospects using our templates or guidance, you are responsible for doing so lawfully. This includes respecting opt-outs and do-not-disturb requests, and following the rules of the channel you use, such as email and WhatsApp messaging rules and telemarketing rules in India. [Specific compliance guidance to be confirmed by a qualified legal professional.]")]),
  ("6. Removal requests", [P("If a business asks us to remove its information, or you ask us to, we will remove it from our records and from any future deliverable, where possible. Write to", EMAIL + ".")]),
  ("7. Prospect data is not shared with others", [P("We do not sell prospect lists. Prospect information is delivered to the client who commissioned the research.")]),
 ], ["Process for removal requests and time frame", "Any additional rules for outreach channels you intend to support"]),

 ("payment-policy", "Payment Policy",
  "How prices, invoices and payments work for SkillBridge services.", [
  ("1. Published prices", [P("The Premium Lead Generation package is published at ₹499 per package. Custom lead plans, business collaboration projects and expert-network projects are priced individually after we review your requirement. We do not publish a price for a service until it is confirmed.")]),
  ("2. Currency", [P("Prices and billing are in Indian Rupees (INR). Any USD figures shown on the website, if any, are for reference only.")]),
  ("3. Before you pay", [P("We confirm the price, what is included, the payment schedule and due dates in writing before you pay. Starting a WhatsApp conversation or submitting a form does not mean that payment is due.")]),
  ("4. Payment methods", [P("The SkillBridge website does not take online card payments. [Accepted payment methods, payee name and bank or UPI details to be confirmed by the owner.] Never send card details, passwords or one-time codes to us by chat or email.")]),
  ("5. Third-party costs", [P("Costs such as advertising spend, platform fees, API usage, email or hosting providers are separate. They are paid to those providers unless the agreement says otherwise.")]),
  ("6. Taxes and invoices", [P("[GST registration status and invoicing details to be confirmed by the owner.] Invoices will show the service agreed in writing.")]),
  ("7. Late or disputed payments", [P("Contact us promptly if you have a question about a payment. We aim to resolve it before pausing any work. [Late-payment terms to be confirmed.]")]),
 ], ["Accepted payment methods and payee details", "GST status and invoicing details", "Late-payment terms"]),

 ("disclaimer", "Disclaimer",
  "Important limits on what this website, its content and our research mean.", [
  ("1. General information", [P("Content on this website, and research or recommendations we provide, is general business information based on the information available at the time. It is not legal, financial, tax or investment advice.")]),
  ("2. No guaranteed results", [P("SkillBridge does not guarantee customers, replies, meetings, projects, sales, partnerships, revenue, rankings or business growth. Results depend on many factors outside our control.")]),
  ("3. Third-party information", [P("We refer to publicly available and third-party information. We do not guarantee its accuracy or completeness.")]),
  ("4. Services and availability", [P("Not every service described on this website is available at all times. Scope, price and timeline are confirmed individually.")]),
  ("5. Specialists", [P("Specialists in our expert network are independent professionals, not employees of SkillBridge or ManavLab, unless a written agreement says otherwise. Being listed or contacted does not mean a specialist has been verified for every skill or approved for any project.")]),
 ], []),

 ("expert-network-policy", "Expert Network Policy",
  "How specialists may join the SkillBridge expert network and be considered for projects.", [
  ("1. What the network is", [P("The expert network is a group of independent professionals who may be considered for projects on a project-by-project basis.")]),
  ("2. Membership does not guarantee work", [P("Joining or being approved for the network does not guarantee projects, clients, income or assignments. Work depends on real client requirements, budget, availability, approval and a written agreement.")]),
  ("3. Application review", [P("We review applications based on the information you provide, such as skills, experience, portfolio and availability. Approval to be in the network is separate from approval for any specific project.")]),
  ("4. Published profiles", [P("We publish a profile only with real information and your permission. We do not publish invented experience, qualifications, ratings, reviews or client names.")]),
  ("5. Independent professionals", [P("You work as an independent professional. You are responsible for your own tools, taxes, insurance and compliance, unless a written agreement says otherwise.")]),
  ("6. Conduct and confidentiality", [P("You must give accurate information, respect client confidentiality, and deliver work you are able to complete. You must not use client information for purposes outside the project.")]),
  ("7. Fees and commission", [P("Fees, rates or any commission for a project are agreed in writing for that project. [Standard commission or fee terms with specialists to be confirmed by the owner.]")]),
 ], ["Whether an expert application process is live, and how applications are submitted", "Standard commission or fee terms, if any"]),

 ("project-collaboration-terms", "Project Collaboration Terms",
  "How a potential collaboration becomes an approved project, and how it runs.", [
  ("1. Stages", [P("A collaboration usually moves through these stages: business inquiry, research, problem analysis, recommendations, proposal, budget approval, specialist selection, project agreement, execution, quality review, delivery and final review. Each stage can stop at any point if the parties do not agree.")]),
  ("2. Before work starts", [P("A project starts only after the scope, deliverables, budget, deadlines, responsibilities and payment terms are agreed in writing.")]),
  ("3. Introductions and consent", [P("We introduce parties only with appropriate permission. Contact details are shared only after the relevant person has agreed.")]),
  ("4. Specialists", [P("Where a specialist is proposed, you approve the involvement and the terms before work starts. Specialists are independent and responsible for their own work, unless the agreement says otherwise.")]),
  ("5. Milestones and changes", [P("Milestones, review points and delivery are set out in the agreement. Changes to scope, cost or timeline are agreed in writing before extra work is done.")]),
  ("6. Confidentiality and ownership", [P("Information shared for a project is used only for that project, unless the parties agree otherwise or the law requires disclosure. Ownership of deliverables is set out in the agreement.")]),
  ("7. Ending a project", [P("A project may end on completion, by agreement, or under the cancellation terms in the agreement and the Refund and Cancellation Policy.")]),
 ], ["Standard written agreement template (this page is a summary and is not a contract)"]),

 ("complaints-policy", "Complaints and Dispute Resolution",
  "How to raise a concern, what happens next, and how disputes are handled.", [
  ("1. How to contact us", [P("Email", EMAIL + " or message", WHATSAPP, "on WhatsApp. Please include your name, how we can reach you, the service or project concerned, and what you would like us to do.")]),
  ("2. What happens next", [P("We acknowledge complaints, review them fairly, and reply with an outcome or the next step. We aim to respond within [time frame to be confirmed].")]),
  ("3. Escalation", [P("If you are not satisfied, you may ask for a second review by writing to us again and marking your message for escalation. Where applicable, you keep any rights you have under Indian law.")]),
  ("4. Disputes", [P("We will try to resolve disputes in good faith first. If that does not work, [dispute resolution process, governing law and courts with jurisdiction to be confirmed by a qualified legal professional].")]),
 ], ["Name of the designated grievance contact (if appointed) and response times", "Dispute resolution process, governing law and jurisdiction"]),
]

NAV = [(s, t) for s, t, *_ in POLICIES]

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#fff;color:#10141f;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.7}
a{color:#16a891}
.l-header{border-bottom:1px solid #e8eaed;padding:16px 24px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;background:#fff}
.l-brand{font:800 19px Manrope,Inter,sans-serif;text-decoration:none;color:#16233f}
.l-brand b{color:#16a891}
.l-back{font-size:14px;font-weight:600;text-decoration:none;color:#16233f}
.l-wrap{max-width:780px;margin:0 auto;padding:40px 24px 80px}
h1{font:800 clamp(28px,4vw,38px)/1.15 Manrope,Inter,sans-serif;color:#16233f;margin:0 0 8px}
h2{font:800 19px Manrope,Inter,sans-serif;color:#16233f;margin:34px 0 8px}
p,li{color:#4d5561}
ul{padding-left:20px}
li{margin:6px 0}
.l-meta{font-size:13.5px;color:#6b7383;margin-bottom:24px}
.draft-notice{background:#fff7e8;border:1px solid #f3dfb8;border-radius:12px;padding:14px 18px;font-size:14px;color:#7a5200;margin:20px 0}
.confirm-box{background:#fafafa;border:1px dashed #c9cdd4;border-radius:12px;padding:16px 20px;margin-top:40px}
.confirm-box h2{margin-top:0;font-size:16px}
.l-index{list-style:none;padding:0}
.l-index li{margin:0;border-top:1px solid #e8eaed}
.l-index a{display:block;padding:16px 4px;text-decoration:none;font-weight:600;color:#16233f}
.l-index a span{display:block;font-weight:400;font-size:14px;color:#4d5561}
.l-footer{border-top:1px solid #e8eaed;padding:24px;text-align:center;font-size:13.5px;color:#6b7383}
.l-footer a{color:#4d5561;margin:0 8px}
a:focus-visible{outline:2px solid #16a891;outline-offset:2px}
@media (max-width:600px){.l-wrap{padding:28px 18px 60px}}
"""

def esc_with_email(text):
    t = html.escape(text)
    e = html.escape(EMAIL)
    t = t.replace(e, f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    return t

def block(b):
    kind, val = b
    if kind == "p":
        return "<p>" + esc_with_email(val) + "</p>"
    return "<ul>" + "".join("<li>" + esc_with_email(i) + "</li>" for i in val) + "</ul>"

def footer():
    links = "".join(f'<a href="{s}.html">{html.escape(t)}</a>' for s, t in NAV[:4])
    return f'<footer class="l-footer"><a href="index.html">Home</a><a href="policies.html">All policies</a>{links}<p>© 2026 SkillBridge — Powered by ManavLab</p></footer>'

def page(slug, title, blurb, sections, missing):
    body = "".join(f"<h2>{html.escape(h)}</h2>" + "".join(block(b) for b in blocks) for h, blocks in sections)
    draft = ('<div class="draft-notice"><strong>Draft — pending legal review.</strong> This page is a working draft dated '
             + UPDATED + ' and has not been reviewed by a qualified legal professional. Items in square brackets must be confirmed by the owner before publication.</div>') if SHOW_DRAFT_NOTICE else ""
    miss = COMMON_OWNER_ITEMS + missing
    box = ('<div class="confirm-box"><h2>Information the owner still needs to provide</h2><ul>'
           + "".join(f"<li>{html.escape(m)}</li>" for m in miss) + "</ul></div>") if SHOW_DRAFT_NOTICE else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} — SkillBridge</title>
<meta name="description" content="{html.escape(blurb)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="l-header"><a class="l-brand" href="index.html">Skill<b>Bridge</b></a><a class="l-back" href="policies.html">All policies</a></header>
<main class="l-wrap">
<h1>{html.escape(title)}</h1>
<p class="l-meta">Last updated: {UPDATED} · SkillBridge, powered by ManavLab</p>
{draft}
{body}
{box}
</main>
{footer()}
</body>
</html>
'''

for slug, title, blurb, sections, missing in POLICIES:
    with open(os.path.join(OUT_DIR, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(page(slug, title, blurb, sections, missing))

items = "".join(f'<li><a href="{s}.html">{html.escape(t)}<span>{html.escape(b)}</span></a></li>' for s, t, b, *_ in POLICIES)
with open(os.path.join(OUT_DIR, "policies.html"), "w", encoding="utf-8") as f:
    f.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Policies — SkillBridge</title>
<meta name="description" content="SkillBridge policies: privacy, terms, cookies, refunds, services, leads, payments, disclaimer, expert network and complaints.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="l-header"><a class="l-brand" href="index.html">Skill<b>Bridge</b></a><a class="l-back" href="index.html">← Back to site</a></header>
<main class="l-wrap">
<h1>Policies</h1>
<p class="l-meta">SkillBridge, powered by ManavLab · Last updated: {UPDATED}</p>
<div class="draft-notice"><strong>Drafts — pending legal review.</strong> These pages have not been reviewed by a qualified legal professional. They describe how SkillBridge currently works, and bracketed items still need owner confirmation.</div>
<ul class="l-index">{items}</ul>
</main>
{footer()}
</body>
</html>
''')
print("generated", len(POLICIES) + 1, "pages in", OUT_DIR)


import re as _re
_SNIPPET = open(os.path.join(OUT_DIR, "src", "consent-inline.html"), encoding="utf-8").read() if os.path.exists(os.path.join(OUT_DIR, "src", "consent-inline.html")) else ""
def inject_consent(path, snippet=None):
    snippet = snippet or _SNIPPET
    s = open(path, encoding="utf-8").read()
    s = _re.sub(r'<script type="module" src="src/consent.js"></script>\s*', '', s)
    s = _re.sub(r'<!--SB-CONSENT-START-->.*?<!--SB-CONSENT-END-->\s*', '', s, flags=_re.S)
    s = s.replace("</body>", "<!--SB-CONSENT-START-->" + snippet + "<!--SB-CONSENT-END-->\n</body>", 1)
    open(path, "w", encoding="utf-8").write(s)
for _slug, *_ in POLICIES:
    inject_consent(os.path.join(OUT_DIR, _slug + ".html"))
inject_consent(os.path.join(OUT_DIR, "policies.html"))
print("consent banner injected into policy pages")
