# ====================== TUTORIAL FROM ALEX HYETT ======================
# =============== MADE SOME CHANGES, ADDED NEW MECHANICS ===============
# =============================== PAMUGR ===============================

import os
import re
import platform
import datetime
import shutil

# Folders for each place to extract from and place to insert
source_folder = "/Users/PAU/Downloads"
target_photos = "/Users/PAU/Desktop/Fotos/Others"
target_cpp = "/Users/PAU/Desktop/CS/C++"
target_python = "/Users/PAU/Desktop/CS/PYTHON"
target_html = "/Users/PAU/Desktop/CS/HTML"
target_documents = "/Users/PAU/Desktop/Documents"
target_photos_camera = "/Users/PAU/Desktop/Fotos/Camera/Ordenar"
target_compressions = "/Users/PAU/Desktop/Compressions"
target_text = "/Users/PAU/Desktop/Text"

# Grouped extensions by type (category -> list of extensions)
EXTENSION_GROUPS = {
    target_photos:           ("jpg", "jpeg", "png", "mov", "mp4"),
    target_photos_camera:    ("rw2",),
    target_documents:        ("pdf", "docx", "doc", "ppxt", "xlsx"),
    target_compressions:     ("zip", "tar", "tgz"),
    target_cpp:              ("cc", "cpp", "hh"),
    target_python:           ("py",),
    target_html:             ("css", "html"),
    target_text:             ("txt",)
}

# Automatically generate a flat extension -> folder mapping (KEY IS THE EXTENSION)
EXTENSION_MAP = {}
for folder, extensions in EXTENSION_GROUPS.items():
    for ext in extensions:
        EXTENSION_MAP[ext] = folder

# Date Extraction Pattern from Alex Hyett
DATE_PATTERN = r'.*(20\d\d)-?([01]\d)-?([0123]\d).*'

# Get folder by year/month to add it as folders
def getFolder(year, monthNumber):
    months = {
        "01": "01 January", "02": "02 February", "03": "03 March", "04": "04 April",
        "05": "05 May", "06": "06 June", "07": "07 July", "08": "08 August",
        "09": "09 September", "10": "10 October", "11": "11 November", "12": "12 December"
    }
    return os.path.join(year, months.get(monthNumber, "Unknown"))

# Get creation or modification date 
def creation_date(path_to_file):
    # Try to get the date that a file was created, falling back to when it was
    # last modified if that isn't possible.
    if platform.system() == 'Windows':
        timestamp = os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            timestamp = stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            timestamp = stat.st_mtime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Get year and month frm filename
def get_date(folder, filename):
    matchObj = re.match(DATE_PATTERN, filename)
    if (matchObj):
        year = matchObj.group(1)
        month = matchObj.group(2)
    else:
        dateCreated = creation_date(folder + "/" + filename)
        matchObj = re.match(DATE_PATTERN, dateCreated)
        if(matchObj):
            year = matchObj.group(1)
            month = matchObj.group(2)
        else:
            year = "0"
            month = "0"
            print("Unable to get date: " + file)

    # Dictionary for year and month
    return {"year": year, "month": month}

# Processing of files from Downloads
files = os.listdir(source_folder)

# Loop going through all files in Downloads
for file in files:
    ext = os.path.splitext(file)[1][1:].lower()
    if ext not in EXTENSION_MAP:
        continue
    
    # We will organize them by date (you can organize them by whatever you want)
    fileData = get_date(source_folder, file)
    year, month = fileData["year"], fileData["month"]

    if year == "0" or month == "0":
        continue

    base_path = EXTENSION_MAP[ext]
    # We will also be adding a folder for each extension so it will be ordered like
    # Folder -> Year -> Month -> EXTENSION
    folder_path = os.path.join(base_path, getFolder(year, month), ext)

    # WARNING! If the folder doesn't exist it will be created
    if not os.path.exists(folder_path):
        print("Creating folder:", folder_path)
        os.makedirs(folder_path)

    source_path = os.path.join(source_folder, file)
    target_path = os.path.join(folder_path, file)

    if not os.path.exists(target_path):
        print("Moving:", file)
        shutil.move(source_path, target_path)
    else:
        if os.stat(source_path).st_size == os.stat(target_path).st_size:
            print("Duplicate found, deleting:", file)
            os.remove(source_path)
        else:
            print("Duplicate with different size:", file)

# Delete the ones left
print("\nCleaning up unclassified files/folders...")

# Re-list the current contents after all moves
remaining_items = os.listdir(source_folder)

# WARNING! Loops to delete each file remaining WARNING!
# COMMENT THIS IF YOU DON'T WANT ANY IMPORTANT FILES NON EXISTENT IN EXTENSIONS REMOVED!!
for item in remaining_items:
    item_path = os.path.join(source_folder, item)

    try:
        if os.path.isfile(item_path):
            print("Deleting unclassified file:", item)
            os.remove(item_path)
        elif os.path.isdir(item_path):
            print("Deleting unclassified folder:", item)
            shutil.rmtree(item_path)
    except Exception as e:
        print(f"Could not delete {item}: {e}")
