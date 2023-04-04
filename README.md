# Real Estate Database
GitHub Link: https://github.com/hordiienkoalina/real-estate-database

## Install

macOS:
```
python3 -m venv test-venv
source test-venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 -m data.insert_data
python3 query_data.py
```

Windows:
```
python3 -m venv test-venv
test-venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 create.py
python3 -m data.insert_data
python3 query_data.py
```