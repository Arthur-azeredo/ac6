a, b, c = input().split()

MaiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2

Maior = (int(MaiorAB) + int(c) + abs(int(MaiorAB) - int(c))) / 2

print("{} eh o maior".format(int(Maior)))

