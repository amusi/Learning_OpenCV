# Summary: Gathering images for harr cascade
# Author:      Amusi
# Date:          2017-12-16
# Steps

import cv2
import numpy as np
import os
import urllib.request

def store_raw_images():
    # negtive images link
    # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513
    # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    neg_images_urls = urllib.request.urlopen(neg_images_link).read().decode()

    # generate folder
    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 1

    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'neg/' + str(pic_num) + '.jpg' )
            img = cv2.imread('neg/' + str(pic_num) + '.jpg', cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite('neg/' + str(pic_num) + '.jpg', resized_image)
            print(pic_num)
            pic_num += 1
            
        except Exception as e:
            print(str(e))

store_raw_images()
