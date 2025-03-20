"""
1. Dicionários em Python (tipo dict)
2. Dicionários são estruturas de dados do tipo par de "chave" e "valor".
3. Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.
4. O valor pode ser de qualquer tipo, incluindo outro dicionário.
5. Usamos as chaves - {} - ou a classe dict para criar dicionários.
6. Imutáveis: str, int, float, bool, tuple
7. Mutável: dict, list

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

"""

pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 18,
    "altura": 1.8,
    "endereços": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa["nome"])
print(pessoa["sobrenome"])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
