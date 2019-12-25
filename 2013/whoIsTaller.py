tot = int(raw_input("Insert '<# of students> <# of height comparisions>': ").split(" ")[1])
inps = []
known = {}
found = 0

for i in range(1, tot + 1):
    curr_inp = raw_input("Insert comparision #{} (<taller student> <shorter student>): ".format(i)).split(" ")
    inps.append([int(curr_inp[0]), int(curr_inp[1])])

unsure_inp = stack = [int(i) for i in raw_input("Insert an unsure comparision (<taller student> <shorter student>): ").split(" ")]

known[unsure_inp[0]] = []
known[unsure_inp[1]] = []

for i in range(len(inps)):
    if inps[i][0] in stack:
        #print "Found {}".format(inps[i][0])
        stack.remove(inps[i][0])
        #print "Stack = {}".format(stack)

        found_unsure_inp = inps[i][0]
        curr_looking_for = inps[i][1]
        known[found_unsure_inp].append(curr_looking_for)

        while True:
            #print "Known = {}".format(known)
            
            found_shorter = False
            for i in range(len(inps)):
                if inps[i][0] == curr_looking_for:
                    curr_looking_for = inps[i][1]
                    found_shorter = True
                    break

            #print "curr_looking_for = {}".format(curr_looking_for)
            if not found_shorter or curr_looking_for == found_unsure_inp:
                #print "lookFor({}) found None".format(curr_looking_for)
                break
            elif len(stack) and curr_looking_for == stack[0]:
                #print "Checkmate, found {}".format(stack[0])
                if found_unsure_inp == unsure_inp[0]:
                    found = 1
                else:
                    found = -1
                break
            known[found_unsure_inp].append(curr_looking_for)
            
if found == -1:
    print "false"
elif found == 1:
    print "true"
else:
    print "unknown"