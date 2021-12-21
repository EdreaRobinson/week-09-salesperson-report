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
        position = salespeople.index(salesperson) #assigns variable to indices of 'salespeople' list

        melons_sold[position] += melons #adds qty of melons to each salesperson's list
    else:
        salespeople.append(salesperson) #adds salesperson to 'salespeople' list
        melons_sold.append(melons) #adds melons to 'melons_sold' list


for i in range(len(salespeople)): #iterates through the 'salespeople' list
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')



#The report does not include the total sales of each salesperson, which would be useful to show.
#The report would be better if presented as a table, instead of this list of statements.
#A dataframe with the data could easily be created to present the data as a table.