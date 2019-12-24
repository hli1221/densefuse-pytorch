from os import listdir, remove
import shutil
import random

dataset_lwri = '/data/huili/database/KAIST-database/lwir/'
dataset_vis = '/data/huili/database/KAIST-database/visible/'
dataset_val_lwir = '/data/huili/database/KAIST-database/validation/lwir/'
dataset_val_vis = '/data/huili/database/KAIST-database/validation/visible/'

# dataset_lwri = "D:/database/ImageFusion/KAIST Multispectral database/set05/lwir/"
# dataset_vis = "D:/database/ImageFusion/KAIST Multispectral database/set05/visible/"
# dataset_val_lwir = "D:/database/ImageFusion/KAIST Multispectral database/test/lwir/"
# dataset_val_vis = "D:/database/ImageFusion/KAIST Multispectral database/test/visible/"

image_paths = listdir(dataset_lwri)
image_paths.sort()
# random
random.shuffle(image_paths)

num_imgs = 10
original_img_paths = image_paths[:num_imgs]
count = 0
for img_path in original_img_paths:
    count += 1
    oldname_lwri = dataset_lwri + img_path
    newname_lwri = dataset_val_lwir + img_path
    shutil.copyfile(oldname_lwri, newname_lwri)
    remove(oldname_lwri)

    oldname_vis = dataset_vis + img_path
    newname_vis = dataset_val_vis + img_path
    shutil.copyfile(oldname_vis, newname_vis)
    remove(oldname_vis)
    if count == 100:
        print('move number:' + str(count))
