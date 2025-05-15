# 📂 File Organizer Script by PAMUGR (Tutorial from Alex HYETT)

This Python script automates the organization of files in your **Downloads** folder by sorting and moving them into categorized folders based on file extensions and creation dates.

---

## 🚀 Features

- Automatically sorts files into folders like **Photos**, **Documents**, **Code**, **Text**, **Compressions**, etc.
- Organizes files by **Year** and **Month** based on filenames or file creation dates.
- Creates target folders automatically if they don’t exist.
- Detects duplicate files by comparing sizes and removes duplicates from the source.
- Cleans up any leftover unclassified files and folders from the source directory.

---

## 🛠 How It Works

1. Define your **source folder** (default: Downloads) and **target folders** for different file types.
2. Specify file extensions grouped by category.
3. Extract date info from the filename or fallback to file creation/modification date.
4. Move files into folders structured as:


5. Delete any files or folders remaining in the source folder that don’t match the known extensions.

---

## ⚠️ Important Notes

- **Backup your files before running this script!**  
The script deletes files considered duplicates or unclassified, so accidental data loss is possible.

- The script supports macOS, Linux, and Windows, but behavior may vary due to differences in how these systems handle file creation dates.

- Modify the folder paths and file extensions inside the script to match your setup and needs.
