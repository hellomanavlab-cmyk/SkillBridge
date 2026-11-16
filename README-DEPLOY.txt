SkillBridge - one-step deploy (replaces the 73 files one by one)

WHAT IT DOES
1. Downloads the current GitHub repository (hellomanavlab-cmyk/SkillBridge).
2. Saves a backup of the OLD website as a zip in this folder (backup-old-repo-....zip).
3. Removes the old files from the repository (including old private admin/dashboard pages).
4. Copies the new website from the "site" folder into the repository.
5. Commits and pushes to the main branch. GitHub Pages then publishes it.

BEFORE YOU RUN IT
- Install Git (https://git-scm.com). On Windows, Git for Windows.
- Sign in to GitHub on this computer (the first push will ask you to log in).
- Make sure you have a copy of anything in the repo you want to keep. The backup zip is created automatically, but check it.

RUN IT
- Windows: double-click deploy.bat
- Mac / Linux: open a terminal in this folder and run:  ./deploy.sh

AFTER IT FINISHES
Wait 1-2 minutes, then open https://hellomanavlab-cmyk.github.io/SkillBridge/ and check the homepage, Explore pages, Premium Membership, Raw Leads and the policy pages.

NOTES
- Settings > Pages must already be set to: Deploy from a branch, branch "main", folder "/ (root)".
- If your default branch is not "main", change BRANCH in deploy.sh / deploy.bat.
- The "site" folder is the complete public website. Do not add secrets (keys, passwords) to it.
