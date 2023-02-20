import sys
import os 

sys.path.append('..')

from dbutility import DBUtility


def test_dbUtility():

    tmpdb = "./temporary.db"
    if os.path.exists(tmpdb):
        os.remove(tmpdb)
    
    db = DBUtility(dbpath = tmpdb)
    db.createtables()
    db.insertoptresult("CCGA", "Ackley", 20, 0.001)
    db.closedb()

    db = DBUtility(dbpath = tmpdb)
    db.createtables()
    rows = db.getcursor().execute("select * from Simulations")
    for row in rows:
        assert row[0] == "CCGA"
        assert row[1] == "Ackley"
        assert row[2] == 20
        assert row[3] == 0.001
    
    os.remove(tmpdb)    


