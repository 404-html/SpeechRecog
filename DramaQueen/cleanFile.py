import easygui

easygui.msgbox("Enter the file you want to clean")

readfile = easygui.fileopenbox()

infile = open(readfile, 'r')

outfile = open('clean_script.txt','w')

for line in infile:
    for ch in line:
        if (ch > '~'):
            outfile.write(" . ")
        elif (ch == '.'):
            outfile.write(" . ")
        elif (ch == ':'):
            outfile.write(" ")
        elif (ord(ch) >= 65 and ord(ch) <= 90):
            num = ord(ch) - 65 + 97
            char = chr(num)
            string = str(char)
            outfile.write(string)
        else:
            outfile.write(ch)
infile.close()
outfile.close()

easygui.msgbox("Clean file saved as clean_script.txt")
