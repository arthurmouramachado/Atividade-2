
"""
Lista de Exercícios POO - Versão Orientada a Objetos
"""

import math

class Terreno:
    """2.1 Problema 'terreno'"""
    def __init__(self):
        self.largura = float(input("Digite a largura do terreno: "))
        self.comprimento = float(input("Digite o comprimento do terreno: "))
        self.valor_metro = float(input("Digite o valor do metro quadrado: "))
    
    def calcular(self):
        area = self.largura * self.comprimento
        preco = area * self.valor_metro
        print(f"Area do terreno = {area:.2f}")
        print(f"Preco do terreno = {preco:.2f}")


class Retangulo:
    """2.2 Problema 'retangulo'"""
    def __init__(self):
        self.base = float(input("Base do retangulo: "))
        self.altura = float(input("Altura do retangulo: "))
    
    def calcular(self):
        area = self.base * self.altura
        perimetro = 2 * (self.base + self.altura)
        diagonal = math.sqrt(self.base**2 + self.altura**2)
        print(f"AREA = {area:.4f}")
        print(f"PERIMETRO = {perimetro:.4f}")
        print(f"DIAGONAL = {diagonal:.4f}")


class Idades:
    """2.3 Problema 'idades'"""
    def __init__(self):
        print("Dados da primeira pessoa:")
        self.nome1 = input("Nome: ")
        self.idade1 = int(input("Idade: "))
        
        print("Dados da segunda pessoa:")
        self.nome2 = input("Nome: ")
        self.idade2 = int(input("Idade: "))
    
    def calcular(self):
        media = (self.idade1 + self.idade2) / 2
        print(f"A idade média de {self.nome1} e {self.nome2} é de {media:.1f} anos")


class Soma:
    """2.4 Problema 'soma'"""
    def __init__(self):
        self.x = int(input("Digite o valor de X: "))
        self.y = int(input("Digite o valor de Y: "))
    
    def calcular(self):
        soma = self.x + self.y
        print(f"SOMA = {soma}")


class Troco:
    """2.5 Problema 'troco'"""
    def __init__(self):
        self.preco = float(input("Preço unitário do produto: "))
        self.quantidade = int(input("Quantidade comprada: "))
        self.dinheiro = float(input("Dinheiro recebido: "))
    
    def calcular(self):
        troco = self.dinheiro - (self.preco * self.quantidade)
        print(f"TROCO = {troco:.2f}")


class Circulo:
    """2.6 Problema 'circulo'"""
    def __init__(self):
        self.raio = float(input("Digite o valor do raio do circulo: "))
    
    def calcular(self):
        area = math.pi * self.raio**2
        print(f"AREA = {area:.3f}")


class Pagamento:
    """2.7 Problema 'pagamento'"""
    def __init__(self):
        self.nome = input("Nome: ")
        self.valor_hora = float(input("Valor por hora: "))
        self.horas = int(input("Horas trabalhadas: "))
    
    def calcular(self):
        pagamento = self.valor_hora * self.horas
        print(f"O pagamento para {self.nome} deve ser {pagamento:.2f}")


class Consumo:
    """2.8 Problema 'consumo'"""
    def __init__(self):
        self.distancia = float(input("Distancia percorrida: "))
        self.combustivel = float(input("Combustível gasto: "))
    
    def calcular(self):
        consumo = self.distancia / self.combustivel
        print(f"Consumo medio = {consumo:.3f}")


class Medidas:
    """2.9 Problema 'medidas'"""
    def __init__(self):
        self.a = float(input("Digite a medida A: "))
        self.b = float(input("Digite a medida B: "))
        self.c = float(input("Digite a medida C: "))
    
    def calcular(self):
        quadrado = self.a ** 2
        triangulo = (self.a * self.b) / 2
        trapezio = ((self.a + self.b) * self.c) / 2
        print(f"AREA DO QUADRADO = {quadrado:.4f}")
        print(f"AREA DO TRIANGULO = {triangulo:.4f}")
        print(f"AREA DO TRAPEZIO = {trapezio:.4f}")


class Duracao:
    """2.10 Problema 'duracao'"""
    def __init__(self):
        self.segundos = int(input("Digite a duracao em segundos: "))
    
    def calcular(self):
        horas = self.segundos // 3600
        resto = self.segundos % 3600
        minutos = resto // 60
        segundos = resto % 60
        print(f"{horas}:{minutos}:{segundos}")


# Menu principal para executar os exercícios
def main():
    while True:
        print("\n" + "="*50)
        print("LISTA DE EXERCÍCIOS POO".center(50))
        print("="*50)
        print("1. Problema 'terreno'")
        print("2. Problema 'retangulo'")
        print("3. Problema 'idades'")
        print("4. Problema 'soma'")
        print("5. Problema 'troco'")
        print("6. Problema 'circulo'")
        print("7. Problema 'pagamento'")
        print("8. Problema 'consumo'")
        print("9. Problema 'medidas'")
        print("10. Problema 'duracao'")
        print("0. Sair")
        print("="*50)
        
        opcao = input("Escolha um exercício (1-10) ou 0 para sair: ")
        
        if opcao == '0':
            print("Programa encerrado.")
            break
        
        exercicios = {
            '1': Terreno,
            '2': Retangulo,
            '3': Idades,
            '4': Soma,
            '5': Troco,
            '6': Circulo,
            '7': Pagamento,
            '8': Consumo,
            '9': Medidas,
            '10': Duracao
        }
        
        try:
            exercicio = exercicios[opcao]()
            exercicio.calcular()
        except KeyError:
            print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
