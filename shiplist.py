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
        lines[i] = '<br>' + line.strip()  # Corrected from lines[i]
        if "Weekly Shiplist for Wednesday" in line:
            start = i + 8
            lines[i] = line.replace(line, "Weekly Shiplist for Wednesday, DD MM YYYY")  # Corrected from lines[i]
            print("Replacement happened!")

    return lines

   
def random_add(lines):
    start = None
    end = None
    for i, line in enumerate(lines):
        if "Weekly Shiplist for Wednesday" in line:
            start = i + 8
            lines[i] = line.replace(line, "Weekly Shiplist for Wednesday, DD MM YYYY")
            print(lines[i], "Replacement happened!")
        if "DC/Lunar Shiplist for Wednesday," in line:
            end = i - 8
            lines[i] = line.replace(line, "DC/Lunar Shiplist for Wednesday,  DD MM YYYY")
            print(lines[i], "Replacement happened!")
            break
    prev_indices = []  # Keep track of previously chosen indices
    if start is not None and end is not None:
        for _ in range(6):
            chosen_index = random.randint(start, end)
            while any(abs(chosen_index - prev_index) <= 3 for prev_index in prev_indices):
                chosen_index = random.randint(start, end)
            lines.insert(chosen_index - 1, '<br><br><b>')
            lines.insert(chosen_index + 1, '</b><ul> TESTING     <em></em></ul><br>')
            line_to_print = lines[chosen_index].replace("<br>", "")
            print(line_to_print + " previewsworld \n")
            lines[chosen_index] = lines[chosen_index].replace("<br>", "")
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
    print("Running.")
    input_filename = uploadedFile
    output_filename = "processed_output.txt"
   
    try:
        with open(input_filename, "r") as input_file:
            file_content = input_file.readlines()  # Read lines into a list
        current_date = datetime.now().strftime("%d %m %Y")
        file_content = [line.replace("DD MM YYYY", next_wednesday()) for line in file_content]  # Replace date
        modified_lines = editor(file_content)  # Apply editor modifications
        random_add(modified_lines)  # Apply random additions
        modified_content = '\n'.join(modified_lines)  # Join lines into a single string
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)  # Write modified content to the output file
       
        print("File processed successfully.")
        print("Processed output saved in:", output_filename)
    except FileNotFoundError:
        print("File not found:", input_filename)
    except Exception as e:
        print("An error occurred during file processing:", str(e))

    print("End of function")  # Add this line to check if the function completes execution

