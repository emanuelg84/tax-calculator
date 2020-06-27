import pandas
import matplotlib.pyplot as plt
import os

Income = input("insert your annual salary: ")
state = input("insert the state you would like to analyse (in capital letters): ")
status = input("insert status (for single enter the lettter s for marreid enter the letter m): ")

State_tax = pandas.read_csv(f'data/State_tax_{status}.csv', names = ['State','Income',"Tax rate"])
Federal_tax = pandas.read_csv(f'data/Federal_tax_{status}.csv',names = ['Income level',"Tax rate"])

agg_income = []

for i, row in State_tax.iterrows():
    if (row['State']) == state:
        d = {"bracket":row['Income'],"tax_rate":row['Tax rate']}
        agg_income.append(d)


float(agg_income_int = 0)

for i in agg_income:
    #print(type(i['tax_rate']))
    b = ((float(i['bracket']) * float(i['tax_rate']))
    agg_income_int = agg_income_int + b
    #agg_income_int=agg_income_int+i['bracket']
    # print(str(int((i['bracket'])) * int(i['tax_rate'])))
    #agg_income_int = agg_income_int + (int(i['bracket']) * int(i['tax_rate']))

print(str(agg_income_int))

#for i in Federal_tax:  
    #print(Federal_tax["i"])   
 