'''
Mrs.Raja is a miser to the core.She saves money even on petite things. One dayshe heard a discount offer announced in a shop. she wants to purchase lot of items to save her money. The discount is given only when atleast two items are bought. Since each item has different discount prices , she finds difficult to check the amount she has saved. So she approaches you to device a automated discount calculator to make her easy while billing. 

INPUT FORMAT:

Input consists of two floating point values denoting price of item1 and item2. 

The third input denotes the discount value in percentage. 

OUTPUT FORMAT: 

The output consists of three floating values denoting total amount, discounted price and amount saved.

 Sample Input

20.50

45.40

10

Sample Output

65.90
59.31
6.59
'''
item1=float(input())
item2=float(input())
dis=float(input())
total_amount=item1+item2
discounted_price=total_amount*(dis/100)
amount_saved=total_amount-discounted_price
print("{:.2f}".format(total_amount))
print("{:.2f}".format(discounted_price))
print("{:.2f}".format(amount_saved))
