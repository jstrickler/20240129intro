class Character:
    def move(self, direction, num_units):
        pass

    def pick_up(self, item):
        pass

    def fight(self, opponent):
        pass

class Wizard(Character):
    def cast_spell(self):
        pass

class Fighter(Character):
    def fight(self):
        pass

class Knight(Fighter):
    def joust(self):
        pass

    def fight(self):
        super().fight()
        pass

class Mercenary(Fighter):
    def bludgeon(self):
        pass


k1 = Knight()
k2 = Knight()
result = k1.joust(k2)
new_location = k1.move('NW', 5)
k1.pick_up('thing')
c = k1.pack_contents()

