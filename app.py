import sqlite3

DATABASE = "AnimalTest.db"


def print_all_animals():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


def print_all_animals_by_name():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY name ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


def print_all_animals_by_name_desc():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY name DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


while True:
    user_input = input(
"""
What would you like to do?
\n1. Print all animals
\n2. Print all animals by alphabetical order
\n3. Print all animals by alphabetical order descending
\n.
""")
    if user_input == "1":
        print_all_animals()
    elif user_input == "2":
        print_all_animals_by_name()
    elif user_input == "3":
        print_all_animals_by_name_desc()
    else:
        print("That was not an option\n")
