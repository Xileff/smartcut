from utils.database import db
from models.Appointment import Appointment
from models.Review import Review
from sqlalchemy import func


class Barbershop(db.Model):
    __tablename__ = "barbershops"
    id = db.Column(db.String(27), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    latitude = db.Column(db.Numeric(10, 8), nullable=False)
    longitude = db.Column(db.Numeric(11, 8), nullable=False)
    user_id = db.Column(
        db.String(21),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    user = db.relationship("User", back_populates="barbershop")
    appointments = db.relationship("Appointment", back_populates="barbershop")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "picture": self.picture,
            "description": self.description,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def serialize_simple(self):
        rating = (
            db.session.query(func.avg(Review.stars))
            .join(Appointment, Review.appointment)
            .join(Barbershop, Appointment.barbershop)
            .filter(Barbershop.id == self.id)
            .scalar()
        )

        return {
            "id": self.id,
            "name": self.name,
            "picture": self.picture,
            "description": self.description,
            "rating": float(rating) or "No rating yet",
        }
