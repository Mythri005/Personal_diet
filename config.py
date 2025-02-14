class Config:
    SECRET_KEY = "your_secret_key"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"  # SQLite for local dev
    SQLALCHEMY_TRACK_MODIFICATIONS = False
