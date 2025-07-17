class StringProcessor:

    @staticmethod
    def calculate_weight(string):
        
        letters = sum(c.isalpha() for c in string)
        numbers = sum(c.isdigit() for c in string)
        spaces = string.count(' ')

        if spaces == 0:
            return 0

        return (letters * 1.5 + numbers * 2) / spaces
    