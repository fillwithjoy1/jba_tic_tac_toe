winners = []
for i in range(int(input())):
    player = input()
    if player.split()[1] == "win":
        winners.append(player.split()[0])
print(winners)
print(len(winners))
