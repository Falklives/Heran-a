class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def frear(self):
        print("Veículo freou.")

    def acelerar(self):
        print("Veículo acelerou.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print("Porta do carro aberta.")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        print("Moto empinada.")

carro = Carro("Toyota", "Corolla", "Vermelho")
moto = Moto("Honda", "CBR 1000RR", 1000)

carro.frear()
carro.abrir_porta()

moto.acelerar()
moto.empinar()




