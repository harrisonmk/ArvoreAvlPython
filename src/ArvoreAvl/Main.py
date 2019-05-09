from No import No
from ArvoreAvl import ArvoreAvl



arvore = ArvoreAvl()

arvore.inserir(20)
arvore.inserir(15)
arvore.inserir(8)
arvore.inserir(12)
arvore.inserir(6)
arvore.inserir(1)
arvore.inserir(4)



print("\nPercurso em pre ordem")
arvore.preOrdem(arvore.raiz)
print("\n")

print("Percurso em ordem")
arvore.emOrdem(arvore.raiz)

print("\n")
print("Percurso em pos ordem")
arvore.posOrdem(arvore.raiz)


arvore.remover(12)

print("\n******************************************")
print ("Remoção do elemento 12 da arvore")

print("\nPercurso em pre ordem")
arvore.preOrdem(arvore.raiz)
print("\n")

print("Percurso em ordem")
arvore.emOrdem(arvore.raiz)

print("\n")
print("Percurso em pos ordem")
arvore.posOrdem(arvore.raiz)
print("\n")