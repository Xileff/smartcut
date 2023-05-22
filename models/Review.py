from utils.database import db


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.String(23), primary_key=True)
    stars = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(100), default="")
    appointment_id = db.Column(
        db.String(20),
        db.ForeignKey("appointments.id", ondelete="CASCADE"),
        nullable=False,
    )

    appointment = db.relationship("Appointment", back_populates="review")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "stars": self.stars,
            "message": self.message,
            "appointment_id": self.appointment_id,
        }
