import full_regression as reg
x = [1, 2, 3, 4, 5, 6, 7]
y = [59, 31, 67, 62, 1,0,0]
reg = reg.RegressionPredict(x, y,"Kohli data in IPL 2025")
print(reg)
reg.plot("Plot Title", "Regression Plot", "X-axis", "Y-axis")
output = reg.predict([6, 7, 8])
print("predicted values for [6,7,8]")
print(reg)
reg.plot("virat_kohli_runs", "virat_kolhi_stacks", "innigs", "runs")
