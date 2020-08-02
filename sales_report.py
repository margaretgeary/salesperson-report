"""Generate sales report showing total melons each salesperson sold."""

def sales_report(file):

    sales_dict = {}
    sales_file = open(file)

    for line in sales_file:
        line = line.rstrip()
        entries = line.split('|')
        
        salesperson = entries[0]
        melons = int(entries[2])

        if salesperson in sales_dict:
            sales_dict[salesperson] += melons
        else:
            sales_dict[salesperson] = melons
    
    for salesperson, melons in sales_dict.items():
        print(f'{salesperson} sold {melons} melons')
 
sales_report("sales-report.txt")

# # Creating lists for salespeople and melon sold.
# salespeople = []
# melons_sold = []

# # Opening txt file
# f = open('sales-report.txt')
# # For each line in the file
# for line in f:
#     # Stripping whitespace to the right
#     line = line.rstrip()
#     # Each entry is separated by a |
#     entries = line.split('|')

#     # Salesperson is at index 0.
#     salesperson = entries[0]
#     # Melons sold int is at index 2
#     melons = int(entries[2])

#     # If salesperson is in the list salespeople:
#     if salesperson in salespeople:
#         # Set variable position to the index of salesperson in list salespeople
#         position = salespeople.index(salesperson)
#         # Add the number of melons sold at that position to melons total
#         melons_sold[position] += melons
#     else:
#     # If a salesperson is not yet in the list salespeople:
#         salespeople.append(salesperson)
#         # Append the list salespeople with salesperson
#         melons_sold.append(melons)
#         # Append the list melons_sold with melons


# for i in range(len(salespeople)):
# # For each item in the range of length of salespeople
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')
#     # Print the the total number of melons sold by each salesperson
