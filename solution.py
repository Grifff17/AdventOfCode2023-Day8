
def solvepart1():
    # format raw data
    data = fileRead("input.txt")
    instructions = data[0].strip()
    nodesRaw = data[2:]
    nodes = {}
    for row in nodesRaw:
        inNode = row[:3]
        outNode1 = row[7:10]
        outNode2 = row[12:15]
        nodes[inNode] = [outNode1, outNode2]

    # run through nodes
    currentNode = "AAA"
    numSteps = 0
    instructionsIter = 0
    while(currentNode != "ZZZ"):
        if (instructions[instructionsIter] == "L"):
            currentNode = nodes[currentNode][0]
        else:
            currentNode = nodes[currentNode][1]
        numSteps = numSteps + 1
        if (instructionsIter < len(instructions) - 1):
            instructionsIter = instructionsIter + 1
        else:
            instructionsIter = 0
    print(numSteps)

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()