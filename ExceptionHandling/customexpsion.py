# def drew_chai(flavor):
#     if flavor not in ["masala","ginger","elaichi"]:
#         raise ValueError("Unsopported chai flavor...")
#     print(f"brewing {flavor} chai...")

# drew_chai("mint")


class OutofIngredientsErrro(Exception):
    pass

def make_chai(milk, sugar):
    if milk ==0 or sugar ==0:
        raise OutofIngredientsErrro("Missing milk or sugar")
    print("chai is ready...")