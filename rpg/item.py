class Item():
    def __init__(self, item_name, item_rarity):
        self.name = item_name
        self.description = ""
        self.rarity = item_rarity

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_description(self, desctription):
        self.description = desctription

    def get_rarity(self):
        return self.rarity

    def describe(self):
        print(self.rarity+" item")
        print(self.description)