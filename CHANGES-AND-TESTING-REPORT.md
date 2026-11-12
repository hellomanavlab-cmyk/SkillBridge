# Change list and testing report — website WITHOUT Free Trial

## Removed files (3)
- free-trial.html
- free-trial.js
- config-supabase.js  (used only by free-trial.html and free-trial.js; confirmed with a search before removal)

## Modified files (2)
- index.html — removed one footer link: <a href="free-trial.html">Free Trial</a> (40 bytes). Nothing else changed.
- vite.config.js (source project only, not in website/) — removed the free-trial.html build entry.

## Unchanged
All other 27 public pages, forms, styling, images (embedded), WhatsApp and email behaviour, policies, cookie banner, intro and Diwali corner flash.

## Checks after removal
- Search for "free-trial", "Free Trial", "config-supabase", "SB_CONFIG", "esm.sh" in all public pages: none left.
- 27 public pages: markup balance, JavaScript syntax, anchors, missing files, local script references: no problems.
- No page loads any external script. The only external requests are Google Fonts (stylesheet) and outbound links.

## Browser test (Chromium, phone width 390 px) — 152 checks, 151 passed
Passed for every page (27): no JavaScript error, no horizontal scroll, title and description present, images load, no Free Trial text or link.
Also passed: all homepage internal links resolve; Join (consent blocks send, WhatsApp to +91 7350259870 with inquiry ID); India order (email draft to skillbridge.manavlab@gmail.com, no price text); International order (WhatsApp to official number); Business Analysis (CTA "Enquire Now", WhatsApp draft); Supplier, Business Owner, Freelancer, Collaboration (empty submit blocked by validation); Diwali corner flash shows and hides itself; Diwali form WhatsApp draft; Cookie "Reject All" saved; signup page Google Form link unchanged.
The one failure: index.html "images load". Cause was the test, not the site: the homepage is 20,783 px tall and the test scrolled only 12,000 px, so a lazy-loaded image had not loaded yet. Re-checked separately after scrolling the full height: 0 images unloaded. The other 151 checks were not re-run after that re-check.

## Not tested
Real Android phone (WhatsApp and email apps), live GitHub Pages deployment, Google Form destination, a full click-through of every policy link in a browser (links checked for existence).
