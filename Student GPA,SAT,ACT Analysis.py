import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###GPA calculator
lettertonumb = {'A':4.0,'A-':3.7,'B+':3.3,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.7,'D+':1.3,'D':1.0,'F':0.0}
numbclasses = int(input('How Many Classes?:'))
unwGPA = 0
wGPA = 0
for i in range(numbclasses):
    a = i+1
    classinput = input(f"Class {a}:").lower()
    gradeinput = input(f"Class {a} Grade:")
    unwGPA += lettertonumb[gradeinput]
    if 'ap ' in classinput or ' ap' in classinput:
        wGPA = wGPA + lettertonumb[gradeinput]+1.0
    elif ' hn' in classinput or 'hn ' in classinput:
        wGPA = wGPA + lettertonumb[gradeinput]+0.5
    else:
        wGPA += lettertonumb[gradeinput]
print(f"Your Unweighted GPA is:{unwGPA/numbclasses}")
print(f"Your Weighted GPA is:{wGPA/numbclasses}")
###Comparison
collegedata = pd.read_csv("AdmissionData.csv")
print('Data available for the following universities:Harvard, Princeton, Yale, Brown, MIT, Cornell, Columbia, UPenn, Stanford')
choosecollege = input('Choose a College:').lower()
collegeindex = {'harvard':0,'princeton':1, 'yale':2, 'brown':3, 'mit':4}
indexvalue = collegeindex[choosecollege]
###GPA
if pd.isna(collegedata['4.0 GPA'][indexvalue]):
    print('This university does not release data on GPA')
else:
    if unwGPA == 4.0:
        print(f"You have the same GPA as {collegedata['4.0 GPA'][indexvalue]} of applicants")
    elif 3.75 <= unwGPA <= 3.99:
        print(f"You have the same GPA as {collegedata['3.99-3.75 GPA'][indexvalue]} of applicants")
    elif 3.50 <= unwGPA <= 3.74:
        print(f"You have the same GPA as {collegedata['3.50-3.74 GPA'][indexvalue]} of applicants")
    elif 3.25 <= unwGPA <= 3.49:
        print(f"You have the same GPA as {collegedata['3.49-3.25 GPA'][indexvalue]} of applicants")
    elif 3.00 <= unwGPA <= 3.24:
        print(f"You have the same GPA as {collegedata['3.24-3.00 GPA'][indexvalue]} of applicants")
    elif 2.50 <= unwGPA <= 2.99:
        print(f"You have the same GPA as {collegedata['2.99-2.50 GPA'][indexvalue]} of applicants")
    elif 2.00 <= unwGPA <= 2.49:
        print(f"You have the same GPA as {collegedata['2.49-2.0 GPA'][indexvalue]} of applicants")
    elif 1.0 <= unwGPA <= 1.99:
        print(f"You have the same GPA as {collegedata['1.99-1.0 GPA'][indexvalue]} of applicants")
    elif unwGPA <= 1.0:
        print(f"You have the same GPA as {collegedata['Below 1.0 GPA'][indexvalue]} of applicants")
    if wGPA >= collegedata['Average GPA'][indexvalue]:
        print(f"Your GPA is {(wGPA - collegedata['Average GPA'][indexvalue]).round(2)} above the average GPA({collegedata['Average GPA'][indexvalue]})")
    if wGPA < collegedata['Average GPA'][indexvalue]:
        print(f"Your GPA is {(collegedata['Average GPA'][indexvalue] - wGPA).round(2)} below the average GPA({collegedata['Average GPA'][indexvalue]})")
###SAT
SATR = int(input('Enter SAT Reading Score:'))
SATM = int(input('Enter SAT Math Score:'))
SATRcolumns = ['SAT Reading and Writing 200-299','SAT Reading and Writing 300-399','SAT Reading and Writing 400-499','SAT Reading and Writing 500-599','SAT Reading and Writing 600-699','SAT Reading and Writing 700-800']
if 700 <= SATR <= 800:
    print(f"You have the same SAT Reading Score as {collegedata['SAT Reading and Writing 700-800'][indexvalue]} of applicants.")
elif 600 <= SATR <= 699:
    print(f"You have the same SAT Reading Score as {collegedata['SAT Reading and Writing 600-699'][indexvalue]} of applicants.")
elif 599 <= SATR <= 500:
    print(f"You have the same SAT Reading Score as {collegedata['SAT Reading and Writing 500-599'][indexvalue]} of applicants.")
elif 400 <= SATR <= 499:
    print(f"You have the same SAT Reading Score as {collegedata['SAT Reading and Writing 400-499'][indexvalue]} of applicants.")
elif 300 <= SATR <= 399:
    print(f"You have the same SAT Reading Score as {collegedata['SAT Reading and Writing 300-399'][indexvalue]} of applicants.")
elif 200 <= SATR <= 299:
    print(f"You have the same SAT Reading Score as {collegedata['SAT Reading and Writing 200-299'][indexvalue]} of applicants.")
SATMcolumns = ['SAT Math 200-299','SAT Math 300-399','SAT Math 400-499','SAT Math 500-599','SAT Math 600-699','SAT Math 700-800']
if 700 <= SATM <= 800:
    print(f"You have the same SAT Math as {collegedata['SAT Math 700-800'][indexvalue]} of applicants.")
elif 600 <= SATM <= 699:
    print(f"You have the same SAT Math as {collegedata['SAT Math 600-699'][indexvalue]} of applicants.")
elif 599 <= SATM <= 500:
    print(f"You have the same SAT Math as {collegedata['SAT Math 500-599'][indexvalue]} of applicants.")
elif 400 <= SATM <= 499:
    print(f"You have the same SAT Math as {collegedata['SAT Math 400-499'][indexvalue]} of applicants.")
elif 300 <= SATM <= 399:
    print(f"You have the same SAT Math as {collegedata['SAT Math 300-399'][indexvalue]} of applicants.")
elif 200 <= SATM <= 299:
    print(f"You have the same SAT Math as {collegedata['SAT Math 200-299'][indexvalue]} of applicants.")
Rvalues = []
Mvalues = []

for i in SATRcolumns:
    Rvalues.append(collegedata[i][indexvalue])
for j in SATMcolumns:
    Mvalues.append(collegedata[j][indexvalue])

###ACT
ACTR = int(input('Enter ACT Reading Score:'))
ACTRcol = ['ACT Reading 25th Percentile','ACT Reading 50th Percentile','ACT Reading 75th Percentile']
if pd.isna(collegedata['ACT Reading 25th Percentile'][indexvalue]):
    print('This university does not release data on ACT Reading')
elif ACTR < collegedata[('ACT Reading 25th Percentile')][indexvalue]:
    print("You are below the 25th Percentile")
else:
    for i in range(len(ACTRcol)-1):
        if collegedata[ACTRcol[i]][indexvalue] <= ACTR <= collegedata[ACTRcol[i+1]][indexvalue]:
            print(f"You are in the {ACTRcol[i]}")
            break
ACTE = int(input('Enter ACT English Score:'))
ACTEcol = ['ACT English 25th Percentile','ACT English 50th Percentile','ACT English 75th Percentile']
if pd.isna(collegedata['ACT English 25th Percentile'][indexvalue]):
    print('This university does not release data on ACT English')
elif ACTE < collegedata['ACT English 25th Percentile'][indexvalue]:
    print("You are below the 25th Percentile")
else:
    for i in range(len(ACTEcol)-1):
        if collegedata[ACTEcol[i]][indexvalue] <= ACTE <= collegedata[ACTEcol[i+1]][indexvalue]:
            print(f"You are in the {ACTEcol[i]}")
            break
ACTW = int(input('Enter ACT Writing Score:'))
ACTWcol = ['ACT Writing 25th Percentile','ACT Writing 50th Percentile','ACT Writing 75th Percentile']
if pd.isna(collegedata['ACT Writing 25th Percentile'][indexvalue]):
    print('This university does not release data on ACT Writing')
elif ACTW < collegedata['ACT Writing 25th Percentile'][indexvalue]:
    print("You are below the 25th Percentile")
else:
    for i in range(len(ACTWcol)-1):
        if collegedata[ACTWcol[i]][indexvalue] <= ACTW <= collegedata[ACTWcol[i+1]][indexvalue]:
            print(f"You are in the {ACTWcol[i]}")
            break
ACTM = int(input('Enter ACT Math Score:'))
ACTMcol = ['ACT Math 25th Percentile','ACT Math 50th Percentile','ACT Math 75th Percentile']
if pd.isna(collegedata['ACT Math 25th Percentile'][indexvalue]):
    print('This university does not release data on ACT Math')
elif ACTM < collegedata['ACT Math 25th Percentile'][indexvalue]:
    print("You are below the 25th Percentile")
else:
    for i in range(len(ACTMcol)-1):
        if collegedata[ACTMcol[i]][indexvalue] <= ACTM <= collegedata[ACTMcol[i+1]][indexvalue]:
            print(f"You are in the {ACTMcol[i]}")
            break
ACTS = int(input('Enter ACT Science Score:'))
ACTScol = ['ACT Science 25th Percentile','ACT Science 50th Percentile','ACT Science 75th Percentile']
if pd.isna(collegedata['ACT Science 25th Percentile'][indexvalue]):
    print('This university does not release data on ACT Science')
elif ACTS < collegedata['ACT Science 25th Percentile'][indexvalue]:
    print("You are below the 25th Percentile")
else:
    for i in range(len(ACTScol)-1):
        if collegedata[ACTScol[i]][indexvalue] <= ACTS <= collegedata[ACTScol[i+1]][indexvalue]:
            print(f"You are in the {ACTScol[i]}")
            break
Ravals = []
Eavals = []
Wavals = []
Mavals = []
Savals = []

for i in ACTRcol:
    Ravals.append(collegedata[i][indexvalue])
for i in ACTEcol:
    Eavals.append(collegedata[i][indexvalue])
for i in ACTWcol:
    Wavals.append(collegedata[i][indexvalue])
for i in ACTMcol:
    Mavals.append(collegedata[i][indexvalue])
for i in ACTScol:
    Savals.append(collegedata[i][indexvalue])

fig, (R,M) = plt.subplots(1,2, figsize=(10,5))
R.bar(SATRcolumns,Rvalues)
R.set_xticks(range(len(SATRcolumns)))
R.set_xticklabels(SATRcolumns, rotation=45)
R.set_title(choosecollege+' SAT Reading Percentages')
M.bar(SATMcolumns, Mvalues)
M.set_xticks(range(len(SATMcolumns)))
M.set_xticklabels(SATMcolumns, rotation=45)
M.set_title(choosecollege+' SAT Math Percentages')
plt.show()


fig, (Ra,Ea,Wa,Ma,Sa) = plt.subplots(1,5, figsize=(10,5))
Ra.bar(ACTRcol,Ravals)
Ra.set_xticks(range(len(ACTRcol)))
Ra.set_xticklabels(ACTRcol, rotation=45)
Ra.set_title(choosecollege+' ACT Reading Percentages')
######
Ea.bar(ACTEcol,Eavals)
Ea.set_xticks(range(len(ACTEcol)))
Ea.set_xticklabels(ACTEcol, rotation=45)
Ea.set_title(choosecollege+' ACT English Percentages')
#####
Wa.bar(ACTWcol,Wavals)
Wa.set_xticks(range(len(ACTWcol)))
Wa.set_xticklabels(ACTWcol, rotation=45)
Wa.set_title(choosecollege+' ACT Writing Percentages')
#####
Ma.bar(ACTMcol,Mavals)
Ma.set_xticks(range(len(ACTMcol)))
Ma.set_xticklabels(ACTMcol, rotation=45)
Ma.set_title(choosecollege+' ACT Math Percentages')
#####
Sa.bar(ACTScol,Savals)
Sa.set_xticks(range(len(ACTScol)))
Sa.set_xticklabels(ACTScol, rotation=45)
Sa.set_title(choosecollege+' ACT Science Percentages')
plt.show()