import os
import csv

def saveRecords(filename, data):
    file_exists = os.path.isfile(filename) #  check if file exists
    
    try:
        with open(filename, mode='a', newline='') as file:
            fieldnames = ["First Name", "Middle Name",
                          "Last Name", "Birthday", "Gender"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # write the header only if the file does not exist 
            if not file_exists:
                writer.writeheader()
    
# Write the new record to the file
            writer.writerow({
                "First Name": data[0],
                "Middle Name": data[1],
                "Last Name": data[2],
                "Birthday": data[3],
                "Gender": data[4]
            })
    except Exception as e:
        print("Error saving record: ", e)
        
        
# FUNCTION load records
def loadRecords(filename):
    try:    
        if not os.path.exists(filename):
            return []
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)       
            records = list(reader)
            return records
    except Exception as e:
        print("Error loading records: ", e)
        return []
    
    
    
            
    