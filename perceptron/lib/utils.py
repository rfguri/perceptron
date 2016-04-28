import db

class Utils():
    def __init__(self,mode='',dbname='nn.db'):
        self.db = db.Database(mode,dbname)

    def dtanh(self, y):
        return 1.0-y*y

    def getstrength(self,fromid,toid,layer):
        if layer==0: table='inputs'
        else: table='outputs'
        res=self.db.con.execute('select strength from %s where fromid=%d and toid=%d' % (table,fromid,toid)).fetchone()
        if res==None:
            if layer==0: return -0.2
            if layer==1: return 0
        return res[0]

    def setstrength(self,fromid,toid,layer,strength):
        if layer==0: table='inputs'
        else: table='outputs'
        res=self.db.con.execute('select rowid from %s where fromid=%d and toid=%d' % (table,fromid,toid)).fetchone()
        if res==None:
            self.db.con.execute('insert into %s (fromid,toid,strength) values (%d,%d,%f)' % (table,fromid,toid,strength))
        else:
            rowid=res[0]
            self.db.con.execute('update %s set strength=%f where rowid=%d' % (table,strength,rowid))

    def generatesynapses(self,inputs,urls):
        if len(inputs)>3: return None
        # Check if a node is already created for this set
        key='_'.join(sorted([str(wi) for wi in inputs]))
        res=self.db.con.execute("select rowid from hiddens where key='%s'" % key).fetchone()
        # If not, create it
        if res==None:
            cur=self.db.con.execute("insert into hiddens (key) values ('%s')" % key)
            hiddenid=cur.lastrowid
            # Put in some default weights
            for input in inputs:
                self.setstrength(input,hiddenid,0,1.0/len(inputs))
            for output in urls:
                self.setstrength(hiddenid,output,1,0.1)
            self.db.con.commit()

    def getsynapses(self,inputs,outputs):
        l1={}
        for input in inputs:
            cur=self.db.con.execute('select toid from inputs where fromid=%d' % input)
            for row in cur: l1[row[0]]=1
        for output in outputs:
            cur=self.db.con.execute('select fromid from outputs where toid=%d' % output)
            for row in cur: l1[row[0]]=1
        return l1.keys()

    def setupnetwork(self,inputs,outputs):
        # unit lists
        self.iu=inputs
        self.hu=self.getsynapses(inputs,outputs)
        self.ou=outputs
        # synapse values
        self.ai = [1.0]*len(self.iu)
        self.ah = [1.0]*len(self.hu)
        self.ao = [1.0]*len(self.ou)
        # weights matrix
        self.wi = [[self.getstrength(input,hiddenid,0) for hiddenid in self.hu] for input in self.iu]
        self.wo = [[self.getstrength(hiddenid,output,1) for output in self.ou] for hiddenid in self.hu]

    def updatedatabase(self):
        for i in range(len(self.iu)):
            for j in range(len(self.hu)):
                self.setstrength(self.iu[i],self.hu[j],0,self.wi[i][j])
        for j in range(len(self.hu)):
            for k in range(len(self.ou)):
                self.setstrength(self.hu[j],self.ou[k],1,self.wo[j][k])
                self.db.con.commit()
