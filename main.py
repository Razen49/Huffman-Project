import txtGen
text= txtGen.genLorem()

#Création du compteur
Dic=  {}
Alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in Alphabet:
    letter= {i: 0}
    Dic.update(letter)

#Mettre tout les lettre en majuscule
text= text.upper()

#Incrémentation du compteur en fonction du txt
for letter in Dic:
    for i in text:
        if i == letter:
            Dic[letter]+=1
print(text)
print(Dic)
