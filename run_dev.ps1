# Start backend and frontend for local development (Windows PowerShell)
Write-Output "Starting backend and frontend..."
Start-Process pwsh -ArgumentList '-NoExit','-Command','cd "backend"; if(!(Test-Path .venv)){ python -m venv .venv }; .\.venv\Scripts\Activate; pip install -r requirements.txt; python app.py'
Start-Process npm -ArgumentList 'run','dev' -WorkingDirectory 'frontend'
