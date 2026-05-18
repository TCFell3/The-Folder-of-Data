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


def print_regions():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM RegionTest"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name                      Continent           Country             Land Mass in KM Squared")
    for RegionTest in results:
        print(f"{RegionTest[1].title():<26}{RegionTest[2].title():<20}{RegionTest[3]:<20}{RegionTest[4]}")
    db.close()


def print_animals_and_region():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Name, Scientific_Name, Max_Age, Max_Height, Cold_or_Warm_Blooded, Pet, Region_Name, Continent, Country, Land_Mass_KM_Squared FROM AnimalTable JOIN LinkTest ON AnimalTable.id = LinkTest.AnimalID JOIN RegionTest ON RegionTest.id = LinkTest.RegionID"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Scientific Name          Max Age   Max Height     Blooded   Pet     Region        Continent      Country        Land Mass in KM Squared")
    for AnimalTable in results:
        print(f"{AnimalTable[0].title():<15}{AnimalTable[1].title():<25}{AnimalTable[2]:<10}{AnimalTable[3]:<15}{AnimalTable[4]:<10}{AnimalTable[5].title():<8}{AnimalTable[6]:<14}{AnimalTable[7]:<15}{AnimalTable[8]:<15}{AnimalTable[9]}")
    db.close()


def print_animals_in_region():
    while True:
        region = input(
    """
    What region are you using
    \n1. Queensland
    \n2. Apocalypse Peaks
    \n3. GuangZhou
    \n4. Ankara
    \n5. Alert
    \n6. Helsinki
    \n7. Dallas
    \n8. Ouro Preto
    \n9. Tel Aviv
    \n10. New Delhi
    """)
        if region == "1":
            regiondata = "Queensland"
        elif region == "2":
            regiondata = "Apocalypse Peaks"
        elif region == "3":
            regiondata = "GuangZhou"
        elif region == "4":
            regiondata = "Ankara"
        elif region == "5":
            regiondata = "Alert"
        elif region == "6":
            regiondata = "Helinski"
        elif region == "7":
            regiondata = "Dallas"
        elif region == "8":
            regiondata = "Ouro Preto"
        elif region == "9":
            regiondata = "Tel Aviv"
        elif region == "10":
            regiondata = "New Delhi"
        else:
            print("Invalid Answer!")
            break
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute(f"SELECT AnimalTable.Name, AnimalTable.Scientific_Name, AnimalTable.Max_Age, AnimalTable.Max_Height, AnimalTable.Cold_or_Warm_Blooded, AnimalTable.Pet, RegionTest.Region_Name, RegionTest.Continent, RegionTest.Country, RegionTest.Land_Mass_KM_Squared FROM AnimalTable JOIN LinkTest ON AnimalTable.id = Linktest.AnimalID JOIN RegionTest ON RegionTest.id = LinkTest.RegionID WHERE Region_Name = '{regiondata}';")
        results = cursor.fetchall()
        print("Name           Scientific Name          Max Age   Max Height     Blooded   Pet     Region        Continent      Country        Land Mass in KM Squared")
        for AnimalTable in results:
            print(f"{AnimalTable[0].title():<15}{AnimalTable[1].title():<25}{AnimalTable[2]:<10}{AnimalTable[3]:<15}{AnimalTable[4]:<10}{AnimalTable[5].title():<8}{AnimalTable[6]:<14}{AnimalTable[7]:<15}{AnimalTable[8]:<15}{AnimalTable[9]}")
        db.close()
        break


def print_region_with_animals():
    while True:
        animal = input(
    """
    What animal are you using
    \n1. Cat
    \n2. Dog
    \n3. Parakeet
    \n4. Goldfish
    \n5. Lizard
    \n6. Rabbit
    \n7. Mouse
    \n8. Kangaroo
    \n9. Giraffe
    \n10. Rhino
    """)
        if animal == "1":
            animaldata = "Cat"
        elif animal == "2":
            animaldata = "Dog"
        elif animal == "3":
            animaldata = "Parakeet"
        elif animal == "4":
            animaldata = "Goldfish"
        elif animal == "5":
            animaldata = "Lizard"
        elif animal == "6":
            animaldata = "Rabbit"
        elif animal == "7":
            animaldata = "Mouse"
        elif animal == "8":
            animaldata = "Kangaroo"
        elif animal == "9":
            animaldata = "Giraffe"
        elif animal == "10":
            animaldata = "Rhino"
        else:
            print("Invalid Answer!")
            break
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute(f"SELECT AnimalTable.Name, AnimalTable.Scientific_Name, AnimalTable.Max_Age, AnimalTable.Max_Height, AnimalTable.Cold_or_Warm_Blooded, AnimalTable.Pet, RegionTest.Region_Name, RegionTest.Continent, RegionTest.Country, RegionTest.Land_Mass_KM_Squared FROM AnimalTable JOIN LinkTest ON AnimalTable.id = Linktest.AnimalID JOIN RegionTest ON RegionTest.id = LinkTest.RegionID WHERE Name = '{animaldata}';")
        results = cursor.fetchall()
        print("Name           Scientific Name          Max Age   Max Height     Blooded   Pet     Region        Continent      Country        Land Mass in KM Squared")
        for AnimalTable in results:
            print(f"{AnimalTable[0].title():<15}{AnimalTable[1].title():<25}{AnimalTable[2]:<10}{AnimalTable[3]:<15}{AnimalTable[4]:<10}{AnimalTable[5].title():<8}{AnimalTable[6]:<14}{AnimalTable[7]:<15}{AnimalTable[8]:<15}{AnimalTable[9]}")
        db.close()
        break


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
\n10. Print all regions
\n11. Print all animals and their region
\n12. Print animals by a region
\n13. Print regions by an animal
\n14. Quit
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
        print_regions()
    elif user_input == "11":
        print_animals_and_region()
    elif user_input == "12":
        print_animals_in_region()
    elif user_input == "13":
        print_region_with_animals()
    elif user_input == "14":
        break
    else:
        print("That was not an option.\n")
