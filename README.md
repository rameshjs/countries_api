## Dev environment setup

This guide will help you set up and run a Django project in a virtual environment.

### Prerequisites
- Python 3.x installed on your system.
- Pip (Python package manager) installed.

### Step 1: Create a Virtual Environment
We recommend using a virtual environment to isolate your project dependencies.

```
python3 -m virtualenv env_name
```

### Step 2: Activate the Virtual Environment
```
source venv/bin/activate
```
### Step 3: Install Project Dependencies
```
pip install -r requirements.txt
```
### Step 4: Set Up the Database
```
./manage.py migrate
```
### Step 5: Populate `Country` and `Currency` Tables
Use custom management commands to populate the `Country` and `Currency` tables.

Note: Run `insert_currencies` first, as the `Country` table needs `Currency` data since the `currency` field in the `Country` table is a `many-to-many` relation.
```
./manage.py insert_currencies
./manage.py insert_countries
```
### Step 6: Start the Django Server
```
./manage.py runserver
```
Your Django development server should now be running. You can access your project at http://localhost:8000/ in your web browser.



