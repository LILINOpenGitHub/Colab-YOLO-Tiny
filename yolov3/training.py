import os

image_files = []
os.chdir(os.path.join("/content/gdrive/MyDrive","yolov3","COCO_Dataset"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("/content/gdrive/MyDrive/yolov3/COCO_Dataset/" + filename)
os.chdir("..")
with open("/content/gdrive/MyDrive/yolov3/train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
