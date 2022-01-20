# implementa __init__( name , tipo , golosinas ):
class Pet:
    def __init__(self, name = "Mr. Nibbles", kind = "Cat", candies = [], health = 10, energy = 10):
        self.name = name
        self.kind = kind
        self.candies = candies
        self.health = health
        self.energy = energy
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
    def sleep(self):
        self.energy += 25
        return self
# comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
# jugar() - incrementa la salud de la mascota en 5
    def play(self):
        self.health += 5
        return self
# sonido() - imprime el sonido que produce la mascota
    def sound(self):
        print("This is the sound of your pet")
        return self