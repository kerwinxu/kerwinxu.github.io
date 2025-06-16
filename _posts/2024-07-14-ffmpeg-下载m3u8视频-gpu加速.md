---
layout: post
title: "ffmpeg 下载m3u8视频 gpu加速"
date: "2024-07-14"
categories: 
  - "图像处理"
---

```
ffmpeg -i "https://lr11.douyincdn.com/byte-dance-cq/169e16b71253642700823375242/playlist3.m3u8?vcodec=bytevc1" -c copy out2.mp4
```

```
ffmpeg -hwaccel cuda -i out.mp4 -y out2.mp4
```

 

如上是用cuda进行加速，下边是查看支持哪种加速

 

```
ffmpeg -hwaccels
ffmpeg version N-116271-g9af348bd1a-20240713 Copyright (c) 2000-2024 the FFmpeg developers
  built with gcc 14.1.0 (crosstool-NG 1.26.0.93_a87bf7f)
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-w64-mingw32- --arch=x86_64 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --disable-w32threads --enable-pthreads --enable-iconv --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-libxml2 --enable-fontconfig --enable-libharfbuzz --enable-libvorbis --enable-opencl --disable-libpulse --enable-libvmaf --disable-libxcb --disable-xlib --enable-amf --enable-libaom --enable-libaribb24 --enable-avisynth --enable-chromaprint --enable-libdav1d --enable-libdavs2 --enable-libdvdread --enable-libdvdnav --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libgme --enable-libkvazaar --enable-libaribcaption --enable-libass --enable-libbluray --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librist --enable-libssh --enable-libtheora --enable-libvpx --enable-libwebp --enable-lv2 --enable-libvpl --enable-openal --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopenmpt --enable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --disable-libdrm --enable-vaapi --enable-libvidstab --enable-vulkan --enable-libshaderc --enable-libplacebo --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-libs=-lgomp --extra-ldflags=-pthread --extra-ldexeflags= --cc=x86_64-w64-mingw32-gcc --cxx=x86_64-w64-mingw32-g++ --ar=x86_64-w64-mingw32-gcc-ar --ranlib=x86_64-w64-mingw32-gcc-ranlib --nm=x86_64-w64-mingw32-gcc-nm --extra-version=20240713
  libavutil      59. 28.100 / 59. 28.100
  libavcodec     61. 10.100 / 61. 10.100
  libavformat    61. 5.101 / 61. 5.101
  libavdevice    61. 2.100 / 61. 2.100
  libavfilter    10. 2.102 / 10. 2.102
  libswscale      8. 2.100 /  8. 2.100
  libswresample   5. 2.100 /  5. 2.100
  libpostproc    58. 2.100 / 58. 2.100
Hardware acceleration methods:
cuda
vaapi
dxva2
qsv
d3d11va
opencl
vulkan
d3d12va
```
