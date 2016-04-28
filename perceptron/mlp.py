from lib import trainer

class Net:
    def __init__(self,mode='',dbname='nn.db'):
        self.trainer = trainer.Trainer(mode,dbname)

    def train(self,inputs,outputs,label):
        self.trainer.train(inputs,outputs,label)

    def eval(self,inputs,outputs):
        self.trainer.utils.setupnetwork(inputs,outputs)
        return self.trainer.feedforward()
