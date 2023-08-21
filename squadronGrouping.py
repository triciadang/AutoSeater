import csv
import easygui

#global variable
SQUADRON_DICT = {'multisquads':[]}

def main():
    notAlreadySeated()
    # alreadySeated()

def alreadySeated():
    #import csv
    path = easygui.fileopenbox()
    with open(path,'r') as csv_file:
    #with open('C:\\Users\\taduser\\Documents\\EventBrite\\registrants.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        #Initiates values
        singular_group = []

        for row in reader:

            #For header row
            if reader.line_num == 1:
                continue

            #For first real row of data
            elif reader.line_num == 2:
                singular_group.append(row)

            #If registrants registered together
            elif prev_row[0] == row[0]:
                singular_group.append(row)

            #If we are on a new group
            elif prev_row[0] != row[0]:
                group_squadron = singular_group[0][6]
                same = True
                for each in singular_group:
                    #if not the first group
                    if each != singular_group[0]:
                        #if each group is different
                        if each[6] != group_squadron:
                            same = False

                #after check if all squads are same
                if same == True:
                    if group_squadron in SQUADRON_DICT.keys():
                        SQUADRON_DICT[group_squadron].append(singular_group)
                    else:
                        #make new group
                        SQUADRON_DICT[group_squadron] = []
                        SQUADRON_DICT[group_squadron].append(singular_group)
                else:
                    #singular groups consists of different groups
                    SQUADRON_DICT['multisquads'].append(singular_group)

                #new different one is only one in group
                singular_group = []
                singular_group.append(row)

            prev_row = row

        # haven't written last group yet
        group_squadron = singular_group[0][6]
        same = True
        for each in singular_group:
            # if not the first group
            if each != singular_group[0]:
                # if each group is different
                if each[6] != group_squadron:
                    same = False

        # after check if all squads are same
        if same == True:
            if group_squadron in SQUADRON_DICT.keys():
                SQUADRON_DICT[group_squadron].append(singular_group)
            else:
                # make new group
                SQUADRON_DICT[group_squadron] = []
                SQUADRON_DICT[group_squadron].append(singular_group)
        else:
            # singular groups consists of different groups
            SQUADRON_DICT['multisquads'].append(singular_group)

    # opens separate csv to write Seating Tables to
    with open("C:\\Users\\trici\\OneDrive\\Documents\\AutoSeater\\SEATEDINCLsquadronGroups.csv", 'w', newline="") as seating_file:
        writer = csv.writer(seating_file)

        for each_key in SQUADRON_DICT.keys():
            for each_entry in SQUADRON_DICT[each_key]:
                for each_subentry in each_entry:
                    each_subentry.insert(0,each_key)
                    writer.writerow(each_subentry)

def notAlreadySeated():

    #import csv
    path = easygui.fileopenbox()
    with open(path,'r') as csv_file:
    #with open('C:\\Users\\taduser\\Documents\\EventBrite\\registrants.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        #Initiates values
        singular_group = []

        for row in reader:
            #ensure not already seated
            if (row[11] == ""):

                #For header row
                if reader.line_num == 1:
                    continue

                #For first real row of data
                elif reader.line_num == 2:
                    singular_group.append(row)

                #If registrants registered together
                elif prev_row[0] == row[0]:
                    singular_group.append(row)

                #If we are on a new group or are at end of file
                elif prev_row[0] != row[0] or row == csv_file.readlines()[-1]:
                    group_squadron = singular_group[0][6]
                    same = True
                    for each in singular_group:
                        #if not the first group
                        if each != singular_group[0]:
                            #if each group is different
                            if each[6] != group_squadron:
                                same = False

                    #after check if all squads are same
                    if same == True:
                        if group_squadron in SQUADRON_DICT.keys():
                            SQUADRON_DICT[group_squadron].append(singular_group)
                        else:
                            #make new group
                            SQUADRON_DICT[group_squadron] = []
                            SQUADRON_DICT[group_squadron].append(singular_group)
                    else:
                        #singular groups consists of different groups
                        SQUADRON_DICT['multisquads'].append(singular_group)

                    #new different one is only one in group
                    singular_group = []
                    singular_group.append(row)
            prev_row = row

    # haven't written last group yet
    group_squadron = singular_group[0][6]
    same = True
    for each in singular_group:
        # if not the first group
        if each != singular_group[0]:
            # if each group is different
            if each[6] != group_squadron:
                same = False

    # after check if all squads are same
    if same == True:
        if group_squadron in SQUADRON_DICT.keys():
            SQUADRON_DICT[group_squadron].append(singular_group)
        else:
            # make new group
            SQUADRON_DICT[group_squadron] = []
            SQUADRON_DICT[group_squadron].append(singular_group)
    else:
        # singular groups consists of different groups
        SQUADRON_DICT['multisquads'].append(singular_group)

    # opens separate csv to write Seating Tables to
    with open("C:\\Users\\trici\\OneDrive\\Documents\\AutoSeater\\NOTSEATEDINCLsquadronGroups.csv", 'w', newline="") as seating_file:
        writer = csv.writer(seating_file)

        for each_key in SQUADRON_DICT.keys():
            for each_entry in SQUADRON_DICT[each_key]:
                for each_subentry in each_entry:
                    each_subentry.insert(0,each_key)
                    writer.writerow(each_subentry)



if __name__ == "__main__":
   main()
