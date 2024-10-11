"""Painel de Consulta Desenvolvido por https://github.com/uwjota"""

import os # Biblioteca Terminal para limpar painel.
import re # Biblioteca para expressões regulares.
from twilio.rest import Client #Biblioteca Consultar numero.

# Credenciais da API de consulta Twilio
account_sid = 'SUA_SID'
auth_token = 'SEU_TOKEN'

client = Client(account_sid, auth_token)

def finalizar_app():
    os.system("cls" if os.name == "nt" else "clear")
    print("Painel Fechado")

def exibir_nome_do_programa ():
    print("PΛIПΣᄂ PЦXΛЯ DΛDӨƧ\n")

def exibir_opcoes():
    print("1. CPF")
    print("2. Placa do Veiculo")
    print("3. Telefone")
    print("4. Sair\n")

def opcao_invalida():
    print("Opção Invalida\n")
    input("Digite qualquer Tecla para Voltar ao painel: ")
    os.system("cls" if os.name == "nt" else "clear")
    main()

def voltar_painel():
    input("\nDigite qualquer tecla para voltar ao painel.")
    os.system("cls" if os.name == "nt" else "clear")
    main()

def validador_cpf(cpf):
    cpf = [int(char) for char in cpf if char.isdigit()]

    if len(cpf) != 11:
        return False

    # Valida os dois dígitos verificadores
    for i in range(9, 11):
        soma = sum(cpf[num] * ((i+1) - num) for num in range(0, i))
        digito = (soma * 10 % 11) % 10
        if digito != cpf[i]:
            return False

    return True

def opcao_cpf():
    numero_cpf = input("Digite o CPF: ")
    if validador_cpf(numero_cpf):
        print(f"CPF {numero_cpf} é válido.")
    else:
        print(f"CPF {numero_cpf} é inválido.")

    voltar_painel()
    


def validar_placa(placa):
    # Regex para o formato antigo: ABC-1234
    padrao_antigo = r'^[A-Z]{3}-\d{4}$'
    # Regex para o formato novo: ABC1D23
    padrao_mercosul = r'^[A-Z]{3}\d[A-Z]\d{2}$'

    if re.match(padrao_antigo, placa) or re.match(padrao_mercosul, placa):
        return True
    else:
        return False

def opcao_placa():
    placa = input("Digite a Placa formatos aceitos: 'ABC-1234' ou 'ABC1D23': ").upper()  # Convertendo a placa para maiúsculas por convenção
    
    if validar_placa(placa):
        print(f"A placa {placa} é válida.")
    else:
        print(f"A placa {placa} é inválida. Formatos aceitos: 'ABC-1234' ou 'ABC1D23'.")
    
    voltar_painel()

def validar_telefone(numero_telefone):
    try:
        # Lookup do número
        phone_number = client.lookups.v1.phone_numbers(numero_telefone).fetch(type='carrier')
        
        # Exibe informações básicas
        print(f"Número: {phone_number.phone_number}")
        print(f"País: {phone_number.country_code}")
        print(f"Operadora: {phone_number.carrier['name']}")
        print(f"Tipo: {phone_number.carrier['type']}")
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")

def opcao_telefone():
    numero = input("Digite o telefone (formato internacional, ex: +5511987654321: ")
    validar_telefone(numero)
    voltar_painel()


def escolher_opcao ():
    try:
        opcao_escolhida = int(input("Escolha alguma opção: "))

        if opcao_escolhida == 1:
            opcao_cpf()
        elif opcao_escolhida == 2:
            opcao_placa()
        elif opcao_escolhida == 3:
            opcao_telefone()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main ():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
