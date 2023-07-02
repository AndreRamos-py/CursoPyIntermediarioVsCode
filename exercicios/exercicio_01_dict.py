# Exercício - sistema de perguntas e respostas



perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
 
for questao in perguntas:
    print('Pergunta:', questao['Pergunta'])
 
    opcoes = questao['Opções']
    for i, opcao in enumerate(opcoes):
        print('{}) {} '.format(i , opcao))
 
    escolha = input('Qual a resposta?: ')
    while not escolha.isdigit() or 0 > int(escolha) or int(escolha) > len(opcoes):
        print('Digite apenas números válidos!')
        escolha = input('Qual a resposta?: ')
 
    escolha_int = int(escolha)
 
    if opcoes[escolha_int] == questao['Resposta']:
        print('Resposta Correta! Parabéns!')
        acertos += 1
    else:
        print('Resposta Errada!')
 
    print()
 
print(f'Você acertou {acertos} de {len(perguntas)}')
