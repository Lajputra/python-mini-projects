
full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    
    stats = [strength, intelligence, charisma]
    if not all(isinstance(x, int) for x in stats):
        return "All stats should be integers"
    if any(x < 1 for x in stats):
        return "All stats should be no less than 1"
    if any(x > 4 for x in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    
    def make_bar(value):
        return "●" * value + "○" * (10 - value)
    
    
    return (
        f"{name}\n"
        f"STR {make_bar(strength)}\n"
        f"INT {make_bar(intelligence)}\n"
        f"CHA {make_bar(charisma)}"
    )
