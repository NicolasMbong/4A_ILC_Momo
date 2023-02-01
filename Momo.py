from flask import Flask 
import sys
import csv # bibliothèque pour éditer et lire les fichiers csv
import datetime # bibliothèque pour utiliser la date et l'heure
import hashlib # bibliothèque pour utiliser le hachage sha256

app = Flask(__name__)



#définition de la classe Personne
class Personne:
    _id = 0
    _nom = ""
    _solde = " "

    def __init__(self, nom, solde):
        self._id += 1
        self._nom = nom
        self._solde = solde
# getters
    def getId(self):
        return self._id

    def getNom(self):
        return self._nom

    def getSolde(self):
        return self._solde
# setters
    def setSolde(self, montant):
        self._solde = self._solde + montant
   


#initilisation des listes
Personnes = []
listTransaction = []



# fonction permettant d'afficher l'ensemble des clients
@app.route("/", methods=['GET'])
def afficherClient():
    if request.method == 'GET':
        affiche = "<h3>Liste de Personne :</h3>\n"
        for personne in range(len(Personnes)):
            affiche += "<p>" + personne.toString() + "</p>\n"
        return affiche
    else:
        return "Methode invalide"

    
    
# fonction permettant d'ajoiter un compte
@app.route("/addCompte/<string:nom>/<float:solde>", methods=['POST'])
def ajoutCompte(Nom, solde):
    for i in range(len(Personnes)):   #verifie que le client est bien unique
        if Personnes[i].getNom() == Nom:
            return "Un client avec les meme nom est deja dans la banque"
    client = Personne(Nom, solde)  # créer un objet de Personne et l'ajoute à la liste de client
    Personnes.append(client) 
    print("le client a été ajouté a la banque")
    return client



# fonction permettant de vérifier si il y a suffisament d'argent sur le compte débité
def verificationtransaction(P1, transac):
    if P1.getSolde() < transac:
        return False
    return True



# fonction permettant d'ajouter une nouvelle transaction - route E1
@app.route("/addTransaction/<int:id1>/<int:id2>/<float:transfert>", methods=['POST'])
def ajoutTransaction(id1, id2, transfert):
    t = datetime.datetime.now()
    array = [id1, id2, transfert, t]
    h = hachage(array)    #crée le hash des 2 clients ainsi que de la somme et de la date
    trans = [id1, id2, t, transfert, h]
    if verificationtransaction(Personnes[id1], transfert): # si la transaction est validée, la somme est retirée du compte 1 et et ajouter sur le compte 2
        Personnes[id1].setSolde(-transfert)
        Personnes[id2].setSolde(transfert)
        listTransaction.append(trans)  # la transaction est ajoutée à la liste des transactions
        return "La transaction d'un montant de:", transfert, "entre ", Personnes[id1].getNom(), " et ", Personnes[
            id2].getNom(), "à été effectué"
    return Personnes[id1], "ne peut pas transferer", transfert, "car son solde est trop faible"



# fonction permettant d'afficher toutes les transactions par ordre chronologique - route E2
@app.route("/afficherTransaction", methods=['GET'])
def afficherTransaction():
    List = trie(listTransaction) # trie les transactions par date
    for i in range(len(List)):
        print(List[i])

 


# fonction permettant de trier une liste selon la 3eme valeurs de la liste
def trie(L):
    return sorted(L, key=lambda L: L[2])




# fonction permettant d'afficher l'ensemble des transactions triées par ordre chronologique qui sont liées à un client dont l'id est donné - route E3
@app.route("/afficherTransactionPersonne/<int:id>", methods=['GET'])
def afficherTransactionPersonne(id):
    list = trie(listTransaction) # trie les transactions par date
    for i in range(len(list)):
        if list[0].getId == id or list[1].getId == id:  #vérifie l'ensemble des transactions et affiche celles liées aux client saisie
            print(list[i])


            
# fonction permettant d'afficher le solde sur le compte d'un client grâce à son id - route E4
@app.route("/printSolde/<int:id>",methods=['GET'])
def afficherSolde(id):
    for i in range(len(Personnes)):
        if Personnes[i].getId() == id:
            return "Le solde du compte est: ", Personnes[i].getsolde(), "euros"

        
        
# fonction permettant de lire un fichier csv et de récuperer les informations dessus - route E5
@app.route("/lectureCSV/<str:fichier_csv>", methods=['GET','POST'])
def lectureCSV(fichier_csv):
    fichier = open(fichier_csv, "r")  # ouvre le fichier fournis en mode lecture
    reader = csv.reader(fichier, delimiter=";")  # créer un bojet de lecture avec ";" comme délimiteur de colonne
    data = list(reader)  # stock les lignes du fichier dans une liste
    return data # retourne les valeurs du fichier



# fonction permettant d'écrire dans un fichier csv
@app.route("/lectureCSV/<str:fichier_csv>", methods=['GET','POST'])
def ecrireCSV(fichier_csv):
    fichier = open(fichier_csv, "w")  # ouvre le fichier fournis en mode lecture
    write = csv.write(fichier, delimiter=";")  # créer un bojet de lecture avec ; comme délimiteur de colonne
    data = list(write)  # stock les lignes du fichier dans une liste
    return data



# fonction de hachage de transaction grâce à sha256
# nous avons choisi la fonction sha256 car elle offre un haut niveau de sécurité 
# de plus elle est déjà utilisé dans de nombreux systèmes afin de sécuriser les informations comme par exemple Bitcoin
def hachage(transaction):
    sha256 = hashlib.sha256()
    h = str(transaction)
    sha256.update(h.encode('utf-8'))
    return sha256.hexdigest()



#initialisation de quelques clients et transaction

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
