from perceptron.lib import db

class test_db:

    def test_db_object(self):
        """
        Test: Database object
        """
        d = db.Database()
        assert d != None

    def test_db_constructor(self):
        """
        Test: Database constructor
        """
        d = db.Database()
        assert d.con != None

    def test_db_maketables(self):
        """
        Test: Make tables
        """
        d = db.Database()
        d.maketables()
        resi=d.con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inputs'").lastrowid
        resh=d.con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='hiddens'").lastrowid
        reso=d.con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='outputs'").lastrowid
        assert resi == None
        assert resh == None
        assert reso == None
