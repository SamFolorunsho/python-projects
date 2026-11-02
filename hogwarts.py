students = [
    {"name": "Flex", "house": "Off Camper", "sport": "Football"},
    {"name": "Demmy", "house": "Off Camper", "sport": "Football"},
    {"name": "Oxy", "house": "Off Camper", "sport": None},
    {"name": "Nicholas", "house": "Angola", "sport": "Basketball"}
]

for student in students:
    print(student["name"], student["sport"], student["house"], sep="--")