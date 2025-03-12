---
layout: post
title: "openxml中在word文档中插入超链接"
date: "2020-07-28"
categories: 
  - "c"
---

代码

```
const string outputFilename = @"c:\temp\linked.docx";
                         
using (var wordDocument = WordprocessingDocument.Create(outputFilename, WordprocessingDocumentType.Document)) {
    var mainPart = wordDocument.AddMainDocumentPart();
 
    // Create the document structure and add some text.
    var doc = mainPart.Document = new Document();
    var body = doc.AppendChild(new Body());
 
    // Start a paragraph with some text
    var para = body.AppendChild(new Paragraph());
    var run = para.AppendChild(new Run());
    run.AppendChild(new Text("This is a formatted hyperlink: ") {
        Space = SpaceProcessingModeValues.Preserve // Need this so the trailing space is preserved.
    });
 
    // Create a hyperlink relationship. Pass the relationship id to the hyperlink below.
    var rel = wordDocument.MainDocumentPart.AddHyperlinkRelationship(new Uri("http://www.example.com/"), true);
                 
    // Append the hyperlink with formatting.
    para.AppendChild(
        new Hyperlink(
            new Run(
                new RunProperties(
                    // This should be enough if starting with a template
                    new RunStyle { Val = "Hyperlink", }, 
                    // Add these settings to style the link yourself
                    new Underline { Val = UnderlineValues.Single },
                    new Color { ThemeColor = ThemeColorValues.Hyperlink }),
                new Text { Text = "Click Here"}
            )) { History = OnOffValue.FromBoolean(true), Id = rel.Id });
 
    doc.Save();
}
```

引用：

- [Adding a formatted hyperlink to a Word document using Open XML](https://ratborg.blogspot.com/2014/10/adding-formatted-hyperlink-to-word.html)
