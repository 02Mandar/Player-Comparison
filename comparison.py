import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("player_comparison.csv")

print("\n===== PLAYER PERFORMANCE COMPARISON SYSTEM =====\n")

# Separate Cricket and Football Players
cricket = data[data["Game"] == "Cricket"].copy()
football = data[data["Game"] == "Football"].copy()

# Cricket Comparison Score
cricket["ComparisonScore"] = (
    cricket["Runs"] * 0.3 +
    cricket["StrikeRate"] * 0.5 +
    cricket["WinPercentage"] * 2 +
    cricket["Consistency"] * 15
)

# Football Comparison Score
football["ComparisonScore"] = (
    football["Goals"] * 15 +
    football["Assists"] * 10 +
    football["WinPercentage"] * 2 +
    football["Consistency"] * 15
)

# Cricket Rankings
cricket_rankings = cricket.sort_values(
    by="ComparisonScore",
    ascending=False
)

print("\n===== CRICKET PLAYER RANKINGS =====\n")
print(cricket_rankings[[
    "Player",
    "ComparisonScore"
]])

# Football Rankings
football_rankings = football.sort_values(
    by="ComparisonScore",
    ascending=False
)

print("\n===== FOOTBALL PLAYER RANKINGS =====\n")
print(football_rankings[[
    "Player",
    "ComparisonScore"
]])

# Cricket Graph
plt.figure(figsize=(10,5))

plt.bar(
    cricket_rankings["Player"],
    cricket_rankings["ComparisonScore"]
)

plt.title("Cricket Player Comparison")
plt.xlabel("Players")
plt.ylabel("Comparison Score")
plt.xticks(rotation=15)

plt.show()

# Football Graph
plt.figure(figsize=(10,5))

plt.bar(
    football_rankings["Player"],
    football_rankings["ComparisonScore"]
)

plt.title("Football Player Comparison")
plt.xlabel("Players")
plt.ylabel("Comparison Score")
plt.xticks(rotation=15)

plt.show()

# Football Win Percentage
plt.figure(figsize=(10,5))

plt.plot(
    football["Player"],
    football["WinPercentage"],
    marker='o'
)

plt.title("Football Win Percentage")
plt.xlabel("Players")
plt.ylabel("Win Percentage")
plt.xticks(rotation=20)

plt.grid(True)

plt.show()

print("\nComparison Analysis Completed Successfully")
