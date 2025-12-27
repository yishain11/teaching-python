def get_non_empty_input(prompt):
    value = input(prompt).strip()
    if value == "":
        return None
    return value


def is_input_msg_allowed(message):
    return len(message) >= 3


def format_encrypted_output(username, encrypted_message):
    return f"User '{username}' encrypted message: {encrypted_message}"
