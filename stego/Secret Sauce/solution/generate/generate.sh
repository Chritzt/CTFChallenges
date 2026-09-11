mkdir secret-sauce-challenge
cd secret-sauce-challenge
git init

git config user.name "Kevin (Lead Dev)"
git config user.email "kevin@clueless-corp.com"

echo "import os" > app.py
echo "print('Starting our production app...')" >> app.py
git add app.py
git commit -m "feat: initial production server setup (bulletproof architecture)"

echo "# TODO: Move this to environment variables later, nobody will see it anyway" >> app.py
echo "API_KEY = 'CLA{G1t_N3v3r_F0rg3ts_D4ngl1ng_0bj3cts}'" >> app.py
git add app.py
git commit -m "wip: added database connection strings and secret sauce keys"

echo "print('App running successfully!')" >> app.py
git add app.py
git commit -m "fix: minor typos in README and bumped version to 1.0.0-alpha"

git reset --hard HEAD~2

echo "print('Starting our production app safely...')" >> app.py
git add app.py
git commit -m "chore: optimized memory leaks and cleaned up legacy code"

git reflog expire --expire=now --all
rm -rf .git/logs

zip -r ../secret_sauce_challenge.zip .