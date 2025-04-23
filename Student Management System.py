import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll No")
    print("4. Update Fees Status")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        fees = input("Fees Paid (Yes/No): ")
        sql = "INSERT INTO student (rollno, name, fees) VALUES (%s, %s, %s)"
        val = (roll, name, fees)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Student Added Successfully")

    elif ch == 2:
        mycursor.execute("SELECT * FROM student")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    elif ch == 3:
        roll = int(input("Enter Roll No to Search: "))
        sql = "SELECT * FROM student WHERE rollno = %s"
        val = (roll,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            print("Roll No:", result[0])
            print("Name:", result[1])
            print("Fees Paid:", result[2])
        else:
            print("Student Not Found")

    elif ch == 4:
        roll = int(input("Enter Roll No to Update Fees: "))
        fees = input("Enter Fees Status (Yes/No): ")
        sql = "UPDATE student SET fees = %s WHERE rollno = %s"
        val = (fees, roll)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Fees Status Updated")

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
