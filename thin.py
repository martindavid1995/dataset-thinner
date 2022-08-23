# TO UPDATE
# First copy the .js file from https://chisel.weirdgloop.org/moid/data_files/itemsmin.js
# Paste in data.py
# Find/replace all ' with \'
# Surround in single quotes and set equal to data variable

from data import *
import re
import json

def main():
    new_data = data.replace('},{', '},*{')
    new_data = re.split(',\*', new_data)          
    objs = []
    for s in new_data:
        objs.append(json.loads(s))
    
    # Need to skip all values that are null or have -1 as noteId
    json_data = []
    for obj in objs:
        if (obj['name'] != 'null' and obj['name'] != 'Null'):
            n_obj = json.dumps({
                "name" : obj['name'],
                "img_url" : "https://static.runelite.net/cache/item/icon/"+str(obj['id'])+".png"
                })
            json_data.append(json.loads(n_obj))
    
    with open("item_images.json", "w") as outfile:
        json.dump(json_data, outfile)
    
if __name__ == "__main__":
    main()


    