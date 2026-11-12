# SkillBridge — Deployment Checklist (website WITHOUT Free Trial)

STATUS: NOT production-ready. Legal-review placeholders remain. This ZIP is a deployable static site, but do not treat it as final until sections A and B below are done.

## A. Owner confirmation required (placeholders still in the policy pages)
Pages with owner-confirmation markers or the "Draft — pending legal review" banner:

| Page | Markers found | Draft banner |
|---|---|---|
| collaboration-policy.html | 0 | yes |
| collaboration-refund-policy.html | 1 | yes |
| collaboration-terms.html | 1 | yes |
| complaints-policy.html | 2 | yes |
| cookie-policy.html | 0 | yes |
| disclaimer.html | 0 | yes |
| expert-network-policy.html | 1 | yes |
| opportunity-policy.html | 1 | yes |
| payment-policy.html | 3 | yes |
| policies.html | 0 | yes |
| privacy-policy.html | 2 | yes |
| project-collaboration-terms.html | 0 | yes |
| refund-cancellation-policy.html | 3 | yes |
| service-policy.html | 1 | yes |
| terms-of-service.html | 2 | yes |

Items to confirm:
1. Legal entity name and business status.
2. Registered address (only if you want it published).
3. Governing law and courts with jurisdiction.
4. Refund window and refund terms.
5. Retention period for WhatsApp and email records, and how deletion requests are handled.
6. Response time for privacy requests and complaints.
7. Name of a grievance contact, if you appoint one.
8. Accepted payment methods, payee details, GST status, late-payment terms.
9. Whether Google Fonts stays (it sends visitor IP to Google) or is self-hosted.
10. Whether any collaboration fee or commission will ever apply.
11. Expert network: whether an application process is live, and commission or fee terms with specialists.

## B. Legal review required
- Every file under "Policies": privacy-policy, terms-of-service, cookie-policy, refund-cancellation-policy, service-policy, opportunity-policy, payment-policy, disclaimer, expert-network-policy, project-collaboration-terms, complaints-policy, collaboration-policy, collaboration-terms, collaboration-refund-policy.
- Have a qualified lawyer review them (including Indian data-protection law) before removing the Draft banner and the "information still to be confirmed" boxes.

## C. Verification not done in this package
- Google Form link (https://forms.gle/PMgchzbLHDzTTywG8, on signup.html): destination NOT verified from the build environment. Open it yourself and confirm it is your registration form.
- WhatsApp and email apps opening on a real Android phone: NOT tested.
- Live GitHub Pages deployment: NOT tested (this ZIP was tested from local files).
- npm run build: NOT run and not needed for this flat HTML site.

## D. GitHub Pages steps
1. Extract SkillBridge-NoFreeTrial.zip. Open the website/ folder.
2. Repository > Add file > Upload files. Select ALL files inside website/ and drag them in. Same-named files are replaced.
3. Commit changes.
4. Settings > Pages: Deploy from a branch, branch main, folder / (root).
5. After 1-2 minutes open https://hellomanavlab-cmyk.github.io/SkillBridge/ and check: intro, Diwali corner flash, Lead Generation, Business Analysis, Join, one WhatsApp draft, one email draft, Cookie Accept/Reject, Policies page.

## E. Private repository files (NOT deleted by this task)
See PRIVATE-FILES-FOR-REVIEW.md. Back them up before deleting anything from the repository.
