import sys
from collections import defaultdict

def tally_scores(scores):
    totals = defaultdict(lambda: 0)
    for score in scores:
        player = score.lower()
        if not player.isalpha():
            continue
        if score == score.lower():
            totals[player] += 1
        elif score == score.upper():
            totals[player] -= 1
    return totals


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file, 'r') as f:
            scores = f.read()
        totals = tally_scores(scores)
        first = True
        out = []
        for key in sorted(totals, reverse=True):
            output = "{player}:{score}"
            if first:
                first = False
            else:
                output = ", {}".format(output)
            out.append(output.format(player=key, score=totals[key]))
        print ''.join(out)
        exit(0)
    else:
        exit(1)
