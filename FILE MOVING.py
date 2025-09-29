import os
import shutil

def move_jpg_files(src_folder, dest_folder):
    # ✅ Create destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)

    # 🔁 Loop through files in the source folder
    for filename in os.listdir(src_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(src_folder, filename)
            destination_path = os.path.join(dest_folder, filename)

            try:
                shutil.move(source_path, destination_path)
                print(f"✅ Moved: {filename}")
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")

#  Replace the paths below with your actual folder locations
source_folder = "C:/Users/YourName/Pictures"         # 👈 Your source folder path
destination_folder = "C:/Users/YourName/Archived_JPGs"  # 👈 Your destination folder path

#Run the function
move_jpg_files("C:\SRC-folder path","C:\Google PHOTOS\dest-folder path") #paste actual path details here
            