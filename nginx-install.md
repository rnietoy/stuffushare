Nginx Installation
==================

*OS: Ubuntu Server*

** Installation of nginx **

* Installation of nginx
> sudo apt-get install nginx

* Start nginx service
> sudo service nginx start

* Should see the following after typing the ip address of the server

![Installation](https://farm6.staticflickr.com/5545/13521631935_ac72b4afcb.jpg)

* Start nginx after reboot
> update-rc.d nginx defaults


*OS: Fedora*

Commands

* yum install nginx
* chkconfig --levels 235 nginx on