from app import app
from utils.database import db
from models.HairstyleCategory import HairstyleCategory
from models.Hairstyle import Hairstyle


def seed_hairstyle_category():
    db.session.add(HairstyleCategory(name="asian"))
    db.session.add(HairstyleCategory(name="western"))

    db.session.commit()


def seed_hairstyle():
    hairstyles = {
        "Asian": {
            "Comma Hair": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/comma-hair.jpg",
            "Two Block": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/two-block.jpg",
            "Messy Medium": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/messy-medium.jpg",
            "Long Layered": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/long-layered.jpg",
            "Textured Spiky": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/textured-spiky.jpg",
            "Curtain": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/curtain.jpg",
            "Brown Undercut": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/brown-undercut.jpg",
            "Almond Middle Part": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/almond-middle-part.jpg",
            "Voluminous Top with Undercut": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/voluminous-top-with-undercut.jpg",
            "Short High Taper Fade": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/short-high-taper-fade.jpg",
            "Asian Pompadour": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/asian-pompadour.jpg",
            "Comb Over Bangs": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/comb-over-bangs.jpg",
            "Asian Slick Back": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/asian-slick-back.jpg",
            "Side Part": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/side-part.jpg",
            "Fringe Up Medium": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/fringe-up.jpg",
            "Super Classic": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/super-classic.jpg",
            "Mullet": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/mullet.jpg",
            "French Crop": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/french-crop.jpg",
            "Men's Bob": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/mens-bob.jpg",
            "Bowl Cut": "https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/bowl-cut.jpg",
        },
        "Western": {},
    }

    for category in hairstyles:
        for hairstyle in hairstyles[category]:
            db.session.add(
                Hairstyle(
                    name=hairstyle,
                    picture=hairstyles[category][hairstyle],
                    category_id=1 if category == "Asian" else 2,
                )
            )

    db.session.commit()


def unseed_hairstyle():
    db.session.execute(db.text("DELETE FROM hairstyle"))
    db.session.commit()


def unseed_hairstyle_category():
    db.session.execute(db.text("DELETE FROM hairstyle_category"))
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        unseed_hairstyle()
        unseed_hairstyle_category()
        seed_hairstyle_category()
        seed_hairstyle()
