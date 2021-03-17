## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],
                        [20.89,98.99,258.62,19.76,101.59],
                        [70.66,190.10,134.54,200.14,15.59],
                        [10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.

print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
print()
total = salesArray.sum()
print('Total sales: ', total)
print()

## Step 2: What was Superstore's smallest and largest sale? Print them.

print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

smallest_sale = np.min(salesArray)
largest_sale = np.max(salesArray)
print()
print("Smallest Sale: ", smallest_sale)
print('Largest Sale: ', largest_sale)
print()

## Step 3: Print an array that will show which sales are greater than or equal to $100.

print("-----------------------------------------------   STEP THREE  -----------------------------------------------")
print()
print('Sales greater than or equal to $100: ', salesArray[salesArray>=100])
print()

## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

print()
total_sales_each = np.sum(salesArray, axis=1)
for i in range(len(total_sales_each)):
    print('Register: ', i+1, 'Sale: ',total_sales_each)
print()

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. 
## Each sale is subject to a 2% credit card fee.
## Using the salesArray, create a new array that stores the 2% fee for each sale and register. 
## Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")

print()
credit_fees = [] 
for i in range(len(salesArray)):
    a = [] 
    for j in range(len(salesArray[0])):
        fee = .02 * salesArray[i][j]
        fee = round(fee, 2)
        a.append(fee)
    credit_fees.append(a)
total_fee = sum(map(sum, credit_fees))
for i in credit_fees:
    print(i)

print('Total fee: ', round(total_fee, 2))
print()

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. 
## Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")

print()
profit = []
for i in range(len(credit_fees)):
    b = []
    for j in range(len(credit_fees[0])):
        c = salesArray [i][j] - credit_fees[i][j]
        c = round(c, 2)
        b.append(c)
    profit.append(b)
total_profit = sum(map(sum, profit))
for i in profit:
    print(i)

print('Total Profit: ', total_profit)
print()

## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")

print()
second = np.sum(salesArray[1])
fourth = np.sum(salesArray[3])
second = round(second, 2)
fourth = round(fourth, 2)

print('2nd Registers Sales: ', second)
print('4th Registers Sales: ', fourth)
print() 

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. 
## Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([17.89,13.59,107.89,176.88,56.78])

'''
print()
salesArray = np.concatenate((salesArray, newRegister), axis=0)
print(salesArray)
print()
'''

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. 
## The sale should have been $20.14. Update the array to correct this error.
## Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")

print()
print('Before: ', salesArray[2][3])

salesArray[2][3] = 20.14
print('After: ', salesArray[2][3])

print()


