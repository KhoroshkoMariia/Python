import mysql_helper_logowany_leszek


def login():
    email = input("Podaj email")
    password = input("Podaj haslo")
    users = mysql_helper_logowany_leszek.login(email, password)
    if len(users) == 1:
        print(users)
        print("Zalogowano sie")
    elif len(users) > 1:
        print("BŁĄD BAZY DANYCH")
    else:
        print("Wprowadzono nieprawidlowy login lub haslo")
    menu()


def register():
    email = input("Podaj email")
    password1 = input("Podaj hasło")
    password2 = input("Powtórz hasło")
    name = input("Podaj imie")
    surname = input("Podaj nazwisko")
    age = int(input("Podaj wiek"))
    phoneNO = input("Podaj nr telefonu")
    gender = input("Podaj płeć")

    if password1 != password2:
        print("Podane hasla nie zgadzaja sie")
        menu()
    if not age > 0:
        print("Podano nieprawidlowy wiek")
        menu()
    if not (gender[0].lower() == 'm' or gender[0].lower() == 'k'):
        print("Podano nieprawidlowa plec")
        menu()

    mysql_helper_logowany_leszek.create_user(email, name, surname, password1, age, phoneNO, gender)
    print("Utworzono użytkownika")
    menu()
def list_of_users():
    print(mysql_helper_logowany_leszek.list_of_users())
    menu()
def change_password():
    email = input("Podaj email uzytkownika dla ktorego chcesz zmienic haslo ")
    password = input("podaj haslo dla konta ktore chcesz zmienic")

    new_password1 = input("Podaj nowe hasło: ")
    new_password2 = input("Powtórz nowe hasło: ")

    user = mysql_helper_logowany_leszek.login(email, password)
    if len(user) == 1:
        print(user)
        print("Znaleziono użyktownika")
    elif len(user) > 1:
        print("BŁĄD BAZY DANYCH")
    else:
        print("Wprowadzono nieprawidlowy login lub haslo")

    if new_password1 != new_password2:
        print("Podane hasła nie zgadzaja się")
        menu()

    mysql_helper_logowany_leszek.change_password(email, password, new_password1)
    print("Zmieniono hasło na " + new_password1)
    menu()

def delete_user():
    pass
def exit():
    pass

def menu():
    print("""
=============MENU=================
1. Logowanie
2. Rejestracja
3. Lista użytkowników
4. Zmien haslo
5. Usun konto 
6. Wyjscie


""")

    choise = int(input())

    if choise == 1:
        login()
    elif choise == 2:
        register()
    elif choise == 3:
        list_of_users()
    elif choise == 4:
        change_password()
    elif choise == 5:
        delete_user()
    elif choise == 6:
        exit()

menu()
