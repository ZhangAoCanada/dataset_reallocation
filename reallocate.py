import os, sys, shutil
import cv2, pickle
import numpy as np
from tqdm import tqdm


def readSequences(filename):
    """ Read sequences from PROJECT_ROOT/sequences.txt """
    sequences = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            sequence_number = int(line.split()[0])
            sequences.append(sequence_number)
    if len(sequences) == 0:
        raise ValueError("err")
    return sequences

def checkDir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


if __name__ == "__main__":
    train_seq = readSequences("./sequences_train.txt")
    test_seq = readSequences("./sequences_test.txt")

    root_dir = "../RADDet_DATASET"

    train_dir = os.path.join(root_dir, "train")
    train_RAD_dir = os.path.join(train_dir, "RAD")
    train_gt_dir = os.path.join(train_dir, "gt")
    train_image_dir = os.path.join(train_dir, "stereo_image")

    test_dir = os.path.join(root_dir, "test")
    test_RAD_dir = os.path.join(test_dir, "RAD")
    test_gt_dir = os.path.join(test_dir, "gt")
    test_image_dir = os.path.join(test_dir, "stereo_image")

    checkDir(root_dir)

    checkDir(train_dir)
    checkDir(train_RAD_dir)
    checkDir(train_gt_dir)
    checkDir(train_image_dir)

    checkDir(test_dir)
    checkDir(test_RAD_dir)
    checkDir(test_gt_dir)
    checkDir(test_image_dir)

    original_dir = "/media/ao/Aooooo/DATASET_stationary"
    count = 1

    for i in tqdm(range(len(train_seq))):
        RAD_part_dir = os.path.join(train_RAD_dir, "part_" + str(count))
        gt_part_dir = os.path.join(train_gt_dir, "part_" + str(count))
        image_part_dir = os.path.join(train_image_dir, "part_" + str(count))
        checkDir(RAD_part_dir)
        checkDir(gt_part_dir)
        checkDir(image_part_dir)

        train_i = train_seq[i]
        RAD_file = os.path.join(os.path.join(original_dir, "RAD"), \
                                            "%.6d.npy"%(train_i))
        gt_file = os.path.join(os.path.join(original_dir, "gt_box"), \
                                            "%.6d.pickle"%(train_i))
        image_file = os.path.join(os.path.join(original_dir, "images"), \
                                            "%.6d.jpg"%(train_i))

        RAD_target_file = os.path.join(RAD_part_dir, "%.6d.npy"%(train_i))
        gt_target_file = os.path.join(gt_part_dir, "%.6d.pickle"%(train_i))
        image_target_file = os.path.join(image_part_dir, "%.6d.jpg"%(train_i))

        # if i == 0:
            # print(RAD_file)
            # print(gt_file)
            # print(image_file)
            # print(RAD_target_file)
            # print(gt_target_file)
            # print(image_target_file)
            # continue

        ##### shutil.move("path/to/current/file.foo", \
        #####            "path/to/new/destination/for/file.foo")
        shutil.move(RAD_file, RAD_target_file)
        shutil.move(gt_file, gt_target_file)
        shutil.move(image_file, image_target_file)

        if (i+1) % 1000 == 0:
            count += 1

    count = 1
    for i in tqdm(range(len(test_seq))):
        RAD_part_dir = os.path.join(test_RAD_dir, "part_" + str(count))
        gt_part_dir = os.path.join(test_gt_dir, "part_" + str(count))
        image_part_dir = os.path.join(test_image_dir, "part_" + str(count))
        checkDir(RAD_part_dir)
        checkDir(gt_part_dir)
        checkDir(image_part_dir)

        test_i = test_seq[i]
        RAD_file = os.path.join(os.path.join(original_dir, "RAD"), \
                                            "%.6d.npy"%(test_i))
        gt_file = os.path.join(os.path.join(original_dir, "gt_box"), \
                                            "%.6d.pickle"%(test_i))
        image_file = os.path.join(os.path.join(original_dir, "images"), \
                                            "%.6d.jpg"%(test_i))

        RAD_target_file = os.path.join(RAD_part_dir, "%.6d.npy"%(test_i))
        gt_target_file = os.path.join(gt_part_dir, "%.6d.pickle"%(test_i))
        image_target_file = os.path.join(image_part_dir, "%.6d.jpg"%(test_i))

        # if i == 0:
            # print(RAD_file)
            # print(gt_file)
            # print(image_file)
            # print(RAD_target_file)
            # print(gt_target_file)
            # print(image_target_file)
            # break

        ##### shutil.move("path/to/current/file.foo", \
        #####            "path/to/new/destination/for/file.foo")
        shutil.move(RAD_file, RAD_target_file)
        shutil.move(gt_file, gt_target_file)
        shutil.move(image_file, image_target_file)

        if (i+1) % 1000 == 0:
            count += 1

