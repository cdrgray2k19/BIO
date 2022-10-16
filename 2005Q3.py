#number of actors
n = int(input())
#number of scenes for each actor
scenes = list(map(int, input().split()))
current = [0 for i in range(0, len(scenes))]
#recursive dfs that will add scenes to actors that have less scenes than senior actors, if they have filmed all their scenes they are skipped over 

#current will hold number of scenes played by each actor
#arrangments will hold current number of complete arangments and will be incremented
def dfs(current):
    #if only one more scene to add then an arrangment is complete and we can add that back
    if sum(current) == sum(scenes) - 1:
        return 1
    #else loop through and if scene can be added to actor then add that and call function again
    arrangments = 0
    for i in range(0, len(current)):
        if i == 0:
            if current[i] < scenes[i]:
                temp = current.copy()
                temp[i] += 1
                arrangments += dfs(temp)
        else:
            if current[i] < current[i-1] and current[i] < scenes[i]:
                #if a less senior actor has less scenes than a more senior actor and still has scenes left we can film their scene and call dfs again
                temp = current.copy()
                temp[i] += 1
                arrangments += dfs(temp)
    
    return arrangments
#most senior actor has to go first so no point checking for that
current[0] = 1
print(dfs(current))