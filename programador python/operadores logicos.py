saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque)
print(saldo <= limite)
# operador E
print(saldo >= saque and saque <= limite)

# operador Ou
print(saldo >= saque or saque <= limite)

# operador de negação
contatos_emergencia = []
print(not 1000 > 1500)

print(not contatos_emergencia)

print(not "saque 1500;")

print(not "")

#parênteses 
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
