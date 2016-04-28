from perceptron import mlp

class test_mlp:

    def test_net_object(self):
        """
        Test: Net object
        """
        n = mlp.Net()
        assert n != None

    def test_net_constructor(self):
        """
        Test: Net constructor
        """
        n = mlp.Net()
        assert n.trainer != None

    def test_net_train(self):
        """
        Test: Train
        """
        n = mlp.Net()
        n.train([101,103],[201,202,203],201)
        rowin = [(101, 1, 0.516117),(103, 1, 0.516117)]
        rowout = [(1, 201, 0.449819),(1, 202, 0.071222),(1, 203, 0.071222)]
        for i, row in enumerate(n.trainer.utils.db.con.execute('select * from inputs')): assert row == rowin[i]
        for i, row in enumerate(n.trainer.utils.db.con.execute('select * from outputs')): assert row == rowout[i]

    def test_net_eval(self):
        """
        Test: Eval
        """
        n = mlp.Net()
        n.train([101,103],[201,202,203],201)
        print n.eval([101,103],[201,202,203])
        assert n.eval([101,103],[201,202,203]) == [0.33506324671253307, 0.055127057492087995, 0.055127057492087995]
