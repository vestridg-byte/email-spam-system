class DatasetFileError(Exception):
    """Raised when the dataset file cannot be found or loaded."""
    pass

class DatasetColumnError(Exception):
    """Raised when required column are missing from the dataset."""
    pass
