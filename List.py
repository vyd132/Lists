import random
team1_goal=[3,0,1]
team2_goal=[3,0,1]
print(team1_goal)
print(team2_goal)
team1wins=0
team2wins=0

if team1_goal[0] > team2_goal[0]:
    print("Выиграла 1 команда",team1_goal[0],":",team2_goal[0])
    team1wins += 1
elif team1_goal[0] < team2_goal[0]:
    print("Выиграла 2 команда",team2_goal[0],":",team1_goal[0])
    team2wins += 1
else:
    print("Ничья", team2_goal[0], ":", team1_goal[0])

if team1_goal[1] > team2_goal[1]:
    print("Выиграла 1 команда",team1_goal[1],":",team2_goal[1])
    team1wins += 1
elif team1_goal[1] < team2_goal[1]:
    print("Выиграла 2 команда",team2_goal[1],":",team1_goal[1])
    team2wins += 1
else:
    print("Ничья", team2_goal[1], ":", team1_goal[1])

if team1_goal[2] > team2_goal[2]:
    print("Выиграла 1 команда",team1_goal[2],":",team2_goal[2])
    team1wins+=1
elif team1_goal[2] < team2_goal[2]:
    print("Выиграла 2 команда",team2_goal[2],":",team1_goal[2])
    team2wins+=1
else:
    print("Ничья", team2_goal[2], ":", team1_goal[2])

if team1wins>team2wins:
    print("Победитель команада 1")
elif team1wins<team2wins:
    print("Победитель команада 2")
else:
    print("Ничья, победил судья")

