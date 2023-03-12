import os
import random
import shutil

# Set the path to the folder containing the files
folder_path = "./combined_raw_data/"

# Set the ratio of files to be used for train, validation, and test sets
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Get a list of all the non-hidden files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') and os.path.isfile(os.path.join(folder_path, f))]
#files = [f[:-4] for f in files]

# Shuffle the list of files randomly to ensure that the files are processed in random pairs
random.shuffle(files)
print(files)

# Split the files into train, validation, and test sets
print(len(files))
num_files = len(files)
num_train = int(num_files * train_ratio)
num_val = int(num_files * val_ratio)
num_test = num_files - num_train - num_val

train_files = files[:num_train]
val_files = files[num_train:num_train+num_val]
test_files = files[num_train+num_val:]

# Create the train, validation, and test folders
train_folder = os.path.join(folder_path, "train")
val_folder = os.path.join(folder_path, "val")
test_folder = os.path.join(folder_path, "test")

os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Copy the files to the appropriate folders
for file_set, folder_name in [(train_files, train_folder), (val_files, val_folder), (test_files, test_folder)]:
    for file in file_set:
        # Get the file names for the image and text files
        image_file = os.path.join(folder_path, file)
        text_file = os.path.join(folder_path, os.path.splitext(file)[0] + ".txt")

        # Create the destination paths for the image and text files
        dest_image_file = os.path.join(folder_name, file)
        dest_text_file = os.path.join(folder_name, os.path.splitext(file)[0] + ".txt")

        # Copy the image and text files to the appropriate folders
        shutil.copy2(image_file, dest_image_file)
        shutil.copy2(text_file, dest_text_file)

        print(f"Copied {file} and its corresponding .txt file to {folder_name}")
