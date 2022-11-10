dic={"Nilo":"Egipto","Danubio":"Alemania","Tamesis":"Inglaterra","Volga":"Rusia","Ebro":"España"}

for rios, paises in dic.items():
    print("El rio", rios, "fluye en medio de ", paises)
    
for rios in dic:
    print("Los rios son: ",rios)
    
for rios, paises in dic.items():
    print("Los paises son: ",paises)
    
