import txtGen

text= txtGen.genLorem()
#text= "Hello World"
###########################################################

#création de l'arbre, supression des lettres non présentes, tri selon le nombre d'occurence (décroissant)
def CreateTree(Dic):
    Tree=[]
    for letter in Dic:
        if letter[1] != 0:
            Tree.append([letter[0], letter[1]])
    Tree.sort(key= lambda M:M[1], reverse= True)
    return Tree

#Création de l'arbre sous forme d'un tableau: [Lettres présentes dans la branche enfant, nombre d'occurence, branche gauche, branche droite]
def SortTree(Tree):
    q=[]
    while len(Tree) > 1:
        Tree.sort(key= lambda M:M[1], reverse= True)
        lenght= len(Tree)
        q = [Tree[lenght-1][0]+Tree[lenght-2][0], Tree[lenght-1][1]+ Tree[lenght-2][1], Tree[lenght-1], Tree[lenght-2]]
        Tree.pop()
        Tree.pop()
        Tree.append(q)
    return Tree

#Création d'une liste associant à chaque lettre présente dans le texte un code
def GenKey(Tree):
    Key= {}
    for i in Tree[0][0]:
        pointer= Tree[0]
        code= ''
        while len(pointer) > 2:
            y= 0
            while pointer[2][0][y] != i and y< len(pointer[2][0])-1:
                y+= 1
            if i== pointer[2][0][y]:
                code= code + '0'
                pointer= pointer[2]
            else:
                code= code + '1'
                pointer= pointer[3]
        # code.reverse()
        Key[i]= code
    return Key

#Affichage du code attribué à cahque lettre et de son nombre d'occurencr
def printKey(Key, Dic):
    for i in Dic:
        if i[1]!= 0:
            print(i[0],'=', Key[i[0]], "apparait",i[1], "fois")

#utilise la clé créée pour encoder le texte.
def EncryptText(Key, Text):
    EncryptedText= ''
    for i in Text:
        if i.isalpha():
            EncryptedText+= Key[i]
        else:
            EncryptedText+= i
    return EncryptedText


#######_MAIN_###################

#Création du compteur
Dic=  []
Alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in Alphabet:
    Dic.append([i, 0])

#Mettre tout les lettre en majuscule
text= text.upper()

#Incrémentation du compteur en fonction du txt
for i in text:
    for letter in Dic:
        if letter[0] == i:
            letter[1]+=1


Tree = CreateTree(Dic)
Tree= SortTree(Tree)
key= GenKey(Tree)
SortedKey= sorted(key.items(), key= lambda M: M[0])
EncryptedText= EncryptText(key, text)

#print(text)
print(key)
printKey(key, Dic)
#print(EncryptedText)
print(SortedKey)



#fenêtre
