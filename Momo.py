from flask import Flask
import sys
import csv
import datetime
import hashlib

app = Flask(__name__)


class Personne:
    _id = 0
    _nom = ""
    _solde = " "

    def __init__(self, nom, solde):
        self._id += 1
        self._nom = nom
        self._solde = solde

    def getId(self):
        return self._id

    def getNom(self):
        return self._nom

    def getSolde(self):
        return self._solde

    def setSolde(self, montant):
        self._solde = self._solde + montant


Personnes = []
listTransaction = []


@app.route("/", methods=['GET'])
def afficherClient():
    if request.method == 'GET':
        affiche = "<h3>Liste de Personne :</h3>\n"
        for personne in range(len(Personnes)):
            affiche += "<p>" + personne.toString() + "</p>\n"
        return affiche
    else:
        return "Methode invalide"


@app.route("/addCompte/<string:nom>/<float:solde>", methods=['POST'])
def ajoutCompte(Nom, solde):
    for i in range(len(Personnes)):
        if Personnes[i].getNom() == Nom:
            return "Un client avec les meme nom est deja dans la banque"
    client = Personne(Nom, solde)
    Personnes.append(client)
    print("le client a été ajouté a la banque")
    return client


def verificationtransaction(P1, transac):
    if P1.getSolde() < transac:
        return False
    return True


@app.route("/addTransaction/<int:id1>/<int:id2>/<float:transfert>", methods=['POST'])
def ajoutTransaction(id1, id2, transfert):
    t = datetime.datetime.now()
    array = [id1, id2, transfert, t]
    h = hachage(array)
    trans = [id1, id2, t, transfert, h]
    if verificationtransaction(Personnes[id1], transfert):
        Personnes[id1].setSolde(-transfert)
        Personnes[id2].setSolde(transfert)
        listTransaction.append(trans)
        return "La transaction d'un montant de:", transfert, "entre ", Personnes[id1].getNom(), " et ", Personnes[
            id2].getNom(), "à été effectué"
    return Personnes[id1], "ne peut pas transferer", transfert, "car son solde est trop faible"


@app.route("/afficherTransaction", methods=['GET'])
def afficherTransaction():
    List = trie(listTransaction)
    for i in range(len(List)):
        print(List[i])


def trie(L):
    return sorted(L, key=lambda L: L[2])


@app.route("/afficherTransactionPersonne/<int:id>", methods=['GET'])
def afficherTransactionPersonne(id):
    list = trie(listTransaction)
    for i in range(len(list)):
        if list[0].getId == id or list[1].getId == id:
            print(list[i])


@app.route("/printSolde/<int:id>",methods=['GET'])
def afficherSolde(id):
    for i in range(len(Personnes)):
        if Personnes[i].getId() == id:
            return "Le solde du compte est: ", Personnes[i].getsolde(), "euros"

@app.route("/lectureCSV/<str:fichier_csv>", methods=['GET','POST'])
def lectureCSV(fichier_csv):
    fichier = open(fichier_csv, "r")  # ouvre le fichier fournis en mode lecture
    reader = csv.reader(fichier, delimiter=";")  # créer un bojet de lecture avec ; comme délimiteur de colonne
    data = list(reader)  # stock les lignes du fichier dans une liste
    return data

@app.route("/lectureCSV/<str:fichier_csv>", methods=['GET','POST'])
def ecrireCSV(fichier_csv):
    fichier = open(fichier_csv, "w")  # ouvre le fichier fournis en mode lecture
    write = csv.write(fichier, delimiter=";")  # créer un bojet de lecture avec ; comme délimiteur de colonne
    data = list(write)  # stock les lignes du fichier dans une liste
    return data


# fonction de hachage de transaction grâce à sha256


def hachage(transaction):
    sha256 = hashlib.sha256()
    h = str(transaction)
    sha256.update(h.encode('utf-8'))
    return sha256.hexdigest()


ajoutCompte("Max", 10)
ajoutCompte("Benjamin", 1000)
ajoutCompte("Baptiste", 0)

# afficherClient()


ajoutTransaction(1, 0, 100)
ajoutTransaction(1, 2, 10)
# afficherTransaction()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
