dados1 = input().split()
cp1 = int(dados1[0])
qp1 = int(dados1[1])
vup1 = float(dados1[2])

dados2 = input().split()
cp2 = int(dados2[0])
qp2 = int(dados2[1])
vup2 = float(dados2[2])

total = (qp1 * vup1) + (qp2 * vup2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
