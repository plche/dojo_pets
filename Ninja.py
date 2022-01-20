from Pet import Pet

# implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
class Ninja:
    def __init__(self, first_name, last_name, awards, pet_food, pet = Pet()):
        self.first_name = first_name
        self.last_name = last_name
        self.awards = awards
        self.pet_food = pet_food
        self.pet = pet
# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def walk(self):
        self.pet.play()
        return self
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def feed(self):
        self.pet.eat()
        return self
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bathe(self):
        self.pet.sound()
        return self