def sumn(n):
    return n + sumn(n-1) if n > 1 else 1

numar = input("Introduceti numarul n: ")
print(sumn(int(numar)))