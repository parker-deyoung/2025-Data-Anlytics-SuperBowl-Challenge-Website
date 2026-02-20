## Create a virtual environment
python3 -m venv venv

## Activate the virtual environment
source venv/bin/activate

## Install dependencies
pip install -r backend_logic/requirments.txt

## Run the server
uvicorn backend_logic.main:app --reload --host 0.0.0.0 --port 8000

## Open the frontend
Open http://localhost:8000 in your browser

## Stop the server
Press Ctrl+C in the terminal where the server is running

## Deactivate the virtual environment
deactivate