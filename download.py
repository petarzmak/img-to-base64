import base64
import os

def down(dir):
    bool = 0
    os.makedirs("out", exist_ok=True)

    folder = dir if dir else "."
    items = os.listdir(folder)

    for x in items:
        path = os.path.join(folder, x)
        if x.lower().endswith((".txt")):
            bool = 1

            try:

                with open(path, "rb") as img:
                    decoded = base64.b64decode(img.read())
            except (base64.binascii.Error, ValueError) as e:
                print(f"ERROR: {x}: Incorrect format")
                continue
            except Exception as e:
                print(f"ERROR: {x}: Failed to read file - {e}")
                continue

            name_without_ext = os.path.splitext(x)[0]

            with open(f"out/{name_without_ext}.jpg", "wb") as f:
                f.write(decoded)
            
            os.remove(path)
    if bool == 0:
        print("No files were found")