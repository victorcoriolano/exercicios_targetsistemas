#######
#Exercícios para inscrição na Targetsistemas
#Os códigos são comentados, para utilizar as def main():'s no mesmo arquivo. Cada trecho é único.
#######

#2
"""
def is_fibonacci(n):
    if n < 0:
        return False

    def fibonacci_sequence(limit):
        sequence = [0, 1]
        while True:
            next_value = sequence[-1] + sequence[-2]
            if next_value > limit:
                break
            sequence.append(next_value)
        return sequence

    fibonacci_numbers = fibonacci_sequence(n)
    
    return n in fibonacci_numbers

def main():
    try:
        number = int(input("Número: "))
        if is_fibonacci(number):
            print(f"Sim, na sequência Fibonacci se tem o número  {number}")
        else:
            print(f"Não, não se tem o número {number} na sequência de Fibonacci.")
    except ValueError:
        print("Informe um número válido.")
"""

#3
"""
import json

def calcular_faturamento(faturamentos):
    
    faturamentos_validos = [f["valor"] for f in faturamentos if f["valor"] > 0]

    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)

    
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

    dias_acima_da_media = sum(1 for f in faturamentos_validos if f > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media //

def main():
    
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    
    faturamentos = dados["faturamento_diario"]

    
    menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(faturamentos)

    
    print(f"Menor valor de faturamento em um dia: {menor_faturamento}")
    print(f"Maior valor de faturamento ocorrido em um dia: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
"""

#4
"""
faturamentos = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamentos.values())

for estado, valor in faturamentos.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
"""

#5
"""
texto = "Texto normal" 

texto_invertido = ""

 for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
   
print(texto_invertido)
"""
