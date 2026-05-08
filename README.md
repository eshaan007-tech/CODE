# 🧠 Alzheimer Detection System

An AI-powered web application for detecting Alzheimer's disease stages using MRI brain scan images and Deep Learning.

Built using:
- Flask
- TensorFlow/Keras
- SQLite
- HTML/CSS
- Xception-based CNN Model

---

# 🚀 Features

✅ User Authentication System  
✅ MRI Image Upload  
✅ Deep Learning Prediction  
✅ Alzheimer Stage Classification  
✅ Confidence Score Output  
✅ Performance Dashboard  
✅ Chart Visualization  
✅ SQLite Database Integration  

---

# 🧠 Prediction Classes

The model predicts the following stages:

- MildDemented
- ModerateDemented
- NonDemented
- VeryMildDemented

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Flask | Backend Web Framework |
| TensorFlow/Keras | Deep Learning |
| SQLite | Database |
| Pillow | Image Processing |
| NumPy | Numerical Operations |
| HTML/CSS | Frontend |

---

# 📂 Project Structure

```bash
CODE/
│
├── app.py
├── requirements.txt
├── users.db
├── alz1.h5
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── result.html
│   ├── chart.html
│   └── performance.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/CODE.git
cd CODE
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python app.py
```

Application will start at:

```bash
http://127.0.0.1:5000
```

---

# 📦 Requirements

```txt
Flask==3.1.2
tensorflow==2.20.0
pillow==11.3.0
```

---

# 🔐 Authentication System

The application includes:

- User Registration
- User Login
- Session Management
- Logout Functionality

Database used:

```bash
SQLite (users.db)
```

---

# 🧠 Model Information

- Architecture: Xception CNN
- Input Size: 256x256
- Framework: TensorFlow/Keras
- Model File: `alz1.h5`

---

# 📊 Performance Metrics

| Metric | Value |
|---|---|
| Accuracy | 92.5% |
| Validation Accuracy | 90.1% |
| Loss | 0.12 |
| Validation Loss | 0.18 |

---

# 📷 How It Works

1. User uploads MRI image
2. Image is preprocessed
3. Model predicts Alzheimer stage
4. Confidence score is generated
5. Result displayed on dashboard

---

# ⚠️ Important Note

This project is developed for:
- Educational Purposes
- Research
- AI Learning

This is NOT a certified medical diagnostic system.

---

# 🔥 Future Improvements

- Doctor Dashboard
- Cloud Deployment
- Model Optimization
- Real-Time Analytics
- PDF Report Generation
- API Integration
- Multi-language Support

---

# 🧪 Dataset

MRI Brain Scan Dataset used for training Alzheimer classification model.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
🧠 Contribute improvements  

---

# 📜 License

This project is licensed under the MIT License.
