from flask import Flask
import sys

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

        def modifSolde(self,montant):
                self._solde-=montant
                return

bidule=Personne("Max",10)
Personnes=[]
Personnes.append(bidule)

def AddCompte(Nom,solde):
        for i in range(len(Personnes)):
                if (Personnes[i].getNom()==Nom):
                        print("marche pô")
                        return
                else:

                        truc=Personne(Nom,solde)
                        Personnes.append(truc)
                        return


def AddTransaction(P1,P2,t,s):
        T=[P1,P2,t,s]
        print("La transaction d'un montant de:", s, "entre ", P1.getNom(), " et ", P2.getNom(), "à été effectué")
        Personnes.append(P1)

        return ;

def AfficherTransactions(T):
        for i in range(len(T)):
                print(T[i])
        return

def Trie(L):
        return sorted(L, key=lambda L: L[2])

def AfficherListe(M):
        for i in range(len(M)-1):
                print(M[i].getNom())
        return


AddCompte("Benjamin",1000)
AddCompte("Baptiste",0)
AddTransaction(Personnes[0],Personnes[1],8,100)

AfficherListe(Personnes)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)
