from dataclasses import dataclass

@dataclass
class Recipe():
    title : str
    ingredient : str
    minutes: int
    cost : float
    avgRating : float

recipes = [Recipe() for index in range(750)]
