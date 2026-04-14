from account import user_interface

user_interface.display_title()
account = user_interface.prompt_info()
while account.logged_in:
    user_interface.prompt_logged_in(account)
