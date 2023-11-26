while True:
    # menu pont valasztó
    menu_pont = str(input("Bejelentkezés: 1 , Regisztárció: 2  |(1:2): "))
    print("")
    # bejelentkezés
    if menu_pont == "1":
        log_felhasznaló = input("Felhasználónév: ")
        log_jelszó = input("Jelszó: ")
        print("")
    # hibas jelszó estén
        while log_felhasznaló != "Admin" or log_jelszó != "123":
            print("Helytelen Felhasznélónév vagy Jelszó")
            log_felhasznaló = input("Felhasználónév: ")
            log_jelszó = input("jelszó: ")
            print("")
    # ha sikeres a belépés
        print(
            f"Sikeres Bejelentkezés, A felhasznéló neved: {log_felhasznaló},A Jelszód pedig: {log_jelszó}")
    # regisztáció
    elif menu_pont == "2":
        reg_felhasznaló = input("Felhasználónév: ")
        reg_jelszó = input("jelszó: ")
        print("")
    # regisztációs adatok
        while reg_felhasznaló == "" or reg_jelszó == "":
            reg_felhasznaló = input("Felhasználónév: ")
            reg_jelszó = input("jelszó: ")
            print("")
    # sikeres regisztáció
        print(
            f"Sikeres Regisztáció, A felhasznéló neved: {reg_felhasznaló},A Jelszód pedig: {reg_jelszó}")
    # ha valami nem elront a felhasználó
    else:
        print("Valamit elronott kérem inditsa úrja a programot")
