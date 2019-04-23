from oficio import Oficio

def abertura():
    print("=============================")
    print("MARRETA - Gerador de Ofícios")
    print("=============================\n")

def main():
    abertura()
    processo = input("Digite o número do Processo \n>> ")
    o = Oficio(processo)

if __name__ == "__main__":
    main()
