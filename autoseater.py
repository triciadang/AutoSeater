import csv


def main():
    #import csv
    header = ['Date Completed','Register','Register ($ Amount)','Rank/Title','Name (Last Name)','Name (First Name)',
              'Unit/Organization/Business','Sponsor or Donor?','Email','Mobile Phone Number',	'Menu Options']
    with open('C:\\Users\\taduser\\Documents\\EventBrite\\registrants.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        with open('C:\\Users\\taduser\\Documents\\EventBrite\\seatingChart.csv','w') as seating_file:
            writer = csv.writer(seating_file)
            writer.writerow(header)
        table_num = 0
        singular_group = []
        number_in_group = 0
        prev_row = None

        for row in reader:
            print(reader.line_num)
            if reader.line_num == 1:
                prev_row = row
                print("here")
            if prev_row[2] == row[2]:
                number_in_group += 1
                singular_group += row
                print("there")
            else:
                for each in singular_group:
                    print(each)
                    each = each + str(table_num)
                    writer.writerow(each)
                table_num += 1
                singular_group = []
                number_in_group = 0
                table_num += 1
                print("s")
            prev_row = row


    #parse csv



if __name__ == "__main__":
   main()
