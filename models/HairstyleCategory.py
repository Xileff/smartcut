from utils.database import db


class HairstyleCategory(db.Model):
    __tablename__ = "hairstyle_category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)

    hairstyles = db.relationship("Hairstyle", back_populates="category")
