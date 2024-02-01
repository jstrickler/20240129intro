import pprint
import itertools
from functools import cache
import time

start_time = time.perf_counter()

@cache
def distance(x1,x2,y1,y2):
    dist = ((x2-x1)**2+(y2-y1)**2)**0.5
    return dist

print('city sorter')

#read cities and points from .txt
citycoord = {}

#pull data from .txt file
with open("citypoints.txt") as points:
    for line in points:
        city,xx,yy = line.split(":")
        citycoord[city] = int(xx),int(yy)

#create list of lists of possible travel routes
itineraries = list(itertools.permutations(citycoord.keys()))

print(f"{len(itineraries) = }")

# remove reversed versions of routes
for r in itineraries:
    itineraries.remove(tuple(reversed(r)))

print(f"{len(itineraries) = }")

# combine lists into one string for readability
combined_itineraries = [''.join(it) for it in itineraries]
print("COMBINED ITINERARIES:", end=" ")
print(combined_itineraries)
print('total runs: ',len(combined_itineraries))

#check max number of cities
totalstops = len(citycoord)

#create range for calculating distance in travel orderl, substarct 1 since range starts at 0
stopnumber = range(totalstops - 1)
print("stopnumber:", stopnumber)

#create a dictionary of itineraries, will later populate with total distances associated with travel order
itinwdist = {}
# unsorted_itineraries = {key: None for key in combined_itineraries} ## IGNORE THIS CODE ##
#print.pprint(unsorted_itineraries)

# print(citycoord['a'][0])
# print(combined_itineraries[0][2])
for comitinerary in combined_itineraries:
    #set distance  to zero on the beginning of new itinerary check
    itinerarydist = 0

    #find total distance in each itinerary by looping through stop number in itinerary
    for stop in stopnumber:  # 0 through 6   due to range(7)
        # print(citycoord['a'][0])
        #find distance between   towns
        ix1 = float(citycoord[f'{comitinerary[stop]}'][0])
        ix2 = float(citycoord[f'{comitinerary[stop+1]}'][0])
        iy1 = float(citycoord[f'{comitinerary[stop]}'][1])
        iy2 = float(citycoord[f'{comitinerary[stop+1]}'][1])
        distcheck = distance(ix1,ix2,iy1,iy2)
        #add to total distance
        itinerarydist += distcheck
        # print(distcheck)
    #save final distance to dictionary key
    itinwdist[comitinerary] = itinerarydist
#sort dictionary by distance
sorted_itinwdist = sorted(
    
    
    itinwdist.items(), key=lambda dis: dis[1])
print(f"{len(sorted_itinwdist) = }")


# pprint.pprint(itinwdist)
# pprint.pprint(sorted_itinwdist)

#print first and last 10 entries of sorted list
for key, value in list(sorted_itinwdist)[:10]:
    print(f'{key}: {value}')
print('.\n'*5)
for key, value in list(sorted_itinwdist)[-10:]:
    print(f'{key}: {value}')


# for key, value in list(itinwdist.items())[-10:]:
#     print(f'{key}: {value}')
# print(f"{ix1},{iy1}")
# print(f"{ix2},{iy2}")
print('-' * 60)
#print(sorted_itinwdist)

end_time = time.perf_counter()

print(f"This run took {(end_time - start_time) / 60:.3f} minutes")

