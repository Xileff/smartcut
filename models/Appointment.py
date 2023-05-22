from utils.database import db


class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.String(21), primary_key=True)
    schedule = db.Column(db.DateTime(), nullable=False)
    is_finished = db.Column(db.Boolean(), nullable=False)
    is_canceled = db.Column(db.Boolean(), nullable=False)
    will_be_canceled = db.Column(db.Boolean(), nullable=False)
    date_canceled = db.Column(db.DateTime())
    barbershop_id = db.Column(
        db.String(27),
        db.ForeignKey("barbershops.id", ondelete="CASCADE"),
        nullable=False,
    )
    user_id = db.Column(
        db.String(21), db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    barbershop = db.relationship("Barbershop", back_populates="appointments")
    user = db.relationship("User", back_populates="appointments")
    review = db.relationship("Review", back_populates="appointment", uselist=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "schedule": self.schedule,
            "is_finished": self.is_finished,
            "is_canceled": self.is_canceled,
            "will_be_canceled": self.will_be_canceled,
            "date_canceled": self.date_canceled,
            "barbershop_id": self.barbershop_id,
            "user_id": self.user_id,
        }
