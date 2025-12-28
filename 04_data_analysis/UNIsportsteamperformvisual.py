import matplotlib.pyplot as plt
import seaborn as sns

Teams = ['Basketball Team', 'Football Team', 'Cricket Team', 'Volleyball Team', 'Badminton Team']
Wins = [14, 10, 16, 12, 18]

plt.figure(figsize=(12,6))
plt.title("University Sports Teams Performance", fontsize=16)
sns.barplot(x=Teams, y=Wins, palette="Set2")

for i, w in enumerate(Wins):
    plt.text(i, w , str(w), ha='center', fontsize=12)

plt.xlabel("Sports Team", fontsize=14)
plt.ylabel("Matches Won", fontsize=14)
 
plt.show()
