import pandas
import matplotlib.pyplot as plt
import os

Income = input("insert your annual salary in dollars: ")
state = input("insert the abbreviation of the state you would like to analyse (in capital letters): ")
status = input("insert status (for single enter the lettter 's' for marreid enter the letter 'm'): ")

State_tax = pandas.read_csv(f'data/State_tax_{status}.csv', names = ['State','Income',"Tax rate"])
Federal_tax = pandas.read_csv(f'data/Federal_tax_{status}.csv',names = ['Income level',"Tax rate"])

agg_income1 = []
agg_income2 = []

for i, row in State_tax.iterrows():
    if (row['State']) == state:
        d = {"bracket":row['Income'],"tax_rate":row['Tax rate']}
        agg_income1.append(d)
        
agg_state_income_tax = 0.00001



for i in agg_income1:
    if int(i['bracket']) < int(Income):
        a = float(i['tax_rate'])
        b = float(i['bracket'])
        c = a*b
        agg_state_income_tax = agg_state_income_tax + c
        current_state_bracket = int((i['bracket']))
        incremental_tax_state = (float(int(Income) - int((i['bracket']))) )* a

#print(str(current_state_bracket) + " incremental: " + str((int(Income) - current_state_bracket)))
#print(str(agg_state_income_tax) + " incremental: " + str(incremental_tax_state))  
print("Your state income tax is: ","$"+"{:,.2f}".format(agg_state_income_tax+incremental_tax_state))


for i, row in Federal_tax.iterrows():
    if (row['Income level']) != "Income level":
        e = {"bracket":row['Income level'],"tax_rate":row['Tax rate']}
        agg_income2.append(e)
        
agg_fed_income_tax = 0.00001
agg_fed_income = 0

for i in agg_income2:
    if int(i['bracket']) < int(Income):
        x = float(i['tax_rate'])
        y = float(i['bracket'])
        z = x*y
        agg_fed_income_tax = agg_fed_income_tax + z
        agg_fed_income = agg_fed_income + int((i['bracket']))
        current_fed_bracket = int((i['bracket']))
        incremental_tax_fed = (float(int(Income) - int((i['bracket']))) )* x

       
#print(str(current_fed_bracket) + " incremental: " + str((int(Income) - current_fed_bracket)))
#print(str(agg_fed_income_tax) + " incremental: " + str(incremental_tax_fed))  

print("Your federal tax is: ","$"+"{:,.2f}".format(agg_fed_income_tax+incremental_tax_fed))

print("Your total tax is: ","$"+"{:,.2f}".format(agg_fed_income_tax+incremental_tax_fed+agg_state_income_tax+incremental_tax_state))
 