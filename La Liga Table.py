import requests
from bs4 import BeautifulSoup
import pandas as pd

prem = 9
laliga = 12
seriea = 11
ligue1 = 13
bundesliga = 20

def leagues_table(league, num):
    url = requests.get(f'https://fbref.com/en/comps/{num}/{league}-Stats').text
    soup = BeautifulSoup(url, 'lxml')
    table = soup.select('table.stats_table')[0]

    league_table = pd.read_html(url, match="Regular season Table")[0]

    print(league_table)
    print()

def stats(league, num, index):
    url = requests.get(f'https://fbref.com/en/comps/{num}/{league}-Stats').text
    soup = BeautifulSoup(url, 'lxml')
    table = soup.select('table.stats_table')[0]

    league_table = pd.read_html(url, match="Regular season Table")[0]    
    links = table.find_all('a')
    links = [l.get('href') for l in links]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f'https://fbref.com{l}' for l in links]

    team_url = team_urls[index-1]
    # print(team_urls)

    data = requests.get(team_url).text

    stats_table = pd.read_html(team_url, match="Standard Stats")[0]
    stats_table.columns = stats_table.columns.droplevel()


    print(stats_table)
    print()


user_input = input('Enter t5 league you wish to see standings of (First letters must be cap and a "-" between spaces): ')

if user_input == 'La-Liga':
    number = laliga

elif user_input == 'Premier-League':
    number = prem

elif user_input == 'Serie-A':
    number = seriea

elif user_input == 'Ligue-1':
    number = ligue1

elif user_input == 'Bundesliga':
    number = bundesliga

else:
    print('The league you inputted is does not exist or is not supported.')

leagues_table(user_input, number)

q = input('Would you like to see the stats of a club by player (y/n)? ')

if q == 'y':
    stats_input = int(input('Enter the position of a club you would like to see the stats of by player (First letters must be cap and a "-" between spaces): '))
    stats(user_input, number, stats_input)


