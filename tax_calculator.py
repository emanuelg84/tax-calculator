import pandas
import matplotlib.pyplot as plt
import os


Income = input("insert your annual salary in dollars: ")

status = input("insert status (for single enter the lettter 's' for marreid enter the letter 'm'): ")

## making sure a valid martial status was inserted


while status != "s" or status !="m":
    status = input("You inserted invalid value, please insert status (for single enter the lettter 's' for marreid enter the letter 'm'): ")
    if status == "s" or status == "m":
        break


State_tax = pandas.read_csv(f'data/State_tax_{status}.csv', names = ['State','Income',"Tax rate"])
Federal_tax = pandas.read_csv(f'data/Federal_tax_{status}.csv',names = ['Income level',"Tax rate"])


state = input("insert the abbreviation of the state you would like to analyse (in capital letters): ")

## making sure the state input exist in the database
check_state = "not_ok"

for i, row in State_tax.iterrows():
    if row['State'] == state:
        check_state = "ok"
    
while check_state != "ok":
    state = input("You inserted invalid value, insert the abbreviation of the state you would like to analyse (in capital letters): ")
    for i, row in State_tax.iterrows():
        if row['State'] == state:
            check_state = "ok"                 
    if check_state == "ok":
        break



agg_income1 = []
agg_income2 = []

for i, row in State_tax.iterrows():
    if (row['State']) == state:
        d = {"bracket":row['Income'],"tax_rate":row['Tax rate']}
        agg_income1.append(d)
        
agg_state_income_tax = 0.00001
incremental_tax_state=0
current_state_bracket = 0
Total_state_tax=0

for i in agg_income1:
    if int(i['bracket']) < int(Income):
        a = float(i['tax_rate'])
        b = float(i['bracket']) - current_state_bracket
        c = a*b
        agg_state_income_tax = agg_state_income_tax + c
        current_state_bracket = int((i['bracket']))
        incremental_tax_state = (float(int(Income) - int((i['bracket']))) )* a

print("****************************************************************")

print("Your state income tax is: ","$"+"{:,.2f}".format(agg_state_income_tax+incremental_tax_state))


for i, row in Federal_tax.iterrows():
    if (row['Income level']) != "Income level":
        e = {"bracket":row['Income level'],"tax_rate":row['Tax rate']}
        agg_income2.append(e)
        
agg_fed_income_tax = 0.00001
agg_fed_income = 0
current_fed_bracket = 0

for i in agg_income2:
    if int(i['bracket']) < int(Income):
        x = float(i['tax_rate'])
        y = float(i['bracket']) - current_fed_bracket
        z = x*y
        agg_fed_income_tax = agg_fed_income_tax + z
        agg_fed_income = agg_fed_income + int((i['bracket']))
        current_fed_bracket = int((i['bracket']))
        incremental_tax_fed = (float(int(Income) - int((i['bracket']))) )* x

       


print("Your federal tax is: ","$"+"{:,.2f}".format(agg_fed_income_tax+incremental_tax_fed))

total_taxes = agg_fed_income_tax+incremental_tax_fed+agg_state_income_tax+incremental_tax_state

net_income = float(Income) - total_taxes
net_monthly_income = net_income / 12

print("Your total tax is: ","$"+"{:,.2f}".format(total_taxes ))
print("****************************************************************")
print("Your annual net income is: ","$"+"{:,.2f}".format(net_income)+" and your monthly net income is: ","$"+"{:,.2f}".format(net_monthly_income))
print("")
print("----------------------------------------------------------------")
print("")



 ######################################################################################################

show = input("Please click any key to show net income in other states: ")
#                              Phase 2 - clculate state tax for each state

total_state_tax = 0

all_state_list = []
net_income_per_state=[]
unique_state = state

agg_income3 = []

for i, row in State_tax.iterrows():
    if row['State'] != unique_state:
        if row['State'] != "State":
            all_state_list.append(unique_state)
            unique_state = row['State']
             


for i in all_state_list:
    for j, row in State_tax.iterrows():
        if (row['State']) == i:
            h = {"bracket":row['Income'],"tax_rate":row['Tax rate']}
            agg_income3.append(h)
            
        current_state_bracket = 0
        agg_state_income_tax = 0.00001        
    for k in agg_income3:
        if int(k['bracket']) < int(Income):
            a = float(k['tax_rate'])
            
            b = float(k['bracket']) - current_state_bracket
           
            c = a*b
            
            agg_state_income_tax = agg_state_income_tax + c
            
            current_state_bracket = int((k['bracket']))
            incremental_tax_state = (float(int(Income) - int((k['bracket']))) )* a
            total_state_tax = agg_state_income_tax + incremental_tax_state
            
    net_income_per_state.append({"state":i,"state_income_tax":"$"+"{:,.2f}".format(total_state_tax),"total taxes":"$"+"{:,.2f}".format(total_state_tax + agg_fed_income_tax+incremental_tax_fed),"net income":"$"+"{:,.2f}".format(float(Income) - total_state_tax - agg_fed_income_tax - incremental_tax_fed)})
        
    
    
        
chart_title = "Projected annual net income per state"

sorted_states = []
sorted_net_income = []

for d in net_income_per_state:
    sorted_states.append(d["state"])
    sorted_net_income.append(d["net income"])

sorted_net_income.sort()
sorted_states.sort()


plt.bar(sorted_states,sorted_net_income)
plt.title(chart_title)
plt.xlabel("State")
plt.ylabel("net income")
plt.show()


