import mysql.connector


def create_user(email, name, surname, password, age, phoneNO, gender):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="haslo",
        database="test2"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO user (email, name, surname, password, age, phone_no, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (email, name, surname, password, str(age), phoneNO, gender)
    mycursor.execute(sql, values)
    mydb.commit()


def login(email, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="haslo",
        database="test2"
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM user where email like %s and password like %s"
    values = (email, password)
    mycursor.execute(sql, values)

    return mycursor.fetchall()

def list_of_users():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="haslo",
        database="test2"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    return myresult

def change_password(email, password, new_password1):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="haslo",
        database="test2"
    )

    mycursor = mydb.cursor()
    sql = "UPDATE user SET password = %s where email = %s and password = %s"
    values = (new_password1, email, password)
    mycursor.execute(sql, values)
    mydb.commit()
