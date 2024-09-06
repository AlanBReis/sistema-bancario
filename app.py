from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Inicializa a conta com saldo zero e saques diários
def get_conta():
    if 'conta' not in session:
        session['conta'] = {'nome': '', 'saldo': 0.0, 'saques_diarios': []}
    return session['conta']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        if nome:
            conta = get_conta()
            conta['nome'] = nome
            session.modified = True
            return redirect(url_for('principal'))
        else:
            flash('Por favor, insira seu nome.')
    return render_template('index.html')

@app.route('/principal', methods=['GET', 'POST'])
def principal():
    conta = get_conta()
    hoje = datetime.now().strftime('%Y-%m-%d')
    
    if request.method == 'POST':
        valor = request.form.get('valor')
        operacao = request.form.get('operacao')
        
        if not valor or not operacao:
            flash('Por favor, preencha todos os campos.')
            return redirect(url_for('principal'))
        
        try:
            valor = float(valor)
            if operacao == 'deposito':
                if valor <= 0:
                    flash('O valor do depósito deve ser positivo.')
                else:
                    conta['saldo'] += valor
                    flash('Depósito realizado com sucesso.')
            elif operacao == 'saque':
                if valor <= 0:
                    flash('O valor do saque deve ser positivo.')
                elif valor > 500:
                    flash('O valor do saque não pode exceder R$ 500.')
                elif valor > conta['saldo']:
                    flash('Saldo insuficiente para saque.')
                else:
                    # Verifica saques diários
                    saques = [s for s in conta['saques_diarios'] if s['data'] == hoje]
                    if len(saques) >= 3:
                        flash('Limite diário de saques atingido.')
                    else:
                        conta['saldo'] -= valor
                        conta['saques_diarios'].append({'data': hoje, 'valor': valor})
                        flash('Saque realizado com sucesso.')
        except ValueError:
            flash('O valor informado deve ser numérico.')
        
        session.modified = True
        return redirect(url_for('principal'))
    
    return render_template('principal.html', saldo=conta['saldo'], nome=conta['nome'])

if __name__ == '__main__':
    app.run(debug=True)
