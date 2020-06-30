***Income tax calculator***
The purpose of this program is to calculate federal and state tax for a given annual income, marital status and current jurisdiction and provide a view of the user’s net income under different tax jurisdictions in the US using graphs and charts 

***Identifying a need***
The tax structure in the US is very complex and varies from sate to state. When an individual is considering a job offer, the tax is significant consideration and might have a greater impact on the individual net earnings. This program provides a calculation of the individual current tax burden and overview of the taxes the individual will in different state. 
I believe that in the current environment where working remotely became essential and probably is the new reality, individuals will consider to move to different states to avoid heavily populated places and decrease costs of living. Tax savings is a significant consideration. Therefore, I believe that the tool I developed will provide insights to users on the tax impact related to their potential relocation as well as a user friendly tool to calculate total taxes in their current location 

***User inputs***
The user is required to provide his annual income, the state where he/she currently resides and filing status (s = single, m= married)

The program will make sure the inputs of state and filing status are valid

***Outputs***
The program will calculate the total tax comprised of federal and state, based on the inputs provided. Moreover, the program will present view of the user net income under different jurisdictions. 

***Creating and activating a virtual environment using Anaconda***
Open Command Prompt and inset the following: 
conda create -n final_project-env python=3.7 # (first time only)
conda activate final_project-env

***Installing package dependencies using Pip***
In command Prompt, insert the following
pip install pandas 
pip install matplotlib
pip install plotly 
pip install altair 
