#Você é o culpado?

perguntas = [                        #dicionário
    "Você telefonou para a vítima?",
     "Você estava no local do crime?",
    "Você mora perto da vítima?",
    "Você devia para a vítima?",
     "Você já trabalhou com vítima?"
]
afirmativa = 0
for pergunta in perguntas: #comparação para os inputs
    resposta = input(pergunta + "(sim/não):")
    if resposta == "sim":
        afirmativa = afirmativa + 1
match afirmativa:
    case 2:
        print("Suspeita")
    case 3 | 4:
        print("Cúmplice")
    case 5:
        print("Assassino")
    case _:
        print("Inocente")


    






