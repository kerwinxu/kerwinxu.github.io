---
layout: post
title: "wpf/mvvm/RelayCommand的异步版本AsyncRelayCommand and AsyncRelayCommand<T>"
date: "2021-08-06"
categories: 
  - "c"
---

```
public class MyViewModel : ObservableObject
{
    public MyViewModel()
    {
        DownloadTextCommand = new AsyncRelayCommand(DownloadText);
    }

    public IAsyncRelayCommand DownloadTextCommand { get; }

    private Task<string> DownloadText()
    {
        return WebService.LoadMyTextAsync();
    }
}
```
