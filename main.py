from pokemon import pokemon as pk, attack as at
from game import main_menu as mm

# Creating Pokémon and assigning some attacks
POKEMONS = [
    pk.Pokemon("Alakazam", 800, [at.Attack("Confusion", 222, 1), at.Attack("Psybeam", 333, 0.75)]),
    pk.Pokemon("Blastoise", 850, [at.Attack("Flash Cannon", 300, 0.8), at.Attack("Water Gun", 200, 0.95)]),
    pk.Pokemon("Pikachu", 700, [at.Attack("Tail Whip", 200, 0.98), at.Attack("Electro Ball", 300, 0.9)]),
    pk.Pokemon("Golem", 1000, [at.Attack("Rock Throw", 150, 0.8), at.Attack("Earthquake", 200, 0.8)]),
    pk.Pokemon("Avonic", 888, [at.Attack("Camera Laser Beam", 250, 0.95)])
]

# Instantiating game object with created Pokémon and starting the game loop
GAME = mm.MainMenu(POKEMONS)
GAME.loop()