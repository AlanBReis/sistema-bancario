from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Inicializa a conta com saldo zero
def get_conta():
    if 'conta' not in session:
        session['conta'] = {'nome': '', 'saldo': 0.0}
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
                elif valor > conta['saldo']:
                    flash('Saldo insuficiente para saque.')
                else:
                    conta['saldo'] -= valor
                    flash('Saque realizado com sucesso.')
        except ValueError:
            flash('O valor informado deve ser numérico.')
        
        session.modified = True
        return redirect(url_for('principal'))
    
    return render_template('principal.html', saldo=conta['saldo'], nome=conta['nome'])

if __name__ == '__main__':
    app.run(debug=True)
