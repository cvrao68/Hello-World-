# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:26:18 2018

@author: Veer Rao
"""
global monthlyAmount, bal, minMonthlyAmount, maxMonthlyAmount
annualInterestRate = 0.2
monthlyRate = annualInterestRate / 12
balance = 320000
minMonthlyAmount = balance/12.0
maxMonthlyAmount = (balance*(1+monthlyRate)**12.0)/12
monthlyPaymentAmount = (minMonthlyAmount+maxMonthlyAmount)/2
def minPayment(bal, InterestRate, monthlyAmount):
    time = 0
    while time < 12:
        monthBalance = bal - monthlyAmount
        bal = monthBalance + (InterestRate/12) * monthBalance
        time += 1
    return monthlyAmount, bal
result, bal = minPayment(balance, annualInterestRate, monthlyPaymentAmount)
def check_bal (result,bal, minMonthlyAmount, maxMonthlyAmount):
    if bal <= -1.00:
        #minMonthlyAmount = balance/12
        maxMonthlyAmount = result
        monthlyPaymentAmount = (minMonthlyAmount+maxMonthlyAmount)/2
        result, bal = minPayment(balance, annualInterestRate, monthlyPaymentAmount)
        check_bal (result, bal, minMonthlyAmount, maxMonthlyAmount)
        return (result, bal)
    #print("Lowest Payment: " + str(round(result,2)))
    elif bal >= 1.00:
        minMonthlyAmount = result
        #maxMonthlyAmount = (balance*(1+monthlyRate)**12.0)/12
        monthlyPaymentAmount = (minMonthlyAmount+maxMonthlyAmount)/2
        result, bal = minPayment(balance, annualInterestRate, monthlyPaymentAmount)
        check_bal (result, bal, minMonthlyAmount, maxMonthlyAmount)
        return (result, bal)
    #print("Lowest Payment: " + str(round(result,2)))
    else:
        print("Lowest Payment: " + str(round(result,2)))
check_bal (result, bal, minMonthlyAmount, maxMonthlyAmount)
#print("Lowest Payment: " + str(round(result,2)))  
