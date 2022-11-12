try:
  arquivo = open("emails.txt", "w")
  
except FileNotFoundError:
  print("arquivo não existe")


  # oq significa o open e o with