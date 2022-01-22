#### 树莓派启动视频

参考视频：https://www.youtube.com/watch?v=zYvkxup76-s

镜像：https://downloads.raspberrypi.org/raspios_arm64/images/

#### putty

```
ping raspberrypi.local
login as:pi
password:raspberry
```

#### 连接本地网络

https://www.bilibili.com/video/BV16U4y1879Q?p=5

#### 换源  & 公钥问题

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

