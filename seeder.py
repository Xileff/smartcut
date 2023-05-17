from app import app
from utils.database import db
from models.HairstyleCategory import HairstyleCategory
from models.Hairstyle import Hairstyle


def seed_hairstyle_category():
    db.session.add(HairstyleCategory(id=1, name="asian"))
    db.session.add(HairstyleCategory(id=2, name="western"))

    db.session.commit()


def seed_hairstyle():
    hairstyles = {
        "Asian": {
            "Comma Hair": "comma-hair.jpg",
            "Two Block": "two-block.jpg",
            "Messy Medium": "messy-medium.jpg",
            "Long Layered": "long-layered.jpg",
            "Textured Spiky": "textured-spiky.jpg",
            "Curtain": "curtain.jpg",
            "Brown Undercut": "brown-undercut.jpg",
            "Almond Middle Part": "almond-middle-part.jpg",
            "Voluminous Top with Undercut": "voluminous-top-with-undercut.jpg",
            "Short High Taper Fade": "short-high-taper-fade.jpg",
            "Asian Pompadour": "asian-pompadour.jpg",
            "Comb Over Bangs": "comb-over-bangs.jpg",
            "Asian Slick Back": "asian-slick-back.jpg",
            "Side Part": "side-part.jpg",
            "Fringe Up Medium": "fringe-up.jpg",
            "Super Classic": "super-classic.jpg",
            "Mullet": "mullet.jpg",
            "French Crop": "french-crop.jpg",
            "Men's Bob": "mens-bob.jpg",
            "Bowl Cut": "bowl-cut.jpg",
        },
        "Western": {
            "Afro": "afro.jpg",
            "Brush Over": "brush-over.jpg",
            "Brush Up": "brush-up.jpg",
            "Classic Crew Up": "classic-crew-up.jpg",
            "Comb Over": "comb-over",
            "Conventional Hipster": "conventional-hipster.jpg",
            "Dumpy Spikes": "dumpy-spikes.jpg",
            "Faux Hawk": "faux-hawk.jpg",
            "High and Tide": "high-and-tide.jpg",
            "Ivy League": "ivy-league.jpg",
            "Long Hairstyles": "long-hairstyles.jpg",
            "Low Half Updo": "low-half-updo.jpg",
            "Middle Part With Low Fade Men": "middle-part-with-low-fade-men.jpg",
            "Mullet Hairstyle": "mullet-hairstyle.jpg",
            "Pompadour": "pompadour.jpg",
            "Razored Shag": "razored-shag.jpg",
            "Short Conservative": "short-conservative.jpg",
            "Short Messy": "short-messy.jpg",
            "Straight Texture": "short-texture.jpg",
            "Textured Fringe": "textured-fringe.jpg"
        },
    }

    for category in hairstyles:
        for hairstyle in hairstyles[category]:
            db.session.add(
                Hairstyle(
                    name=hairstyle,
                    picture="https://storage.googleapis.com/smartcut-backend-bucket/hairstyle/" + hairstyles[category][hairstyle],
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
        # unseed_hairstyle()
        # unseed_hairstyle_category()
        seed_hairstyle_category()
        seed_hairstyle()
