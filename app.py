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


def print_all_animals_by_scientificname():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY scientific_name ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


def print_all_animals_by_scientificnamedesc():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY scientific_name DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


def print_all_animals_by_age():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY max_age;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


def print_all_animals_by_height():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY max_height;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


def print_all_animals_by_blood():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY cold_or_warm_blooded;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name      Scientific Name               Max Age   Max Height     Cold or Warm-Blooded   Pet")
    for AnimalTable in results:
        print(f"{AnimalTable[1].title():<10}{AnimalTable[2].title():<30}{AnimalTable[3]:<10}{AnimalTable[4]:<15}{AnimalTable[5].title():<23}{AnimalTable[6]}")
    db.close()


def print_all_animals_by_pet():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM AnimalTable ORDER BY pet DESC;"
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
\n4. Print all animals by scientific name
\n5. Print all animals by scientific name descending
\n6. Print all animals by maximum age
\n7. Print all animals by maximum height
\n8. Print all animals by warmth of blood
\n9. Print all animals by how suitable they are for a pet
\n10. Stop
\n.
""")
    if user_input == "1":
        print_all_animals()
    elif user_input == "2":
        print_all_animals_by_name()
    elif user_input == "3":
        print_all_animals_by_name_desc()
    elif user_input == "4":
        print_all_animals_by_scientificname()
    elif user_input == "5":
        print_all_animals_by_scientificnamedesc()
    elif user_input == "6":
        print_all_animals_by_age()
    elif user_input == "7":
        print_all_animals_by_height()
    elif user_input == "8":
        print_all_animals_by_blood()
    elif user_input == "9":
        print_all_animals_by_pet()
    elif user_input == "10":
        break
    else:
        print("That was not an option\n")
