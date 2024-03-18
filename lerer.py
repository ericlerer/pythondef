import numbers


def contagem_regressiva(num):
  while num >= 0:
    print(num)
    num -= 1

def contagem_regressiva2(num):
  for cont in range(num, -1, -1):
    print(cont)
    contagem_regressiva2(5)

def ola_varias_vezes(n):
  for _ in range(n):
    print("Olá")
    ola_varias_vezes(5) 

def pula_mult_3(maximo):
  for x in range(1, maximo + 1):
    if x % 3 == 0:
      continue
    print(x)

pula_mult_3(10)

def para_antes_de_10(maximo):
    for x in range(1, maximo + 1):
      if x >= 10:
        break
      print(x)

    print("acabou")
    print("-" * 30)
    para_antes_de_10(20)

def fatorial(n):
    if n < 0:
        return None  # Retornar None para entradas inválidas (números negativos)
    elif n == 0:
        return 1  # O fatorial de 0 é 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

# Exemplo de uso:
#numero = 5
#print("O fatorial de", numero, "é:", fatorial(numero))


if num == 1:
   return 1
return num * fatoral2(num -1)

print (fatorial2(5))