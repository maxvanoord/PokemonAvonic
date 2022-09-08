import random as rd
import output_helper as oh

class Pokemon:
    def __init__(self, name, hit_points, attacks):
        self.name = name
        self.static_hit_points = hit_points
        self.current_hit_points = hit_points
        self.attacks = attacks

    def show_attacks(self, with_indexes):
        for index, attack in enumerate(self.attacks):
            if with_indexes:
                print(f"{index + 1} > {attack.name} ({attack.power})")
            else:
                print(f"- {attack.name} ({attack.power})")

    def attack(self, attack_index, opponent):
        # Used to withdraw the chosen attack power from the opponents hit points
        # If the random generated hit_number is within the attacks hit probability then it is a hit, otherwise it misses
        attack = self.attacks[attack_index]

        oh.print_wait(f"{self.name} uses {attack.name} ")

        random_hit_number = rd.random()

        if random_hit_number < attack.hit_probability:
            opponent.defend(attack)
            oh.print_wait(f"{attack.name} hits effectively! ")
        else:
            oh.print_wait(f"{attack.name} misses ")

    def defend(self, attack):
        # Do not let the hit points go beneath zero to keep a nice feedback to the player
        self.current_hit_points -= attack.power
        if self.current_hit_points < 0:
            self.current_hit_points = 0

    def restore_hit_points(self):
        self.current_hit_points = self.static_hit_points