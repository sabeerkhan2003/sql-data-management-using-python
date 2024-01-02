from tabulate import tabulate
import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root', password='Sabeer@20', database='sk3')
if conn:
    print("connection successful")
else:
    print("connection error")


def insert(ID, name, age, place, ):
    res = conn.cursor()
    sql = "insert into student(ID,name,age,place)values(%s,%s,%s,%s)"
    user = (ID, name, age, place)
    res.execute(sql, user)
    conn.commit()
    print("Data inseted successfully")


def UPDATE(ID, name, age, place, ):
    res = conn.cursor()
    sql = "UPDATE student SET name=%s,age=%s,place=%s where ID=%s"
    user = (name,age,place,ID)
    res.execute(sql,user)
    conn.commit()
    print("Data updated successfully")


def SELECT():
    res = conn.cursor()
    sql = "SELECT ID, name, age, place FROM student"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "name", "age", "place"]))



def DELETE(ID):
    res = conn.cursor()
    sql = "DELETE FROM student where ID=%s"
    user = (ID,)
    res.execute(sql, user)
    conn.commit()
    print("Data deleted successfully")


while True:
    print("1.Insert data")
    print("2.Update data")
    print("3.Select data")
    print("4.Delete data")
    print("5.Exit")
    choice = int(input("select your choice :"))
    if choice == 1:
        ID = int(input("enter a ID:"))
        name = input("Enter a name:")
        age = int(input("Enter a age:"))
        place = input("enter the place:")
        insert(ID, name, age, place)

    elif choice == 2:
        ID = int(input("enter a ID:"))
        name = input("Enter a name:")
        age = int(input("Enter a age:"))
        place = input("enter the place:")
        UPDATE(ID,name,age,place)

    elif choice == 3:
        SELECT()

    elif choice == 4:
        ID = int(input("enter ID to delete:"))
        DELETE(ID)

    elif choice >= 5 :
        exit()
