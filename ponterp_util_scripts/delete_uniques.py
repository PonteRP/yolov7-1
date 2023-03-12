import os

folder_path = "./data/val" # replace with the actual path of the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg"):
        txt_file_name = os.path.splitext(file_name)[0] + ".txt"
        if not os.path.isfile(os.path.join(folder_path, txt_file_name)):
            os.remove(os.path.join(folder_path, file_name))
            print(f"Deleted {file_name}")
