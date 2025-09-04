
# 🛠 IngcoTumbaco — Service & Warranty Management App

A Flask-based enterprise web app built for managing service and warranty requests efficiently.

---

##  Features

- **User Authentication**: Secure login system with role-based access.  
- **Dashboard Interface**: Administrators can view, approve, and manage service tickets.  
- **Excel Integration**: Upload spreadsheets to create tickets—updates automatically.  
- **Efficiency Gains**:  
  - 60% faster ticket lookup (vs Excel)  
  - 80% reduction in manual data entry time  
  - 35% improvement in overall operational workflow  
- **Backend Stack**:
  - Python with Flask  
  - SQLAlchemy for ORM  
  - Pandas & Openpyxl for data processing  
  - MySQL/Postgres connector as primary database support  

---

##  Project Structure

```

IngcoTumbaco/
├─ app.py                  # Flask application entrypoint
├─ table\_create.py         # Script to initialize the database schema
├─ upload\_excel\_handler.py # Handles Excel validation and insertion
├─ usuarios.py             # User management (login, registration)
├─ requirements.txt        # Project dependencies
├─ templates/              # HTML templates for the UI
├─ static/                 # CSS, JS, images (if any)
├─ routes/                 # Flask route modules
├─ database/               # Database connection setup modules
├─ uploads/                # Temporary Excel upload storage
└─ venv/                   # Python virtual environment (should be .gitignored)

````

---

##  Installation & Setup

```bash
git clone https://github.com/marcobarreno2003/IngcoTumbaco.git
cd IngcoTumbaco

python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

pip install -r requirements.txt
````

---

## Running the App

1. Run `table_create.py` to set up the database.

```bash
python table_create.py
```

2. Start the Flask server:

```bash
python app.py
```

3. Open your browser at: `http://localhost:5000/`

---

## Performance Impact

* **60% faster ticket lookup** than using spreadsheets.
* **80% less manual data entry** due to Excel upload automation and error checking.
* **35% increase in workflow efficiency**, handling 65+ tickets per month.

---

## License

Licensed under the **MIT License**.

---

## Author

**Marco Barreno**
[LinkedIn](https://www.linkedin.com/in/marco-barreno-uh/) | [GitHub](https://github.com/marcobarreno2003)



