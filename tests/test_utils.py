from perceptron.lib import utils

class test_utils:

    def test_utils_object(self):
        """
        Test: Utils object
        """
        u = utils.Utils()
        assert u != None

    def test_utils_constructor(self):
        """
        Test: Utils constructor
        """
        u = utils.Utils()
        assert u.db != None

    def test_utils_dtanh(self):
        """
        Test: Double precision dtanh
        """
        u = utils.Utils()
        assert u.dtanh(1) == 0
        assert u.dtanh(2) == -3
        assert u.dtanh(3) == -8
        assert u.dtanh(4) == -15
        assert u.dtanh(5) == -24

    def test_utils_backpropagate(self):
        """
        Test: Get strength
        """
        u = utils.Utils()
        assert u.getstrength(101,1,0) == -0.2

    def test_utils_setstrength(self):
        """
        Test: Set strength
        """
        u = utils.Utils()
        u.setstrength(101,1,0,0.5)
        for i, row in enumerate(u.db.con.execute('select * from inputs')): assert row == (101,1,0.5)

    def test_utils_generatesynapses(self):
        """
        Test: Generate synapses
        """
        u = utils.Utils()
        u.generatesynapses([101,103],[201,202,203])
        rowin = [(101, 1, 0.5),(103, 1, 0.5)]
        rowout = [(1, 201, 0.1),(1, 202, 0.1),(1, 203, 0.1)]
        for i, row in enumerate(u.db.con.execute('select * from inputs')): assert row == rowin[i]
        for i, row in enumerate(u.db.con.execute('select * from outputs')): assert row == rowout[i]

    def test_utils_getallsynapses(self):
        """
        Test: Get all synapses
        """
        u = utils.Utils()
        u.generatesynapses([101,103],[201,202,203])
        assert u.getsynapses([101,103],[201,202,203]) == [1]

    def test_utils_setupnetwork(self):
        """
        Test: Setup network
        """
        u = utils.Utils()
        u.generatesynapses([101,103],[201,202,203])
        u.setupnetwork([101,103],[201,202,203])
        assert u.iu == [101,103]
        assert u.hu == [1]
        assert u.ou == [201,202,203]
        assert u.ai == [1.0,1.0]
        assert u.ah == [1.0]
        assert u.ao == [1.0, 1.0, 1.0]

    def test_utils_updatedatabase(self):
        """
        Test: Update dataset
        """
        u = utils.Utils()
        u.generatesynapses([101,103],[201,202,203])
        u.setupnetwork([101,103],[201,202,203])
        u.updatedatabase()
        rowin = [(101, 1, 0.5),(103, 1, 0.5)]
        rowout = [(1, 201, 0.1),(1, 202, 0.1),(1, 203, 0.1)]
        for i, row in enumerate(u.db.con.execute('select * from inputs')): assert row == rowin[i]
        for i, row in enumerate(u.db.con.execute('select * from outputs')): assert row == rowout[i]


