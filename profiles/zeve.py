class zeve:
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

    def getacc():
        accscore = 0
        if len(outbuff) == 0:
            accuracy = 100
            return accuracy
        else:
            for i in range(0, len(outbuff)):
                if i > len(outbuff) or i > len(origorder):
                    break
                else:
                    if outbuff[i] == origorder[i]:
                        accscore += 1
                    else:
                        pass
        accuracy = accscore / len(origorder) * 100
        return accuracy
