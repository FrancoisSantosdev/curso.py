


# estruturas condicionais aninhada
conta_normal = True
conta_universitaria = False



saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")    
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!") 
    else:
        print("Saldo insuficiente!")           
    
