class StringProcessor:
    """
    A utility class for processing strings according to specific metric rules.
    
    Provides static methods for:
    - Calculating string weight based on character composition
    - Detecting invalid string patterns (double 'a's)
    """

    @staticmethod
    def calculate_weight(string: str) -> float:
        """
        Calculate the weighted metric for a given string.
        
        The formula is: (letters * 1.5 + numbers * 2) / spaces
        
        Args:
            string (str): The input string to be evaluated
            
        Returns:
            float: Calculated weight. Returns 0 if string contains no spaces.
            
        Example:
            >>> StringProcessor.calculate_weight("abc 123")
            10.5  # (3*1.5 + 3*2)/1
        """
        letters = sum(c.isalpha() for c in string)
        numbers = sum(c.isdigit() for c in string)
        spaces = string.count(' ')

        if spaces == 0:
            return 0

        return (letters * 1.5 + numbers * 2) / spaces
    
    @staticmethod
    def has_double_a(string: str) -> bool:
        """
        Check if string contains any variation of double 'a' (case insensitive).
        
        Args:
            string (str): The string to check
            
        Returns:
            bool: True if 'aa', 'AA', 'aA', or 'Aa' is found, False otherwise
            
        Example:
            >>> StringProcessor.has_double_a("sample Aa string")
            True
            >>> StringProcessor.has_double_a("normal string")
            False
        """
        return 'aa' in string.lower()