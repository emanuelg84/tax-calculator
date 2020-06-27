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

current_state_bracket = 0

for i in agg_income1:
    if int(i['bracket']) < int(Income):
        a = float(i['tax_rate'])
        b = float(i['bracket']) - current_state_bracket
        c = a*b
        agg_state_income_tax = agg_state_income_tax + c
        current_state_bracket = int((i['bracket']))
        incremental_tax_state = (float(int(Income) - int((i['bracket']))) )* a


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

       
#print(str(current_fed_bracket) + " incremental: " + str((int(Income) - current_fed_bracket)))
#print(str(agg_fed_income_tax) + " incremental: " + str(incremental_tax_fed))  

print("Your federal tax is: ","$"+"{:,.2f}".format(agg_fed_income_tax+incremental_tax_fed))

total_taxes = agg_fed_income_tax+incremental_tax_fed+agg_state_income_tax+incremental_tax_state

net_income = float(Income) - total_taxes
net_monthly_income = net_income / 12

print("Your total tax is: ","$"+"{:,.2f}".format(total_taxes ))

print("Your annual net income is: ","$"+"{:,.2f}".format(net_income)+" and your monthly net income is: ","$"+"{:,.2f}".format(net_monthly_income))
print("")
print("----------------------------------------------------------------")
print("")

 ######################################################################################################


#                               Phase 2 - clculate state tax for each state


all_state_list = []
net_income_per_state=[]
unique_state = state

agg_income3 = []

for i, row in State_tax.iterrows():
    if row['State'] != unique_state:
        if row['State'] != "State":
            all_state_list.append(unique_state)
            unique_state = row['State']
             

#print(all_state_list)


for i in all_state_list:
    for j, row in State_tax.iterrows():
        if (row['State']) == i:
            h = {"bracket":row['Income'],"tax_rate":row['Tax rate']}
            agg_income3.append(h)
            #print(h)
        current_state_bracket = 0
        agg_state_income_tax = 0.00001        
    for k in agg_income3:
        if int(k['bracket']) < int(Income):
            a = float(k['tax_rate'])
            #print(a)
            b = float(k['bracket']) - current_state_bracket
            #print(b)
            c = a*b
            #print(c)
            agg_state_income_tax = agg_state_income_tax + c
            #print(agg_state_income_tax)
            current_state_bracket = int((k['bracket']))
            incremental_tax_state = (float(int(Income) - int((k['bracket']))) )* a
            total_state_tax = agg_state_income_tax + incremental_tax_state
            #print(total_state_tax)
    #print(total_state_tax)
    net_income_per_state.append({"state":i,"state_income_tax":"$"+"{:,.2f}".format(total_state_tax),"total taxes":"$"+"{:,.2f}".format(total_state_tax + agg_fed_income_tax+incremental_tax_fed),"net income":"$"+"{:,.2f}".format(float(Income) - total_state_tax - agg_fed_income_tax - incremental_tax_fed)})
        
    
    
#print(net_income_per_state.append)
 
        
chart_title = "Projected annual net income per state"

sorted_states = []
sorted_net_income = []

for d in net_income_per_state:
    sorted_states.append(d["net income"])
    sorted_net_income.append(d["state"])
   

plt.bar(sorted_states, sorted_net_income)
plt.title(chart_title)
plt.xlabel("Annual net income")
plt.ylabel("State")
plt.show()



