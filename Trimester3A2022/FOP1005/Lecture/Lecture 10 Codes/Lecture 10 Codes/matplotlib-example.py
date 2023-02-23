import pandas as pd
import matplotlib.pyplot as plt

budget = pd.read_csv("/home/tinigam/FOP1005/Lecture/Lecture 10 Codes/Lecture 10 Codes/budget.csv")
plt.style.use = 'default' #can use in matplotlib too
budget.index = budget["Department"]
print(budget)
budget_plot = budget.plot(kind="bar",
						  title="MN Capital Budget - 2014",
						  legend=False)
fig = budget_plot.get_figure()
fig.savefig("2014-mn-capital-budget.png")