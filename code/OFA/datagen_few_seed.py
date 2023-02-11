import os
import sys
import random
import base64
import torch
import numpy as np
import pandas as pd
from PIL import Image
from io import BytesIO


# synset_words.txt to dict


def synset_words2dict(path=r'/home/xuwei/data/mini_imagenet/synset_words.txt'):
    dict_swords = {}
    with open(path, 'r') as fs:
        for line in fs.readlines():
            line = line.strip()
            k = line.split(' ', 1)[0]
            v = line.split(' ', 1)[1].split(',', 1)[0].lower()
            dict_swords[k] = v
    return dict_swords

# class2label_new.txt to dict


def class2label2dict(path=r'/home/xuwei/data/mini_imagenet/class2label.txt'):
    dict_labels = {}
    with open(path, 'r') as fl:
        for line in fl.readlines():
            line = line.strip()
            k = line.split(': ', 1)[0][1:-1]
            v = line.split(': ', 1)[1]
            dict_labels[k] = v
    return dict_labels

# seed setting


def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True

# generate top shot tsv file


def split_data_few_seed(inpath, outpath, shot, seed):
    if int(shot) == -1:
        print('Prepare to generate full shot tsv dataset file'.format(shot))
    elif int(shot) > 0:
        print('Prepare to generate {} shot tsv dataset file'.format(shot))
    else:
        print('Please check the setting of SHOT, now shot == {}.'.format(shot))
        sys.exit(1)

    setup_seed(seed)
    dict_swords = synset_words2dict()
    dict_labels = class2label2dict()

    data = pd.DataFrame({'base64': [], 'imgid': [], 'label': []})
    files = os.listdir(inpath)
    count = 0
    for file in files:
        count += 1
        filepath = os.path.join(inpath, file)
        print('Now processing @ {}'.format(filepath))
        images = os.listdir(filepath)
        random.shuffle(images)  # random shuffle images
        few_images = images[:shot]  # select top shot images
        for image in few_images:
            imagepath = os.path.join(filepath, image)
            # img to base64
            img = Image.open(imagepath)  # path to file
            img_buffer = BytesIO()
            img.save(img_buffer, format=img.format)
            byte_data = img_buffer.getvalue()
            base64_str = base64.b64encode(byte_data)  # bytes
            base64_str = base64_str.decode('utf-8')  # str
            temp_dataframe = pd.DataFrame({'base64': [base64_str], 'imgid': [
                                          dict_labels.get(dict_swords.get(file))], 'label': [dict_swords.get(file)]})
            # print(temp_dataframe)
            data = pd.concat([data, temp_dataframe], ignore_index=True)
    data.to_csv(outpath, sep='\t', index=False, header=False)
    print('Successfully processed {} fodels, {} images.'.format(count, count*shot))


if __name__ == '__main__':
    shot = 1  # set to -1 for full data
    seed = 4
    modality = 'val'  # train or val
    rootpath = r'/home/xuwei/data/mini_imagenet/'
    inpath = os.path.join(rootpath, modality)
    savepath = os.path.join(
        rootpath, '{}_shot{}_seed{}'.format(modality, shot, seed))
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    outpath = os.path.join(
        savepath, 'mini_imagenet_{}_shot{}_seed{}.tsv'.format(modality, shot, seed))
    split_data_few_seed(inpath, outpath, shot, seed)
