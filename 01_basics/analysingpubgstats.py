import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV
file_path = "fake_pubg_20000_matches.csv"
df = pd.read_csv(file_path)

# Step 2: Basic exploration
print("First 5 rows of the dataset:")
print(df.head())
print("\nColumns in dataset:", df.columns)
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 3: Clean/format the data
# Example: Fill missing numeric values with 0
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Example: Standardize column names (lowercase, replace spaces with _)
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Step 4: Organize key stats
# Let's say we focus on kills, damage dealt, and match wins
stats_df = df[['player_name', 'kills', 'damage_dealt', 'win_place']]

# Optional: Sort players by kills
top_killers = stats_df.sort_values(by='kills', ascending=False).head(10)
print("\nTop 10 players by kills:")
print(top_killers)

# Step 5: Visualizations
plt.figure(figsize=(12,6))
sns.histplot(df['kills'], bins=30, kde=True, color='blue')
plt.title("Distribution of Kills in PUBG Matches")
plt.xlabel("Kills")
plt.ylabel("Number of Matches")
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(data=df, x='damage_dealt', y='win_place', hue='kills', palette='viridis')
plt.title("Damage Dealt vs Match Placement")
plt.xlabel("Damage Dealt")
plt.ylabel("Match Placement")
plt.gca().invert_yaxis()  # Lower win_place is better
plt.show()
