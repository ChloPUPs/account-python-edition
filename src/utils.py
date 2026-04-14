def input_no_space(prompt: str) -> str:
    user_input = ""
    valid_input = False
    while not valid_input:
        user_input = input(prompt)
        user_input = user_input.strip()
        if ' ' in user_input:
            print("Invalid Input: Input contains non-trailing/leading spaces.")
        else:
            valid_input = True
    return user_input
