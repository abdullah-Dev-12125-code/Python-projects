import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")

plt.title("Relationship Between Total Bill and Tips")
sns.scatterplot(
    data,
    x='total_bill',
    y='tip',
    hue='sex',
    palette={'Male':'blue','Female':'pink'}    
)
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip Amount ($)')
plt.show()