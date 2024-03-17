import os
from tkinter import filedialog

folderpath = filedialog.askdirectory()
#filepath = filedialog.askopenfilename()

if folderpath  != "":
    os.chdir(folderpath)
else:
    exit()

for i in os.listdir():
    text_touple = os.path.splitext(i)
    extension = text_touple[-1]

    if extension != "":
        extension = extension.replace(".",",")

        try:
            os.mkdir(f"{extension}_files")
        except FileExistsError:
            pass
        except Exception as e:
            print(e)

    else:
         print(f"FOLDER_{i}")
         pass
    
print("\n\n\t\t:") 

        