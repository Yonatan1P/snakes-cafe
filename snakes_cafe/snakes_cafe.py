intro = "**************************************\n\
**  Welcome to the Snakes Cafe!     **\n\
**  Please see our menu below.      **\n\
**\n\
** To quit at any time, type \"quit\" **\n\
**************************************"
print(f"{intro}\n")
appetizers = ["Wings", "Spring Rolls"]
print(f"Appetizers\n----------\n{appetizers[0]}\n{appetizers[1]}\n")
entrees = ["Salmon","Steak","Meat Tornado", "A Literal Garden"]
print(f"Entrees\n----------\n{entrees[0]}\n{entrees[1]}\n{entrees[2]}\n{entrees[3]}\n")
desserts=["Ice Cream", "Cake", "Pie","Cookies"]
print(f"Desserts\n----------\n{desserts[0]}\n{desserts[1]}\n{desserts[2]}\n{desserts[3]}\n")
drinks=["Coffee","Tea","Unicorn Tears"]
print(f"Drinks\n----------\n{drinks[0]}\n{drinks[1]}\n{drinks[2]}\n")
menu=appetizers+entrees+desserts+drinks
print(menu)
prompt = "***********************************\n\
** What would you like to order? **\n\
***********************************"
print(f"{prompt}")
order = input("> ")
counter=0
for item in menu:
    if item ==order:
        counter=counter+1
        print(f"> {item}\n** {counter} order of {item} have been added to your meal **")
while order !="quit":
    order = input("> ")
    for item in menu:
        if item ==order:
            counter=counter+1
            print(f"\n> {item}\n\n** {counter} order of {item} have been added to your meal **\n")