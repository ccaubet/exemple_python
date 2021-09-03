# def changement_up ():

#     chainecaractere="dkjsdksjdkj"
#     result=chainecaractere.title()
#     print(result)

# changement_up()



#!/usr/bin/python3

def capital_case(v):
    return v.capitalize()   #permet de passer la première lettre en majuscule

def test_capital_case():  #je lance la fonction pytest .\src\app.py dans le terminal pour ne lancer que cette fonction car la fonction commence par test_
    resultat=capital_case("adrien")
    assert resultat=='Adrien'
