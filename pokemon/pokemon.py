class Pokemon:
    # metod inicializador de la clase 
    def __init__(self, name, pokemonType, level, healthPoints, attackPoints):
       #atributos de los pokemones 
        self.name = name
        self.pokemonType = pokemonType
        self.level = level
        self.healthPoints = healthPoints
        self.attackPoints = attackPoints

#metodo que realiza un ataque 
    def attack(self, otherPokemon):
        """
        Realiza un ataque al otro pokemon y ajusta sus puntos de salud
        """
        print(f"{self.name} ataca a {otherPokemon.name} con {self.attackPoints} puntos de ataque")

        # caso de ataque bajo
        if self.attackPoints < otherPokemon.healthPoints / 2:
            otherPokemon.healthPoints -= 1
            print(f"el ataque es bajo. {otherPokemon.name} pierde 1 punto de salud")
        # caso de ataque fuerte
        elif self.attackPoints >= otherPokemon.healthPoints:
            otherPokemon.healthPoints -= int(otherPokemon.healthPoints * 0.2)
            print(f"el ataque es fuerte. {otherPokemon.name} pierde el 20% de su salud")
        # caso de ataque medio
        else:
            damage = max(2, (self.attackPoints - otherPokemon.healthPoints // 2) // 2)
            otherPokemon.healthPoints -= damage
            print(f"el ataque es medio. {otherPokemon.name} pierde {damage} puntos de salud")

        # evitar que la salud sea negativa
        if otherPokemon.healthPoints < 0:
            otherPokemon.healthPoints = 0

        print(f"salud de {otherPokemon.name} ahora es {otherPokemon.healthPoints}")

    # metdo para subir de nivel
    def levelUp(self):
        """
        Sube de nivel y mejora los atributos de salud y ataque
        """
        self.level += 1
        self.healthPoints += 2
        self.attackPoints += 3
        print(f"{self.name} sube al nivel {self.level}. salud aumentada a {self.healthPoints}, ataque aumentado a {self.attackPoints}")

# creacion de las instancias 
pokemon1 = Pokemon("pokemon1", "elctrico", 5, 30, 15)
pokemon2 = Pokemon("pokemon2", "fuego", 6, 35, 10)

print("estado inicial de los pokemones :")
print(f"{pokemon1.name} - tipo: {pokemon1.pokemonType}, nivel : {pokemon1.level}, salud: {pokemon1.healthPoints}, ataque: {pokemon1.attackPoints}")
print(f"{pokemon2.name} - tipo: {pokemon2.pokemonType}, nivel: {pokemon2.level}, salud : {pokemon2.healthPoints}, ataque : {pokemon2.attackPoints}\n")

# simulacion de un ataque
pokemon1.attack(pokemon2)
pokemon2.attack(pokemon1)

# subida de nivel a cada pokemon
pokemon1.levelUp()
pokemon2.levelUp()

print("\nestado final de los pokemones:")
print(f"{pokemon1.name} - tipo : {pokemon1.pokemonType}, nivel: {pokemon1.level}, salud: {pokemon1.healthPoints}, ataque: {pokemon1.attackPoints}")
print(f"{pokemon2.name} - tipo: {pokemon2.pokemonType}, nivel: {pokemon2.level}, salud: {pokemon2.healthPoints}, ataque : {pokemon2.attackPoints}")