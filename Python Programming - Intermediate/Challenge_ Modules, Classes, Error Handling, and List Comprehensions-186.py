## 2. Introduction to the Data ##

import csv
#f=open("nfl_suspensions_data.csv","r")
nfl_suspensions=list(csv.reader(open("nfl_suspensions_data.csv","r")))[1:]
years={}
for each in nfl_suspensions:
    row_year=each[5]
    if row_year in years:
        years[row_year]+=1
    else:
        years[row_year]=1
print(years)


## 3. Unique Values ##

import csv
nfl_suspensions=list(csv.reader(open("nfl_suspensions_data.csv","r")))[1:]
#print(nfl_suspensions)
team=[each[1] for each in nfl_suspensions]
unique_teams=set(team)
print(unique_teams)
games=[each[2] for each in nfl_suspensions]
unique_games=set(games)
print(unique_games)


## 4. Suspension Class ##

class Suspension:
    def __init__(self,lists):
        self.name=lists[0]
        self.team=lists[1]
        self.games=lists[2]
        self.year=lists[5]
third_suspension=Suspension(nfl_suspensions[2])
print(third_suspension.name)

## 5. Tweaking the Suspension Class ##

['class Suspension():\n    def __init__(self,row):\n        self.name = row[0]\n        self.team = row[1]\n        self.games = row[2]\nclass Suspension():\n    def __init__(self,row):\n        self.name = row[0]\n        self.team = row[1]\n        self.games = row[2] \n        try:\n            self.year = int(row[5])\n        except Exception:\n             self.year = 0\n    def get_year(self):\n        return(self.year)\n                \nmissing_year = Suspension(nfl_suspensions[22])\ntwenty_third_year = missing_year.get_year()']