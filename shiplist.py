import random 


def open_file(filename):
    with open(filename, "r") as f:
        all_lines = f.readlines()
    return all_lines


def editor(lines):
    
    index_shiplist = -1
        
    for i, line in enumerate(lines):
        if "Weekly Shiplist for Wednesday" in line:
            index_shiplist = i
            del lines[:index_shiplist] 
            i = 0
            lines.insert(i + 1, '</b></u></em>')
            lines.insert(i, '<b><u><em>DC/Lunar Shortages</b></u></em><ul></ul><br><br><b><u><em>Diamond Shortages</b></u></em><ul></ul><br><br><b><u><em>Delayed by Diamond</b></u></em><ul></ul><br><br><b><u><em>')  
            break

    for i, line in enumerate(lines):  
        lines[i] = '<br>' + lines[i].strip()

    return lines

   
def random_add(lines):
    
    i = 2
    
    
    for i, line in enumerate(lines):
        if "Weekly Shiplist for Wednesday" in line:
            start = i + 8
            

        if "DC/Lunar Shiplist for Wednesday," in line:
            end = i - 8
            break
           
    prev_indices = []  # Keep track of previously chosen indices
    
    for _ in range(6):
        chosen_index = random.randint(start, end)
        
        # Check if the chosen index is within 3 lines of any previous index
        while any(abs(chosen_index - prev_index) <= 3 for prev_index in prev_indices):
            chosen_index = random.randint(start, end)
        
      
        # Insert new content at chosen index
        lines.insert(chosen_index - 1, '<br><br><b>')
        lines.insert(chosen_index + 1, '</b><ul> TESTING     <em></em></ul><br>')
        
        # Print the line with "previewsworld" and remove <br> from it
        line_to_print = lines[chosen_index].replace("<br>", "")
        print(line_to_print + " previewsworld \n")
        
        # Remove <br> from the chosen line
        lines[chosen_index] = lines[chosen_index].replace("<br>", "")
        
        
        
        # Add chosen index to the list of previous indices
        prev_indices.append(chosen_index)
        

        

from datetime import datetime, timedelta
import calendar

def next_wednesday():
    today = datetime.today()
    # Calculate the number of days until the next Wednesday (0=Monday, 1=Tuesday, ..., 6=Sunday)
    days_until_wednesday = (2 - today.weekday() + 7) % 7
    # Add the number of days until Wednesday to the current date
    next_wednesday_date = today + timedelta(days=days_until_wednesday)
    
    # Get month name from month number
    month_name = calendar.month_name[next_wednesday_date.month]
    
    return f"{month_name} {next_wednesday_date.day} {next_wednesday_date.year}"



import sys
from datetime import datetime

def runFile(uploadedFile):
    input_filename = uploadedFile
    output_filename = "processed_output.txt"
    
    try:
        with open(input_filename, "r") as input_file:
            file_content = input_file.read()

        # Get the current date in the format "DD MM YYYY"
        current_date = datetime.now().strftime("%d %m %Y")
        
        # Replace "DD MM YYYY" with the current date
        file_content = file_content.replace("DD MM YYYY", next_wednesday())
        
        # Process the file content here
        # For demonstration, let's just copy the content to the output file
        with open(output_filename, "w") as output_file:
            output_file.write(file_content)
            
        print("File processed successfully.")
        print("Processed output saved in:", output_filename)
        
    except FileNotFoundError:
        print("File not found:", input_filename)
    except Exception as e:
        print("An error occurred during file processing:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        uploadedFile = sys.argv[1]
        runFile(uploadedFile)
