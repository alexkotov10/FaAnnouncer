#import necessary modules
import csv
filename= input("What is the name of the csv? (please include the .csv)")
reader = csv.DictReader(open(filename))
for raw in reader:
    print(raw)
