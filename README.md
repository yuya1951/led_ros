# ロボットシステム学2020課題2

# テーマ
ROSを用いて、LEDを点灯させる。

[youtube動画](https://www.youtube.com/watch?v=QerocIwOUpk&feature=youtu.be)

# 内容
コード1．授業で使用したパブリッシャーでカウントさせた値を2倍してサブスクライバーに表示させるプログラムを利用して、パブリッシャーでカウントした値の８で割った余りに応じて、点灯する組み合わせが変わるプログラム。

コード2．1の内容を自分で入力して点灯の組み合わせを任意で選べるようにしたプログラム。

# 使用方法
1．catkin_ws/src に移動する。
  
    $sudo cd catkin_ws/src
  
2．リポジトリをクローンする。

    $git clone https://github.com/yuya1951/ros_led.git
    
3．catkin_makeする。

    $cd ..
    $catkin_make

4．ledのファイルに移り、make、モジュールのインストール、パーミッションの変更を行う。

    $cd src/ros_led/scripts/led
    $bash setup.bash
    
5．パーミッションの設定を行う。

    $cd ..
    $bash ROSsetup.bash

6．コード１を行う場合以下のように行う。（抜け出す場合はctrl + C）

    $roscore
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
    

# 参考

[千葉工業大学　上田先生の作成したリポジトリ](https://github.com/ryuichiueda/robosys_device_drivers)

# LICENSE

[LICENSE](https://github.com/yuya1951/ros_led/blob/main/COPYING)
    
    
