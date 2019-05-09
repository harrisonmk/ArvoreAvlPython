class No(object):

    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.pai = None
        self.chave = chave
        self.balanceamento = 0
        self.altura = 0

    def getEsquerda(self):
        return self.esquerda

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def getDireita(self):
        return self.direita

    def setDireita(self, direita):
        self.direita = direita

    def getPai(self):
        return self.pai

    def setPai(self, pai):
        self.pai = pai

    def getChave(self):
        return self.chave

    def setChave(self, chave):
        self.chave = chave

    def getBalanceamento(self):
        return self.balanceamento

    def setBalanceamento(self, balanceamento):
        self.balanceamento = balanceamento

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def __str__(self):
       return ("%d, "%(self.chave))