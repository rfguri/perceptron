import utils, math

class Trainer():
    def __init__(self,mode='',dbname='nn.db'):
        self.utils = utils.Utils(mode,dbname)

    def feedforward(self):
        for i in range(len(self.utils.iu)):
            self.utils.ai[i] = 1.0
        # hidden activations
        for j in range(len(self.utils.hu)):
            sum = 0.0
            for i in range(len(self.utils.iu)):
                sum = sum + self.utils.ai[i] * self.utils.wi[i][j]
            self.utils.ah[j] = math.tanh(sum)
        # output activations
        for k in range(len(self.utils.ou)):
            sum = 0.0
            for j in range(len(self.utils.hu)):
                sum = sum + self.utils.ah[j] * self.utils.wo[j][k]
            self.utils.ao[k] = math.tanh(sum)
        return self.utils.ao[:]

    def backpropagate(self, targets, N=0.5):
        # calculate errors for output layer
        odeltas = [0.0] * len(self.utils.ou)
        for k in range(len(self.utils.ou)):
            error = targets[k]-self.utils.ao[k]
            odeltas[k] = self.utils.dtanh(self.utils.ao[k]) * error
        # calculate errors for hidden layer
        hdeltas = [0.0] * len(self.utils.hu)
        for j in range(len(self.utils.hu)):
            error = 0.0
            for k in range(len(self.utils.ou)):
                error = error + odeltas[k]*self.utils.wo[j][k]
            hdeltas[j] = self.utils.dtanh(self.utils.ah[j]) * error
        # update output weights
        for j in range(len(self.utils.hu)):
            for k in range(len(self.utils.ou)):
                change = odeltas[k]*self.utils.ah[j]
                self.utils.wo[j][k] = self.utils.wo[j][k] + N*change
        # update input weights
        for i in range(len(self.utils.iu)):
            for j in range(len(self.utils.hu)):
                change = hdeltas[j]*self.utils.ai[i]
                self.utils.wi[i][j] = self.utils.wi[i][j] + N*change

    def train(self,inputs,outputs,label):
        self.utils.generatesynapses(inputs,outputs)
        self.utils.setupnetwork(inputs,outputs)
        self.feedforward()
        targets=[0.0]*len(outputs)
        targets[outputs.index(label)]=1.0
        error = self.backpropagate(targets)
        self.utils.updatedatabase()
