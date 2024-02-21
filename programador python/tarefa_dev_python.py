N = int(input())

while N > 0:
    entrada = input().split(" ")

    A = entrada[0]
    B = entrada[1]

    if len(B) > len(A):
        print("nao encaixa")
    elif A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")

    N -= 1
