from flask import Flask

app = Flask(__name__)

@app.route("/")

def AddTransaction(P1,P2,t,s):
	print("La transaction d'un montant de:", s , "entre ", P1 , " et ", P2 , "à été effectué à: ", t)
	return [P1,P2,t,s];

def AfficherTransactions(T):
	for i in len(T):
		print(T[i])
	return


if __name__ == '__main__';
	app.run
