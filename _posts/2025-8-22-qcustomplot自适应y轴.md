---
layout: post
title: "qt中ComboBox实现下拉框显示事件"
date: "2025-08-22"
categories: ["计算机语言", "c"]
---

修改一下源码,qcustomplot.cpp中，9217行的。
```c
void QCPAxis::rescale(bool onlyVisiblePlottables)
{
  QCPRange newRange;
  bool haveRange = false;
  double maxRangeSize=0,maxRangeSizeTmp=0;

  foreach (QCPAbstractPlottable *plottable, plottables())
  {
    if (!plottable->realVisibility() && onlyVisiblePlottables)
      continue;
    QCPRange plottableRange;
    bool currentFoundRange;
    QCP::SignDomain signDomain = QCP::sdBoth;
    if (mScaleType == stLogarithmic)
      signDomain = (mRange.upper < 0 ? QCP::sdNegative : QCP::sdPositive);
    if (plottable->keyAxis() == this)
      plottableRange = plottable->getKeyRange(currentFoundRange, signDomain);
    else
    {
        plottableRange = plottable->getValueRange(currentFoundRange, signDomain);
    }
    // 多加了范围判断
    if(plottableRange.size() > 0){
        maxRangeSizeTmp =    plottableRange.size() /50;
    }else{
        if(plottableRange.size() == 0){ // 这里是判断范围等于0
            if(qFuzzyIsNull(plottableRange.upper)){
                maxRangeSizeTmp = 1;
            }else{
                maxRangeSizeTmp = abs(plottableRange.upper)/50;
            }
        }else{
            maxRangeSizeTmp = 1;
        }
    }
    if(maxRangeSize < maxRangeSizeTmp) maxRangeSize = maxRangeSizeTmp;


    if (currentFoundRange)
    {
      if (!haveRange)
        newRange = plottableRange;
      else
        newRange.expand(plottableRange);
      haveRange = true;
    }
  }
  if (haveRange)
  {
    if (!QCPRange::validRange(newRange)) // likely due to range being zero (plottable has only constant data in this axis dimension), shift current range to at least center the plottable
    {
      double center = (newRange.lower+newRange.upper)*0.5; // upper and lower should be equal anyway, but just to make sure, incase validRange returned false for other reason
      if (mScaleType == stLinear)
      {
        newRange.lower = center-mRange.size()/2.0;
        newRange.upper = center+mRange.size()/2.0;
      } else // mScaleType == stLogarithmic
      {
        newRange.lower = center/qSqrt(mRange.upper/mRange.lower);
        newRange.upper = center*qSqrt(mRange.upper/mRange.lower);
      }
    }else{
        newRange.lower =  newRange.lower - newRange.size()/50;
        newRange.upper =  newRange.upper + newRange.size()/50;
    }

    setRange(newRange);
  }

}
```
