def obter_ano_nascimento():
    return int(input("Digite seu ano de nascimento: "))

def main():
    ano = obter_ano_nascimento()
    print(f"Ano informado: {ano}")

if __name__ == "__main__":
    main()
