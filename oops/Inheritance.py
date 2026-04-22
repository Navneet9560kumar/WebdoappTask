class BaseChai:
    def __init__(self):
        self.type = type_

    def prepare(self):
        print(f"Preaping{self.type} chai....")


class  MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")