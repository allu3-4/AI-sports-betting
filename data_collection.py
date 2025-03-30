import requests
import pandas as pd

# NHL API URL for team data
url = "https://statsapi.web.nhl.com/api/v1/teams"
response = requests.get(url)
data = response.json()

# Extract relevant team details
teams = []
for team in data["teams"]:
    teams.append({
        "id": team["id"],
        "name": team["name"],
        "venue": team["venue"]["name"],
        "division": team["division"]["name"]
    })

# Convert to DataFrame and save as CSV
df = pd.DataFrame(teams)
df.to_csv("nhl_teams.csv", index=False)

print("NHL team data saved successfully!")
