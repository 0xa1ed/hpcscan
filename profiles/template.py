class template:
    def __init__(self):
        self.procstart = []
        self.procterm = []
        self.regset = []
        self.regdel = []
        self.filewrite = []
        self.filedel = []
        self.score = 0
        self.accuracy = 0
        self.origorder = []
        self.outbuff = []

    def getacc(self):
        accscore = 0.0
        if not self.outbuff or not self.origorder:
            return 0 
        else:
           # print self.outbuff[0]
            for i in range(0, len(self.outbuff)):
                if i < len(self.origorder):
                    if self.origorder[i] != self.outbuff[i]:
                        self.outbuff.insert(i, "0")
            for i in range(0, len(self.outbuff)):
                if i < len(self.origorder):
                    #print "comparing " + self.outbuff[i] + " and " + self.origorder[i]
                    if self.outbuff[i] == self.origorder[i]:
                    #    print "match"
                        accscore += 1
                    else:
                        pass
                else:
                    break
        if accscore == 0:
            return 0
        else:
            self.accuracy = accscore / len(self.origorder) * 100
            #print self.accuracy
        return self.accuracy
