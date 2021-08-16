import sqlite3

class Database:
    def __init__(self, db):
        try:
            self.con = sqlite3.connect(db)
            self.c = self.con.cursor()
            self.c.execute("""
                CREATE TABLE IF NOT EXISTS datas(
                    pid INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    address TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    mail TEXT NOT NULL 
                    )
                """)
            self.con.commit()
            print("Table Created Successfully")
        except Exception as e:
            print("Error:", e)

    def insert_record(self):
        name = input("Enter Your Name:")
        age = input("Enter Your Age:")
        gender = input("Enter Your Gender:")
        address = input("Enter Your Address:")
        contact = input("Enter Your Contact:")
        mail = input("Enter Your Mail:")
        sql = """
                INSERT INTO datas VALUES(NULL,?,?,?,?,?,?)
            """
        self.c.execute(sql, (name, age, gender, address, contact, mail))
        self.con.commit()
        print("Record Added Successfully")

    def fetch_record(self):
        self.c.execute("SELECT * FROM datas")
        data = self.c.fetchall()
        print("\n")
        print("List of Records")
        print("---------------")
        for datas in data:
            print(datas)

    def update_record(self):
        print("1.Name")
        print("2.Age")
        print("3.Gender")
        print("4.Address")
        print("5.Contact")
        print("6.Mail")
        option = int(input("\nWhich field you want to update?:"))
        if option == 1:
            pid = input("Enter Your ID:")
            name = input("Enter Your Name:")
            sql = """ UPDATE datas set name=? where pid=?"""
            self.c.execute(sql, (name, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 2:
            pid = input("Enter Your ID:")
            age = input("Enter Your Age:")
            sql = """ UPDATE datas set age=? where pid=?"""
            self.c.execute(sql, (age, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 3:
            pid = input("Enter Your ID:")
            gender = input("Enter Your Gender:")
            sql = """ UPDATE datas set gender=? where pid=?"""
            self.c.execute(sql, (gender, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 4:
            pid = input("Enter Your ID:")
            address = input("Enter Your Address:")
            sql = """ UPDATE datas set address=? where pid=?"""
            self.c.execute(sql, (address, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 5:
            pid = input("Enter Your ID:")
            contact = input("Enter Your Contact:")
            sql = """ UPDATE datas set contact=? where pid=?"""
            self.c.execute(sql, (contact, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 6:
            pid = input("Enter Your ID:")
            mail = input("Enter Your Mail:")
            sql = """ UPDATE datas set mail=? where pid=?"""
            self.c.execute(sql, (mail, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        else:
            print("Invalid")

    def remove_record(self):
        pid = input("Enter Your ID:")
        sql = "DELETE FROM datas WHERE pid=?"
        self.c.execute(sql, (pid,))
        self.con.commit()
        obj.fetch_record()
        print("\n")
        print("Record Deleted Successfully")


obj=Database("Sqlitedatabase.db")

while True:
    print("\n")
    print("1)Insert Record")
    print("2)Fetch Record")
    print("3)Update Record")
    print("4)Delete Record")

    print("\n")

    option = int(input("Please Enter Your Operation:"))

    if option == 1:
        obj.insert_record()
    elif option == 2:
        obj.fetch_record()
    elif option == 3:
        obj.update_record()
    elif option == 4:
        obj.remove_record()
    else:
        quit()
