---
title: "openxml生成word文档中的图片"
date: "2020-07-28"
categories: 
  - "c"
---

```
using A = DocumentFormat.OpenXml.Drawing;
using DW = DocumentFormat.OpenXml.Drawing.Wordprocessing;
using PIC = DocumentFormat.OpenXml.Drawing.Pictures;

string picFileName = "clear.png";
ImagePart imagePart = mainPart.AddImagePart(ImagePartType.Png);
using (FileStream stream = new FileStream(picFileName, FileMode.Open))
{
    imagePart.FeedData(stream);
}
AddImageToBody(wordDocument, mainPart.GetIdOfPart(imagePart));

private static void AddImageToBody(WordprocessingDocument wordDoc, string relationshipId)
{
    var element = new Drawing(
        new DW.Anchor(
            new DW.SimplePosition() { X = 0, Y = 0 },
            new DW.HorizontalPosition(
                new DW.PositionOffset("-9525")
                )
            { RelativeFrom = DW.HorizontalRelativePositionValues.Column },
            new DW.VerticalPosition() { RelativeFrom = DW.VerticalRelativePositionValues.Paragraph, PositionOffset = new DW.PositionOffset("360000") },
            new DW.Extent() { Cx = 8863330, Cy = 1763395 },
            new DW.WrapTopBottom(),
            new DW.DocProperties()
            {
                Id = 1U,
                Name = "Picture 1"
            },
            new DW.NonVisualGraphicFrameDrawingProperties(
                     new A.GraphicFrameLocks() { NoChangeAspect = true }
                     ),
            new A.Graphic(
                new A.GraphicData(
                    new PIC.Picture(
                        new PIC.NonVisualPictureProperties(
                                 new PIC.NonVisualDrawingProperties()
                                 {
                                     Id = 0U,
                                     Name = "New Bitmap Image.jpg"
                                 },
                                 new PIC.NonVisualPictureDrawingProperties()
                                 ),
                        new PIC.BlipFill(
                                 new A.Blip()
                                 {
                                     Embed = relationshipId
                                 },
                                 new A.Stretch(
                                     new A.FillRectangle()
                                     )
                                     ),
                             new PIC.ShapeProperties(
                                 new A.Transform2D(
                                     new A.Extents() { Cx = 8863330, Cy = 1763395 }
                                     ),
                                 new A.PresetGeometry() { Preset = A.ShapeTypeValues.Rectangle }
                                 )
                        )
                    )
                { Uri = "http://schemas.openxmlformats.org/drawingml/2006/picture" }
                )
            )
        {
            SimplePos = false,
            RelativeHeight = 251658240U,
            BehindDoc = false,
            Locked = false,
            LayoutInCell = true,
            AllowOverlap = true }
        );

    wordDoc.MainDocumentPart.Document.Body.AppendChild(new Paragraph(new Run(element)));
}
```

 

- 图片在文档中有两种布局方式：**内嵌**和**浮动**。示例 [如何：在字处理文档中插入图片](https://docs.microsoft.com/zh-cn/office/open-xml/how-to-insert-a-picture-into-a-word-processing-document) 使用的是内嵌布局，而本文使用的是浮动布局。内嵌布局用 `Inline` 表示，浮动布局用 `Anchor` 表示。
- 图片显示的大小由 `ShapeProperties.Transform2D.Extents` 设置，`Extents.Cx` 和 `Extents.Cy` 分别表示宽和高。`Extents.Cx` 和 `Extents.Cy` 的单位是 EMU (English Metric Units，英语公制单位)。EMU 与厘米的换算关系如下：

$$ 1 emu = \\frac{1}{914400} US\\ \\ inch = \\frac{1}{360000} cm $$
