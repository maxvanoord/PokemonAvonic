import os
import output_helper as oh
import random as rd
import input_helper as ih

# This class is responsible for the execution of a battle between two Pokémon
class BattleArena:
    def __init__(self):
        self.round = 0
        self.player_pokemon = None
        self.opponent_pokemon = None

    def new_battle(self, player_pokemon, opponent_pokemon):
        self.round = 0
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon

        self.loop()

    def end_battle(self):
        if self.player_pokemon.current_hit_points == 0:
            oh.print_wait(f"{self.player_pokemon.name} FAINTED!")
        else:
            oh.print_wait(f"{self.opponent_pokemon.name} FAINTED!")

        oh.print_wait("Press enter to exit the arena ")

    def loop(self):
        # A battle lasts untill one of the Pokémon fainted (has no hit points left)
        while self.player_pokemon.current_hit_points > 0 and self.opponent_pokemon.current_hit_points > 0:
            os.system("cls")
            self.show_battle_progress()

            if self.round % 2 == 0:
                oh.print_wait(f"{self.player_pokemon.name}'s turn! ")
                self.player_attacks()
            else:
                oh.print_wait(f"{self.opponent_pokemon.name}'s turn! ")
                self.opponent_attacks()

            self.round += 1

        os.system("cls")
        self.show_battle_progress()
        self.end_battle()

    def player_attacks(self):
        # Player chooses an attack from its main Pokémon and that attack is executed
        print()

        self.player_pokemon.show_attacks(True)

        chosen_attack_index = ih.get_number_from_user("Attack", self.player_pokemon.attacks)

        self.player_pokemon.attack(chosen_attack_index, self.opponent_pokemon)

    def opponent_attacks(self):
        # Simulates opponents attack by picking a random attack from Pokémon
        random_attack_index = rd.randint(0, len(self.opponent_pokemon.attacks) -1)

        self.opponent_pokemon.attack(random_attack_index, self.player_pokemon)

    def show_battle_progress(self):
        print(f"~~~~~~~~~~~~ <><> BATTLE ARENA <><> ~~~~~~~~~~~~")
        print()

        player_info = f"{self.player_pokemon.name} (HP {self.player_pokemon.current_hit_points}/{self.player_pokemon.static_hit_points})"
        opponent_info = f"{self.opponent_pokemon.name} (HP {self.opponent_pokemon.current_hit_points}/{self.opponent_pokemon.static_hit_points})"

        print(f"{player_info} .................. {opponent_info}")