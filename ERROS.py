# Erros em tempo de compilação
# Erros em tempo de execução
# Erros de lógicas

# 3 principais ERROS

try:
    a= float(input("Digite o numero A: "))
    b= float(input("Digite um numero B: "))

    print(a/b)

except ValueError as error:
    print("digite apenas números")
except ZeroDivisionError as error:
    print("Não pode ser feita divisão por zero")
except Exception as error:
    print("algum erro ocorreu")
    print(error)
finally:
    print("Fim do programa")

    # TRY E EXCEPT E FINALLY








#try # expect expection