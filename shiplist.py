import random

def open_file(filename):
    with open(filename, "r") as f:
        all_lines = f.readlines()
    return all_lines

def replace_line(lines, line_number, new_line):
    if 0 < line_number <= len(lines):
        lines[line_number - 1] = new_line + "\n"  
    else:
        print("Invalid line number.")

def editor(lines):
    modified_lines = [] 
    index_shiplist = -1



    for i, line in enumerate(lines):
        if "Penguin Random House Shiplist for Wednesday" in line:
                index_shiplist = i  
        
        # Replace the line with the desired format
                print(lines[i])
                html_start = "<b><u><em>"
                new_line = "Penguin Random House Shiplist for Wednesday, DD MM YYYY"
                lines.insert(i + 2, '</b></u></em>')     
                replace_line(lines, i, html_start + new_line)
                replace_line(lines, i + 1, "")
                for i, line in enumerate(lines):
                    if i != index_shiplist and "Penguin Random House Shiplist for Wednesday" in line:
                        replace_line(lines, i, "")
                        break
                print("We are updatin'!")
                print(f"Line replaced at index {i}: {new_line}")  # Debugging print
                break

    # title index
    for d, line in enumerate(lines):
        if "DC/Lunar Shiplist for Wednesday" or "Lunar/DC" in line:  
            print("DC/Lunar shiplist found.")
            html_start2 = "<b><u><em>"    
            replace_line(lines, d, html_start2 + "DC/Lunar Shiplist for Wednesday, DD MM YYYY </b></em></u>")
            replace_line(lines, d + 1, "")
            print(lines[d])  # Print the modified line
            break

    for t, line in enumerate(lines): 
        if "DC/Lunar Shortages" in line:  
            print("Shortages found.")
            html_start2 = "<b><u><em>"    
            replace_line(lines, t + 1, html_start2 + lines[t] + "</b></em></u>")
            print(lines[t])  # Print the modified line
            
        if "Delayed by Diamond" in line:
            print("Delays found.")
            html_start2 = "<b><u><em>"    
            replace_line(lines, t + 1, html_start2 + "Delayed by Diamond </b></em></u>")

            print(lines[t + 1])  # Print the modified line
            
        if "Penguin Random House Shortages" in line:  
            html_start2 = "<b><u><em>"    
            replace_line(lines, t + 1, html_start2 + "Diamond Shortages </b></em></u>")

            print(lines[t + 1])  # Print the modified line

        if "PRH Comics:" in line:  
            html_start2 = "<b><u><em>"    
            replace_line(lines, t + 1, html_start2 + "PRH Comics: </b></em></u>")

            print(lines[t + 1])  # Print the modified line

        if "PRH Manga:" in line:  
            html_start2 = "<b><u><em>"    
            replace_line(lines, t + 1, html_start2 + "PRH Manga: </b></em></u>")

            print(lines[t + 1])  # Print the modified line         

        if "PRH YA Books:" in line:  
            html_start2 = "<b><u><em>"    
            replace_line(lines, t + 1, html_start2 + "PRH YA Books: </b></em></u>")

            print(lines[t + 1])  # Print the modified line 


    # Add '<br>' to the beginning of lines if not already present!
    for line in lines:  
        if not line.strip().startswith('<br>'):
            modified_lines.append('<br>' + line.strip())
        else:
            modified_lines.append(line.strip())

    print("Editor changes applied successfully.")
    return modified_lines  # Return the modified lines



def random_add(lines):
    print("Running random additions:")
    start = None
    for i, line in enumerate(lines):
        if "Penguin Random House Shiplist" in line:
            start = i + 6
            print("Start found at line", start)
            break


# find the end of editable titles    
    end = None
    for i, line in enumerate(lines):
        if "DC/Lunar Shiplist" in line or "Lunar/DC Shiplist" in line:
            end = i + 14;
            print("End found at line", end)
            break


    prev_indices = []  

    for _ in range(6):
        while True:
            chosen_index = random.randint(start, end)
            line_text = lines[chosen_index].strip()

            # Ensure index is not too close to previous ones, not a forbidden line, and not blank
            if (line_text
                and all(abs(chosen_index - prev_index) > 3 for prev_index in prev_indices)
                and line_text not in [
                    "DC/Lunar Shiplist for Wednesday",
                    "</b><ul>",
                    "<em>	</em></ul> previewsworld",
                    "previewsworld",
                    " "
                ]):
                break  # Valid line found

        lines.insert(chosen_index - 1, '<br><br><b>')
        lines.insert(chosen_index + 1, '</b><ul>\n<em>	</em></ul><br>')

        line_to_print = lines[chosen_index].replace("<br>", "")
        print(line_to_print + " previewsworld \n")
        lines[chosen_index] = lines[chosen_index].replace("<br>", "")
        prev_indices.append(chosen_index)

    print("Random additions applied successfully.")
    return lines





from datetime import datetime, timedelta
import calendar


# confirm date is correct lol
def next_wednesday():
    today = datetime.today()
    days_until_wednesday = (2 - today.weekday() + 7) % 7
    next_wednesday_date = today + timedelta(days=days_until_wednesday)
    
    # month name from month number
    month_name = calendar.month_name[next_wednesday_date.month]
    
    return f"{month_name} {next_wednesday_date.day} {next_wednesday_date.year}"


def runFile(uploadedFile):

    input_filename = uploadedFile
    output_filename = "processed_output.txt"
   
    try:
        with open(input_filename, "r") as input_file:
            file_content = input_file.readlines() 
        current_date = datetime.now().strftime("%d %m %Y")
        
        # editor mods
        modified_lines = editor(file_content)  
        
        # random mods
        modified_lines = random_add(modified_lines)  
        
        modified_lines = [line.replace("DD MM YYYY", next_wednesday()) for line in modified_lines]

        modified_content = '\n'.join(modified_lines) 
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content) 
       
    except FileNotFoundError:
        print("File not found:", input_filename)
    except Exception as e:
        print("An error occurred during file processing:", str(e))


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        uploadedFile = sys.argv[1]
        runFile(uploadedFile)
