# ロボットシステム学2020課題2      

# 概要
ロボットシステム学2020のROSを使用した課題です。

# 使用したもの
・ Raspberry Pi4 ModelB

・ Ubuntu 20.04

・ ROS Melodic Morenia

・ ブレットボード、LED3つ、220Ωの抵抗3つ

# 目的
ROSを搭載したラズベリーパイで、LEDを点灯する。（ラズベリーパイはUbuntu20.04を入れています。）

# 内容
コード1．授業で使用したパブリッシャーでカウントさせた値を2倍してサブスクライバーに表示させるプログラムを利用して、パブリッシャーでカウントした値の８で割った余りに応じて、点灯する組み合わせが変わるプログラム。

コード2．1の内容を自分で入力して点灯の組み合わせを任意で選べるようにしたプログラム。

# インストール方法

ROSのインストールは、千葉工業大学 上田先生の作成したものを使用。[リンクはこちら](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)

# 使用方法
0．GPIO23、24、25　にそれぞれLEDの+側につなぎ、GNDを-側につなぐ。

1．catkin_ws/src に移動する。
  
    $cd catkin_ws/src
  
2．リポジトリをクローンする。

    $git clone https://github.com/yuya1951/ros_led.git
    
3．catkin_makeする。

    $cd ..
    $catkin_make

4．ledのファイルに移り、make、モジュールのインストール、パーミッションの変更を行う。この時、別のターミナルでroscoreも行う。

    $roscore
    別の端末を起動。この別端末で以下の操作を行う。
    $cd src/ros_led/scripts/led
    $bash setup.bash
    
5．パーミッションの設定を行う。

    $cd ..
    $bash ROSsetup.bash

6．コード１を行う場合以下のように行う。（抜け出す場合はctrl + C）

    $roslaunch ros_led LED1.launch  

7．コード２を行う場合以下のように行う。（抜け出す場合はctrl + C）

    $roscore
    $roslaunch ros_led LED2.launch
    0       //全てのledを消す
    1       //赤のledを点ける
    2       //緑のledを点ける
    3       //青のledを点ける
    4       //赤と緑のledを点ける
    5       //赤と青のledを点ける
    6       //青と緑のledを点ける
    7       //全てのledを点ける
    
# デモ動画のリンク
[youtube動画](https://www.youtube.com/watch?v=QerocIwOUpk&feature=youtu.be)

# 参考

[上田先生の作成したリポジトリ](https://github.com/ryuichiueda/robosys_device_drivers)

# LICENSE

[LICENSE](https://github.com/yuya1951/ros_led/blob/main/COPYING)
    
    
