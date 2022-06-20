# from shelve import Shelf


print("This is Mama Kila's shop")

shelf={"Pkts of Milk":90,"Bread":75,"1kg Omo":30,"1kgJembe":45}

price_shelf={"1pkt of Milk":50,"Bread":50,"1kg Omo":30,"1kgJembe":150}
print(f"Mama Kila has this items in her shelf {shelf}")
print("1pkt of Milk is  @50,Bread is @50 ,1kg Omo is @30,1kgJembe is @150")

print("You can buy an item")
print("You can also remove the item you bought,if it doesn't suit you.")
price=list(shelf.values())

#print the two options belonging to shop
#request user for their option
#create empty list for customer
#request for type and number of items
#loop through the values of the dictionary and multiply price and number
#create empty list for customer
#append the amount of money they spent
def shopping():
    option1=str(input("Do wish to buy an item? "))
    # option2=str(input("Do you wish to remove an item? "))
    option3=str(input("Do you wish to see the items we have"))
    if option1=="yes" or "Yes":
        quest1=str(input("Which item would you like to buy instead? "))
        if quest1=="Milk" or "milk":
            print("1pkt of Milk is  @50,Bread is @50 ,1kg Omo is @30,1kgJembe is @150")
            questfour=int(input("How many would packets of milk would you like to buy? "))
            price=list(price_shelf.values())
            # for i in price:
            z=price[0]*questfour
            customer=[]
            customer.append(z)
            print(f"your list is {customer}")
            print(f"That would be sh{z} ")
            pressing=int(input("Press 1 if you want to remove item from list "))
            if pressing==2:
                customer.pop(0)
            elif pressing==0:
                 option4=str(input("Do wish to buy another item? "))
            if option4=="yes" or "Yes":
               quest5=str(input("Which item would you like to buy instead? "))
               if quest5=="bread" or "Bread":
                 print("1pkt of Milk is  @50,Bread is @50 ,1kg Omo is @30,1kgJembe is @150")
                 questsix=int(input("How many would loaves of bread  would you like to buy? "))
                 price=list(price_shelf.values())
            # for i in price:
                 p=price[1]*questsix
                 customer=[]
                 customer.append(p)
                 print(f"your list is {customer}")
                 print(f"That would be sh{p} ")
            pressing=int(input("Press 1 if you want to remove item from list "))
            if pressing==2:
                customer.pop(1)
            option4=str(input("Do wish to buy another item? "))
            if option4=="yes" or "Yes":
               quest5=str(input("Which item would you like to buy instead? "))
               if quest5=="omo" or "Omo":
                 print("1pkt of Milk is  @50,Bread is @50 ,1kg Omo is @30,1kgJembe is @150")
            questseven=int(input("How many satchets of omo  would you like to buy? "))
            price=list(price_shelf.values())
            # for i in price:
            w=price[2]*questseven
            customer=[]
            customer.append(w)
            print(f"your list is {customer}")
            print(f"That would be sh{w} ")
            pressing=int(input("Press 2 if you want to remove item from list "))
            if pressing==2:
                customer.pop(1)
            elif pressing==0:
                option4=str(input("Do wish to buy another item? "))
            if option4=="yes" or "Yes":
               quest5=str(input("Which item would you like to buy instead? "))
               if quest5=="jembe" or "1kgJembe":
                 print("1pkt of Milk is  @50,Bread is @50 ,1kg Omo is @30,1kgJembe is @150")
            questeight=int(input("How many 1kg of Jembe flour  would you like to buy? "))
            price=list(price_shelf.values())
            # for i in price:
            x=price[3]*questeight
            customer=[]
            customer.append(x)
            # print(f"your list is {customer}")
            print(f"That would be sh{x} ")
            pressing=int(input("Press 2 if you want to remove item from list "))
            if pressing==2:
                customer.pop(2)
            elif pressing==0:
              
                #   customer=[]
                  customer.append(x)
                  print(f"your list is {customer}")
                  print(f"That would be sh{x} ")
            # pressing=int(input("Press 1 if you want to remove item from list "))
            # if pressing==2:
            #     customer.pop(3)
            print(f"this is your final list {customer}")
            purple=sum(customer)
            print(f"Your bill is {purple}")
shopping()
# shopping()
#create a for loop and loop through the whole shelf
#Request for users input 
# If milk:ask for the number 
# if i is Bread 


#how can we append many items in list.
            


