rounds = []
chr_to_rps = {x : r for (x,r) in zip("AXBYCZ", "RLPDSW")}
score = {'R' : 1, 'P' : 2, 'S' : 3,
         'L' : 0, 'D' : 3, 'W' : 6}

def right_move(opp, outcome):
    game = ['R', 'P', 'S']
    opp_i = game.index(opp)
    # if the opponents move is at game[i], what move do we play to win/draw/lose? game[(i+?)%3]
    outcome_map = {'L' : -1, 'D' : 0, 'W' : 1}
    offset = outcome_map[outcome]
    move = game[(opp_i + offset)%3]
    return score[move] + score[outcome]

with open('inp1.txt', 'r') as file:
    for row in file:
        opp, strat = row.strip().split()
        strat = chr_to_rps[strat]
        opp = chr_to_rps[opp]
        rounds.append(right_move(opp, strat))

print(sum(rounds))