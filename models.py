from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=True)
    low_bp = db.Column(db.Boolean, nullable=True)
    high_bp = db.Column(db.Boolean, nullable=True)
    sugar = db.Column(db.Integer, nullable=True)
    diabetes = db.Column(db.Boolean, nullable=True)
    heart_disease = db.Column(db.Boolean, nullable=True)
    menstrual_health = db.Column(db.Boolean, nullable=True)
    recommended_diet = db.Column(db.JSON, nullable=True)

def init_db(app):
    """Initialize the database with the application context."""
    db.init_app(app)
    with app.app_context():
        db.create_all()
