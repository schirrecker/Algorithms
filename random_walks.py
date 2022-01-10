import random

def random_walk(n):
    x, y = 0, 0
    for _ in range(n):
        (dx, dy) = random.choice([(0,1), (0,-1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

number_of_walks = 10000
limit = 6
delta_from_half = 50
best_walk_length = 0

for walk_length in range(1, 40):
    under_limit = 0
    for _ in range (number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= limit:
            under_limit += 1
    percentage = 100* (under_limit / number_of_walks)
    if abs(percentage - 50) < delta_from_half:
        best_walk_length = walk_length
        delta_from_half = abs(percentage - 50)
    print ("Walk length: ", walk_length, " ,percentage: ", percentage)

print ("-------------------------------------------------")
print ("Best walk length: ", best_walk_length)
    


        
