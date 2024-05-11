import random

def open_file(filename):
    with open(filename, "r") as f:
        all_lines = f.readlines()
    return all_lines

def replace_line(lines, line_number, new_line):
    if 0 < line_number <= len(lines):
        lines[line_number - 1] = new_line + "\n"  # Adjust line number to 0-based index
    else:
        print("Invalid line number.")

def editor(lines):
    modified_lines = []  # Initialize an empty list to store modified lines
    index_shiplist = -1

    # Find the index where "Weekly Shiplist for Wednesday" appears
    for i, line in enumerate(lines):
        if "Weekly Shiplist for Wednesday" in line:
                index_shiplist = i  # Store the index of the first occurrence
                       # Replace the line with the desired format
                print(lines[i])
                html_start = "<b><u><em>DC/Lunar Shortages</b></u></em><ul></ul><br><br><b><u><em>Diamond Shortages</b></u></em><ul></ul><br><br><b><u><em>Delayed by Diamond</b></u></em><ul></ul><br><br><b><u><em>"
                new_line = "Weekly Shiplist for Wednesday, DD MM YYYY"
                lines.insert(i + 2, '</b></u></em>')     
                replace_line(lines, i, html_start + new_line)
                replace_line(lines, i + 1, "")
                for i, line in enumerate(lines):
                    if i != index_shiplist and "Weekly Shiplist for Wednesday" in line:
                        replace_line(lines, i, "Hello!")
                        break
                print(f"Line replaced at index {i}: {new_line}")  # Debugging print
                # Delete lines before the modified line
                del lines[:i]
                break

    # Find the index where "DC/Lunar Shiplist for Wednesday," appears
    for t, line in enumerate(lines):
        if "DC/Lunar Shiplist for Wednesday," in line:  
            html_start2 = "<b><u><em>"    
            replace_line(lines, t, html_start2 + "DC/Lunar Shiplist for Wednesday, DD MM YYYY </b></em></u>")
            replace_line(lines, t + 1, "")

            print(lines[t])  # Print the modified line
            break

    # Add '<br>' to the beginning of lines if not already present
    for line in lines:  
        if not line.strip().startswith('<br>'):
            modified_lines.append('<br>' + line.strip())
        else:
            modified_lines.append(line.strip())

    print("Editor changes applied successfully.")
    return modified_lines  # Return the modified lines



def random_add(lines):
    # Find the index where "Weekly Shiplist for Wednesday" appears
    start = None
    for i, line in enumerate(lines):
        if "Weekly Shiplist for Wednesday" in line:
            start = i + 6
            break

    # Find the index where "DC/Lunar Shiplist for Wednesday," appears
    end = None
    for i, line in enumerate(lines):
        if "DC/Lunar Shiplist for Wednesday," in line:
            end = i - 4
            break
    prev_indices = []  # Keep track of previously chosen indices
    if start is not None and end is not None:
        for _ in range(6):
            chosen_index = random.randint(start, end)
            while any(abs(chosen_index - prev_index) <= 3 for prev_index in prev_indices):
                chosen_index = random.randint(start, end)
            lines.insert(chosen_index - 1, '<br><br><b>')
            lines.insert(chosen_index + 1, '</b><ul>\n<em>TESTING</em></ul><br>')
            line_to_print = lines[chosen_index].replace("<br>", "")
            print(line_to_print + " previewsworld \n")
            lines[chosen_index] = lines[chosen_index].replace("<br>", "")
            prev_indices.append(chosen_index)

    print("Random additions applied successfully.")
    return lines


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


def runFile(uploadedFile):
    #print("Running.")
    input_filename = uploadedFile
    output_filename = "processed_output.txt"
   
    try:
        with open(input_filename, "r") as input_file:
            file_content = input_file.readlines()  # Read lines into a list
        current_date = datetime.now().strftime("%d %m %Y")
        
        # Apply editor modifications
        modified_lines = editor(file_content)  
        
        # Apply random additions
        modified_lines = random_add(modified_lines)  
        
        # Replace "DD MM YYYY" with the next Wednesday's date
        modified_lines = [line.replace("DD MM YYYY", next_wednesday()) for line in modified_lines]

        modified_content = '\n'.join(modified_lines)  # Join lines into a single string
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)  # Write modified content to the output file
       
        #print("File processed successfully.")
       # print("Processed output saved in:", output_filename)
    except FileNotFoundError:
        print("File not found:", input_filename)
    except Exception as e:
        print("An error occurred during file processing:", str(e))

    #print("End of function")  # Add this line to check if the function completes execution

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        uploadedFile = sys.argv[1]
        runFile(uploadedFile)
