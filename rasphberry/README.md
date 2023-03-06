#### 1.树莓派启动视频

参考视频：https://www.youtube.com/watch?v=zYvkxup76-s

镜像：https://downloads.raspberrypi.org/raspios_arm64/images/

#### putty

```
ping raspberrypi.local
login as:pi
password:raspberry
```

#### 2.连接本地网络

https://www.bilibili.com/video/BV16U4y1879Q?p=5

#### 3.换源  & 公钥问题

注意更改`/etc/apt/sources.list.d/raspi.list`

用`lsb_release -a`查看系统信息

https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/

使用`sudo apt-get update`可能会出现报错，可以用下面命令修改
报错：

```
Err:7 http://mirrordirector.raspbian.org/raspbian jessie InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 9165938D90FDDD2E
Err:10 http://archive.raspberrypi.org/debian jessie InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 82B129927FA3303E
Reading package lists... Done
W: GPG error: http://mirrordirector.raspbian.org/raspbian jessie InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 9165938D90FDDD2E
E: The repository 'http://mirrordirector.raspbian.org/raspbian jessie InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: http://archive.raspberrypi.org/debian jessie InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 82B129927FA3303E
E: The repository 'http://archive.raspberrypi.org/debian jessie InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```
命令：
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9165938D90FDDD2E
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 82B129927FA3303E
9165938D90FDDD2E 和 82B129927FA3303E 是key
```

之后就可以使用`sudo apt-get update` 和 `sudo apt-get upgrade`

#### 4.MariaDB

```
sudo apt install mariadb-server -y
sudo mysql_secure_installation 
```

将`/etc/mysql/mariadb.conf.d/50-server.cnf`里的` bind-address=0.0.0.0`注释掉

运行命令`sudo service mysql restar` [参考连接](https://www.cnblogs.com/anyiz/p/10657232.html)

**分配权限**进入mysql

2.开启mysql远程访问
(1)修改/etc/mysql/my.cnf文件
sudo nano /etc/mysql/my.cnf
找到下面这行，并用#注释掉，
bind-address        = 127.0.0.1
或者修改为bind-address        = 0.0.0.0
(2)登录mysql，输入下面命令
mysql> grant all privileges on *.* to username@"%" identified by "password"; （username一般是root，password是新的密码）
mysql> FLUSH PRIVILEGES;

3.开启3306端口远程访问（如果不用防火墙，这一步可以忽略）
这里的iptable命令和centos中命令不一样，所以参考了一下文档，使用ufw软件来开启3306端口
(1)安装ufw
sudo apt-get install ufw
(2)启用ufw
sudo ufw enable
sudo ufw default deny
(3)开启3306、22（ssh端口）端口
sudo ufw allow 3306 
sudo ufw allow 22 
sudo ufw allow 80 
sudo ufw allow 3389
sudo ufw allow 3350
sudo ufw allow 5910
注意：请将常用的端口都添加到防火墙规则中，如果不开启22端口，下次启动树莓派时，系统的22端口会禁用，不能使用ssh登录树莓派

4.重启mysql服务

sudo service mysql restart
————————————————
版权声明：本文为CSDN博主「清山博客」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/a497785609/article/details/77942890

#### 无线通讯

https://circuitdigest.com/microcontroller-projects/wireless-rf-communication-between-arduino-and-raspberry-pi-using-nrf24l01

https://stackoverflow.com/questions/67473554/radio-transmition-between-arduino-uno-and-raspberry-pi-4-not-working-using-nrf2

https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/

python page

https://github.com/BLavery/lib_nrf24

https://github.com/nRF24/RF24

[注意要启动SPI接口](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/)

### 重启网络

```
sudo /etc/init.d/networking restart
```

