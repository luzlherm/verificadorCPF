def verifica_cpf(cpf):
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    0
    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    # Verificar se os dígitos verificadores estão corretos
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False

# Solicitar  CPF
cpf = input("Digite o CPF (apenas números): ")

# Verificar CPF
if verifica_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
