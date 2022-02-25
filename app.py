lista = [1, 10]

try:
    divisao = 10 /1
    numero = lista[1]
    x = a
except ZeroDivisionError:

    print("Não é possivel realizar divisão por 0")

except IndexError:
    print("Erro ao acessar, index invalido da lista !!") 

except BaseException as ex:
    print(f"Erro desconhecido : ERRO-->{ex}")