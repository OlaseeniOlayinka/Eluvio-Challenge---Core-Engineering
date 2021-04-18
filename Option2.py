import os

def is_binary(file_name):
    try:
        with open(file_name, 'tr') as f:  # try open file in text mode
            print(f.read())
            return False
    except:  # if fail then file is non-text (binary)
        return True

directory = 'C:/Users/Seeni/OneDrive/Desktop/Resume/Eluvio/Sample_files'

output_map = {}

len_repeated_line = 0
res = ""

for a in (os.scandir(directory)):
    filename = str(a).split('\'')[1]
    full_file_name = directory + "/" + filename
    #print(full_file_name)
    if is_binary(full_file_name):
        infile = open(full_file_name, 'rb')
        i = 1
        for line in infile:
            #output.append(line)
            i += len(line)
            if line not in output_map:
                output_map[line] = [(filename, i)]
            else:
                output_map[line].append((filename, i))

                if len_repeated_line < len(line):
                    len_repeated_line = len(line)
                    res = line

        infile.close()

with open('output.txt', 'w') as file:
    file.write("length of strand " + str(len(res)) + '\n')

    for value in output_map[res]:
        file.write("file name: " + value[0] + "; ")
        file.write("strand offset: " + str(value[1]) + "\n")