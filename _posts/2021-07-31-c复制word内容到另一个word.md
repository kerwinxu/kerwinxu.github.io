---
title: "C#复制Word内容到另一个Word"
date: "2021-07-31"
categories: 
  - "c"
---

# 工具

[https://www.e-iceblue.cn/Downloads/Free-Spire-Doc-NET.html](https://www.e-iceblue.cn/Downloads/Free-Spire-Doc-NET.html)

请注意这个免费版本的有限制。

# 复制部分内容

```
//新建一个word文档对象doc1并加载需要复制的word文档。
Document doc1 = new Document();
doc1.LoadFromFile("sample.docx");

//新建一个word文档对象doc2
Document doc2 = new Document();

//给doc2添加一个section，并将doc1的第一二段的内容和格式等复制到doc2中
Section s2 = doc2.AddSection();
Paragraph NewPara1 = (Paragraph)p1.Clone();
s2.Paragraphs.Add(NewPara1);
Paragraph NewPara2 = (Paragraph)p2.Clone();
s2.Paragraphs.Add(NewPara2);

//保存并重新打开文档
doc2.SaveToFile("copy.docx", FileFormat.Docx2010);
System.Diagnostics.Process.Start("copy.docx");

```

# 复制全部内容（除页眉页脚外）

```
//新建两个word document对象，并加载待复制的源word文档和目标word文档
Document sourceDoc = new Document("sample.docx");
Document destinationDoc = new Document("target.docx");

//遍历源word文档中的所有section并把它们的内容复制到目标word文档
foreach (Section sec in sourceDoc.Sections)
{
    foreach (DocumentObject obj in sec.Body.ChildObjects)
    {
        destinationDoc.Sections[0].Body.ChildObjects.Add(obj.Clone());
    }
}
//保存并运行目标word文档
destinationDoc.SaveToFile("target.docx");
System.Diagnostics.Process.Start("target.docx");

```
