import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
matches = pd.read_csv("matches.csv")

# Top teams by wins
wins = matches['match_winner'].value_counts()

# Plot
plt.figure()
wins.head(8).plot(kind='bar')
plt.title("Top IPL Teams by Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.show()


teams = matches['team1'].value_counts() + matches['team2'].value_counts()
teams.sort_values(ascending=False).head(8).plot(kind='bar')
plt.title("Most Active IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Matches")   
plt.show()


venue = matches['venue'].value_counts().head(10)
venue.plot(kind='barh')
plt.title("Top IPL Venues")
plt.show()


toss_win_match = matches[matches['toss_winner'] == matches['match_winner']]
print("Toss win leads to match win %:",
      (len(toss_win_match)/len(matches))*100)