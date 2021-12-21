"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #declares an empty list
melons_sold = [] #declares an empty list

f = open('sales-report.txt')  #opens the sales-report file
for line in f:  #begins the loop
    line = line.rstrip()  #removes any trailing characters from line
    entries = line.split('|') #splits string into a list

    salesperson = entries[0]  #adds entry to list
    melons = int(entries[2])  #converts datatype to integer

    if salesperson in salespeople:  #begins conditional
        position = salespeople.index(salesperson) #assig

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


print(salesperson)
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')



