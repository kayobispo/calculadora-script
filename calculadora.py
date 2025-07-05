#Menu de operadores
def menu ():
  return input (
      "\nEscolha a operação:\n"
      " 1) Adição\n"
      " 2) Subtração\n"
      " 3) Multiplicação\n"
      " 4) Divisão\n"
      " 5) Finalizar\n"
      "Digite a opção: "
  )

#Função responsável pelos cálculos
def operacao (atual, valor, operador):
  if operador == '1':
    resultado = atual + valor
    print(f"{atual} + {valor} = {resultado}")
    return resultado
  elif operador == '2':
    resultado = atual - valor
    print(f"{atual} - {valor} = {resultado}")
    return resultado
  elif operador == '3':
    resultado = atual * valor
    print(f"{atual} * {valor} = {resultado}")
    return resultado
  elif operador == '4':
    if valor == 0:
      print("Não é possível dividir por zero.")
      return atual
    resultado = atual / valor
    print(f"{atual} / {valor} = {resultado}")
    return resultado
  else:
    print("Operador inválido.")
    return atual

#Função responsável pelo funcionamento da calculadora
def calculadora ():
  try:
    total = float(input("Insira um valor: "))
  except:
    print("Digite um número válido.")
    return

  while True:
    operador = menu ()
    if operador == '5':
      print(f"\nO total é {total}.")
      print("Operação finalizada!")
      break
    try:
      valor = float(input("Insira um valor: "))
    except:
      print("Digite um número válido.")
      continue

    total = operacao (total, valor, operador)

#Executar
calculadora()
