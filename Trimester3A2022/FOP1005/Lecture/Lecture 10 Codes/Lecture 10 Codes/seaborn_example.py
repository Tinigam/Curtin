import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
budget = pd.read_csv("/home/tinigam/FOP1005/Lecture/Lecture 10 Codes/Lecture 10 Codes/budget.csv")
budget = budget.sort_values(by='Budget',ascending=False)[:10]
#This section of code sets the order, and styles the plot and bar chart colors:
sns.set_style("darkgrid")

bar_plot = sns.barplot(x=budget["Department"],y=budget["Budget"],
palette="muted", order=budget["Department"].tolist())
plt.xticks(rotation=90)
plt.show()