from cga.db_utility import DBUtility
import os


def test_db_utility():

    tmpdb = "./temporary.db"
    if os.path.exists(tmpdb):
        os.remove(tmpdb)

    db = DBUtility(dbpath=tmpdb)
    db.createtables()
    db.insertoptresult("CCGA", "Binary", "Ackley", 0, 25, 1.14, "tournament", "onepoint", "swap", "c9", 5, 5, 100, 0.9, 0.3)

    db = DBUtility(dbpath=tmpdb)
    db.createtables()
    rows = db.getcursor().execute("select * from ExperimentResults")
    for row in rows:
        assert row[0] == "CCGA"
        assert row[1] == "Binary"
        assert row[2] == "Ackley"
        assert row[3] == 0
        assert row[4] == 25
        assert row[5] == 1.14
        assert row[6] == "tournament"
        assert row[7] == "onepoint"
        assert row[8] == "swap"
        assert row[9] == "c9"
        assert row[10] == 5
        assert row[11] == 5
        assert row[12] == 100
        assert row[13] == 0.9
        assert row[14] == 0.3

    db.closedb()

    os.remove(tmpdb)
