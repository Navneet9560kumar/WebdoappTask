# class sam:
#     pass

# print(type(sam))
# # this is a ssimple class and it it work like  if check the class is show  class so these it work 

# tap = sam()
# print(type(sam()))
# print(type(tap)is sam)
# # is opnly the how to make a class 

# class Chai:
#     origin = "India"

# print(Chai.origin)

# Chai.is_hot = True
# print(Chai.is_hot)

# # creating objecting from class 

# masala = Chai()
# print(masala.origin)
# print(masala.is_hot)


# this is 3 topic and this is Attribute


# class Chai:
#     temperature = "hot"
#     strength = "Strong"

# cutting = Chai()
# print(cutting.temperature)

# cutting.temperature = "Mild"
# print("After changing",cutting.temperature)
# print("Direct look into the class ", cutting.temperature)


# del cutting.temperature
# print(cutting.temperature)


# topic 4 selfargs

class Chaicup:
    size =150

    def describe(self):
        return f"A{self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe())