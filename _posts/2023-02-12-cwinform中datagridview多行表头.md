---
layout: post
title: "c#winform中DataGridView多行表头"
date: "2023-02-12"
categories: ["计算机语言", "c"]
---

```c#
public class BoundGridView : DataGridView
    {
        private int _baseColumnHeadHeight;

        public BoundGridView() : base()
          {
              this.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.DisableResizing;
              _baseColumnHeadHeight = this.ColumnHeadersHeight;
              this.Headers = new HeaderCollection(this.Columns);
         }
 
         public HeaderCollection Headers { get; private set; }
 
         protected override void OnCellPainting(DataGridViewCellPaintingEventArgs e)
         {
             if (e.ColumnIndex == -1 || e.RowIndex != -1)
             {
                 base.OnCellPainting(e);
                 return;
             }
            int lev = this.Headers.GetHeaderLevels();
            this.ColumnHeadersHeight = (lev + 1) * _baseColumnHeadHeight;
           for (int i = 0; i <= lev; i++)
               {
                   HeaderItem tempHeader = this.Headers.GetHeaderByLocation(e.ColumnIndex, i);
                   if (tempHeader == null || i != tempHeader.EndY || e.ColumnIndex != tempHeader.StartX) continue;
                   DrawHeader(tempHeader, e);
               }
            e.Handled = true;
        }

        private int ComputeWidth(int startX, int endX)
        {
            int width = 0;
            for (int i = startX; i <= endX; i++)
                width += this.Columns[i].Width;
            return width;
        }

        private int ComputeHeight(int startY, int endY)
        {
            return _baseColumnHeadHeight * (endY - startY + 1);
        }

        private void DrawHeader(HeaderItem item, DataGridViewCellPaintingEventArgs e)
        {
            if (this.ColumnHeadersHeightSizeMode != DataGridViewColumnHeadersHeightSizeMode.DisableResizing)
                this.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.DisableResizing;
            int lev = this.Headers.GetHeaderLevels();
            lev = (lev - item.EndY) * _baseColumnHeadHeight;

            SolidBrush backgroundBrush = new SolidBrush(e.CellStyle.BackColor);
            SolidBrush lineBrush = new SolidBrush(this.GridColor);
            Pen linePen = new Pen(lineBrush);
            StringFormat foramt = new StringFormat();
            foramt.Alignment = StringAlignment.Center;
            foramt.LineAlignment = StringAlignment.Center;

            Rectangle headRec = new Rectangle(e.CellBounds.Left, lev, ComputeWidth(item.StartX, item.EndX) - 1, ComputeHeight(item.StartY, item.EndY) - 1);
            e.Graphics.FillRectangle(backgroundBrush, headRec);
            e.Graphics.DrawLine(linePen, headRec.Left, headRec.Bottom, headRec.Right, headRec.Bottom);
            e.Graphics.DrawLine(linePen, headRec.Right, headRec.Top, headRec.Right, headRec.Bottom);
            e.Graphics.DrawString(item.Content, this.ColumnHeadersDefaultCellStyle.Font, Brushes.Black, headRec, foramt);
        }
    }

    public class HeaderItem
    {
        private int _startX;
        private int _startY;
        private int _endX;
        private int _endY;
        private bool _baseHeader;

        public HeaderItem(int startX, int endX, int startY, int endY, string content)
        {
            this._endX = endX;
            this._endY = endY;
            this._startX = startX;
            this._startY = startY;
            this.Content = content;
        }

        public HeaderItem(int x, int y, string content):this(x, x, y, y, content)
        {

        }

        public HeaderItem()
        {

        }

        public static HeaderItem CreateBaseHeader(int x, int y, string content)
        {
            HeaderItem header = new HeaderItem();
            header._endX = header._startX = x;
            header._endY = header._startY = y;
            header._baseHeader = true;
            header.Content = content;
            return header;
        }

        public int StartX
        {
            get { return _startX; }
            set
            {
                if (value > _endX)
                {
                    _startX = _endX;
                    return;
                }
                if (value < 0) _startX = 0;
                else _startX = value;
            }
        }

        public int StartY
        {
            get { return _startY; }
            set
            {
                if (_baseHeader)
                {
                    _startY = 0;
                    return;
                }
                if (value > _endY)
                {
                    _startY = _endY;
                    return;
                }
                if (value < 0) _startY = 0;
                else _startY = value;
            }
        }

        public int EndX
        {
            get { return _endX; }
            set
            {
                if (_baseHeader)
                {
                    _endX = _startX;
                    return;
                }
                if (value < _startX)
                {
                    _endX = _startX;
                    return;
                }
                _endX = value;
            }
        }

        public int EndY
        {
            get { return _endY; }
            set
            {
                if (value < _startY)
                {
                    _endY = _startY;
                    return;
                }
                _endY = value;
            }
        }

        public bool IsBaseHeader
        { get{ return _baseHeader; } }

        public string Content { get; set; }
    }

    public class HeaderCollection
    {
        private List<HeaderItem> _headerList;
        private bool _iniLock;

        public DataGridViewColumnCollection BindCollection { get; set; }

        public HeaderCollection(DataGridViewColumnCollection cols)
        {
            _headerList = new List<HeaderItem>();
            BindCollection = cols;
            _iniLock = false;
        }

        public int GetHeaderLevels()
        {
            int max = 0;
            foreach (HeaderItem item in _headerList)
                if (item.EndY > max)
                    max = item.EndY;

            return max;
        }

        public List<HeaderItem> GetBaseHeaders()
        {
            List<HeaderItem> list = new List<HeaderItem>();
            foreach (HeaderItem item in _headerList)
                if (item.IsBaseHeader) list.Add(item);
            return list;
        }

        public HeaderItem GetHeaderByLocation(int x, int y)
        {
            if (!_iniLock) InitHeader();
            HeaderItem result = null;
            List<HeaderItem> temp = new List<HeaderItem>();
            foreach (HeaderItem item in _headerList)
                if (item.StartX <= x && item.EndX >= x)
                    temp.Add(item);
            foreach (HeaderItem item in temp)
                if (item.StartY <= y && item.EndY >= y)
                    result = item;

            return result;
        }

        public IEnumerator GetHeaderEnumer()
        {
            return _headerList.GetEnumerator();
        }

        public void AddHeader(HeaderItem header)
        {
            this._headerList.Add(header);
        }

        public void AddHeader(int startX, int endX, int startY, int endY, string content)
        {
            this._headerList.Add(new HeaderItem(startX, endX, startY, endY, content));
        }

        public void AddHeader(int x, int y, string content)
        {
            this._headerList.Add(new HeaderItem(x, y, content));
        }

        public void RemoveHeader(HeaderItem header)
        {
            this._headerList.Remove(header);
        }

        public void RemoveHeader(int x, int y)
        {
           HeaderItem header = GetHeaderByLocation(x, y);
           if (header != null) RemoveHeader(header);
        }

        private void InitHeader()
        {
            _iniLock = true;
            for (int i = 0; i < this.BindCollection.Count; i++)
                if (this.GetHeaderByLocation(i, 0) == null)
                this._headerList.Add(HeaderItem.CreateBaseHeader(i, 0, this.BindCollection[i].HeaderText));
            _iniLock = false;
        }
    }
```

 

使用是这样子的

首先在控件里写所有的列，这些列默认都会显示在第0行，如果需要多列，增加如下的代码。

请注意，最底下是0行，往上是1行

```
HeaderItem item= this.boundGridView1.Headers.GetHeaderByLocation(0, 0);  //获取包括坐标(0,0)的单元格
            item.EndY = 2;
            item = this.boundGridView1.Headers.GetHeaderByLocation(9,0 );
            item.EndY = 2;
            item = this.boundGridView1.Headers.GetHeaderByLocation(10, 0);
            item.EndY = 2;
            item = this.boundGridView1.Headers.GetHeaderByLocation(11, 0);
            item.EndY = 2;

            this.boundGridView1.Headers.AddHeader(1, 2, 1, 1, "语文"); //增加表头，起始坐标(1,1) ,终止坐标(2,1) 内容"语文"
            this.boundGridView1.Headers.AddHeader(3, 4, 1, 1, "数学");  //增加表头，起始坐标(3,1) ,终止坐标(4,1) 内容"数学"
            this.boundGridView1.Headers.AddHeader(5, 6, 1, 1, "英语");  //增加表头，起始坐标(5,1) ,终止坐标(6,1) 内容"英语"
            this.boundGridView1.Headers.AddHeader(7, 8, 1, 1, "X科");  //增加表头，起始坐标(7,1) ,终止坐标(8,1) 内容"X科"
            this.boundGridView1.Headers.AddHeader(1, 8, 2, 2, "成绩");  //增加表头，起始坐标(1,2) ,终止坐标(8,2) 内容"成绩"
```

效果图

 

引用

- [多维表头的DataGridView](https://www.cnblogs.com/HopeGi/archive/2013/04/03/2982837.html)
