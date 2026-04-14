class Account:
    def __init__(
        self,
        user_name: str,
        display_name: str,
        pass_word: str,
        email: str,
    ) -> None:
        self.user_name = user_name
        self.display_name = display_name
        self.pass_word = pass_word
        self.email = email
        self.logged_in = True

    def post(self, message: str) -> None:
        print("\nCreated new post!")
        print(f"{self.display_name}: {message}")
    
    def display_info(self) -> None:
        details_to_print = [
            f"\n\tUser Name: {self.user_name}",
            f"\n\tDisplay Name: {self.display_name}",
            f"\n\tPassword: {self.pass_word}",
            f"\n\tEMail: {self.email}",
        ]
        print(f"Account -> {{{"".join(details_to_print)}\n}}")
