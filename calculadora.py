from datetime import date

def obter_ano_nascimento():
    return int(input("Digite seu ano de nascimento: "))

def calcular_idade(ano_nascimento):
    return date.today().year - ano_nascimento

def faixa_etaria(idade):
    if idade < 13:
        return "criança"
    elif idade < 18:
        return "adolescente"
    elif idade < 60:
        return "adulto"
    return "idoso"

def main():
    ano = obter_ano_nascimento()
    idade = calcular_idade(ano)
    unidade = "ano" if idade == 1 else "anos"
    print(f"Sua idade aproximada é {idade} {unidade}.")
    print(f"Faixa etária: {faixa_etaria(idade)}")

if __name__ == "__main__":
    main()
