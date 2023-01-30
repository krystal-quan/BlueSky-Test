import json

class matches:
    def __init__(self, match_id, livestream_provider, winner, httplink, region, team1, team2):
        self.match_id = match_id
        self.livestream_provider = livestream_provider
        self.winner = winner
        self.httplink = httplink
        self.region = region
        self.team1 = team1
        self.team2 = team2
    
    def print_match(self):
        print('Match ID: ', self.match_id)
        print('Livestream Provider: ', self.livestream_provider)
        print('Winner: ', self.winner)
        print('Http Link: ', self.httplink)
        print('Region: ', self.region)
        print('Team 1: ', self.team1)
        print('Team 2: ', self.team2)
        print('\n')

class withheld_matches:
    def __init__(self, match_id, team1, team2):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
    
    def print_match(self):
        print('Match ID: ', self.match_id)
        print('Team 1: ', self.team1)
        print('Team 2: ', self.team2)
        print('\n')
international_count = 0

match_set = set()
withheldmatches_set = set()
max_winner_team = ''
max_score = 0

region_name = ['north', 'south', 'central']
region_count = [0, 0, 0]

jsonfile = open('py_challange_input.json', 'r')
data = json.load(jsonfile)
for sport in data['Cricket']: 
    for formats_detail in sport['formats']:
        for region in formats_detail['regions']:
            region_name = region['name']
            for match in region['matches']:
                if match['isInternational']:
                    international_count += 1
                id = match['id']
                livestream_provider = match['streaming']['liveStream']['provider']
                winner = match['results']['winner']
                if match['results']['points'] > max_score:
                    max_score = match['results']['points']
                    max_winner_team = match['results']['winner']
                httplink = match['httpLink']
                team1 = match['team1']
                team2 = match['team2']
                match1 = matches(id, livestream_provider, winner, httplink, region_name, team1, team2)
                match_set.add(match1)
                if match['results']['resultsWithheld']:
                    withheld_match = withheld_matches(id, team1, team2)
                    withheldmatches_set.add(withheld_match)

for matchprint in match_set:
    matchprint.print_match()
print('Total International Matches: ', international_count)
print('Team with maximum points: ', max_winner_team)
print('Maximum points: ', max_score)
print('List of withheld matches: ')
for withheldmatchprint in withheldmatches_set:
    withheldmatchprint.print_match()

jsonfile.close()
