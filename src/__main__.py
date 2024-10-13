import json

quantidade_blocos = 1 #int(input(f"\nQuantos Blocos de Atividade?: "))
blocos_de_atividade = {}

for i in range(quantidade_blocos):
    blocos_de_atividade[f"Bloco {i+1}"]= []

for item in blocos_de_atividade:
    quantidade_atividade = 1 #int(input(f"\nQuantas atividades no Bloco {item}?: "))
    counter = 0

    lista = [[],[]]

    while counter < quantidade_atividade:
        blocos_de_atividade[item].append({
            "Tempo": 20,#input(f"\nTempo: "),
            "Medida": "m", #input("Medida: "),
            "Tag": "Lento", #input("Tag: "),
            "Ritmo": 5.30 #input("Ritmo: ")  
        })

        lista[0].append(blocos_de_atividade[item][counter]["Ritmo"])
        lista[1].append(blocos_de_atividade[item][counter]["Tempo"])
        counter += 1

    ritmo = sum(float(i) for i in lista[0])

    tempo = sum(int(i) for i in lista[1])

    print(f"\nDistancia percorrida no Bloco {item}: {round(tempo/ritmo, 2)}\n")
    print(f"\n Velocidade média no Bloco {round(60 / ritmo, 2)}Km/H")










print(json.dumps(blocos_de_atividade, indent=2))