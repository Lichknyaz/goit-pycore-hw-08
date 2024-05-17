class InvalidDateFormatError(ValueError):
    """Exception raised for invalid date format."""

    def __init__(self, message="Invalid date format. Use DD.MM.YYYY"):
        super().__init__(message)