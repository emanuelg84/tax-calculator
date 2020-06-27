import pandas
import matplotlib.pyplot as plt
import os

Income = input("insert your annual salary: ")
state = input("insert the state you would like to analyse (in capital letters): ")
status = input("insert status (for single enter the lettter s for marreid enter the letter m): ")

State_tax = pandas.read_csv(f'data/State_tax_{status}.csv', names = ['State','Income',"Tax rate"])
Federal_tax = pandas.read_csv(f'data/Federal_tax_{status}.csv',names = ['Income level',"Tax rate"])

agg_income1 = []
agg_income2 = []

for i, row in State_tax.iterrows():
    if (row['State']) == state:
        d = {"bracket":row['Income'],"tax_rate":row['Tax rate']}
        agg_income1.append(d)
        print(d)

agg_income_tax = 0.00001

for i in agg_income1:
    if int(i['bracket']) < int(Income):
        a = float(i['tax_rate'])
        b = float(i['bracket'])
        c = a*b
        agg_income_tax = agg_income_tax + c


for i, row in Federal_tax.iterrows():
    if (row['Income level']) != "Income level":
        e = {"bracket":row['Income level'],"tax_rate":row['Tax rate']}
        agg_income2.append(e)
        print(e)




for i in agg_income2:
    if int(i['bracket']) < int(Income):
        x = float(i['tax_rate'])
        y = float(i['bracket'])
        z = x*y
        agg_income_tax = agg_income_tax + z
    




print(str(agg_income_tax))


 