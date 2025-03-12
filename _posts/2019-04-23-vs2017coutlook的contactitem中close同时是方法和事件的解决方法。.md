---
title: "vs2017,c#,outlook的ContactItem中Close同时是方法和事件的解决方法。"
date: "2019-04-23"
categories: 
  - "c"
---

```
public interface ContactItem : _ContactItem, ItemEvents_10_Event

```

but \_ContactItem interface and ItemEvents\_10\_Event interface have the same name: Close

```
public interface _ContactItem
{
    [DispId(61475)]
    void  Close (OlInspectorClose SaveMode);
}
public interface ItemEvents_10_Event
{
    event ItemEvents_10_CloseEventHandler  Close;
}

```

I found the solution ,

```
ItemEvents_10_Event appointmentItemEvent = (ItemEvents_10_Event)outlook_contact;
appointmentItemEvent.Close += AppointmentItemEvent_Close;

```
