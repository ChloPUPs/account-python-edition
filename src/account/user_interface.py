from .account import Account as _Account
from utils import input_no_space as _input_no_space

def display_title() -> None:
    print("--ACCOUNT v0.1.0 (py-edition)--")

def prompt_info() -> _Account:
    user_name = _input_no_space("User Name: ")
    display_name = input("Display Name: ")
    pass_word = _input_no_space("Password: ")
    email = _input_no_space("EMail: ")
    return _Account(user_name, display_name, pass_word, email)

def prompt_logged_in(account: _Account) -> None:
    print("\n(1) Display Info, (2) Post, (3) Log Out")
    user_input = input(": ")
    match user_input:
        case "1":
            account.display_info()
        case "2":
            print("\nWhat would you like to post?")
            post_input = input(": ")
            account.post(post_input)
        case "3":
            print("Goodbye! Logging out...")
            account.logged_in = False
        case _:
            print(f"Invalid Input: '{user_input}' is not an option")
