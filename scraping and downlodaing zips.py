#  website:
#  https://www.sec.gov/dera/data/edgar-log-file-data-set.html?fbclid=IwAR3MF48uhSzKM3p9su5Txs14sk-16AOpjpNDjsjmygFVwluvEc89UtEJ0Lw

import urllib.request
import requests
import os,re
import sys  
import zipfile 
from datetime import datetime 

## Download all of files from online urls ##
def get_url_list(file):
    URLfile = open('E:/Log/'+file,'r')
    file_content = URLfile.readlines()
    for whole_url in file_content:
        url_list = whole_url.split()

    return url_list


def download(url):
    url = 'http://' + url
    zipfile_name = url.split('/')[-1]
    urllib.request.urlretrieve(url,zipfile_name)


def main_dowmload():
    file = 'urlfile.txt'
    os.makedirs('E:/Log/Data',exist_ok=True)
    os.chdir('E:/Log/Data')
    
    for url in get_url_list(file):
        download(url)


## Unzip all of zip files##
# First, open the certain zip file through zipfile module
# Second, input files name list, file path and save path

def Decompression(files,file_path,save_path,file_restriction):
    for file_name in files:
        os.getcwd()
        os.chdir(file_path)
        print(file_name)
        r = zipfile.is_zipfile(file_name) # if it is a zip file
        if r:
            file_date = file_name.split('log')[1].split('.zip')[0]
            if datetime.strptime(file_date,'%Y%m%d').strftime('%Y-%m-%d') < file_restriction:
                zpfd = zipfile.ZipFile(file_name) # read the zip file 
                os.chdir(save_path) # get into the save path
                zpfd.extractall()
                zpfd.close()
            else:
                print('Finished')
                break

def files_save(open_path,save_path,file_restriction):
    for file_path,sub_dirs,files in os.walk(open_path): #get all of file names and paths
        print(file_path,sub_dirs,files)
        Decompression(files,file_path,save_path,file_restriction)

def main_unzip(file_restriction):
    open_path= r'C:\Users\CH.4644\Desktop\zip'
    save_path= r'C:\Users\CH.4644\Desktop\csv'
    files_save(open_path,save_path,file_restriction)


########################################## run workspace ########################################
if __name__ == '__main__':
    #main_dowmload()
    file_restriction = '2003-01-03'
    main_unzip(file_restriction)




