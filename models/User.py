from utils.database import db


class User(db.Model):
    __tablename__ = "users"

    # columns
    id = db.Column(db.String(21), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(102), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.BigInteger(), unique=True, nullable=False)
    picture = db.Column(db.String(255), nullable=True, default=None)
    date_joined = db.Column(db.DateTime, nullable=False)
    is_email_verified = db.Column(db.Boolean(), nullable=False, server_default="0")
    is_barber = db.Column(db.Boolean(), nullable=False, server_default="0")

    # relationship
    email_verification_code = db.relationship(
        "EmailVerificationCode", uselist=False, back_populates="user"
    )

    def __repr__(self):
        return "<User %r>" & self.name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "phone": str(self.phone),
            "picture": self.picture,
            "dateJoined": self.date_joined,
        }

    def update_picture(self, data: dict):
        self.picture = data["picture"]
        db.session.commit()
