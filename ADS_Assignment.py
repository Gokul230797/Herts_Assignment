# Import modules
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Define functions
def create_line_plot(data):
    # Create a line plot for the Soccer Power Index of the first 10 teams.
    team_1 = data['team1'].head(10)
    spi = data['spi1'].head(10)

    plt.figure(figsize=(17, 6))
    plt.plot(team_1, spi, label='Soccer Power Index', color='green')
    plt.title("Soccer Power Index for UCL Teams")
    plt.xlabel("Teams")
    plt.ylabel("Soccer Power Index")
    plt.legend()
    plt.show()

def create_pie_chart(data):
    # Create a pie chart based on the count of matches played by teams.
    team_counts = data['team1'].value_counts().head(10)

    plt.figure(figsize=(12, 6))
    plt.pie(team_counts, labels=team_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title("Distribution of Matches played by Teams in UCL")
    plt.show()

def create_bar_chart(data):
    # creating a pie chart based on the count of matches played by teams
    team_counts = data['team1'].value_counts().head(10)

    min_count = team_counts.min()
    max_count = team_counts.max()

    plt.figure(figsize=(12, 6))
    bars = team_counts.plot(kind='bar', color='orange', label='Team Counts')

    for bar in bars.patches:
        if bar.get_height() == min_count:
            bar.set_color('blue')
        elif bar.get_height() == max_count:
            bar.set_color('red')

    plt.title("Distribution of Matches played by Teams in UCL")
    plt.xlabel("Teams")
    plt.ylabel("Count")
    plt.legend()
    plt.show()

    return min_count, max_count

#Read data
ucl = pd.read_csv("/Users/user1/Downloads/soccer-spi/spi_matches_latest-UCL.csv")
sns.set_style("whitegrid")

# Calling the functions
create_line_plot(ucl)
create_pie_chart(ucl)
min_max_values = create_bar_chart(ucl)
