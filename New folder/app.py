
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import time

app = Flask(__name__)
app.secret_key = "secret123"

# ✅ الاتصال بقاعدة البيانات مع retry (مهم)
def get_db():
    for i in range(10):
        try:
            db = mysql.connector.connect(
                host="db",       # مهم في docker-compose
                user="root",
                password="1234",
                database="mydb"
            )
            return db
        except:
            print("⏳ Waiting for database...")
            time.sleep(2)
    raise Exception("❌ Database connection failed")

# 🏠 الصفحة الرئيسية
@app.route("/")
def home():
    return redirect(url_for("login"))

# 🔐 تسجيل الدخول
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            db = get_db()
            cursor = db.cursor()

            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))

            user = cursor.fetchone()

            if user:
                session["user"] = username
                return redirect(url_for("dashboard"))
            else:
                error = "Invalid username or password ❌"

        except Exception as e:
            print("🔥 ERROR:", e)
            error = "Database error ❌"

    return render_template("login.html", error=error)

# 📊 Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])

# 🚪 Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ▶️ تشغيل التطبيق
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)