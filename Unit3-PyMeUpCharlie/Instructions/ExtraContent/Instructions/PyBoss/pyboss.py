import os
import csv

#Path to collect data from the Resources folder
file_path = os.path.join("Resources", "employee_data.csv")

#Global variables
rows = []


#Import the employee_data.csv file into the rows list
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    rows = []
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            rows.append(row)

print rows[0:5]

# #Loop through the rows list and calculate the change.  Append it to the rows list.
# for row in rows:
#     row_value = int(row[1])
#     net_prf_loss += row_value
#     if previous_value == 0:
#         change = 0
#     else:
#         change = row_value - previous_value
#     row.append(change)
#     previous_value =  row_value

# #Loop through the rows list and calculate the total change.  
# #Find the rows with the greatest increase and decrease and set the corresponding variables
# #Find the average change
# for change in rows:
#     change_value = change[2]
#     total_change += change_value
#     increase_value = change[2]
#     if increase_value > greatest_increase:
#         greatest_increase= increase_value
#         greatest_increase_month = change[0]
#     elif increase_value < greatest_decrease:
#         greatest_decrease= increase_value
#         greatest_decrease_month = change[0]
#     else:
#         continue
# average_change = round(total_change / (len(rows)-1),2)

# #Print data
# print("Financial Analysis")
# print ("-------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${net_prf_loss}")
# print(f"Average Change: ${average_change}")
# print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
# print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# # Output to file
# output_path = os.path.join("Output", "financial_analysis.csv")

# # Open the file using "write" mode and specify the variable
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the Title and Totals
#     csvwriter.writerow(['Financial Analysis'])
#     csvwriter.writerow(['Total Months',total_months])
#     csvwriter.writerow(['Total Months',net_prf_loss])
#     csvwriter.writerow(['Greatest Increase in Profits',greatest_increase_month, greatest_increase])
#     csvwriter.writerow(['Greatest Decrease in Profits',greatest_decrease_month, greatest_decrease])
