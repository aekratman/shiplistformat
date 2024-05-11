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
        

        
  #      
#def runFile(uploadedFile):
 #   file = open_file(uploadedFile)
  #  modified_lines = editor(file)
   # random_add(modified_lines)

    #for line in modified_lines:
     #   print(line)



import sys

def runFile(uploadedFile):
    input_filename = uploadedFile
    output_filename = "processed_output.txt"
    
    try:
        with open(input_filename, "r") as input_file:
            file_content = input_file.read()

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




        
        
        