from No import No


class ArvoreAvl(object):

    def __init__(self):
        self.raiz = None

    def getRaiz(self):
        return self.raiz

    def inserir(self, k):
        n = No(k)
        self.inserirAVL(self.raiz, n)

    def inserirAVL(self, aComparar, aInserir):

        if aComparar == None:
            self.raiz = aInserir
        else:
            if aInserir.getChave() < aComparar.getChave():
                if aComparar.getEsquerda() == None:
                    aComparar.setEsquerda(aInserir)
                    aInserir.setPai(aComparar)
                    self.verificarBalanceamento(aComparar)
                else:
                    self.inserirAVL(aComparar.getEsquerda(), aInserir)

            elif (aInserir.getChave() > aComparar.getChave()):
                if aComparar.getDireita() == None:
                    aComparar.setDireita(aInserir)
                    aInserir.setPai(aComparar)
                    self.verificarBalanceamento(aComparar)
                else:
                    inserirAVL(aComparar.getDireita(), aInserir)
            else:
                None

    def verificarBalanceamento(self, atual):
        self.setBalanceamento(atual)
        balanceamento = atual.getBalanceamento()
        if balanceamento == -2:
            if self.altura(atual.getEsquerda().getEsquerda()) >= self.altura(atual.getEsquerda().getDireita()):
                atual = self.rotacaoDireita(atual)
            else:
                atual = self.duplaRotacaoEsquerdaDireita(atual)
        elif balanceamento == 2:
            if altura(atual.getDireita().getDireita()) >= altura(atual.getDireita().getEsquerda()):
                atual = rotacaoEsquerda(atual)
            else:
                atual = duplaRotacaoDireitaEsquerda(atual)
        if atual.getPai() != None:
            self.verificarBalanceamento(atual.getPai())
        else:
            self.raiz = atual

    def rotacaoEsquerda(self, inicial):

        direita = inicial.getDireita()
        direita.setPai(inicial.getPai())

        inicial.setDireita(direita.getEsquerda())

        if inicial.getDireita() != None:
            inicial.getDireita().setPai(inicial)

        direita.setEsquerda(inicial)
        inicial.setPai(direita)

        if direita.getPai() != None:

            if direita.getPai().getDireita() == inicial:
                direita.getPai().setDireita(direita)

            elif direita.getPai().getEsquerda() == inicial:
                direita.getPai().setEsquerda(direita)

        self.setBalanceamento(inicial)
        self.setBalanceamento(direita)

        return direita

    def rotacaoDireita(self, inicial):

        esquerda = inicial.getEsquerda()
        esquerda.setPai(inicial.getPai())

        inicial.setEsquerda(esquerda.getDireita())

        if inicial.getEsquerda() != None:
            inicial.getEsquerda().setPai(inicial)

        esquerda.setDireita(inicial)
        inicial.setPai(esquerda)

        if esquerda.getPai() is not None:

            if esquerda.getPai().getDireita() == inicial:
                esquerda.getPai().setDireita(esquerda)

            elif esquerda.getPai().getEsquerda() == inicial:
                esquerda.getPai().setEsquerda(esquerda)

        self.setBalanceamento(inicial)
        self.setBalanceamento(esquerda)

        return esquerda

    def duplaRotacaoEsquerdaDireita(self, inicial):
        inicial.setEsquerda(self.rotacaoEsquerda(inicial.getEsquerda()))
        return self.rotacaoDireita(inicial)

    def duplaRotacaoDireitaEsquerda(self, inicial):
        inicial.setDireita(rotacaoDireita(inicial.getDireita()))
        return rotacaoEsquerda(inicial)

    def sucessor(self, q):

        if q.getDireita() != None:
            r = q.getDireita()
            while r.getEsquerda() != None:
                r = r.getEsquerda()
            return r
        else:
            p = q.getPai()

            while p != None and q == p.getDireita():
                q = p;
                p = q.getPai()

            return p

    def setBalanceamento(self, no):
        no.setBalanceamento(self.altura(no.getDireita()) - self.altura(no.getEsquerda()))

    def altura(self, r):
        if r != None:
            AlturaE = self.altura(r.esquerda)
            AlturaD = self.altura(r.direita)
            if AlturaE > AlturaD:
                return AlturaE + 1
            else:
                return AlturaD + 1

        else:
            return 0

    def remover(self, k):
        self.removerAVL(self.raiz, k)

    def removerAVL(self, atual, k):
        if (atual == None):
            return

        else:

            if (atual.getChave() > k):
                self.removerAVL(atual.getEsquerda(), k)

            elif (atual.getChave() < k):
                self.removerAVL(atual.getDireita(), k)

            elif (atual.getChave() == k):
                self.removerNoEncontrado(atual)

    def removerNoEncontrado(self, aRemover):

        r = No

        if (aRemover.getEsquerda() == None or aRemover.getDireita() == None):

            if aRemover.getPai() == None:
               this.raiz = None
               aRemover = None
               return

            r = aRemover

        else:
             r = self.sucessor(aRemover)
             aRemover.setChave(r.getChave())

        p = No
        if r.getEsquerda() != None:
           p = r.getEsquerda()
        else:
            p = r.getDireita()

        if p != None:
           p.setPai(r.getPai())

        if r.getPai() == None:
          this.raiz = p;
        else:
           if r == r.getPai().getEsquerda():
            r.getPai().setEsquerda(p)
           else:
              r.getPai().setDireita(p)

              self.verificarBalanceamento(r.getPai())

        r = None

    def preOrdem(self, no):
        if no is not None:
            print(no.getChave(), " ",end="")
            self.preOrdem(no.getEsquerda())
            self.preOrdem(no.getDireita())

    def emOrdem(self, no):
        if no is not None:
            self.emOrdem(no.getEsquerda())
            print(no.getChave(), " ",end="")
            self.emOrdem(no.getDireita())

    def posOrdem(self, no):
        if no is not None:
            self.posOrdem(no.getEsquerda())
            self.posOrdem(no.getDireita())
            print(no.getChave(), " ",end="")
