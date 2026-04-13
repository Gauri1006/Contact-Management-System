# 📇 Contact Management System (Flask)

A simple and responsive **Contact Management Web Application** built using **Flask, HTML, and CSS**.
This app allows users to **add, view, edit, and delete contacts** with a clean UI.

---

## 🚀 Features

* ➕ Add new contacts
* 📋 View all contacts
* ✏️ Edit existing contacts
* ❌ Delete contacts
* 🎨 Styled user interface using CSS
* ⚡ Fast and lightweight (Flask backend)

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **Templating Engine:** Jinja2
* **Storage:** In-memory list (temporary)

---

## Screenshots
<img width="2872" height="1600" alt="image" src="https://github.com/user-attachments/assets/01107718-179b-4f31-bd85-a1f101aa39a4" />

<img width="2879" height="1615" alt="image" src="https://github.com/user-attachments/assets/a8191d99-67fe-4d4c-8d94-b847a790fd6f" />

## 📁 Project Structure

```
Contact Management System/
│── app.py
│── templates/
│   ├── index.html
│   ├── add_contact.html
│   ├── edit_contact.html
│── static/
│   └── style.css
│── venv/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd "Contact Management System"
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate virtual environment

**Windows:**

```
venv\Scripts\activate
```

### 4️⃣ Install dependencies

```
pip install flask
```

### 5️⃣ Run the application

```
python app.py
```

---

## 🌐 Run Locally

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

* Flask handles routing and backend logic
* HTML templates display data using Jinja2
* Forms send data via POST requests
* Contacts are stored in a Python list (temporary storage)

---

## ⚠️ Limitations

* Data is not stored permanently (resets on restart)
* No authentication system
* No database integration

---

## 🚀 Future Improvements

* 💾 Add SQLite database (persistent storage)
* 🔍 Search functionality
* 🔐 User authentication (login/signup)
* 📱 Fully responsive design
* 🌙 Dark mode

---

## 👩‍💻 Author

**Gauri Katiyar**

* 💼 B.Tech CSE Student
* 🌐 Interested in Web Development & Full Stack

---

## ⭐ Acknowledgement

This project was built as a learning project to understand Flask basics and CRUD operations.

---

## 📌 Note

Make sure your folder name is **static (lowercase)** for CSS to work correctly.

---
