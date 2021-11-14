
# call the open function with an argument of "um-server-01.txt", which is the file we want to open. The open function opens the file and returns it as a file object. We store that file object in a variable called log_file.
log_file = open("um-server-01.txt")

# create a function called sales_reports that takes a file object as a parameter. 
def sales_reports(log_file):
    # we have a for loop that loops through every line in the file object
    for line in log_file:
        #removes any trailing white space from the line
        line = line.rstrip()
        #make a copy of the first three characters of a line and store then in the "day" variable
        day = line[0:3]
        # conditional statement checking if the chars in day = "Mon" 
        if day == "Mon":
            # if true, print the line in the terminal
            print(line)

# invoke the sales_reports function with an argument of log_file, which is the file object we opened on line 3
sales_reports(log_file)

log_file.close()

########### extra credit ###########


log_file = open("um-server-01.txt")

def melon_orders_over_10(log_file):
    for line in log_file:
        line_words = line.rstrip('\n').split(' ')

        melon_number = int(line_words[2])

        if melon_number > 10:
            print(line.rstrip())

melon_orders_over_10(log_file)

log_file.close()