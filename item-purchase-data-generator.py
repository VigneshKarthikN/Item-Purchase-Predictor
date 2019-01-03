import random as r
import csv

rows = []

for i in range(10001):  

    cust_score = r.randrange(1, 101) #cust score
    days_in_cart = r.randrange(1, 61) #days in cart
    purchase_hist = r.randrange(0, 2) #purchase history 0 = not purchased
    gender = r.randrange(0, 2) #0 = female, 1 = male
    rating = r.randrange(0, 6) #rating
    
    if cust_score > 80 or (cust_score > 60 and rating > 4 and (purchase_hist == 0 or days_in_cart < 20)):
        purchase = 1
    elif cust_score < 20 and rating < 3:
        purchase = 0
    else:
        purchase = r.randrange(0, 2)
        
    rows.append(str(i))
    rows.append(str(1500+i))
    rows.append(str(cust_score))
    rows.append(str(days_in_cart))
    rows.append(str(purchase_hist))
    if gender == 0:
        rows.append('female')
    else:
        rows.append('male')
    rows.append(str(rating))
    rows.append(str(purchase))
    
    with open('item-purchase-data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(rows)
    file.close()
    
    rows=[]
