import battle_arena as bt
import input_helper as ih
import output_helper as oh
import os

# This class is responsible for showing the main menu
# It contains functionality for setting your main Pokémon and starting a new battle with another Pokémon
class Game:
    def __init__(self, pokemons):
        self.menu_options = ["Choose your main Pokémon", "Battle!", "Exit"]
        self.pokemons = pokemons
        self.battle_arena = bt.BattleArena()
        self.main_pokemon_index = None
        self.main_pokemon = None

    def loop(self):
        # The game loop shows the menu_options untill the player chooses to exit the game

        os.system("cls")
        oh.print_wait("~~~~~~~~~~~~ Welcome traveller! ~~~~~~~~~~~")

        while True:
            self.show_main_menu_options()

            chosen_main_menu_option_index = ih.get_number_from_user("Menu option", self.menu_options)

            if chosen_main_menu_option_index == 0:
                self.choose_main_pokemon()
            elif chosen_main_menu_option_index == 1:
                self.choose_opponent_pokemon()
            else:
                oh.print_wait("Thanx for playing this game ;)    - Max van Oord")
                break

    def choose_main_pokemon(self):
        # Show all Pokémon, choose the main and set the Pokémon attributes accordingly

        oh.print_wait("~~~~~~ Choose your Pokémon of choice! ~~~~~")
        self.show_pokemon()
        self.set_main_pokemon(ih.get_number_from_user("Pokémon", self.pokemons))
        os.system("cls")

    def set_main_pokemon(self, pokemon_index):
        self.main_pokemon_index = pokemon_index
        self.main_pokemon = self.pokemons[self.main_pokemon_index]

    def choose_opponent_pokemon(self):
        # Check if players main Pokémon is set, if so, show all available Pokémon to battle, choose opponent and enter battle arena
        if self.main_pokemon is not None:
            oh.print_wait("~~ Now choose your desired opponent to enter the Battle Arena! ~~")
            self.show_pokemon(self.main_pokemon_index)
            opponent_pokemon_index = ih.get_number_from_user("Pokémon", self.pokemons, self.main_pokemon_index)
            self.enter_battle_arena(opponent_pokemon_index)
            os.system("cls")
        else:
            oh.print_wait("~~ Choose your main Pokémon first! ~~")

    def enter_battle_arena(self, opponent_pokemon_index):
        # Starts a new battle inside the battle_arena object

        opponent_pokemon = self.pokemons[opponent_pokemon_index]
        self.battle_arena.new_battle(self.main_pokemon, opponent_pokemon)

    def show_main_menu_options(self):
        os.system("cls")
        print("~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~")
        print()

        for menu_option_index, menu_option in enumerate(self.menu_options):
            print(f"{menu_option_index + 1} - {menu_option}")

    def show_pokemon(self, index_to_skip = None):
        # The index to skip argument is used to skip the main Pokémon when choosing an opponent

        for pokemon_index, pokemon in enumerate(self.pokemons):
            if pokemon_index == index_to_skip:
                continue

            print()
            print(f"{pokemon_index + 1} - {pokemon.name} (HP {pokemon.static_hit_points})")
            pokemon.show_attacks(False)