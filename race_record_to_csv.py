import requests
import csv
from bs4 import BeautifulSoup

url = "https://racing.hkjc.com/racing/information/English/racing/RaceCard.aspx?RaceDate=2023/07/06&Racecourse=HV&RaceNo=1"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
rows = soup.find_all("tr", class_="f_tac f_fs13")

filename = "horse_data.csv"

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Position", "Race History", "Horse Image", "Horse Name", "Horse ID", "Weight", "Jockey",
                     "Jockey ID", "Wins", "Trainer", "Trainer ID", "Trainer's Season Wins", "Trainer's Season Runs",
                     "Prize Money", "Gear", "Owner", "Sire", "Dam", "Dam's Sire"])

    for row in rows:
        columns = row.find_all("td")

        position = columns[0].text.strip()
        race_history = columns[1].text.strip()
        horse_image = columns[2].find("img")["src"]
        horse_name = columns[3].text.strip()
        horse_id = columns[4].text.strip()
        weight = columns[5].text.strip()
        jockey = columns[6].find("a").text.strip()
        jockey_id = columns[6].find("a")["href"].split("=")[-1]
        wins = columns[8].text.strip()
        trainer = columns[9].find("a").text.strip()
        trainer_id = columns[9].find("a")["href"].split("=")[-1]
        trainer_wins = columns[11].text.strip()
        trainer_runs = columns[12].text.strip()
        prize_money = columns[13].text.strip()
        gear = columns[21].text.strip()
        owner = columns[23].text.strip()
        sire = columns[24].text.strip()
        dam = columns[25].text.strip()
        dam_sire = columns[26].text.strip()

        writer.writerow([position, race_history, horse_image, horse_name, horse_id, weight, jockey, jockey_id,
                         wins, trainer, trainer_id, trainer_wins, trainer_runs, prize_money, gear, owner, sire,
                         dam, dam_sire])

print("Data saved to", filename)
