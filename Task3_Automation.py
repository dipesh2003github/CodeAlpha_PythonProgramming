import os
import shutil

source_folder = "F:\CodeAlpha Intership\Main Image"
destination_folder = "F:\CodeAlpha Intership\Second Image"

# Create destination folder if not exists
os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source_folder, file),
                    os.path.join(destination_folder, file))
        print(f"Moved: {file}")

print("All .jpg files moved successfully!")