class User:
    def __init__(self, name: str, email: str, password: str, icon: str):
        self.name = name
        self.email = email
        self.password = password
        self.icon = icon
        
    def __str__(self):
        return f"{self.name}, {self.email}, {self.password}, {self.icon}"