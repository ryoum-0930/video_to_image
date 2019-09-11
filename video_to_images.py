import os
import cv2
from tqdm import tqdm

movie_name = ''   # 動画のファイル名
mp4_files = []  # mp4のファイルをリストで取得
movie_path = './movies'

def get_fileName():
    Mfiles = os.listdir('{0}/'.format(movie_path)) #Mfilesにpath内のすべてのフォルダを挿入
    for file in Mfiles:
        fname, ext = os.path.splitext(file)   #fnameにファイル名,'_'に拡張子　拡張子はいらない
        if (ext == '.mp4'): # 末尾文字列に'.mp4'が含まれているならTrue
            mp4_files.append(fname)  # mp4_filesにfileを追加 => mp4ファイルを追加

def movie_read(file):
    # 動画ファイルを読み込む場合はVideoCapture()の引数にpathを指定する
    cap = cv2.VideoCapture('./{0}/{1}'.format(movie_path, file + '.mp4'))

    ### 確認
    # print(type(cap))
    interpret = cap.isOpened() #interpret=受け取る
    print("Loading video... ",end='')
    print(interpret) #動画が読み込めていたら Ture
    if(interpret == False):
        print("-------------------------------")
        print("Can't read movie_file")
        exit(-1)
    return cap

def main():
    count = 0
    # while(True):
    get_fileName()
    for file in mp4_files:
        cap = movie_read(file)  # 動画ファイルを読み込む
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 総フレーム数を取得
        fps = cap.get(cv2.CAP_PROP_FPS) #FPSを取得
        step = int(fps)*30  # fps*10 :約10秒

        img_dir = '{0}/{1}'.format(movie_path, file)
        # フォルダが存在しない時に作成する
        if not(os.path.exists(img_dir)): # フォルダが無い時
            os.mkdir(img_dir)
            print(file+' folder was Created !')
        # else:
            # print('既にフォルダが存在しています\n')

        for num in tqdm(range(1, frame_count, step)):
            # ret: bool, frame: 画像の配列 ndarrayのタプル。アンパックでそれぞれの変数に入る
            ret, frame = cap.read()
            if(ret == True):    # if(ret)でも可　retはbool型で受け取っているため
                cap.set(cv2.CAP_PROP_POS_FRAMES,num)    # numフレームに飛ぶ
                #'{0:05d}'.format(12) =>'00012' |   '{0:5d}'.format(12) =>'___12'   となる
                cv2.imwrite('{0}/{1}_{2:04d}.jpg'.format(img_dir, file, int((num)/step)+1), cap.read()[1])
            else:
                print(file + 'is Complete ...')
                break

if __name__ == "__main__":
    # print(movie_name)
    main()
    print("------------")
    print("video to img Complete !\n")
