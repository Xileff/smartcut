from models.Hairstyle import Hairstyle
from models.HairstyleCategory import HairstyleCategory
from werkzeug.exceptions import NotFound


def get_hairstyles(name, category):
    if name and category:
        hairstyles = Hairstyle.query.filter(
            Hairstyle.name.like("%" + name + "%"),
            Hairstyle.category.has(HairstyleCategory.name == category),
        )
    elif name and not category:
        hairstyles = Hairstyle.query.filter(Hairstyle.name.like("%" + name + "%"))
    elif not name and category:
        hairstyles = Hairstyle.query.filter(
            Hairstyle.category.has(HairstyleCategory.name == category)
        )
    else:
        hairstyles = Hairstyle.query.all()

    return [hairstyle.serialize() for hairstyle in hairstyles]

def get_hairstyle_by_id(id):
    hairstyle = Hairstyle.query.filter_by(
        id = id
    ).first()
    if not hairstyle:
        raise NotFound("Hairstyle not found")


    return hairstyle.serialize_complete()

