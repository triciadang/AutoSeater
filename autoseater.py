import csv

#global variable
SEATING_TABLE = {str(i): 8 for i in range(1, 126)}

def what_table_number(number_in_group):
    table_number = 1
    table_found = 0

    while table_found == 0:
        if SEATING_TABLE[str(table_number)] >= number_in_group:
            table_number = str(table_number)
            SEATING_TABLE[str(table_number)] = SEATING_TABLE[str(table_number)]-number_in_group
            # exits while loop
            table_found = 1
        else:
            table_number += 1


    return table_number

def main():

    #import csv
    with open("C:\\Users\\trici\\Downloads\\registrants (18).csv",'r') as csv_file:
    #with open('C:\\Users\\taduser\\Documents\\EventBrite\\registrants.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        #opens separate csv to write Seating Tables to
        with open("C:\\Users\\trici\\Downloads\\seatingChart.csv",'w',newline="") as seating_file:
        #with open('C:\\Users\\taduser\\Documents\\EventBrite\\seatingChart.csv','w') as seating_file:
            writer = csv.writer(seating_file)

            #Initiates values
            singular_group = []
            number_in_group = 0

            for row in reader:
                #For header row
                if reader.line_num == 1:
                    row.append("Table Number")
                    writer.writerow(row)

                #For first real row of data
                elif reader.line_num == 2:
                    singular_group.append(row)
                    number_in_group += 1

                #If registrants registered together
                elif prev_row[0] == row[0]:
                    singular_group.append(row)
                    number_in_group += 1

                #If we are on a new group
                else:
                    n = 0
                    overall_number_in_group = number_in_group
                    while number_in_group > 8:
                        table_num = what_table_number(8)
                        for i in range(8 * n + 0, 8 * n + 8):
                            singular_group[i].append(table_num)
                            writer.writerow(singular_group[i])
                        n += 1
                        number_in_group -= 8

                    # reduce until get a number <= 8
                    table_num = what_table_number(number_in_group)
                    for i in range(8 * n + 0, overall_number_in_group):
                        singular_group[i].append(table_num)
                        writer.writerow(singular_group[i])

                    #new different one is only one in group
                    singular_group = []
                    singular_group.append(row)
                    number_in_group = 1

                prev_row = row

            #no more rows read - write final group
            n = 0
            overall_number_in_group = number_in_group
            while number_in_group > 8:
                table_num = what_table_number(8)
                for i in range(8 * n + 0, 8 * n + 8):
                    singular_group[i].append(table_num)
                    writer.writerow(singular_group[i])
                n += 1
                number_in_group -= 8

            #reduce until get a number < 8
            table_num = what_table_number(number_in_group)
            for i in range(8 * n + 0, overall_number_in_group):
                singular_group[i].append(table_num)
                writer.writerow(singular_group[i])


if __name__ == "__main__":
   main()
