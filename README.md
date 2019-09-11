# README
## video_to_images.py
* 実行するとmoviesの中のすべての動画ファイルから画像を１０秒ごとに切り取る
* 画像の保存先
    1. 動画ファイルと同じ名前のフォルダが作成される
    2. `movies/video-name/*_00000.jpg`で保存される

## move_file.py
* 使用例
```
python move_file.py ./aaa ./movies/
```
* コマンドライン引数の役割
    * 第一引数:宛先フォルダ
    * 第二引数:移動させたいフォルダ/ファイル

## test.py
* 各関数などの挙動の動きを確認するために使用した。
