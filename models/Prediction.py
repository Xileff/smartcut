from utils.database import db


class Prediction(db.Model):
    __tablename__ = "predictions"
    id = db.Column(db.String(20), primary_key=True)
    picture = db.Column(db.String(255), nullable=False)
    compatibility = db.Column(db.Numeric(4, 2), nullable=False, default=0)
    hairstyle_id = db.Column(
        db.Integer, db.ForeignKey("hairstyles.id", ondelete="CASCADE"), nullable=False
    )
    user_id = db.Column(
        db.String(21), db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    hairstyle = db.relationship("Hairstyle", back_populates="predictions")
    user = db.relationship("User", back_populates="predictions")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "picture": self.picture,
            "comptability": self.compatibility,
            "hairstyle_id": self.hairstyle_id,
            "user_id": self.user_id,
        }
