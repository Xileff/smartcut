from utils.database import db
from dotenv import load_dotenv
import os


class Hairstyle(db.Model):
    __tablename__ = "hairstyles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    picture = db.Column(db.String(255), nullable=True, default=None)
    description = db.Column(
        db.Text, nullable=False, default="Lorem ipsum dolor sit amet"
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("hairstyle_categories.id", ondelete="CASCADE"),
        nullable=False,
    )

    category = db.relationship("HairstyleCategory", back_populates="hairstyles")
    predictions = db.relationship("Prediction", back_populates="hairstyle")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture": "https://storage.googleapis.com/"
            + os.getenv("STORAGE_BUCKET")
            + "/"
            + os.getenv("HAIRSTYLE_PICTURE_PATH")
            + self.picture,
            "category": self.category.name,
        }

    def serialize_complete(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture": self.picture,
            "description": self.description,
            "category": self.category.name,
        }
