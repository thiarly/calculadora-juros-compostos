from flask import Flask, render_template, request
from calculadora import app



@app.route('/', methods=['GET', 'POST'])
def calculadora_juros_compostos():
    if request.method == 'POST':
        nome = request.form['nome']
        dinheiro_inicial = float(request.form['dinheiro_inicial'])
        tempo_desejado = int(request.form['tempo_desejado'])
        taxa = float(request.form['taxa']) / 100
        aporte = float(request.form['aporte'])
        salario_desejado = float(request.form['salario_desejado'])

        tempo_decorrido = 0
        montante = dinheiro_inicial

        while tempo_decorrido < tempo_desejado:
            if tempo_decorrido == 0:
                montante = montante * (1 + taxa) ** 1
            else:
                montante = (montante + aporte) * (1 + taxa) ** 1
            tempo_decorrido += 1

        montante = round(montante, 2)
        salario_mensal = (montante * taxa)
        salario_mensal = round(salario_mensal, 2)
        
        resultado = {
        'nome': nome,
        'montante': "R$ {:,.2f}".format(montante).replace(",", "v").replace(".", ",").replace("v", "."),
        'salario_mensal': "R$ {:,.2f}".format(salario_mensal).replace(",", "v").replace(".", ",").replace("v", "."),
        'salario_desejado': "R$ {:,.2f}".format(salario_desejado).replace(",", "v").replace(".", ",").replace("v", ".")
    }

        return render_template('resultado.html', resultado=resultado)
    return render_template('calculadora.html')
