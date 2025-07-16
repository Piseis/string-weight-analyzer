class StringProcessor:

    @staticmethod
    def calculate_weight(string):
        letters = sum(c.isalpha for c in string)
        numbers = sum(c.isdigit for c in string)
        spaces = string.count(' ')

        return (letters * 1.5 + numbers * 2) / spaces
    