"""Generates the static policy pages. Run: python3 build_policies.py
Edit POLICIES below, then re-run. (Output files are committed so no build step is needed to deploy.)"""
import html

UPDATED = "17 October 2026"
EMAIL = "hello.manavlab@gmail.com"
SHOW_DRAFT_NOTICE = True   # set False to hide the "draft" banner once a qualified legal professional has reviewed the page
COMMON_MISSING = [
    "Registered legal name and business status of the entity operating SkillBridge (sole proprietorship, company, etc.)",
    "Registered business address (only if you want it published)",
    "Governing law and jurisdiction for disputes",
]
def P(*a): return ("p", " ".join(a))
def L(*items): return ("ul", list(items))

POLICIES = [
 ("privacy-policy", "Privacy Policy", "How SkillBridge collects, uses and protects personal information.", [
  ("Who we are", [P("SkillBridge is a project powered by ManavLab. This policy explains how information is handled when you use this website, submit an inquiry or use a SkillBridge account. Contact:", EMAIL + ".")]),
  ("Information we collect", [L(
    "Inquiry form (Google Forms): name, business email, business or organisation name, website or social link, and the details you choose to write about your business needs. Google Forms may also record the email address of the respondent.",
    "SkillBridge account (if you have one): name, email, and profile details you enter such as phone, country, city, skills, services, portfolio link, target industries and markets; plus campaign, opportunity and plan data you create or that is created for your account.",
    "Messages you send us by email or WhatsApp.",
    "Technical storage in your browser, described in the Cookie Policy.")]),
  ("How we use it", [L("To respond to inquiries and assess whether our services may be relevant.", "To deliver services you have agreed to and to operate your account.", "To keep the service secure and to prevent misuse.", "To meet legal obligations.")]),
  ("Who we share it with", [P("We do not sell personal information. We use service providers to run the site and handle data, including Google (Forms), Supabase (account database and authentication) and the website hosting provider. Specialists or other third parties receive your information only where it is needed for a project you have approved and, where appropriate, with your permission.")]),
  ("Retention and deletion", [P("We keep information only as long as needed for the purposes above or as required by law. You may ask us to correct or delete your information by emailing", EMAIL + ". Specific retention periods are to be confirmed (see the box below).")]),
  ("Your choices and rights", [P("You can ask to access, correct or delete your information and can withdraw consent for optional processing at any time. Indian data-protection law, including the Digital Personal Data Protection Act, 2023, may apply to this processing; the exact rights, timelines and notices should be confirmed with a qualified legal professional.")]),
  ("Security", [P("We use access controls on accounts and database records so users can only see their own information. No method of storage or transmission is completely secure, so we cannot guarantee absolute security.")]),
  ("Children", [P("This website is intended for businesses and professionals and is not directed at children under 18.")]),
  ("Changes", [P("We may update this policy. The date at the top shows the latest version.")]),
 ], ["Data retention periods for inquiries and account data", "Name and contact details of the person responsible for privacy requests and the expected response time", "Whether an explicit consent tick-box will be added to the Google Form (the current form does not include one)"]),

 ("terms-of-service", "Terms of Service", "The terms for using the SkillBridge website and services.", [
  ("About these terms", [P("By using this website or submitting an inquiry you agree to these terms. SkillBridge is a project powered by ManavLab.")]),
  ("What SkillBridge offers", [P("SkillBridge researches potential business opportunities, analyses business challenges, shares recommendations and may help identify specialists for potential projects. Not every service is available for every business; availability, scope and price are confirmed individually before any work begins.")]),
  ("No guarantees", [P("SkillBridge does not guarantee customers, replies, meetings, projects, sales, revenue, search rankings or business growth. Research and recommendations are based on the information available at the time.")]),
  ("Your responsibilities", [L("Provide accurate and lawful information.", "Do not misuse the website, attempt to access other users' data, or interfere with its operation.", "You are responsible for decisions you make using our research or recommendations.")]),
  ("Agreements for projects", [P("A project starts only after scope, deliverables, budget, timeline, responsibilities and payment terms have been agreed in writing (for example by email or a signed proposal). Submitting an inquiry does not create a project or an obligation on either side.")]),
  ("Third-party services", [P("The website relies on third-party services such as Google Forms and Supabase. Their own terms and privacy policies apply to their services.")]),
  ("Intellectual property", [P("Website content and branding belong to SkillBridge / ManavLab unless stated otherwise. Ownership of project deliverables is set out in the agreement for that project.")]),
  ("Limitation of liability", [P("To the extent permitted by law, SkillBridge is not liable for indirect or consequential losses arising from use of the website or reliance on research or recommendations. The exact wording of this clause requires review by a qualified legal professional.")]),
  ("Changes and contact", [P("We may update these terms; the date above shows the latest version. Questions:", EMAIL + ".")]),
 ], ["Governing law, court jurisdiction and dispute process", "Whether any liability cap should apply and its amount"]),

 ("cookie-policy", "Cookie Policy", "What browser storage this website uses and how to change your choice.", [
  ("What we use today", [L(
    "Essential storage: if you log in to a SkillBridge account, your login session is kept in your browser's local storage so you stay signed in. Your cookie choice is also stored in local storage (key: sb_cookie_consent). These are needed for the site to work and are always on.",
    "Third-party requests: the site loads fonts from Google Fonts. Google may receive your IP address and browser details when the fonts are requested. We are evaluating hosting fonts ourselves to remove this.",
    "Optional analytics or marketing cookies: none are active at the time of writing.")]),
  ("Your choice", [P("When you first visit, a banner lets you accept or reject optional cookies. Rejecting does not affect essential storage. Clicking the Cookie Policy link on the banner is not treated as consent.")]),
  ("Changing your preference", [P("Use the “Cookie preferences” link in the site footer at any time to review or change your choice.")]),
  ("If this changes", [P("If we add optional analytics or marketing tools, they will stay switched off until you accept optional cookies, and we will ask for your choice again.")]),
  ("Contact", [P("Questions about this policy:", EMAIL + ".")]),
 ], ["Confirm whether you will self-host fonts or keep Google Fonts", "List any analytics or advertising tools you plan to add (this policy and the consent version must be updated first)"]),

 ("refund-cancellation-policy", "Refund and Cancellation Policy", "How cancellations and refunds are handled.", [
  ("General principle", [P("Cancellation and refund terms for any paid work are set out in the written proposal or agreement for that engagement and are agreed before payment is due.")]),
  ("Before an agreement", [P("Submitting an inquiry is free and creates no payment obligation.")]),
  ("Cancellation", [P("Either party may request cancellation of a project by written notice. Work already completed, third-party costs already incurred and any agreed non-refundable amounts are handled as stated in the agreement.")]),
  ("Refunds", [P("Whether a refund is available, and in what amount, depends on the agreed terms and on the work delivered up to the cancellation date. Research findings and recommendations that have been delivered cannot be returned.")]),
  ("Advertising and third-party spend", [P("Amounts paid to third-party platforms (for example advertising spend) are paid to that platform and are generally not refundable by SkillBridge.")]),
  ("How to request", [P("Write to", EMAIL, "with your name, the project and the reason for the request.")]),
 ], ["Actual refund windows, eligible situations and processing time", "Which listed prices (if any) are non-refundable once work starts", "Payment method(s) used for refunds"]),

 ("service-policy", "Service Policy", "How SkillBridge services are scoped, delivered and reviewed.", [
  ("Scope", [P("Each service is assessed individually. We confirm scope, deliverables, timeline, budget and responsibilities before starting.")]),
  ("Research and analysis", [P("Reports distinguish verified observations, evidence and sources, potential problems, possible causes, recommendations, priorities and information that remains unverified. We do not state that a problem exists unless evidence supports it.")]),
  ("Client responsibilities", [P("Provide accurate information, timely feedback and any access needed for the agreed work.")]),
  ("Delivery and review", [P("Deliverables are provided as agreed. Reasonable review and correction rounds are defined in the project agreement.")]),
  ("Availability", [P("Services may be declined or paused if we cannot deliver them properly or if a request is unlawful or unsuitable.")]),
  ("No guarantees", [P("Services support decision-making. They do not guarantee customers, sales, revenue, rankings or growth.")]),
 ], ["Standard turnaround times, if any", "Number of revision rounds included in a typical engagement"]),

 ("opportunity-policy", "Potential Customer Research and Opportunity Policy", "What researched opportunities are and are not.", [
  ("What an opportunity is", [P("A researched opportunity is a business or prospect that may be relevant to a client's service or target market, based on publicly available information and analysis.")]),
  ("What it is not", [L("Not a verified buyer or active customer.", "Not a promise that the business will reply, meet, buy or become a client.", "Not a guarantee that contact details are current or complete.")]),
  ("Scores and priority", [P("Opportunity scores and priorities are prioritisation indicators based on research. They are not a probability of conversion.")]),
  ("Sources and accuracy", [P("We use publicly available and permitted sources. If an opportunity cannot be sufficiently researched we leave it out rather than invent details. Information can change; clients should verify before relying on it.")]),
  ("Outreach", [P("Outreach is only carried out through supported, authorised channels and with the client's approval. Recipients who opt out or bounce are not contacted again by automated follow-ups. SkillBridge never asks clients for email passwords.")]),
  ("Client responsibility", [P("Clients remain responsible for the content of their outreach and for complying with laws and platform rules that apply to their communications.")]),
 ], ["Whether you will remove a researched prospect on request, and how requests are handled"]),

 ("payment-policy", "Payment Policy", "How payments for SkillBridge services work.", [
  ("Agreed before work", [P("Prices, what is included, billing schedule and due dates are stated in the proposal or agreement. Where a service has no published price, it is quoted individually (“Request a Quote”).")]),
  ("Currency", [P("Billing is in Indian Rupees (INR) unless the agreement says otherwise. Any USD figures shown on the website are for reference only.")]),
  ("Third-party costs", [P("Costs such as advertising spend, API usage, email or hosting providers may be separate and are paid to those providers unless the agreement states otherwise.")]),
  ("Payment methods", [P("Payment methods are confirmed in the proposal. The website does not currently take online card payments.")]),
  ("Taxes and invoices", [P("Invoices and any applicable taxes are handled as stated in the agreement.")]),
  ("Late or disputed payments", [P("Contact us promptly about any payment question or dispute. We aim to resolve it before pausing any work.")]),
 ], ["Accepted payment methods and payee details", "GST registration status and invoicing details (if applicable)", "Late-payment terms"]),

 ("disclaimer", "Disclaimer", "Important limits on what this website and its content mean.", [
  ("Information only", [P("Content on this website, and research or recommendations we provide, is general business information based on the information available at the time. It is not legal, financial, tax or investment advice.")]),
  ("No guaranteed results", [P("SkillBridge does not guarantee customers, replies, meetings, projects, sales, revenue, rankings or business growth. Results depend on many factors outside our control.")]),
  ("Third-party information", [P("We reference publicly available and third-party information and do not guarantee its accuracy or completeness.")]),
  ("Services and availability", [P("Not all services described are available at all times. Scope, price and timeline are confirmed individually.")]),
  ("Specialists", [P("Specialists are independent professionals, not employees of SkillBridge or ManavLab, unless an agreement says otherwise. Being listed or contacted does not mean a specialist has been verified for every skill or approved for any project.")]),
 ], []),

 ("expert-network-policy", "Expert Network Policy", "How specialists may collaborate with SkillBridge.", [
  ("What the network is", [P("The expert network is a group of independent professionals who may be considered for projects on a project basis.")]),
  ("No guarantee of work", [P("Membership or interest does not guarantee projects, clients, income or assignments. Work depends on real client requirements, budget, availability, approval and agreement.")]),
  ("Applications and review", [P("Applications are reviewed on the information provided, such as skills, portfolio and availability. Approval for the network is separate from approval for any specific project.")]),
  ("Published profiles", [P("Profiles are published only when the information is real and the specialist has given permission. We do not publish invented experience, qualifications, ratings or client names.")]),
  ("Independent professionals", [P("Specialists work independently and are responsible for their own tools, taxes and compliance, unless an agreement states otherwise.")]),
  ("Conduct", [P("Specialists must give accurate information, respect client confidentiality, and deliver work they are able to complete.")]),
 ], ["Whether you currently run an expert application process and how applications are submitted", "Standard commission or fee terms with specialists, if any"]),

 ("project-collaboration-terms", "Project Collaboration Terms", "How approved projects are agreed and run.", [
  ("Before work starts", [P("A project begins only after scope, deliverables, budget, timeline, responsibilities and payment terms are agreed in writing.")]),
  ("Specialist involvement", [P("Where a specialist is suggested, the client approves the involvement and the terms. Contact details are shared only with permission.")]),
  ("Milestones and delivery", [P("Milestones, review points and delivery are set out in the agreement. Deliverables are reviewed against the agreed scope.")]),
  ("Changes", [P("Changes to scope, cost or timeline are agreed in writing before the extra work is done.")]),
  ("Confidentiality", [P("Information shared for a project is used only for that project and is not disclosed to others except as agreed or required by law.")]),
  ("Ending a project", [P("A project may end on completion, by agreement, or according to the cancellation terms in the agreement and the Refund and Cancellation Policy.")]),
 ], ["Standard written agreement template to be used (this page is a summary, not a contract)"]),

 ("complaints-policy", "Complaints and Contact Policy", "How to raise a concern and what to expect.", [
  ("How to contact us", [P("Email", EMAIL + ". You can also message us on WhatsApp using the link on our contact section.")]),
  ("What to include", [P("Your name, how to reach you, the project or interaction concerned, and what you would like us to do.")]),
  ("What happens next", [P("We acknowledge complaints, review them fairly and reply with an outcome or next step. Target response times are to be confirmed.")]),
  ("Escalation", [P("If you are not satisfied, you may ask for a second review. Where applicable, you also keep any rights you have under Indian law.")]),
 ], ["Name of a designated grievance contact (if you appoint one) and target response times"]),
]

def render_block(b):
    kind, val = b
    if kind == "p": return f"<p>{html.escape(val).replace(html.escape(EMAIL), f'<a href=\"mailto:{EMAIL}\">{EMAIL}</a>')}</p>"
    return "<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in val) + "</ul>"

def page(slug, title, blurb, sections, missing):
    body = "".join(f"<h2>{html.escape(h)}</h2>" + "".join(render_block(b) for b in blocks) for h, blocks in sections)
    miss = COMMON_MISSING + missing
    draft = '<div class="draft-notice"><strong>Draft — pending legal review.</strong> This page is a working draft prepared on ' + UPDATED + ' and has not been reviewed by a qualified legal professional. Items still to be confirmed by the owner are listed at the end.</div>' if SHOW_DRAFT_NOTICE else ""
    box = '<div class="confirm-box"><h2>Information still to be confirmed by the owner</h2><ul>' + "".join(f"<li>{html.escape(m)}</li>" for m in miss) + "</ul></div>" if SHOW_DRAFT_NOTICE else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} — SkillBridge</title>
<meta name="description" content="{html.escape(blurb)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="src/styles/legal.css">
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
<footer class="l-footer"><a href="index.html">Home</a><a href="policies.html">Policies</a><button type="button" class="linklike" data-cookie-prefs>Cookie preferences</button><p>© 2026 SkillBridge — Powered by ManavLab</p></footer>
<script type="module" src="src/consent.js"></script>
</body>
</html>
'''

for slug, title, blurb, sections, missing in POLICIES:
    open(f"{slug}.html", "w", encoding="utf-8").write(page(slug, title, blurb, sections, missing))

index_items = "".join(f'<li><a href="{s}.html">{html.escape(t)}<span>{html.escape(b)}</span></a></li>' for s, t, b, _, _ in POLICIES)
open("policies.html", "w", encoding="utf-8").write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Policies — SkillBridge</title>
<meta name="description" content="SkillBridge legal and policy pages.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="src/styles/legal.css">
</head>
<body>
<header class="l-header"><a class="l-brand" href="index.html">Skill<b>Bridge</b></a><a class="l-back" href="index.html">← Back to site</a></header>
<main class="l-wrap">
<h1>Policies</h1>
<p class="l-meta">SkillBridge, powered by ManavLab · Last updated: {UPDATED}</p>
{'<div class="draft-notice"><strong>Drafts — pending legal review.</strong> These pages are working drafts and have not been reviewed by a qualified legal professional.</div>' if SHOW_DRAFT_NOTICE else ''}
<ul class="l-index">{index_items}</ul>
</main>
<footer class="l-footer"><a href="index.html">Home</a><button type="button" class="linklike" data-cookie-prefs>Cookie preferences</button><p>© 2026 SkillBridge — Powered by ManavLab</p></footer>
<script type="module" src="src/consent.js"></script>
</body>
</html>
''')
print("generated", len(POLICIES) + 1, "pages")
