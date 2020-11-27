#introductory statement explaining the situation to the user
intro = "**************************************\n\
**  Welcome to the Snakes Cafe!     **\n\
**  Please see our menu below.      **\n\
**\n\
** To quit at any time, type \"quit\" **\n\
**************************************"
print(f"{intro}\n")

#the full menu, split into categories
appetizers = ["Wings", "Spring Rolls"]
print(f"Appetizers\n----------\n{appetizers[0]}\n{appetizers[1]}\n")

entrees = ["Salmon","Steak","Meat Tornado", "A Literal Garden"]
print(f"Entrees\n----------\n{entrees[0]}\n{entrees[1]}\n{entrees[2]}\n{entrees[3]}\n")

desserts=["Ice Cream", "Cake", "Pie","Cookies"]
print(f"Desserts\n----------\n{desserts[0]}\n{desserts[1]}\n{desserts[2]}\n{desserts[3]}\n")

drinks=["Coffee","Tea","Unicorn Tears"]
print(f"Drinks\n----------\n{drinks[0]}\n{drinks[1]}\n{drinks[2]}\n")

#entire menu to iterate over for matching input items to menu items
menu=appetizers+entrees+desserts+drinks

#print the prompt to ask user to type in order
prompt = "***********************************\n\
** What would you like to order? **\n\
***********************************"
print(f"{prompt}")

#first customer order being placed
order = input("> ")
#counter to see how many times a customer ordered an item
counter=0
#go through the menu and match the item to the 
for item in menu:

    if item ==order:

        counter=counter+1
        print(f"> {item}\n** {counter} order of {item} have been added to your meal **")
#while the user has not quit, keep taking orders and adding to the counter if item repeats
while order !="quit":
    
    order = input("> ")
    
    for item in menu:
        
        if item ==order:
            
            counter=counter+1
            print(f"\n> {item}\n\n** {counter} order of {item} have been added to your meal **\n")