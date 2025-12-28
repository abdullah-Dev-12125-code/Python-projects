import matplotlib.pyplot as plt
import seaborn as sns

teams = ['Tigers', 'Lions', 'Eagles', 'Sharks', 'Wolves']
wins = [18, 22, 15, 25, 20]
colors = []

for w in wins:
    if w == max(wins):
        colors.append("red")   
    else:
        colors.append("blue")  

sns.barplot(x=teams, y=wins, palette=colors)

for i, w in enumerate(wins):
    plt.text(i, w + 0.5, w, ha='center') 

plt.xlabel("Teams")
plt.ylabel("Games Won")
plt.title("Basketball Team Performance - Last Season")
plt.show()
