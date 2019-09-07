import shutil
import os
import sys

def main(this_path,target_path):
    # shutil.move(移動させたい, 移動先)
    shutil.move(this_path,target_path)

if __name__ == "__main__":
    args = sys.argv
    # print(args)
    # (移動先,移動元)
    if len(args) == 3:
        main(args[2],args[1])
    else:
        print('ERROR : Wrong way of writing arguments')
        print('NOTATION -> python move_file.py [Destination] [Want_Move_dir]')
