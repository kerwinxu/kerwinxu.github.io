---
layout: post
title: "No module named pip.req"
date: "2019-02-28"
categories: 
  - "python"
---

This is happening lately because of a change in pip 10.

The fix is pretty easy. You probably have something like:

```
from pip.req import parse_requirements

```

Change that to something like:

```
try: # for pip .version  >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

```

That should do it.
