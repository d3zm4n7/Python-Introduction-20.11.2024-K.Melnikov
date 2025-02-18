from MyModule import *
while True:
    print("\n######################################")
    print("\n#### Tere tulemast meie süsteemi! ####\n1 - Registreerimine\n2 - Automatiseerimine\n3 - Kasutajanime või parooli muutmine\n4 - Unustanud parooli taastamine\n5 - Lõpetamine")
    print("\n######################################")
    valik=input("\nSisestage valik (number): ")

    


    # 1. Sign Up
    if valik=="1":
        print("\n--- Registreerimine ---\n")
        registreeri_kasutaja()


    # 2. Sigh in
    elif valik=="2":
        print("\n--- Automatiseerimine ---\n")
        vana_login=sisesta_login(sisselogimised)
        vana_parool=sisesta_parool(sisselogimised,paroolid,vana_login)

        print("\nAutoriseerimine õnnestus!")


    # 3. Change login or password
    elif valik=="3":
        print("\n--- Kasutajanime või parooli muutmine ---\n")
        muuda_kasutaja_andmeid()


    # 4. Recover password
    elif valik=="4":
        print("\n--- Unustanud parooli taastamine ---\n")
        while True:
            vana_login=input("Sisestage kasutajanimi: ")
            if vana_login not in sisselogimised:
                print("Kasutajanimi ei leitud. Proovige uuesti!")
            else:
                index_parool=sisselogimised.index(vana_login)
                uus_parool=genereeri_parool()    # Generate new password
                paroolid.pop(index_parool)  # Delete old password
                paroolid.insert(index_parool,uus_parool)  # Insert new password
                print(f"\nTeie uus parool on: {uus_parool}")
                break


    # 5. Exit
    elif valik=="5":
        print("\n--- Head aega! ---\nProgrammi lõpetamine...")
        break
    else:
        print("Valige tegevus või tegevuse number!")
