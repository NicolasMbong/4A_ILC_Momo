from flask import Flask
import sys
import csv


app= Flask(__name__)
@app.route("/")

class Personne:
        _nom =""
        _solde =" "

        def __init__(self, nom,solde):
                self._nom = nom
                self._solde = solde

        def getNom(self):
                return self._nom

        def getSolde(self):
                return self._solde

        def setSolde(self,montant):
                self._solde= self._solde + montant
                return


def addCompte(liste, Nom, solde):
    for i in range(len(liste)):
        if (liste[i].getNom()==Nom):
            print("Un client avec les meme nom est deja dans la banque")
    client=Personne(Nom,solde)
    liste.append(client)
    print("le client a été ajouté a la banque")
                        
                    
def checktransaction(P1,transac):
    if (P1.getSolde() < transac) :
        return False
    return True


def addTransaction(P1,P2,t,transfert):        
    T=[P1,P2,t,transfert]
    if (checktransaction(P1, transfert) == True) : 
        print("La transaction d'un montant de:", transfert, "entre ", P1.getNom(), " et ", P2.getNom(), "à été effectué")
        P1.setSolde(transfert)
        P2.setSolde(-transfert)
    else  :
        print(P1, "ne peut pas transferer", transfert, "car son solde est trop faible")


def afficherTransactions(listClient):
    for i in range(len(listClient)):
        print(listClient[i])


def trie(L):
    return sorted(L, key=lambda L: L[2])


def afficherClient(M):
    for i in range(len(M)):
        print(M[i].getNom())
    return


Personnes=[]

addCompte(Personnes,"Max", 10)
addCompte(Personnes,"Benjamin",1000)
addCompte(Personnes,"Baptiste",0)
afficherClient(Personnes)

addTransaction(Personnes[1],Personnes[0],8,100)



if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)
