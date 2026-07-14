import os
import shutil

TARGET_DIRECTORY  = os.path.expanduser("~/Downloads")

MAPPINGS = {
    "Images":[".jpg", ".png", ".gif", "jpeg" ],
    "Documents":[".pdf", ".docx", ".txt", ".xlsx"],
    "Videos":[".mp4", ",.mkv", ".mov"] ,
    "Music":[".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code":[".py", ".js", ".html", ".css"],
}

for filename in os.listdir(TARGET_DIRECTORY):
    file_path = os.path.join(TARGET_DIRECTORY, filename) 

    if os.path.isdir(file_path):
        continue
    
    ext= os.path.splitext(filename)[1].lower()

    folder_name = next((k for k , exts in MAPPINGS.items() if ext in exts),"Others")
    dest_dir = os.path.join(TARGET_DIRECTORY , folder_name)

    os.makedirs(dest_dir , exist_ok=True)
    shutil.move(file_path, os.path.join(dest_dir, filename))

print("Organization complete!")  

    
 