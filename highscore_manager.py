def save_high_score(new_high_score):
    with open("highscore.txt", "w") as file:
        file.write(str(new_high_score))

def get_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0
