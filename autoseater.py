import csv

#global variable
SEATING_TABLE = {str(i): 8 for i in range(1, 126)}

def what_table_number(number_in_group):
    table_number = 1
    table_found = 0

    if number_in_group > 8:
        print("NEED HELP")

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

        with open("C:\\Users\\trici\\Downloads\\seatingChart.csv",'w',newline="") as seating_file:
        #with open('C:\\Users\\taduser\\Documents\\EventBrite\\seatingChart.csv','w') as seating_file:
            writer = csv.writer(seating_file)

            table_num = 1
            singular_group = []
            number_in_group = 0

            for row in reader:
                if reader.line_num == 1:
                    row.append("Table Number")
                    writer.writerow(row)
                elif reader.line_num == 2:
                    singular_group.append(row)
                    number_in_group += 1
                elif prev_row[0] == row[0]:
                    singular_group.append(row)
                    number_in_group += 1
                else:
                    table_num = what_table_number(number_in_group)
                    for each in singular_group:
                        print(each)
                        each.append(table_num)
                        writer.writerow(each)

                    #need to change
                    #table_num += 1
                    #new one is only one in group
                    singular_group = []
                    singular_group.append(row)
                    number_in_group = 1

                prev_row = row


    #parse csv



if __name__ == "__main__":
   main()
