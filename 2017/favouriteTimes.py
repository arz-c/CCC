inp = int(raw_input("Insert the number of minutes spent watching: "))
inpH = inp // 60
inpM = inp % 60
hours = 12
totHours = 0
mins = [0, 0]
count = 0

#print inpH, inpM
def clock(inpH, inpM, hours, totHours, mins, count):
    while True:
        for mins[0] in range(0, 6):
            for mins[1] in range(0, 10):
                if inpH <= totHours and inpM < int(str(mins[0]) + str(mins[1])):
                    return count
                if len(str(hours)) == 2:
                    if int(str(hours)[0]) - int(str(hours)[1]) == int(str(hours)[1]) - mins[0] == mins[0] - mins[1]:
                        count += 1
                        #print "{}:{}{}".format(hours, mins[0], mins[1])
                elif hours - mins[0] == mins[0] - mins[1]:
                    count += 1
                    #print "{}:{}{}".format(hours, mins[0], mins[1])
        for hours in range(1, 12):
            totHours += 1
            for mins[0] in range(0, 6):
                for mins[1] in range(0, 10):
                    if inpH < totHours and inpM < int(str(mins[0]) + str(mins[1])):
                        return count
                    if len(str(hours)) == 2:
                        if int(str(hours)[0]) - int(str(hours)[1]) == int(str(hours)[1]) - mins[0] == mins[0] - mins[1]:
                            count += 1
                            #print "{}:{}{}".format(hours, mins[0], mins[1])
                    elif hours - mins[0] == mins[0] - mins[1]:
                        count += 1
                        #print "{}:{}{}".format(hours, mins[0], mins[1])
print clock(inpH, inpM, hours, totHours, mins, count)