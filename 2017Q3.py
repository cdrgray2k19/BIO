from functools import lru_cache
numOfParcels, max, numOfItems, weight = map(int, input().split())
#number of parcels, number of parcel weights allowed 1-i, number of items in all parcels, weight of each parvel
#number of ways to make up a parcel given a number of items and weight chosen is always max so that no combination can be repeated
#then do function do find number of parcels and reference ways to make 1 less parcels * the number of ways to make the give parcel with the given number of items
@lru_cache(maxsize=None)
def items(numsOfItems, max, weight):
    if numsOfItems == 0 and weight == 0:
        return 1
    if numOfItems <= 0 or weight <= 0:
        return 0
    return sum(
        items(numsOfItems-1, i, weight-i) for i in range(1, max+1)
    )
@lru_cache(maxsize=None)
def parcels(numOfParcels, max, numOfItems, weight):
    if numOfParcels == 0 and numOfItems == 0:
        return 1
    if numOfParcels <= 0 or numOfItems <= 0:
        return 0
    return sum(
        parcels(numOfParcels-1, max, numOfItems-i, weight)*items(i, max, weight) for i in range(1, numOfItems+1)
    )

print(parcels(numOfParcels, max, numOfItems, weight))