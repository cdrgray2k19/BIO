j, n = map(int, input().split())
jugs = list(map(int, input().split()))
volumes = [[0 for i in range(0, j)]]
#recursive bfs
visited = set(tuple(volumes[0]))
def bfs(volumes, jugs, n, depth):
    newVolumes = []
    for i in range(0, len(volumes)):
        if n in volumes[i]:
            return depth
    for i in range(0, len(volumes)):
        for j in range(0, len(volumes[i])):
            temp = volumes[i].copy()
            temp[j] = jugs[j]
            if tuple(temp.copy()) not in visited:
                newVolumes.append(temp.copy())
                visited.add(tuple(temp.copy()))
            temp = volumes[i].copy()
            if temp[j] != 0:
                temp[j] = 0
                if tuple(temp.copy()) not in visited:
                    newVolumes.append(temp.copy())
                    visited.add(tuple(temp.copy()))
            for k in range(0, len(volumes[i])):
                if j != k:
                    temp = volumes[i].copy()
                    if temp[j] != 0:
                        if temp[k] != jugs[k]:
                            val = min(jugs[k]-temp[k], temp[j])
                            temp[j] -= val
                            temp[k] += val
                            if tuple(temp.copy()) not in visited:
                                newVolumes.append(temp.copy())
                                visited.add(tuple(temp.copy()))
    return bfs(newVolumes, jugs, n, depth+1)

print(bfs(volumes, jugs, n, 0))