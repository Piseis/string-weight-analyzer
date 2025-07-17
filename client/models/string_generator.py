import string
import random

class StringGenerator:
    """
    A class to generate random strings following specific rules.
    
    The generated strings will:
    - Contain only a-zA-Z0-9 and spaces
    - Have length between 50-100 characters
    - Contain 3-5 non-consecutive spaces
    - Never start or end with a space
    """

    def __init__(self):
        self.characters = string.ascii_letters + string.digits  # All allowed non-space characters
        self.space = ' '

    def generate_string(self) -> str:
        """
        Generate a single random string following all specified rules.
        
        Returns:
            str: A randomly generated string that meets all requirements.
            
        Algorithm:
            1. Determines random length (50-100) and space count (3-5)
            2. Selects random non-consecutive positions for spaces
            3. Builds the string ensuring no leading/trailing spaces
        """
        length = random.randint(50, 100)
        space_count = random.randint(3, 5)

        possible_positions = list(range(1, length - 1))
        space_positions = sorted(random.sample(possible_positions, space_count))

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