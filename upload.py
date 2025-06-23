import base64
import os

def up(dir):
   bool = 0
   os.makedirs("out", exist_ok=True)

   folder = dir if dir else "."
   items = os.listdir(folder)

   for x in items:
      path = os.path.join(folder, x)
      if x.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
         bool = 1
         with open(path, "rb") as img:
            encoded = base64.b64encode(img.read())

         name_without_ext = os.path.splitext(x)[0]

         with open(f"out/{name_without_ext}.txt", "wb") as f:
            f.write(encoded)
            
         os.remove(path)
   if bool == 0:
      print("No pictures were found")