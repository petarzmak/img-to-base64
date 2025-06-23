import upload
import download

print("Hello")
print("Welcome to Pete's base64 Encoder and Decoder")
dir = input("Please enter the directory where your files are located (if they are in the same dir as this exe, simply hit enter):")
print("If you would like to Encode input \'1\'")
print("If you would like to Decode input \'2\'")

hi = input()

if hi == "1":
    upload.up(dir)
elif hi == "2":
    download.down(dir)
else:
    print("Invalid Input")

print("Thank you for using Pete's Program. If successful, your files will be in the \'out\' folder")
input("Please hit enter to exit")