def calculadora_juros_compostos():
    """
    Calculadora de juros compostos que ajuda o usuário a entender o montante acumulado ao longo do tempo
    e se ele alcançará o salário desejado na aposentadoria.
    """
    nome = input('Qual o seu nome? ')
    print(f'Olá! {nome}, seja bem vindo aos juros compostos! Aqui nós cuidamos da sua aposentadoria :)')

    dinheiro_inicial = int(input('Digite o valor inicial para investimento: '))
    tempo_desejado = int(input('Digite quantos meses você pretende deixar o dinheiro investido: '))
    taxa = float(input('Digite, em decimal, qual a taxa mensal de retorno do seu investimento: '))
    aporte = int(input('Qual o valor que vai aportar por mês? R$: '))
    salario_desejado = int(input('Digite o salário mensal que você quer receber ao se aposentar: '))

    tempo_decorrido = 0

    while tempo_decorrido < tempo_desejado:
        if tempo_decorrido == 0:
            montante = dinheiro_inicial * (1 + taxa) ** 1
            montante = round(montante, 2)
            tempo_decorrido += 1
        else:
            montante = (montante + aporte) * (1 + taxa) ** 1
            tempo_decorrido += 1

    print('-------------------------------------------------')
    print('Parabéns {}! Ao final do período você terá R$ {:,.2f}'.format(nome, montante).replace('.', '#').replace(',', '.').replace('#', ','))

    salario_mensal = (montante * taxa)
    salario_mensal = round(salario_mensal, 2)

    if salario_mensal > salario_desejado:
        print(f'Parabéns! Você pode se aposentar! Seu salário mensal é de R$ {salario_mensal:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ','))
    elif salario_mensal < salario_desejado:
        print(f'Infelizmente não é possível se aposentar ainda com esse salário R$ {salario_mensal:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ','))

# Para executar a função:
# calculadora_juros_compostos()

