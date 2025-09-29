import os
import shutil

def move_jpg_files():
    # 🔹 Define your source and destination folders here
    src_folder = "C:\src-folder-path"        # 👈 SOURCE folder (where your .jpg files are now)
    dest_folder = "C:\dest folder path"        # 👈 DESTINATION folder (where you want to move them)

    # Create destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)

    # Loop through files in the source folder
    for filename in os.listdir(src_folder):
        if filename.lower().endswith(".pdf"): #CHANGE FORMAT HERE i.e .jpg to .pdf for other fromat of files if not .jpg
            source_path = os.path.join(src_folder, filename)
            destination_path = os.path.join(dest_folder, filename)

            try:
                shutil.move(source_path, destination_path)
                print(f"✅ Moved: {filename}")
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")

#  Just call the function — no need to pass anything
move_jpg_files()