#%%
import os
from tqdm import tqdm
import re
import shutil

def get_yearmonth(filename):
    pat = r"(\d{8})"
    m = re.search(pat, filename)
    if m:
        x = m.group(1)        
        return x[:4], x[4:6]
    else:
        return None

def move_file(filename, target_path):    
    year_month = get_yearmonth(filename)
    if year_month:
        year, month = year_month
        path = os.path.join(target_path, year, month)        
        if not os.path.exists(path):
            os.makedirs(path)

        f = os.path.split(filename)
        shutil.move(filename, os.path.join(path, f[1]))
#%%
path = "E:/Camera"
target_path = "E:/Processed"

n_files = 0

for f in tqdm(os.listdir(path)):
    if os.path.isfile(os.path.join(path, f)):
        n_files = n_files + 1
        move_file(os.path.join(path, f), target_path)

print(f"Number of files proecessed: {n_files}")

# %%
path = "E:/pictures/photos"
target_path = "E:/DCIM"
for f in tqdm(os.listdir(path)):
    if len(f) == 7:
        year, month = f.split("-")
        path1 = os.path.join(target_path, year, month)   
        if not os.path.exists(path1):
            os.makedirs(path1)
        for f1 in os.listdir(os.path.join(path, f)):
            if re.search("picasa", f1) == None:                                
                shutil.move(os.path.join(path, f, f1), (os.path.join(path1, f1)))
# %%
root = "C:/Users/ausle/python"
for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))
# %%
