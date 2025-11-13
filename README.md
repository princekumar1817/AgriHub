🌾 AgriHub — Smart Farm Management System

A modern and feature-rich Django-based farm management platform that helps farmers track and manage employees, crops, livestock, machinery, milk & egg production analytics, and more — all in one place.
Designed with a clean UI/UX, easy navigation, and powerful dashboards.

✨ Features
🔹 Dashboard

Clean UI with hero section and quick navigation

Shows access to major modules

🔹 Employee Management

Add, update, delete employee records

Track assignments & payroll details

🔹 Crop Management

Crop operations, sales & expenses

Add/update/delete records

🔹 Livestock Management

Tag-based livestock tracking

Production & health monitoring

🔹 Machinery Management

Machinery inventory

Maintenance schedules & activity logs

🔹 Milk Production Analytics

Select year/month

Generate daily production & consumption charts

Auto-rendered bar charts using Matplotlib

🔹 Egg Production Analytics

Track daily egg collections

Feed consumption, comments, insights

Clean and modern analytics table

🔹 Fully Responsive UI

Modern layout

Works on mobile, tablet, and desktop

🏗️ Tech Stack
Component	Technology
Backend	Python, Django
Frontend	HTML, CSS, JavaScript, Boxicons, Google Fonts
Database	SQLite (development)
Visualization	Matplotlib
Deployment Ready	Railway / Render / GitHub Pages (static)
📦 Installation Guide (Run Locally)

Follow these steps to run the project on your computer.

🚀 1. Clone the Repository
git clone https://github.com/yourusername/agrihub.git
cd agrihub

🐍 2. Create Virtual Environment
python -m venv venv


Activate it:

Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate

📥 3. Install Dependencies

Make sure requirements.txt exists.

pip install -r requirements.txt


If you don’t have it, generate using:

pip freeze > requirements.txt

⚙️ 4. Apply Migrations
python manage.py migrate

👤 5. Create Superuser
python manage.py createsuperuser

▶️ 6. Run Development Server
python manage.py runserver


Access the project in your browser:
👉 http://127.0.0.1:8000

🚀 Deployment Guide (Railway / Render Hosting)
1. Add these two files in project root:
📌 Procfile
web: gunicorn agrihub.wsgi

📌 requirements.txt

(Already created earlier)

📌 runtime.txt
python-3.10

2. Push your code to GitHub
git add .
git commit -m "Initial commit"
git push origin main

3. Deploy on Railway

Visit: https://railway.app

Create New Project → Deploy from GitHub

Add environment variable:

PORT=8000


Railway installs dependencies & deploys automatically

📂 Project Structure
AgriHub/
│── homepage/                # Main Django app
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│── agrihub/                 # Django project config
│── manage.py
│── requirements.txt
│── Procfile
│── runtime.txt
│── README.md

🧪 Screenshots

(Add your screenshots here)

![Dashboard](screenshots/dashboard.png)
![Milk Analytics](screenshots/milk.png)
![Egg Production](screenshots/egg.png)

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

📧 Contact

Developer: Prince Kumar

📩 Email: princekumarsingh1817@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/prince-kumar-400134247/

🐙 GitHub: https://github.com/princekumar1817

⭐ Support

If you like this project, please ⭐ star the repo — it motivates me to build more!