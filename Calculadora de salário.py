while True:
    print('###Calculadora de salário###')
    print('1 - Vendedor')
    print('2 - Gerente')
    cargo = int(input('Digite o código referente ao seu cargo: '))
    while cargo < 1 or cargo > 2:
        cargo = int(input('Digite o código referente ao seu cargo: '))
    salario_base = float(input('Insira o salário base: '))
    comissao = ''
    if cargo == 1:
        venda = float(input('Quanto você vendeu no mês? '))
        if venda >= 50000:
            comissao = venda * 0.01
        if 50000 > venda >= 40000:
            comissao = venda * 0.009
        if 40000 > venda >= 30000:
            comissao = venda * 0.008
        if 30000 > venda >= 20000:
            comissao = venda * 0.007
        if 20000 > venda >= 16000:
            comissao = venda * 0.006
        if 16000 > venda >= 15000:
            comissao = venda * 0.005
        if venda < 15000:
            comissao = 0
    elif cargo == 2:
        venda = float(input('Quanto a loja vendeu no mês: '))
        if venda >= 300000:
            comissao = venda * 0.01
        if 300000 > venda >= 270000:
            comissao = venda * 0.007
        if 270000 > venda >= 200000:
            comissao = venda * 0.005
        if 200000 > venda >= 150000:
            comissao = venda * 0.003
        if venda < 150000:
            comissao = 0
    salario_bruto = salario_base + comissao
    desconto_passagem = salario_base * 0.06
    desconto_inss = ''
    if salario_bruto >= 3641.04:
        desconto_inss = 345.92 + ((salario_bruto - 3641.04) * 0.14)
    if 3641.04 > salario_bruto >= 2427.36:
        desconto_inss = 199.38 + ((salario_bruto - 2427.36) * 0.12)
    if 2427.36 > salario_bruto >= 1212.01:
        desconto_inss = 90.90 + ((salario_bruto - 1212.01) * 0.09)
    if salario_bruto <= 1212.00:
        desconto_inss = salario_bruto * 0.075
    imposto_renda = ''
    if salario_bruto > 4664.68:
        imposto_renda = 413.40 + ((salario_bruto - 4664.68) * 0.275)
    if 4664.68 > salario_bruto >= 3751.05:
        imposto_renda = 207.84 + ((salario_bruto - 3751.05) * 0.225)
    if 3751.05 > salario_bruto >= 2826.65:
        imposto_renda = 69.19 + ((salario_bruto - 2826.65) * 0.15)
    if 2826.65 > salario_bruto >= 1903.99:
        imposto_renda = (salario_bruto - 1903.99) * 0.075
    if salario_bruto <= 1903.98:
        imposto_renda = 0
    vale = 0
    vale_cond = input('Recebe vale-alimentação? (S/N) ')
    if vale_cond == 'S' or vale_cond =='s':
        vale = 390
    elif vale_cond == 'N' or vale_cond == 'n':
        vale = 0
    onibus = int(input('Quantos ônibus você pega no total? '))
    valor_passagem = float(input('Qual o valor de cada passagem? '))
    dias_uteis = int(input('Quantos dias úteis têm no mês? '))
    passagem = onibus * valor_passagem * dias_uteis

    salario_liquido = salario_bruto - desconto_inss - desconto_passagem - imposto_renda
    print('')
    print('###Proventos###')
    print('Salário base: R${:.2f}'.format(salario_base))
    print('Comissões: R${:.2f}'.format(comissao))
    print('Salário Bruto: R${:.2f}'.format(salario_bruto))
    print('Vale-alimentação: R${:.2f}'.format(vale))
    print('Vale-transporte: R${:.2f}'.format(passagem))
    print('')
    print('###Descontos###')
    print('Desconto vale-transporte: R${:.2f}'.format(desconto_passagem))
    print('Desconto INSS: R${:.2f}'.format(desconto_inss))
    print('Imposto de renda: R${:.2f}'.format(imposto_renda))
    print('Total de descontos: R${:.2f}'.format(desconto_inss + desconto_passagem + imposto_renda))
    print('')
    print('###Total###')
    print('Salário líquido: R${:.2f}'.format(salario_liquido))
    print('Valor a receber: R${:.2f}'.format(salario_liquido + vale + passagem))
    print('')
    repeat = input('Deseja refazer o calcúlo? (S/N) ')
    if repeat == 'n' or repeat == 'N':
        print('Encerrando o programa...')
        break
    print('')
    print('')
