#import modules
import csv
csvname = str(input("What is the name of your CSV?: "))
if not ".csv" in csvname:
  csvname += ".csv"
# detects if .csv is used.
with open(csvname, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
                print("**"+ str(row[0]) + '** will sign with the **@' + str(row[1]) + '** on a $' + str(row[2]) + "M contract for " + str(row[3]), end='')
                # writes basic announcement code.
                print(' year' if row[3] == "1" else '' + ' years', end='')
                # plural detection
                print(' with a player option!' if row[4] == "PO" else '' ' with a team option!' if row[4] == "TO" else '' + '!')
                # checks for an Option
                if row[5] !='':
                        print("The @" + str(row[5]) + " have 24 hours to match.\n")
                else:
                        print('')
                # checks if the player is an RFA or not.

