class Movie:
    def __init__(self, title: str, year: int, age_group: int, description: str, rating: int, duration: int, genre: str):
        self.title = title 
        self.year = year 
        self.age_group = age_group 
        self.description = description 
        self.rating = rating 
        self.duration = duration 
        self.genre = genre
        
        
    def __str__(self):
        return f"{self.title}, {self.year}, {self.age_group}, {self.duration}, {self.genre}, {self.rating}"