import string
import random

class StringGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits
        self.space = ' '

    def generate_string(self):
        length = random.randint(50, 100)
        space_count = random.randint(3, 5)

        possible_positions = list(range(1, length - 1))
        space_positions = sorted(random.sample(possible_positions, space_count))

        # avoid consecutive spaces
        for i in range(1, len(space_positions)):
            if space_positions[i] - space_positions[i - 1] == 1:
                space_positions[i] += 1

        result = []
        for i in range(length):
            if i in space_positions:
                result.append(self.space)
            else:
                result.append(random.choice(self.characters))
        
        return ''.join(result)

        