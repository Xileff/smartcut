from utils.database import db


class IdCard(db.Model):
    __tablename__ = "id_cards"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=False)
    picture = db.Column(db.String(255), nullable=False, unique=True)
    user_id = db.Column(
        db.String(21),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    user = db.relationship("User", back_populates="id_card")

    def save(self):
        db.session.add(self)
        db.session.commit()
