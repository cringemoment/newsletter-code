#muck with this stuff
week = 15

#this stuff dont muck with
import datetime
dotw = int(datetime.datetime.now().strftime("%w"))
if(dotw == 0):
    dotw = 7

startdate = str((datetime.datetime.now() - datetime.timedelta(days = 0)).date())
startdate = startdate.replace("-", "/")

print("**Week %s - ** %s" % (str(week), startdate))
prescript = open("prescript.txt").read()
print(prescript)
print("**PBs :sparkles:**")

#for maintability:
#first argument is the file
#the second argument is which way it's sorted. 0 is biggest to smallest, 1 is vice versa
#the third argument is whether it includes what game it is
#the fourth argument is basically just for pc pbs but its to see if you need to add PC


files = [["pcpbs.txt", 0, 0, 1], ["10pcsprint.txt", 1, 0, 0], ["pcultra.txt", 0, 1, 0], ["pcblitz.txt", 0, 1, 0], ["ppbultra.txt", 0, 1, 0]]
titles = ["Consecutive PBs", "10 PC sprint", "Pure PC Ultra", "Pure PC blitz", "PPB Ultra"]

from natsort import natsorted

for v, file in enumerate(files):
    currentpb = [i.split(" ") for i in open(file[0]).read().splitlines()]
    if(not currentpb == []):
        print("___%s___" % titles[v])
        print("```")
        longestlength = 0
        longestpblength = 0

        if(file[1] == 0):
            currentpb.sort(key=lambda x: x[1], reverse = True)
        else:
            currentpb.sort(key=lambda x: x[1], reverse = False)

        currentpbswithoutrepeat = []
        for i in currentpb:
            for j in currentpbswithoutrepeat:
                if(i[0] == j[0]):
                    break
            else:
                currentpbswithoutrepeat.append(i)

        for i in range(len(currentpbswithoutrepeat)):
            if(len(currentpbswithoutrepeat[i][0]) > longestlength):
                longestlength = len(currentpbswithoutrepeat[i][0])
            if(len(str(currentpbswithoutrepeat[i][1])) > longestpblength):
                longestpblength = len(str(currentpbswithoutrepeat[i][1]))

        game = ["Jstris", "TETR.IO"]

        for i in range(len(currentpbswithoutrepeat)):
            print(str(i + 1) + ". " + str(currentpbswithoutrepeat[i][0]) + (" " * (longestlength - len(currentpbswithoutrepeat[i][0]) + 2 + longestpblength - len(str(currentpbswithoutrepeat[i][1])))) + str(currentpbswithoutrepeat[i][1]), end = "")
            if(file[3] == 1):
                print(" PC", end = "")
            if(file[2] == 0):
                print(" (%s)" % game[int(currentpbswithoutrepeat[i][2])], end = "")
            if(len(currentpbswithoutrepeat[i]) == 4):
                print(" %s %s" % (currentpbswithoutrepeat[i][3][0], currentpbswithoutrepeat[i][3][1:]), end = "")
            print()
        print("```")

thisweek = open("topplayers.txt").read()
runs = thisweek.split("Jstris Bot Stats v0.6")
runvalues = []

for i in runs:
    try:
        pcplayer = i[i.index("played by ") + 10 : i.index("!\nTime")]
        pcnum = (i[i.index("PCs\n") + 3 : i.index("Blocks")]).split("\n")[1]
        runvalues.append([pcplayer, int(pcnum)])
    except ValueError:
        pass

runvalues.sort(key=lambda x: x[1], reverse = True)
runvalueswithoutrepeat = []
for i in runvalues:
    for j in runvalueswithoutrepeat:
        if(i[0] == j[0]):
            break
    else:
        runvalueswithoutrepeat.append(i)

longestlength = 0
longestpblength = 0

try:
    for i in range(5):
        if(len(runvalueswithoutrepeat[i][0]) > longestlength):
            longestlength = len(runvalueswithoutrepeat[i][0])
        if(len(str(runvalueswithoutrepeat[i][1])) > longestpblength):
            longestpblength = len(str(runvalueswithoutrepeat[i][1]))

    print("**Top PC players of the week** :man_running:\n```")
    for i in range(5):
        print(str(i + 1) + ". " + str(runvalueswithoutrepeat[i][0]) + (" " * (longestlength - len(runvalueswithoutrepeat[i][0]) + 2 + longestpblength - len(str(runvalueswithoutrepeat[i][1])))) + str(runvalueswithoutrepeat[i][1]) + " PC")
    print("```")
except IndexError:
    pass

print("""**Top #pc-pics of the week** :eyes:
This section is just for notes
[pc-pic-collage-thanks-image-compositer.png]
[MakeItHigher.png, then new post]
""")

print("**Top Chokes of the week** :sadge: ")
chokes = [i.split("https://") for i in open("chokes.txt").read().splitlines()]
for i in chokes:
    print(i[0])
    print("https://" + i[1])

print()
print("**Research** :test_tube: ")
research = [i.split("https://") for i in open("research.txt").read().splitlines()]
for i in research:
    print(i[0])
    print("https://" + i[1])

print("")
postscript = open("postscript.txt").read()
print("**Postscript** :star:")
print(postscript)
