users = []
_next_id = 1


def generate_user_id():
    global _next_id

    generated_id = _next_id
    _next_id += 1

    return generated_id