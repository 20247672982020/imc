def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    Fórmula: IMC = peso / (altura ** 2)
    """
    return peso / (altura ** 2)

def main():
    print("Calculadora de IMC")
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")

if __name__ == "__main__":
    main()