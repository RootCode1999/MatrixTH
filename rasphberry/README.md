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

#### 4.mysql

```
sudo apt install mariadb-server -y
sudo mysql_secure_installation 
password : lky+学号
```

将`/etc/mysql/mariadb.conf.d/50-server.cnf`里的` bind-address=0.0.0.0`注释掉

运行命令`sudo service mysql restar` [参考连接](https://www.cnblogs.com/anyiz/p/10657232.html)

**分配权限**进入mysql

参考链接
https://blog.csdn.net/idomyway/article/details/81210420
https://blog.csdn.net/u012294515/article/details/90078153
https://blog.csdn.net/u012294515/article/details/90078153

```
mysql> GRANT ALL PRIVILEGES ON *.* TO 'user'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION; 
// %:表示从任何主机连接到mysql服务器
// %:password是设置的密码
mysql> FLUSH PRIVILEGES;
```

**防火墙开启关闭、开放端口号**

[参考连接](https://blog.csdn.net/weixin_43484014/article/details/109329252)

```
sudo apt-get install ufw
sudo ufw disable
sudo ufw allow 3306
```

#### 无线通讯

https://circuitdigest.com/microcontroller-projects/wireless-rf-communication-between-arduino-and-raspberry-pi-using-nrf24l01

https://stackoverflow.com/questions/67473554/radio-transmition-between-arduino-uno-and-raspberry-pi-4-not-working-using-nrf2

https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/

python page

https://github.com/BLavery/lib_nrf24
