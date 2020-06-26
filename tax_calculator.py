import pandas
import matplotlib.pyplot as plt
import os

Income = input("insert your annual salary: ")
state = input("insert the state you would like to analyse: ")
status = input("insert status (for single enter "s" for marreid enter "m"): ")

State_tax = pandas.read_csv(f'data/State_tax_{status}.csv')
Federal_tax = pandas.read_csv(f'data/Federal_tax_{status}.csv')