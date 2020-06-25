pyramidList = []
results = []
with open('input') as f:
    content = f.readline()
    content = content.rstrip("\n")
    pyramidList.append(content.split(" "))
    while content != "":
        content = f.readline()
        content = content.rstrip("\n")
        pyramidList.append(content.split(" "))
    f.closed


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False;

    return True

def recursiveSearch(x, y, sum):
    if (y == len(pyramidList) - 2):
        results.append(sum + int(pyramidList[y][x]))
        return

    if(isPrime(int(pyramidList[y][x]))):
        return
    else:
        sum += int(pyramidList[y][x])


    recursiveSearch(x, y+1, sum)
    recursiveSearch(x+1, y+1, sum)

recursiveSearch(0,0,0)


print(max(results))