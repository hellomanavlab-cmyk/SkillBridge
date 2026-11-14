#!/usr/bin/env bash
# One-step deploy of the SkillBridge website to GitHub Pages.
# 1) backs up the current repository as a zip next to this script
# 2) replaces the repository contents with the files in ./site
# 3) commits and pushes to the main branch
# Requires: git, and you must already be signed in to GitHub on this computer.
set -e
REPO="${REPO:-https://github.com/hellomanavlab-cmyk/SkillBridge.git}"
BRANCH="${BRANCH:-main}"
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d)"

echo "Cloning $REPO ..."
git clone --branch "$BRANCH" "$REPO" "$WORK/repo"
cd "$WORK/repo"

BACKUP="$HERE/backup-old-repo-$(date +%Y%m%d-%H%M%S).zip"
git archive --format=zip -o "$BACKUP" HEAD
echo "Backup of the old website saved: $BACKUP"

find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -R "$HERE/site/." .

git add -A
if git diff --cached --quiet; then
  echo "No changes to deploy."
else
  git -c user.name="SkillBridge Deploy" -c user.email="skillbridge.manavlab@gmail.com" commit -m "Website update: policies, leads, premium, explore pages"
  git push origin "$BRANCH"
  echo "Pushed. Wait 1-2 minutes, then open https://hellomanavlab-cmyk.github.io/SkillBridge/"
fi
rm -rf "$WORK"
