from models.emotion_model import analyze_emotion
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

app = Flask(__name__)

# -----------------------------------
# Configuration
# -----------------------------------

app.config["SECRET_KEY"] = "mindtrack-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"

login_manager.login_message_category = "info"


# -----------------------------------
# User Model
# -----------------------------------

class User(UserMixin, db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    journals = db.relationship(
        "Journal",
        backref="author",
        lazy=True,
        cascade="all, delete"
    )


# -----------------------------------
# Journal Model
# -----------------------------------

class Journal(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    content = db.Column(db.Text, nullable=False)

    mood = db.Column(db.String(50), default="Unknown")

    confidence = db.Column(db.Float, default=0.0)

    ai_summary = db.Column(db.Text, default="")

    created_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

# -----------------------------------
# Flask Login
# -----------------------------------

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# -----------------------------------
# Home
# -----------------------------------

@app.route("/")
def home():

    return render_template("index.html")

# -----------------------------------
# Register
# -----------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        existing_user = User.query.filter(
            (User.username == username) |
            (User.email == email)
        ).first()

        if existing_user:
            flash("Username or Email already exists.", "danger")
            return redirect(url_for("register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully. Please log in.", "success")

        return redirect(url_for("login"))

    return render_template("register.html")


# -----------------------------------
# Login
# -----------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):

            login_user(user)

            flash("Welcome back!", "success")

            return redirect(url_for("dashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("login.html")


# -----------------------------------
# Dashboard
# -----------------------------------

@app.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",
        username=current_user.username
    )


# -----------------------------------
# Logout
# -----------------------------------

@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.", "info")

    return redirect(url_for("home"))

# -----------------------------------
# Journal
# -----------------------------------

@app.route("/journal", methods=["GET", "POST"])
@login_required
def journal():

    if request.method == "POST":

        title = request.form["title"].strip()
        content = request.form["content"].strip()

        if not title or not content:
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("journal"))

        emotion, confidence, summary = analyze_emotion(content)

        entry = Journal(
            title=title,
            content=content,
            mood=emotion,
            confidence=confidence,
            ai_summary=summary,
            user_id=current_user.id
        )

        db.session.add(entry)
        db.session.commit()

        flash("Journal entry saved successfully!", "success")

        return redirect(url_for("journal"))

    entries = Journal.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Journal.created_at.desc()
    ).all()

    return render_template(
        "journal.html",
        entries=entries
    )

# -----------------------------------
# Create Database
# -----------------------------------

with app.app_context():
    db.create_all()


# -----------------------------------
# Run Application
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)