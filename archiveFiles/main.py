import os
import sys
import datetime
import zipfile

req_path = input("Enter the path: \n")    
# if path exists and if directory exists,go into each directory and look for files 
if os.path.exists(req_path):        
    if os.path.isdir(req_path):
        for each_dir in os.listdir(req_path):
            each_dir_path =  os.path.join(req_path, each_dir)
            for each_file in each_dir_path:
                each_file_path =  os.path.join(req_path, each_file)
                if os.path.isfile(each_file_path):
                    today = datetime.datetime.now()
                    file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
                    diff_days = (today - file_creation_date).day
                    if diff_days >= 45:         # if the file is older than 45 days remove files
                        os.remove(each_file_path)
                    # if the file is older than 7days but less than 45days then archive files & move to new directory
                    elif diff_days >= 7  and diff_days < 45:
                        zip_file = zipfile.ZipFile(each_file_path,'w')
                        zip_file.write(each_file_path, compress_type=zipfile.ZIP_DEFLATED)
                        zip_file.close()
                    else:
                        sys.exit()
                sys.exit()
    else:
        print('Directory does not exist!.')
        sys.exit()
else:
    print("'path does not exist!.")
    sys.exit()
