orders = ["Masala", "ginger"]

# print(order[2])
# # frist errr is index and  keyError, ZeroDivisonError , typeerror , 

def process_order(item, quantity):
    try:
        price= {"masala":20}[item]
        cost = price* quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("QUantity must be in number")


process_order("ginger",2)
process_order("masala","two")