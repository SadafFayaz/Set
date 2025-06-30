nom=""
while nom=="":
nom=input("Ton nom:")

age=0
while age==0:
age=input("Ton age:")

try:
    age_prochain=int(age)+1
except:
    print("Erreur vous devez ecrire des nombres")
else:
    print("vous appellez "+nom)
    print("vous avez "+str(age)+"ans l'an prochain vous aurez "+str(age_prochain)"ans")
