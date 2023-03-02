from db_utility import DBUtility
import os


def test_db_utility():

    tmpdb = "./temporary.db"
    if os.path.exists(tmpdb):
        os.remove(tmpdb)

    db = DBUtility(dbpath=tmpdb)
    db.createtables()
    db.insertoptresult("CCGA", "Ackley", 20, 0.001)

    db = DBUtility(dbpath=tmpdb)
    db.createtables()
    rows = db.getcursor().execute("select * from Simulations")
    for row in rows:
        assert row[0] == "CCGA"
        assert row[1] == "Ackley"
        assert row[2] == 20
        assert row[3] == 0.001

    db.closedb()

    # os.remove(tmpdb)
