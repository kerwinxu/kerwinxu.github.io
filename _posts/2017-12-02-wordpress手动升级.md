---
title: "wordpress手动升级"
date: "2017-12-02"
categories: 
  - "wordpress相关"
---

1. 下载最新版本
2. 连接上ftp
3. 删除掉服务器上的wp-includes和wp-admin目录下的文件
4. 除了wp-content目录外的所有文件都上传并覆盖到你博客主机相对应的位置。遇到是否覆盖时，选择全部覆盖就是了。（特别注意是wp-config.php不要覆盖，否则又要重新写上数据库服务器的配置了）
