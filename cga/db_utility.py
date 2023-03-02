import sqlite3


class DBUtility:

    _conn_: sqlite3.Connection = None

    def __init__(self, dbpath="./simulations.db"):
        self._conn_ = sqlite3.connect(database=dbpath)

    def getconnection(self) -> sqlite3.Connection:
        return self._conn_

    def getcursor(self) -> sqlite3.Cursor:
        return self._conn_.cursor()

    def commit(self) -> None:
        self._conn_.commit()

    def createtables(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS Simulations 
            (method text, testf text, p int, optimum float)
        """
        self.getcursor().execute(sql)
        self.commit()

    def insertoptresult(self, method: str, f: str, p: int, optimum: float):
        sql = """
            INSERT INTO Simulations 
            (method, testf, p, optimum)
            VALUES 
            ('{}', '{}', {}, {})
        """.format(method, f, p, optimum)
        self.getcursor().execute(sql)
        self.commit()

    def closedb(self) -> None:
        self._conn_.close()

# Sample use
# db = DBUtility()
# db.createtables()
# db.insertoptresult("CCGA", "Ackley", 10, 0.032)
# db.insertoptresult("CCGA", "Ackley", 10, 0.0198)
# db.closedb()
