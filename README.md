# Automatic File Sorter

A Python script that sorts a cluttered folder into categorised subfolders by file type.

I built this because my Downloads folder had a few hundred files in it — installers, coursework, screenshots, zip archives — with no structure at all. Running this sorts everything in one go.

## What it does

The script goes through every item in a target folder and:

- skips any subfolders, so only files get moved
- reads each file's extension
- looks the extension up in a dictionary to find the right destination folder
- creates that folder if it doesn't already exist
- moves the file into it

Anything with an extension the script doesn't recognise goes into an `Other` folder, so nothing is left behind or silently skipped.

## Categories

| Folder | Extensions |
|---|---|
| Images | `.png` `.jpg` `.jpeg` `.webp` `.gif` |
| Documents | `.pdf` `.docx` `.doc` `.txt` `.pptx` `.xlsx` |
| Archives | `.zip` `.rar` `.7z` `.tar` `.gz` |
| Programs | `.exe` `.msi` `.msix` |
| Data | `.json` `.csv` `.log` |
| Other | anything else |

Adding a new file type is a single line in the `file_types` dictionary — no new logic needed.

## Usage

Set `downloads` to the folder you want to sort, then run:
