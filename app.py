import os
import shutil

file_types = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".webp": "Images",
    ".gif": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".xlsx": "Documents",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    ".exe": "Programs",
    ".msi": "Programs",
    ".msix": "Programs",

    ".json": "Data",
    ".csv": "Data",
    ".log": "Data",
}

downloads = "C:/Users/Abdulqader/Downloads"
for i in os.listdir(downloads):
    if os.path.isdir( os.path.join(downloads, i)) == True:
        continue
    ext = os.path.splitext(i)[1].lower()

    folder_name = file_types.get(ext, "Other")
    folder_path = os.path.join(downloads, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    source = os.path.join(downloads, i)
    destination = os.path.join(folder_path, i)

    shutil.move(source, destination)
