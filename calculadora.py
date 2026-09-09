from datetime import date

def obter_ano_nascimento():
    return int(input("Digite seu ano de nascimento: "))

def calcular_idade(ano_nascimento):
    return date.today().year - ano_nascimento

def main():
    ano = obter_ano_nascimento()
    idade = calcular_idade(ano)
    print(f"Sua idade aproximada é {idade} anos.")

if __name__ == "__main__":
    main()
