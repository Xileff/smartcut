from datetime import datetime, timedelta
from utils.database import db


class EmailVerificationCode(db.Model):
    __tablename__ = "email_verification_codes"

    # columns
    code = db.Column(db.String(8), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    expired_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(
        db.String(21),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    # relationship
    user = db.relationship("User", back_populates="email_verification_code")

    # constraints
    __table_args__ = (db.PrimaryKeyConstraint(code, name="email_verification_code_pk"),)
