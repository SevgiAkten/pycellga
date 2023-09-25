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
        # sql = """
        #     CREATE TABLE IF NOT EXISTS Simulations
        #     (method text, testf text, p int, optimum float)
        # """
        sql2 = """
            CREATE TABLE IF NOT EXISTS ExperimentResults
            (
            Method TEXT,
            Gen_Type TEXT,
            TestFunction TEXT,
            Best_Solution FLOAT,
            Found_at_Generation NUMERIC,
            Time FLOAT,
            Selection TEXT,
            Recombination TEXT,
            Mutation TEXT,
            Neighborhood TEXT,
            Number_of_Columns INTEGER,
            Number_of_Rows INTEGER,
            Number_of_Generation INTEGER,
            Probability_of_Crossover NUMERIC,
            Probability_of_Mutation NUMERIC
            )
        """
        self.getcursor().execute(sql2)
        self.commit()

    def insertoptresult(self, method: str, gen_type: str, test_function: str, best_solution: float, found_at_generation: int, time: float, selection: str, recombination: str, mutation: str, neighborhood: str, n_cols: int, n_rows: int, n_gen: int, p_cross: float, p_mut: float):
        # sql = """
        #     INSERT INTO Simulations
        #     (method, testf, p, optimum)
        #     VALUES
        #     ('{}', '{}', {}, {})
        # """.format(method, f, p, optimum)

        sql2 = """
            INSERT INTO ExperimentResults VALUES ('{}','{}','{}',{},{},{},'{}','{}','{}','{}','{}',{},{},{},{})
        """.format(method, gen_type, test_function, best_solution, found_at_generation, time, selection, recombination, mutation, neighborhood, n_cols, n_rows, n_gen, p_cross, p_mut)

        self.getcursor().execute(sql2)
        self.commit()

    def closedb(self) -> None:
        self._conn_.close()

# Sample use
# db = DBUtility()
# db.createtables()
# db.insertoptresult("CCGA", "Ackley", 10, 0.032)
# db.insertoptresult("CCGA", "Ackley", 10, 0.0198)
# db.closedb()
