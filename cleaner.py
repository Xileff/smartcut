from app import app
from utils.database import db

if __name__ == "__main__":
    with app.app_context():
        db.session.execute(db.text("DELETE FROM users"))
        db.session.commit()
