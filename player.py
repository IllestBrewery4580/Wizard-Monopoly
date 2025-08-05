class Player:
    def __init__(self, name, color, start_money=1500):
        self.name = name
        self.color = color # for token drawing
        self.money = start_money
        self.position = 0
        self.in_wizard_realm = False
        self.wizard_turns_remaining = 0
        self.properties = []

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size
        
    def pay(self, amount):
        self.money -= amount

    def recieve(self, amount):
        self.money += amount
