# SkillBridge — Supabase auth setup (matches your live schema)

## 1. Public values only
Edit js/supabase-config.js and replace the two placeholders:
  url:            "SUPABASE_URL"               -> your Project URL (https://xxxx.supabase.co)
  publishableKey: "SUPABASE_PUBLISHABLE_KEY"   -> your Publishable key
Never put a service_role or secret key in this website.

## 2. Supabase > Authentication > URL Configuration
- Site URL:      https://hellomanavlab-cmyk.github.io/SkillBridge/
- Redirect URLs: https://hellomanavlab-cmyk.github.io/SkillBridge/auth.html
- Providers > Email: enabled, "Confirm email" ON.

## 3. Database: NO CHANGES
This website does not change your database. It uses your existing schema:
- Email comes from Supabase Auth (session.user.email). public.profiles has no email column.
- public.profiles is used only for full_name and account_type (read own row; update own full_name and account_type).
- Sign-up sends full_name and account_type in user metadata. Your existing trigger
  on_auth_user_created creates the profile row. The frontend never inserts into profiles.
- If the trigger ever fails, the dashboard shows "Your profile is not available yet" and does not invent data.

## 4. Deploy
Run deploy.bat (Windows) or ./deploy.sh (Mac/Linux) from this folder.
Then open https://hellomanavlab-cmyk.github.io/SkillBridge/auth.html

## 5. What to test on the live site (not yet verified by us)
- Sign up as each account type, then check the verification email link opens auth.html
- Log in with the verified email; wrong password shows a clear message
- Dashboard loads your name, email and account type; saving name/account type persists after reload
- Forgot password sends a link; the reset link opens auth.html and lets you set a new password
- Log out returns to auth.html; dashboard.html is blocked when logged out
