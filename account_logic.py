
from random import seed
from random import randint
import account


def is_unique_account_number(random_number):
    account_dict = account.fetch_one_with_account_number(random_number)
    if account_dict:
        return False
    else:
        return True


def generate_unique_account_number():
    seed(1)
    random_number = randint(11111, 55555)
    while not is_unique_account_number(random_number):
        random_number = randint(11111, 55555)

    return random_number


