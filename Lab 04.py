#Q1
print "steve and johns' list of groceries"

print '----------------------------------'

#a.
groceries = ['bananas','strawberries','apples','bread']

print groceries

groceries.insert(4,'champagne')

print groceries

print''

#b.
groceries.remove('bread')

print groceries

print''

#c.
grocery_aisle={'bananas':'b','strawberries':'s','apples':'a','champagne':'c'}

for i in grocery_aisle:

    print i,grocery_aisle[i]

print''    

#Q2
#b.
item_price = {'apple':'7.3','bananas':'5.5','bread':'1.0','carrots':'10.0','champagne':'20.90','strawberry':'32.6'}

for i in item_price:
    
    print i,item_price[i]

print''

#c.
item_price['strawberries'] = '63.43'

for i in item_price:
    
    print i,item_price[i]

print''
#d.
item_price['Chicken'] = '6.5'

for i in item_price:

    print i,item_price[i]
    
print''

#Q3
#b.
in_stock = ['apple','bananas','bread','carrots','champagne','strawberry']

for x in in_stock:

    print x

print''

#c. and d.
always_in_stock = ('apple','bananas','bread','carrots','champagne','strawberry')   

print 'Come to shoprite! we always sell: '

for j in always_in_stock:
    
    print j

print''


