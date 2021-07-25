import csv
import random
import math
from calendar import monthrange, month_name

class Income:
    def __init__(self):
        self.year = self.input_check("Enter year in YYYY format: ")
        self.month = self.input_check("Enter month in 1-12 Format: ")
        self.min = self.input_check("Enter minimum amount: ")
        self.max = self.input_check("Enter maximum amount: ")

    def input_check(self, text):
        while True:
            var1 = input(text)
            if var1.isnumeric():
                var1 = int(var1)
                if "amount" in text:
                    return var1
                elif "month" in text:
                    if var1>0 and var1<13:
                        return var1
                    print("INVALID INPUT\nPlease Input 1-12 only")
                    continue
                else:
                    if len(str(var1)) == 4:
                        return var1
                    print("INVALID INPUT\nPlease Input YYYY format")
                    continue
            print("INVALID INPUT \nPlease Input numeric value only")

    def number_of_days(self):
        return monthrange(self.year, self.month)

    def round_up(self, number, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(number * multiplier) / multiplier

    def random_list(self):
        num_days = self.number_of_days()[1]
        num_list = [int(self.round_up(random.randint(self.min, self.max), -1)) for num in range(num_days)]
        return num_list

    def generate(self):
        random_number = self.random_list()
        write_list = [[f"{month_name[self.month]} {day+1}", random_number[day]] for day in range(len(random_number))]
        with open('record.csv', 'w') as file:
            fieldnames = ['Date','Amount']
            csv_writer = csv.writer(file, delimiter='\t')
            csv_writer.writerow(fieldnames)
            for line in write_list:
                csv_writer.writerow(line)



if __name__ == "__main__":
    blufips = Income()
    blufips.generate()
