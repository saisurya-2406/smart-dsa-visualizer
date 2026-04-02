Render deployment notes

1) Push your repo to GitHub.
2) On Render.com create a new Web Service and connect your GitHub repo.
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start command: `gunicorn dsa_project.wsgi --log-file -`
3) Add environment variables in Render Dashboard -> Environment:
   - `SECRET_KEY` : a secure random string
   - `DEBUG` : `False`
   - `ALLOWED_HOSTS` : your domain or `localhost` (comma-separated)
4) After deploy, run migrations on Render shell if you switch to a DB other than SQLite.

Notes:
- SQLite is not recommended for multi-instance production. For production use PostgreSQL and update `DATABASES`.
- Collectstatic must run during build to populate `staticfiles` for WhiteNoise.

Quick Git/GitHub/Render steps

1. Initialize git, commit, and push to GitHub (one-time):

```bash
git init
git add .
git commit -m "Initial commit - prepare for Render"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. On Render: create a new Web Service, connect the repo, then set:
- Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Start command: `gunicorn dsa_project.wsgi --log-file -`

3. Configure environment variables in the Render dashboard (do NOT commit secrets):
- `SECRET_KEY` — a secure random value
- `DEBUG` — `False`
- `ALLOWED_HOSTS` — e.g. `yourdomain.com`

4. If you plan to use PostgreSQL, add a managed database on Render, update `DATABASES` in `settings.py` to read credentials from env vars, then run migrations from the Render shell.

Local test commands

```bash
python -m venv .venv
& .venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn dsa_project.wsgi --log-file -
```

If you want, I can add a `render` GitHub Action or update `DATABASES` to use Postgres and a template `docker-compose.yml` for local dev. Which should I do next?

GitHub Action (auto-deploy)

I added `.github/workflows/deploy-to-render.yml` which triggers on pushes to `main` and calls the Render Deploys API.

Add these GitHub repository secrets before using the Action:
- `RENDER_API_KEY` — your Render API key (from Render Dashboard -> Account -> API Keys)
- `RENDER_SERVICE_ID` — the Service ID for the created Web Service (from Render Dashboard -> Service -> Settings -> ID)

After setting those secrets, push to `main` to trigger a deploy.
