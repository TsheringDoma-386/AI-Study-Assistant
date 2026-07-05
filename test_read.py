from database.models import get_all_materials

materials = get_all_materials()

for material in materials:
    print(material)