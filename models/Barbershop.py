from utils.database import db


class Barbershop(db.Model):
    __tablename__ = "barbershops"
    id = db.Column(db.String(27), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255), nullable=False)
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
            "address": self.address,
            "picture": self.picture,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "user_id": self.user_id,
        }
