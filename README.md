# File Organizer Script by PAMUGR
This Python script automates the organization of files in your Downloads folder by moving them into categorized folders based on their file extensions and creation dates.

Features
Automatically sorts files into folders like Photos, Documents, Code, Text, Compressions, etc.

Organizes files by year and month based on file names or creation dates.

Creates necessary folders if they don’t exist.

Detects duplicates by file size and removes duplicates from source.

Cleans up unclassified files/folders left in the source folder.

How it Works
Define the source folder (Downloads) and multiple target folders for file types.

Specify file extensions grouped by category.

For each file, extract the date from the filename or creation date.

Move files into folders structured as:
TargetFolder/Year/Month/Extension/

Delete files/folders in source folder that do not match the known extensions.

Important Notes
Back up your files before running this script! It deletes files it considers duplicates or unclassified.

The script assumes macOS/Linux or Windows but may behave differently on some systems due to how file creation dates are retrieved.

Modify folder paths and extensions in the script as needed.

