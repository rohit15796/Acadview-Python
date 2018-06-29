import sqlite3
class Data:
    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstorestore (id INTEGER PRIMARY KEY, title TEXT, "
                    "author TEXT, year INTEGER, isbn INTEGER)")
        self.connection.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO bookstore VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
        self.connection.commit()


    def view(self):
        self.cur.execute("SELECT * FROM bookstore")
        rows = self.cur.fetchall()

        return rows

    def search(self,isbn=""):
        self.cur.execute("SELECT * FROM bookstore WHERE isbn=?",(isbn,))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM bookstore WHERE id = ?", (id,))
        self.connection.commit()

    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE bookstore SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
