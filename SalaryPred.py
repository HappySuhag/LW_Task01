import pandas
ds = pandas.read_csv('SalaryData.csv')
x = ds[['YearsExperience']].values
y = ds['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.predict([[0]]))