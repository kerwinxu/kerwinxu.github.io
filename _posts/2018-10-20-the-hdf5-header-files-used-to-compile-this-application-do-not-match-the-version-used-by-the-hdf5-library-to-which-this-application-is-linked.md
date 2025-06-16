---
layout: post
title: "The HDF5 header files used to compile this application do not match the version used by the HDF5 library to which this application is linked."
date: "2018-10-20"
categories: ["计算机语言", "Python"]
---

我安装tensorflow-gpu和升级hdf5后出现这个问题，

 

Warning! \*\*\*HDF5 library version mismatched error\*\*\* The HDF5 header files used to compile this application do not match the version used by the HDF5 library to which this application is linked. Data corruption or segmentation faults may occur if the application continues. This can happen when an application was compiled by one version of HDF5 but linked with a different version of static or shared HDF5 library. You should recompile the application or check your shared library related settings such as 'LD\_LIBRARY\_PATH'. You can, at your own risk, disable this warning by setting the environment variable 'HDF5\_DISABLE\_VERSION\_CHECK' to a value of '1'. Setting it to 2 or higher will suppress the warning messages totally. Headers are 1.8.11, library is 1.8.9 SUMMARY OF THE HDF5 CONFIGURATION =================================

General Information:

...

 

原因是conda和pip安装了2个hdf5，所以出现这个问题，解决方法

pip uninstall hdf5 ，用pip卸载掉这个就可以了。
