import os
import sys
import cv2
# path = './movies/'
movie_name = '_-9LGOgMwf2LE.f137'   #動画のファイル名
movie = './movies/'+ movie_name +'.mp4'    #動画の場所
movie_path = './movies/'
mp4_files = []

def get_fileName():
    Mfiles = os.listdir(movie_path) #Mfilesにpath内のすべてのフォルダを挿入
    for file in Mfiles:
        if (file.endswith('.mp4')): # 末尾文字列に'.mp4'が含まれているならTrue
            fname,ext = os.path.splitext(file)
            mp4_files.append(fname)  # mp4_filesにfileを追加 => mp4ファイルを追加
            # print(ext)  # .(ピリオドを含む)

def movie_read():
    # 動画ファイルを読み込む場合はVideoCapture()の引数にpathを指定する
    cap = cv2.VideoCapture(movie)

    ### 確認
    # print(type(cap))
    interpret = cap.isOpened() #interpret=受け取る
    print(interpret) #動画が読み込めていたらture

    if interpret == False:
        print("Can't read movie_file")
        exit(-1)
    ###
    return cap

def main():
    cap = movie_read()
    get_fileName()
    for file in mp4_files:
        img_dir = movie_path + file
        print(file+'の有無')
        if not os.path.exists(img_dir): #フォルダの走査
            print("フォルダが存在しません\n")
            os.mkdir(img_dir)
            print("フォルダを作成しました\n")
        else:
            print('フォルダが既に存在しています\n')



if __name__ == "__main__":
    main()
    # get_fileName()
    # print(mp4_files)
    print('-------------\nfin')
