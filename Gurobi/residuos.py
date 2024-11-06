#Y = generateRandomNumbers(b, y)

#randomStationsPeople = random.randint(p + 10, p + 15) # Create bigger instances idk
#stationsPeople = c * randomStationsPeople
#P = np.array(generateRandomNumbers(randomStationsPeople, p)) * c
#
#randomSheltersDifference = randomStationsPeople + random.randint(1, 10)
#sheltersCapacity = stationsPeople + (c * (randomSheltersDifference - randomStationsPeople))
#S = np.array(generateRandomNumbers(randomSheltersDifference, s)) * c
def generateRandomNumbers(total, num_numbers):
    numbers = [random.uniform(1, 2) for _ in range(num_numbers)]
    s = sum(numbers)
    numbers = [round(total * (i/s)) for i in numbers]
    numbers[-1] = total - sum(numbers[:-1])  # adjust last value to make sum correct

    return numbers

#for j, v, t in b_:
#    print(f"b_[{j}, {v}, {t}]")

#for i, j, v, t in x:
#    print(f"x[{i}, {j}, {v}, {t}] = {x[i, j, v, t].x}")

#for j in s_range:
#    for t in range(t_evac):
#        for v in range(b):
#            for i in p_range:
#                print(f"x[{i}, {j}, {v}, {t}] = {x[i, j, v, t].x}")

#print()
#for v in range(b):
#    for t1 in range(t_evac):
#        for i in N:
#            if b_[i, v, t1].x > 0:
#                if t1 == 0:
#                    print(f"El bus {v} recoge {b_[i, v, t1].x} personas en el nodo {i} después del instante {t1}.")
#                else:
#                    if t1 % 2 == 1:
#                        print(f"El bus {v} deja {b_[i, v, t1].x} personas en el nodo {i} después del instante {t1}.")
#                    else:
#                        print(f"El bus {v} recoge {b_[i, v, t1].x} personas en el nodo {i} después del instante {t1}.")
#    print()

#middleFirstPoint = (len(Y) - 1) / 2
#middleSecondPoint = (len(P) + 1) / 2
#middleThirdPoint = (len(S) - 1) / 2
#
#nodeVerticalDistances = 1
#nodeHorizontalDistances = 1
#
#offset = 0
#
#firstNodesPositions = {}
#secondNodesPositions = {}
#thirdNodesPositions = {}
#for i in range(y):
#    plt.plot(offset, nodeVerticalDistances*middleSecondPoint + nodeVerticalDistances*(i - middleFirstPoint), marker='o', markersize=5, color="red")
#    firstNodesPositions[i] = [offset, nodeVerticalDistances*middleSecondPoint + nodeVerticalDistances*(i - middleFirstPoint)]
#
#for i in range(p):
#    plt.plot(offset + nodeHorizontalDistances, nodeVerticalDistances*(i + 1), marker='o', markersize=5, color="blue")
#    secondNodesPositions[i] = [offset + nodeHorizontalDistances, nodeVerticalDistances*(i + 1)]
#
#for i in range(s):
#    plt.plot(offset + 2*nodeHorizontalDistances, nodeVerticalDistances*middleSecondPoint + nodeVerticalDistances*(i - middleThirdPoint), marker='o', markersize=5, color="green")
#    thirdNodesPositions[i] = [offset + 2*nodeHorizontalDistances, nodeVerticalDistances*middleSecondPoint + nodeVerticalDistances*(i - middleThirdPoint)]
#
#for i in range(y):
#    for j in range(p):
#        for v in range(b):
#            if x[i, j + y, v, 0].x == 1:
#                plt.plot([firstNodesPositions[i][0], secondNodesPositions[j][0]], [firstNodesPositions[i][1], secondNodesPositions[j][1]], color="black")
#
#for i in range(p):
#    for j in range(s):
#        for v in range(b):
#            for t1 in range(1, t_evac, 2):
#                if x[i + y, j + y + p, v, 1].x == 1:
#                    plt.plot([secondNodesPositions[i][0], thirdNodesPositions[j][0]], [secondNodesPositions[i][1], thirdNodesPositions[j][1]], color="limegreen")
#
#for i in range(s):
#    for j in range(p):
#        for v in range(b):
#            for t1 in range(2, t_evac, 2):
#                if x[i + y + p, j + y, v, t1].x == 1:
#                    plt.plot([secondNodesPositions[j][0], thirdNodesPositions[i][0]], [secondNodesPositions[j][1], thirdNodesPositions[i][1]], color="orange")   