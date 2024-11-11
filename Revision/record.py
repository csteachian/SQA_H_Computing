# Records

from dataclasses import dataclass
@dataclass
class book:
    bookTitle : str = ''
    bookAuthor : str = ''
    bookPrice : float = 0.0
    bookStock : int = 0

# Array of records

books = [ book() for index in range(50) ] # 50 book records in this array