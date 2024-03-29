import random


def random_select(select_el):
    # Get all the options and count it
    number_of_options = len(select_el.options) - 1
    # Limit options to 10 to save time
    limit_options = number_of_options if number_of_options <= 10 else 10
    # Random select
    idx = random.randint(1, limit_options)
    select_el.select_by_index(idx)