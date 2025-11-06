# 🔍 Asset Lookup Web App

A simple Flask-based web application that allows users to search for assets by their **Asset Number**.  
The app reads data from an Excel file (`assets.xlsx`) and displays details such as:

- Description
- Model
- Serial Number (SN)
- Date
- Location

---

## 🚀 Features
- Search assets by Asset Number
- Clean, user-friendly HTML output
- Built with **Flask** + **Pandas**
- Ready for deployment on **Render**

---

## 📂 Project Structure
asset-lookup/
│
├── main.py            # Flask app entry point
├── assets.xlsx        # Asset data file
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/MohamedAmin2010/asset-lookup.git
   cd asset-lookup
   gunicorn app:app --bind 0.0.0.0:$PORT
   # Asset Lookup Web App

## Features
- Search assets by asset number
- Clean, user-friendly HTML output
- Built with Flask + pandas
- Ready for deployment on Render

## Installation & Usage
```bash
git clone https://github.com/MohamedAmir010/asset-lookup.git
cd asset-lookup
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:8080
asset-lookup/
├── app.py
├── assets.xlsx
├── requirements.txt
├── templates/
└── README.md
### 4. Save the file

### 5. Push changes to GitHub
```bash
git add README.md
git commit -m "Update README with correct setup instructions"
git push origin main

   
   
