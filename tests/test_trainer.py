from perceptron.lib import trainer

class test_trainer:

    def test_trainer_object(self):
        """
        Test: Trainer object
        """
        t = trainer.Trainer()
        assert t != None

    def test_trainer_constructor(self):
        """
        Test: Trainer constructor
        """
        t = trainer.Trainer()
        assert t.utils != None

    def test_trainer_feedforward(self):
        """
        Test: Feedforward
        """
        t = trainer.Trainer()
        t.train([101,103],[201,202,203],201)
        print t.feedforward()
        assert t.feedforward() == [0.33506294978429246, 0.05512695704100274, 0.05512695704100274]

    def test_trainer_backpropagate(self):
        """
        Test: Backpropagate
        """
        t = trainer.Trainer()
        t.train([101,103],[201,202,203],201)
        targets=[0.0]*len([201,202,203])
        targets[[201,202,203].index(201)] = 1.0
        rowin = [(101, 1, 0.516117),(103, 1, 0.516117)]
        rowout = [(1, 201, 0.449819),(1, 202, 0.071222),(1, 203, 0.071222)]
        for i, row in enumerate(t.utils.db.con.execute('select * from inputs')): assert row == rowin[i]
        for i, row in enumerate(t.utils.db.con.execute('select * from outputs')): assert row == rowout[i]

    def test_trainer_train(self):
        """
        Test: Train
        """
        t = trainer.Trainer()
        t.train([101,103],[201,202,203],201)
        rowin = [(101, 1, 0.516117),(103, 1, 0.516117)]
        rowout = [(1, 201, 0.449819),(1, 202, 0.071222),(1, 203, 0.071222)]
        for i, row in enumerate(t.utils.db.con.execute('select * from inputs')): assert row == rowin[i]
        for i, row in enumerate(t.utils.db.con.execute('select * from outputs')): assert row == rowout[i]
