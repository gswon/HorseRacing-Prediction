import requests
from bs4 import BeautifulSoup

url = "https://racing.hkjc.com/racing/information/English/racing/RaceCard.aspx?RaceDate=2023/07/06&Racecourse=HV&RaceNo=1"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
rows = soup.find_all("tr", class_="f_tac f_fs13")


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
    
    print("Position:", position)
    print("Race History:", race_history)
    print("Horse Image:", horse_image)
    print("Horse Name:", horse_name)
    print("Horse ID:", horse_id)
    print("Weight:", weight)
    print("Jockey:", jockey)
    print("Jockey ID:", jockey_id)
    print("Wins:", wins)
    print("Trainer:", trainer)
    print("Trainer ID:", trainer_id)
    print("Trainer's Season Wins:", trainer_wins)
    print("Trainer's Season Runs:", trainer_runs)
    print("Prize Money:", prize_money)
    print("Gear:", gear)
    print("Owner:", owner)
    print("Sire:", sire)
    print("Dam:", dam)
    print("Dam's Sire:", dam_sire)
    print("---")  
