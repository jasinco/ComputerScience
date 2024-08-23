# TCIVS CS Website

## Deploy 
```bash
cd frontend
pnpm run build # or npm run build
cd ../server
python -m venv .venv
source .venv/bin/activate.sh
pip install -r requirements.txt
fastapi dev server.py
```
