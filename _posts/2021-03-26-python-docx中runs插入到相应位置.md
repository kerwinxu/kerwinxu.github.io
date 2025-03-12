---
title: "python-docx中runs插入到相应位置"
date: "2021-03-26"
categories: 
  - "python"
---

```
from docx.text.run import Run
from docx.oxml.text.run import CT_R
# ...
for run in p.runs:
    if 'text' in run.text:
        new_run_element = p._element._new_r()
        run._element.addnext(new_run_element)
        new_run = Run(new_run_element, run._parent)
        # ---do things with new_run, e.g.---
        new_run.text = 'Foobar'
        new_run.bold = True
```

If you want to insert the new run prior to the existing run, use `run._element.addprevious(new_run_element)`. These two are methods on the `lxml.etree._Element` class which all `python-docx` elements subclass. [https://lxml.de/api/lxml.etree.\_Element-class.html](https://lxml.de/api/lxml.etree._Element-class.html)

 

引用：

- [Python-docx: Is it possible to add a new run to paragraph in a specific place (not at the end)](https://stackoverflow.com/questions/52740630/python-docx-is-it-possible-to-add-a-new-run-to-paragraph-in-a-specific-place-n)
