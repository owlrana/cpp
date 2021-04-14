# to calculate best region acc to Broadcast Type, TIme, Upbeat & final prob/cost

type = ["cartoon", "movie", "sports"]
time = ["5-7", "7-10", "10-12"]

# HORIZONTAL
typeDict = {"cartoon": 0.25, "movie": 0.25, "sports": 0.6}
timeDict = {"5-7": 0.25, "7-10": 0.68, "10-12": 0.37}
upbeatDict = {"yes": 0.55, "no": 0.41}
# CALCULATION
for i in range(3):
    for j in range(3):
        print((type[i]), " & ", (time[j]), " = ", (typeDict[type[i]]) * (timeDict[time[j]]))

# VERTICAL
# taking base probability 1/totalData instead of exactly 0
segment = ["s1", "s2", "s3" "s4"]
cartoonDict = {"s1": 0.02, "s2": 0.02, "s3": 0.33333, "s4": 0.66666}
sportsDict = {"s1": 0.4, "s2": 1, "s3": 0.6, "s4": 0.4}
movieDict = {"s1": 0.75, "s2": 0.02, "s3": 0.75, "s4": 0.02}

time57 = {"s1": 0.25, "s2": 0.25, "s3": 0.5, "s4": 0.02}
time710 = {"s1": 0.75, "s2": 0.75, "s3": 1, "s4": 0.5}
time1012 = {"s1": 0.5, "s2": 0.25, "s3": 0.25, "s4": 0.5}

#CALCULATION
for i in range(4):
    for j in range(4):
        for k in range(4):
            