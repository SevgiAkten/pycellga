import sqlite3

class DBUtility:
    """
    A utility class for handling SQLite database operations.

    Attributes
    ----------
    _conn_ : sqlite3.Connection
        SQLite connection object.
    """

    _conn_: sqlite3.Connection = None

    def __init__(self, dbpath="./simulations.db"):
        """
        Initialize the database connection.

        Parameters
        ----------
        dbpath : str, optional
            The path to the SQLite database file. Default is "./simulations.db".
        """
        self._conn_ = sqlite3.connect(database=dbpath)

    def getconnection(self) -> sqlite3.Connection:
        """
        Get the SQLite connection object.

        Returns
        -------
        sqlite3.Connection
            The SQLite connection object.
        """
        return self._conn_

    def getcursor(self) -> sqlite3.Cursor:
        """
        Get a cursor object for executing SQL queries.

        Returns
        -------
        sqlite3.Cursor
            The SQLite cursor object.
        """
        return self._conn_.cursor()

    def commit(self) -> None:
        """
        Commit any pending transactions to the database.
        """
        self._conn_.commit()

    def createtables(self) -> None:
        """
        Create the 'ExperimentResults' table if it does not already exist.
        """
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
        """
        Insert optimization results into the 'ExperimentResults' table.

        Parameters
        ----------
        method : str
            The method used for the experiment.
        gen_type : str
            The type of generation used.
        test_function : str
            The test function used in the experiment.
        best_solution : float
            The best solution found.
        found_at_generation : int
            The generation at which the best solution was found.
        time : float
            The time taken for the experiment.
        selection : str
            The selection method used.
        recombination : str
            The recombination method used.
        mutation : str
            The mutation method used.
        neighborhood : str
            The neighborhood type used.
        n_cols : int
            The number of columns in the experimental setup.
        n_rows : int
            The number of rows in the experimental setup.
        n_gen : int
            The number of generations run.
        p_cross : float
            The probability of crossover.
        p_mut : float
            The probability of mutation.
        """
        sql2 = """
            INSERT INTO ExperimentResults VALUES ('{}','{}','{}',{},{},{},'{}','{}','{}','{}',{},{},{},{},{})
        """.format(method, gen_type, test_function, best_solution, found_at_generation, time, selection, recombination, mutation, neighborhood, n_cols, n_rows, n_gen, p_cross, p_mut)

        self.getcursor().execute(sql2)
        self.commit()

    def closedb(self) -> None:
        """
        Close the SQLite database connection.
        """
        self._conn_.close()