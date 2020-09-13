products = {
    "daffodil" : 0.35,
    "tulip" : 0.33,
    "crocus" : 0.25,
    "hyacinth" : 0.75,
    "bluebell" : 0.50

}

maryOrder = {
    "daffodil" : 50,
    "tulip" : 100,
    "crocus" : 0,
    "hyacinth" : 0,
    "bluebell" : 0

}

products["tulip"] = round(products["tulip"] * 1.25, 2)

maryOrder['hyacinth'] += 30

output ="You have purchased the following bulbs:\n\n"

costs = []
orders = []
for item in maryOrder:
    if maryOrder[item] != 0:
        code = (item[:3]).upper()
        costs.append(round(maryOrder[item] * products[item],2))
        orders.append('%-5s'%(code) + ' *' + '%4s'%(maryOrder[item]) + ' = $' + '%6.2f'%(costs[-1]))
        
orders = sorted(orders)

for order in orders:
    output += order + '\n'

totalCost = 0
for amount in costs:
    totalCost += amount

output += '\nThank you for purchasing ' + str(maryOrder['daffodil'] + maryOrder['hyacinth'] + maryOrder['tulip']) + ' bulbs from Bluebell Greenhouses\n' + "Your total comes to $" + '%6.2f'%(totalCost) + '.' 
print(output)
input()


'''
Exercise 1: Python Warm Up (must complete) 
Problem: Follow the steps below to create a program for Bluebell 
Greenhouses that prints a purchase receipt.  
In the process, practice using dictionaries and formatting strings. 
1. Bluebell Greenhouses sells the following Spring flower bulbs.  
Create a dictionary that stores this information.  
Which data should be the keys (must be unique), 
and which should be the values? Flower Bulb Name Price Per Bulb 
daffodil $ 0.35 tulip $ 0.33 crocus $ 0.25 hyacinth $ 0.75 bluebell $ 0.50 
 
2. Mary has a standing order with Bluebell Greenhouses for 50 
daffodil bulbs and 100 tulip bulbs every year.  
Create a new dictionary that stores this information.   
3. Demand for tulips this year has dramatically outpaced demand.  
As a result, the price of tulip bulbs has increased by 25%. 
Update the price of tulip bulbs in the appropriate dictionary.  
(Round the price per bulb to 2 decimal places.) 
 
4. This year, Mary would also like to try planting hyacinths.  
Add 30 hyacinth bulbs to the dictionary that is storing her order. 
 
5.  Display Mary’s purchase order for this year on the screen.  
Each line should be formatted as follows: 
 
bulb code  * number of bulbs  =  $ subtotal field width: 5   field width: 4     field width: 6 left-aligned   right-aligned     right-aligned         2 decimal places single space 

where the code for each bulb name is the first three letters of its name, 
all in capital letters.  
The lines should be printed so that the bulb codes are in alphabetical order. 
 
6. Calculate the total number of bulbs that Mary purchased this year, 
as well as the total cost of her order.  
Include this information at the bottom of her purchase order.  
Format the total cost float value so that it is right-aligned in a field width of 6, 
with 2 decimal places. 
'''