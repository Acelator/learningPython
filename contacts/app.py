import sqlite3
import sys

version = "0.1.0"


class Application:
    def __init__(self):
        self.name = "Contacts App"
        self.db = sqlite3.connect("data.db")
        self.cursor = self.db.cursor()
        self.is_running = True
        self.main()

    def main(self):
        print(f"Welcome to CONTACTS App v{version}")
        while self.is_running:
            print(
                "What operation would you like to perform: Display contacts (1), add a new one (2), or remove one (3)?")
            try:
                option = int(input())
                if option == 1:
                    self.display()
                elif option == 2:
                    self.new()
                elif option == 3:
                    self.delete()
            except ValueError:
                print("Please introduce a valid option")
                self.is_running = False
                sys.exit()

    # def new_db(self):
    #     db = self.cursor.execute("CREATE TABLE CONTACTS ("
    #                              "ID     integer PRIMARY KEY autoincrement NOT NULL,"
    #                              "NAME   VARCHAR(20)                   NOT NULL,"
    #                              "AGE integer,"
    #                              "EMAIL CHAR(30),"
    #                              "NUMBER integer,"
    #                              "NOTES CHAR(50)"
    #                              ");"
    #                              )
    #     self.db.commit()

    def display(self):
        data = self.cursor.execute("SELECT * FROM CONTACTS").fetchall()
        if not data:
            print("There are no contacts. Try adding a new one")
        if data:
            for x in data:
                print(x)

    def new(self):
        print("You're creating a new contact \nInsert it's name")
        name = str(input())
        print("How old is him/her?")
        age = str(input())
        print("Write his/her email address")
        email = str(input())
        print("Mobile number")
        number = int(input())
        print("Addition info?")
        notes = str(input())

        contact = self.cursor.execute(
            "INSERT INTO CONTACTS (NAME, AGE, EMAIL, NUMBER, NOTES) VALUES (?, ?, ?, ?, ?)",
            (name, age, email, number, notes))
        self.db.commit()

    # TODO: Check if contact to delete exists
    def delete(self):
        print("You're about to delete a contact")
        print("would you like to find it by name, email or phone number?")
        search = str(input())

        print(f"Introduce it's exact {search.lower()}:")
        value = str(input())

        if search.upper() == 'PHONE NUMBER':
            search = 'NUMBER'
            pass

        print(search)
        # Delete the contact
        sql = "DELETE FROM CONTACTS WHERE {} = '{}'".format(search.upper(), value)
        contact = self.cursor.execute(sql)
        self.db.commit()
        print(f"Contact with {search.lower()} {value} deleted")


if __name__ == '__main__':
    try:
        app = Application()
    except KeyboardInterrupt:
        print()
        try:
            sys.exit(0)
        except SystemExit:
            print("Bye!")
            sys.exit(0)
