# from importlib.resources import path
# from docx import  Document

""" >>> The backslash character is interpreted as an escape. Use double backslashes for windows paths!!! or you could use raw strings adding r before the string"""
# mypath='C:\\Users\\ligia\\Documents\\faculdade\\autoensino\\codigo[s]\\exercicios\\'
# mypath= r'C:\Users\ligia\Documents\faculdade\autoensino\codigo[s]\exercicios'
# mypath=os.path.normpath(r'C:\Users\ligia\Documents\faculdade\autoensino\codigo[s]\exercicios')#adds double slashes to the path

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]#list of the file elements in the folder

# mypath= os.getcwd()#returns current directory of python script
# onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.abspath(f))]#list of the file elements in the folder

# files_path = [os.path.abspath(x) for x in os.listdir()if os.path.isfile(os.path.abspath(x))] #makes a list of the complete path of all the files in the directory of the code

#========================================================================================================================
import os
import textract
import unidecode
mypath= os.path.dirname(os.path.realpath(__file__))#returns current directory of python script
print(mypath)
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.abspath(f))]#list of the file elements in the folder
# print(onlyfiles)
for file in onlyfiles:
    if ".pdf" in file or ".docx" in file:#identify word document on directory 
        python_file = open(mypath+"\\"+ file[:file.index(".")]+".py", "w")#create python file of the same name as the word file on the current directory
        text = textract.process(file)#extract text from microsoft word file
        text = unidecode.unidecode(text.decode("utf-8")) #convert the object text to a string and remove the accents on the string
        # print(text)

        text_lines=text.split("\n")
        python_file.write('"""') 
        for line in text_lines:
            if "Exerc" in line or "Desaf"in line:#desafio e exercicio
                python_file.write(f'"""\n\n"""{"="*15}{line[:-1]}{"="*15}\n')
            elif line=="":
                python_file.write(line)
            else:
                if len(line)>150:#line is too big and next sentence should be placed on line bellow for better reading
                    python_file.write(line[:line.index(".")+1]+"\n"+line[line.index(".")+1:]+"\n")
                else:
                    python_file.write(line+"\n")  

        python_file.write('"""')
        python_file.close()
