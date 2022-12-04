rounds = []
chr_to_rps = {x : r for (x,r) in zip("AXBYCZ", "RRPPSS")}
score = {'R' : 1, 'P' : 2, 'S' : 3}
def win(opp, you):
    game = ['R', 'P', 'S']
    if you == opp:
        return 3
    you_i = game.index(you)
    opp_i = game.index(opp)
    if (you_i + 1)%3 == opp_i:
        return 0
    else:
        return 6


with open('inp1.txt', 'r') as file:
    for row in file:
        opp, you = row.strip().split()
        you = chr_to_rps[you]
        opp = chr_to_rps[opp]
        # rounds.append((score[you] + win(opp, you), opp, you))
        rounds.append(score[you] + win(opp, you))

print(sum(rounds))
