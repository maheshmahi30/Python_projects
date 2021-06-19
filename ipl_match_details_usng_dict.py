########################## the only mistake was assigning the same dictionary to all, now a copy of dictionary is assigned so no 
# worry
"""
6
CSK;RR;loss
RR;DD;draw
MI;KKR;win
KKR;RR;loss
CSK;DD;draw
MI;DD;draw

op:
Team: RR, Matches Played: 3, Won: 2, Lost: 0, Draw: 1, Points: 7
Team: MI, Matches Played: 2, Won: 1, Lost: 0, Draw: 1, Points: 4
Team: DD, Matches Played: 3, Won: 0, Lost: 0, Draw: 3, Points: 3
Team: CSK, Matches Played: 2, Won: 0, Lost: 1, Draw: 1, Points: 1
Team: KKR, Matches Played: 2, Won: 0, Lost: 2, Draw: 0, Points: 0
"""




n = int(input())
dict_players = dict()
if(n == 0):
    print("No Output")
else:
    for i in range(n):
        game = {
            "matches":0,
            "win":0,
            "loss":0,
            "draw":0,
            "points":0
        }
        matches= 0
        draw = 0
        loss = 0
        win = 0
        points = 0
        team1,team2,result = map(str,input().split(';'))
        
        if(team1 not in dict_players):
            dict_players[team1] = game.copy()
            dict_players[team1]["matches"] = 1
            if(result == "loss"):
                dict_players[team1]["loss"] = 1
                dict_players[team1]["points"] = 0
            elif(result == "win"):
                dict_players[team1]["win"] = 1
                dict_players[team1]["points"] = 3
            elif(result == "draw"):
                dict_players[team1]["draw"] = 1
                dict_players[team1]["points"] = 1
                
            #print(team1,dict_players[team1]["matches"],dict_players[team1]["win"],dict_players[team1]["loss"],dict_players[team1]["draw"])
        
        else:
            matches = dict_players[team1]["matches"]
            #print(team1,matches)
            matches = matches + 1
            dict_players[team1]["matches"] = matches
            if(result == "loss"):
                loss = dict_players[team1]["loss"]
                dict_players[team1]["loss"] = 1 + loss
            elif(result == "win"):
                win = dict_players[team1]["win"]
                dict_players[team1]["win"] = 1 + win
                
                points = dict_players[team1]["points"]
                dict_players[team1]["points"] = points + 3
            elif(result == "draw"):
                draw = dict_players[team1]["draw"]
                dict_players[team1]["draw"] = 1 + draw
                
                points = dict_players[team1]["points"]
                dict_players[team1]["points"] = points + 1
            #print(team1,dict_players[team1]["matches"],dict_players[team1]["win"],dict_players[team1]["loss"],dict_players[team1]["draw"])
        
        #print(game)
        
        if(team2 not in dict_players):
            dict_players[team2] = game.copy()
            dict_players[team2]["matches"] = 1
            if(result == "win"):
                dict_players[team2]["loss"] = 1
                dict_players[team2]["points"] = 0
            elif(result == "loss"):
                dict_players[team2]["win"] = 1
                dict_players[team2]["points"] = 3
            elif(result == "draw"):
                dict_players[team2]["draw"] = 1
                dict_players[team2]["points"] = 1
            #print(team2,dict_players[team2]["matches"],dict_players[team2]["win"],dict_players[team2]["loss"],dict_players[team2]["draw"])
            
        else:
            matches = dict_players[team2]["matches"]
            #print(team2,matches)
            matches = matches + 1
            dict_players[team2]["matches"] = matches
            if(result == "win"):
                loss = dict_players[team2]["loss"]
                dict_players[team2]["loss"] = 1 + loss
            elif(result == "loss"):
                win = dict_players[team2]["win"]
                dict_players[team2]["win"] = 1 + win
                
                points = dict_players[team2]["points"]
                dict_players[team2]["points"] = points + 3
            elif(result == "draw"):
                draw = dict_players[team2]["draw"]
                dict_players[team2]["draw"] = 1 + draw
                
                points = dict_players[team2]["points"]
                dict_players[team2]["points"] = points + 1
            #print(team2,dict_players[team2]["matches"],dict_players[team2]["win"],dict_players[team2]["loss"],dict_players[team2]["draw"])
        #print(game)
    result = []
    for i in dict_players.keys():
        result.append(dict_players[i]["points"])
    result.sort(reverse=True)
    #print(result)
    
    for i in result:
        for j in dict_players.keys():
            if(i == dict_players[j]["points"]):
                print("Team: {}, Matches Played: {}, Won: {}, Lost: {}, Draw: {}, Points: {}".format(j,dict_players[j]["matches"],dict_players[j]["win"],dict_players[j]["loss"],dict_players[j]["draw"],dict_players[j]["points"]))
