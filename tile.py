class Tile:
    def __init(self, name, tile_type, price=0, rent=0, special_effect=None):
        self.name = name
        self.tile_type = tile_type # w.g. "property?, ?event", "portal"
        self.price = price
        self.rent = rent
        self.owner = None
        self.special_effect = special_effect # function to call on landing

    def is_available(self):
        return self.tile_type == "property" and self.owner is None
    
    def charge_rent(self, player):
        if self.owner and self.owner != player:
            player.pay(self.rent)
            self.owner.recieve(self.rent)
