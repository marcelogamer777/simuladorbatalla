import random

class Personaje:
    def __init__(self, nombre, hp, ataque):
        self.nombre = nombre
        self.hp = hp
        self.ataque = ataque

    def atacar(self, otro_personaje):
        # Calcula el daño aleatorio basado en el ataque del personaje
        dano = random.randint(1, self.ataque)
        otro_personaje.hp -= dano
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {dano} puntos de daño.")
        print(f"{otro_personaje.nombre} ahora tiene {otro_personaje.hp} puntos de vida.\n")

class SimuladorBatalla:
    def __init__(self, personaje1, personaje2):
        self.personaje1 = personaje1
        self.personaje2 = personaje2

    def simular(self):
        print("¡Comienza la batalla!\n")
        turno = 1
        while self.personaje1.hp > 0 and self.personaje2.hp > 0:
            print(f"--- Turno {turno} ---")
            if turno % 2 != 0:
                self.personaje1.atacar(self.personaje2)
            else:
                self.personaje2.atacar(self.personaje1)
            turno += 1

        # Determina el ganador
        if self.personaje1.hp <= 0:
            print(f"\n{self.personaje2.nombre} ha ganado la batalla.")
        else:
            print(f"\n{self.personaje1.nombre} ha ganado la batalla.")

# Ejemplo de uso
personaje1 = Personaje("Guerrero", hp=100, ataque=20)
personaje2 = Personaje("Mago", hp=80, ataque=25)

batalla = SimuladorBatalla(personaje1, personaje2)
batalla.simular()
