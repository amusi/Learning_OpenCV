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

def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv2.imread('uglies/' + str(ugly))
                    question = cv2.imread(current_image_path)
                    
                    if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                        print('dayyyyummmm girl you ugly!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
                    
                    
def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
                    
            elif file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.data', 'a') as f:
                    f.write(line)
                                      
                                      
create_pos_n_neg()
#sfind_uglies()
#store_raw_images()
                                      
