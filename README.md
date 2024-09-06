# Sistema Bancário em Flask

Este projeto é um sistema bancário simples desenvolvido com Flask. Ele permite aos usuários criar uma conta, realizar depósitos e saques, e exibe informações sobre a conta, como saldo e limites de saque.

## Funcionalidades

- **Cadastro de Usuário:** Os usuários podem inserir seu nome para criar uma conta.
- **Operações Bancárias:** Os usuários podem realizar depósitos e saques.
- **Limite de Saque:** O sistema permite um máximo de 3 saques diários, com um limite de R$ 500 por saque.
- **Gerador de Conta:** Após o login, um número de agência e conta é gerado aleatoriamente para o usuário.

## Tecnologias Utilizadas

- Flask
- HTML/CSS para o frontend
- Bootstrap para a estilização

## Pré-requisitos

Certifique-se de ter o Python 3.6 ou superior instalado em seu sistema. Além disso, é necessário ter o Flask instalado. Você pode instalar as dependências do projeto listadas no `requirements.txt` com o seguinte comando:

```bash
pip install -r requirements.txt
