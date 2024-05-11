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
        

        
        
        
        
file = open_file(filename="/Users/abbeykratman/Downloads/4_30.txt")
modified_lines = editor(file)
random_add(modified_lines)

for line in modified_lines:
    print(line)



        
        
        