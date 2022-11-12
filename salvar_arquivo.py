try:
  with open("nomes.txt", "a") as arquivo:
    arquivo.write("joao\n")
except Exception as error:
  print("algum erro ocorreu")
  print(error)




  # modo r - abre para ler
  # modo w- abre para escrever
  # modo a- abre para escrever
  # modo b- modo binário
  # modo +
  # lê o arquivo open (PYTHON)

  #\n pula linha