import sqlite3
import sys

version = "0.2.0"


class Application:
    def __init__(self):
        self.name = "Contacts App"
        self.is_running = True

        # Checks if db exists, if not create a new one
        self.db = sqlite3.connect("./data.db")
        self.cursor = self.db.cursor()

        is_table = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='CONTACTS'")
        valid = is_table.fetchone()

        # Table exists
        if valid[0] == 'CONTACTS':
            self.main()
        # Create table
        else:
            self.is_running = True
            self.main()

    def main(self):
        print(f"Welcome to CONTACTS App v{version}")
        while self.is_running:
            print()
            print(
                "What operation would you like to perform: Display contacts (1), add a new one (2), remove one (3),"
                " or update a existing contact (4)?")
            try:
                option = int(input())
                if option == 1:
                    print()
                    self.display()
                elif option == 2:
                    print()
                    self.new()
                elif option == 3:
                    print()
                    self.delete()
                elif option == 4:
                    print()
                    self.update()
                elif option == 5:
                    print()
                    self.reset_db()
                else:
                    print()
                    print("You have selected an invalid option")
            except ValueError:
                print()
                print("Please introduce a valid option")

    def create_db(self):
        print("His")
        self.cursor.execute("CREATE TABLE CONTACTS ("
                            "ID     integer PRIMARY KEY autoincrement NOT NULL,"
                            "NAME   VARCHAR(30)                   NOT NULL,"
                            "AGE integer,"
                            "EMAIL CHAR(30),"
                            "NUMBER integer,"
                            "NOTES CHAR(50)"
                            ");"
                            )
        self.db.commit()

    def reset_db(self):
        self.db.execute("DROP TABLE CONTACTS")
        self.db.commit()
        db = self.cursor.execute("CREATE TABLE CONTACTS ("
                                 "ID     integer PRIMARY KEY autoincrement NOT NULL,"
                                 "NAME   VARCHAR(30)                   NOT NULL,"
                                 "AGE integer,"
                                 "EMAIL CHAR(30),"
                                 "NUMBER integer,"
                                 "NOTES CHAR(50)"
                                 ");"
                                 )

        print("Database reset successfully")
        self.db.commit()

    def display(self):
        data = self.cursor.execute("SELECT * FROM CONTACTS").fetchall()
        if not data:
            print("There are no contacts. Try adding a new one")
        if data:
            print("{:<7} {:<30} {:<5} {:<30} {:<13} {:<50}".format('Id', 'Name', 'Age', 'Email', 'Number', 'Notes'))
            # Create a separation between header and contacts
            print("{:<7} {:<30} {:<5} {:<30} {:<13} {:<50}".format('-------', '------------------------------', '-----',
                                                                   '------------------------------',
                                                                   '-------------',
                                                                   '--------------------------------------------------')
                  )
            for x in data:
                id_, name, age, email, number, notes = x
                print("{:<7} {:<30} {:<5} {:<30} {:<13} {:<50}".format(id_, name, age, email, number, str(notes)))

    def new(self):
        print("You're creating a new contact \nInsert it's name")
        name = str(input()).title()
        print("How old is him/her?")
        age = str(input())
        print("Write his/her email address")
        email = str(input())
        print("Mobile number")
        number = int(input())
        print("Addition info?")
        notes = str(input())

        if notes.upper() == "" or "No":
            notes = None
            pass

        contact = self.cursor.execute(
            "INSERT INTO CONTACTS (NAME, AGE, EMAIL, NUMBER, NOTES) VALUES (?, ?, ?, ?, ?)",
            (name, age, email, number, notes))
        self.db.commit()

    def search(self, column, value) -> list:
        sql = "SELECT * FROM CONTACTS WHERE {} = '{}'".format(str(column), str(value))
        contact = self.cursor.execute(sql)
        return contact.fetchall()

    def delete(self):
        print("You're about to delete a contact")
        print("would you like to find it by name, email or phone number?")
        search = str(input())

        print(f"Introduce it's exact {search.lower()}:")
        value = str(input())

        if search.upper() == 'PHONE NUMBER':
            search = 'NUMBER'
            pass

        is_valid = self.search(search, value)
        if is_valid:
            # Delete the contact
            sql = "DELETE FROM CONTACTS WHERE {} = '{}'".format(search.upper(), value)
            contact = self.cursor.execute(sql)
            self.db.commit()
            print(f"Contact with {search.lower()} {value} deleted")
        else:
            print("Contact doesn't exist")

    def update(self):
        print("What contact would you like to update?")
        print("Introduce it's id")
        id_ = int(input())

        contact = self.search('ID', id_)
        if contact:
            # Printing contact name
            print("You're updating contact {}".format(contact[0][1]))
            print("What property would you like to update?")
            search = str(input())

            print("OKey, introduce it's new {}".format(search.lower()))
            value = str(input())

            sql = "UPDATE CONTACTS SET {} = '{}' WHERE ID = '{}'".format(search.upper(), value, id_)
            self.cursor.execute(sql)
            self.db.commit()
            print("Contact with id {} updated successfully".format(id_))
        else:
            print("You have introduced an invalid id")


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
