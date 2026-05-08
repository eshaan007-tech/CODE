from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load your trained model
model = load_model("alz1.h5")

IMG_SIZE = (256, 256)
class_names = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

DB_NAME = "users.db"

# =======================
# Database Setup
# =======================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT username, password FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user

# Initialize DB
init_db()

# =======================
# Image Preprocessing
# =======================
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize(IMG_SIZE)
    img_array = np.array(image) / 255.0
    img_array = img_array.astype(np.float32)
    return np.expand_dims(img_array, axis=0)

# =======================
# Routes
# =======================
@app.route('/')
def home():
    if session.get('username'):
        return redirect(url_for('index'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        user = get_user(username)

        if user and user[1] == password:  # check stored password
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        confirm = request.form['confirm_password'].strip()

        if not username or not password:
            flash('Username and password are required.', 'warning')
        elif password != confirm:
            flash('Passwords do not match.', 'warning')
        elif not add_user(username, password):
            flash('Username already exists.', 'warning')
        else:
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if not session.get('username'):
        flash('Please login to access this page.', 'warning')
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'image' not in request.files or request.files['image'].filename == '':
            flash('Please upload an image.', 'danger')
            return redirect(url_for('index'))
        try:
            image_bytes = request.files['image'].read()
            img = preprocess_image(image_bytes)
            prediction = model.predict(img)
            predicted_class = class_names[np.argmax(prediction[0])]
            confidence = float(np.max(prediction[0]))
            session['predicted_class'] = predicted_class
            session['confidence'] = confidence
            return redirect(url_for('result'))
        except Exception as e:
            flash(f"Error processing image: {str(e)}", 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/result')
def result():
    if not session.get('username'):
        flash('Please login to access this page.', 'warning')
        return redirect(url_for('login'))

    predicted_class = session.get('predicted_class')
    confidence = session.get('confidence')

    if not predicted_class or confidence is None:
        flash('No prediction data found. Please try again.', 'warning')
        return redirect(url_for('index'))

    return render_template('result.html', predicted_class=predicted_class, confidence=confidence)

@app.route('/chart')
def chart():
    data = {
        'labels': ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented'],
        'values': [20, 10, 50, 20]
    }
    return render_template('chart.html', data=data)

@app.route('/performance')
def performance():
    stats = {
        'accuracy': '92.5%',
        'loss': '0.12',
        'val_accuracy': '90.1%',
        'val_loss': '0.18',
        'epochs': 25
    }
    return render_template('performance.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
