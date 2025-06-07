import sys
import pandas as pd 
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

phy=[40,40,40,39]
chem=[40,39,40,40]
maths=[40,40,39,40]
result=["Pass","Fail","Fail","Fail"]
status = [1,0,0,0]
df=pd.DataFrame({"PHY":phy,"CHEM":chem,"MATHS":maths,"RESULT":result,"STATUS":status})
resulttonumber = {'Fail': 0, 'Pass': 1}
numbertoresult = {0: 'Fail', 1: 'Pass'}

df['RESULT'] = df['RESULT'].map(resulttonumber)
print(df['RESULT'])


features = ['PHY', 'CHEM', 'MATHS']

x = df[features]
y = df['RESULT']
