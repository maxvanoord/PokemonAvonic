def get_number_from_user(topic, list_to_choose_from, cannot_choose_index = None):
    # This function is responsible for fetching an input number from the user
    # The number cannot not extend the limits of the list to choose from
    # The number cannot be the same as cannot_choose_index
    print()

    while True:
        console_in = input(f"Choose {topic} (by number) > ")
        try:
            chosen_index = int(console_in) -1
            if chosen_index != cannot_choose_index and -1 < chosen_index < len(list_to_choose_from):
                return chosen_index
            else:
                raise ValueError
        except ValueError:
            print(f"[Please provide a valid {topic} number]")