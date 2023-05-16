from utils.database import db


class Hairstyle(db.Model):
    __tablename__ = "hairstyle"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    picture = db.Column(db.String(255), nullable=True, default=None)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("hairstyle_category.id", ondelete="CASCADE"),
        nullable=False,
    )

    category = db.relationship("HairstyleCategory", back_populates="hairstyles")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture": self.picture,
            "category": self.category.name,
        }
