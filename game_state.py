import random
from player import Player
from tile import Tile

class GameState:
    def __init__(self):
        self.players = []
        self.current_turn = 0
        self.tiles = self.create_board()

    def create_board(self):
        return [
            Tile("Start Portal", "start"),
            Tile("Ancient Porest", "property", price=100, rent=20),
            Tile("Time Rift", "portal", special_effect=self.enter_wizard_realm),
            Tile("Cursed Library", "property", price=120, rent=25),
            Tile("Mana Tax", "event", special_effect=self.lose_money_event),
            Tile("Enchanted Armory", "property", price=150, rent=30),
            Tile("Wizard's Gate", "portal", special_effect=self.enter_wizard_realm),
        ]
    
    def add_player(self, name, color):
        self.players.append(Player(name, color))

    def roll_dice(self):
        return random.randint(1, 6)
    
    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def handle_tile(self, player):
        tile = self.tiles[player.position]
        if tile.tile_type == "property":
            if tile.is_available() and player.money >= tile.price:
                tile.owner = player
                player.pay(tile.price)
                player.properties.append(tile)
            elif tile.owner and tile.owner != player:
                tile.charge_rent(player)
        elif tile.tile_type == "event" and tile.special_effect:
            tile.special_effect(player)
        elif tile.tile_type == "portal" and tile.special_effect:
            tile.special_effect(player)

    def lose_money_event(self, player):
        player.pay(50)

    def enter_wizard_realm(self, player):
        player.in_wizard_realm = True
        player.wizard_turns_remaining = 3
        print(f"{player.name} has been pilled into the Wizard Realm!")
