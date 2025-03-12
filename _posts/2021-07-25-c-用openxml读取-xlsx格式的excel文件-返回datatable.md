---
layout: post
title: "c# 用OpenXmL读取.xlsx格式的Excel文件 返回DataTable、DataSet"
date: "2021-07-25"
categories: 
  - "c"
---

# 如下是返回DataSet

```
public static class ExcelHelper
  {
      private static string GetColumnName(string cellReference)
      {
          // Create a regular expression to match the column name portion of the cell name.
          Regex regex = new Regex("[A-Za-z]+");
          Match match = regex.Match(cellReference);
          return match.Value;
      }
      private static int? GetColumnIndexFromName(string columnNameOrCellReference)
      {
          int columnIndex = 0;
          int factor = 1;
          for (int pos = columnNameOrCellReference.Length - 1; pos >= 0; pos--) // R to L
          {
              if (Char.IsLetter(columnNameOrCellReference[pos])) // for letters (columnName)
              {
                  columnIndex += factor * ((columnNameOrCellReference[pos] - 'A') + 1);
                  factor *= 26;
              }
          }
          return columnIndex;
      }
      private static string GetCellValue(SpreadsheetDocument document, DocumentFormat.OpenXml.Spreadsheet.Cell cell)
      {
          DateTime ReleaseDate = new DateTime(1899, 12, 30);
          SharedStringTablePart stringTablePart = document.WorkbookPart.SharedStringTablePart;
          object value = string.Empty;
          DocumentFormat.OpenXml.Spreadsheet.CellFormats cellFormats = (DocumentFormat.OpenXml.Spreadsheet.CellFormats)document.WorkbookPart.WorkbookStylesPart.Stylesheet.CellFormats;
          string format = string.Empty; uint formatid = 0;
          if (cell.DataType == null)
          {
              DocumentFormat.OpenXml.Spreadsheet.CellFormat cf = new CellFormat();
              if (cell.StyleIndex == null)
              {
                  cf = cellFormats.Descendants<DocumentFormat.OpenXml.Spreadsheet.CellFormat>().ElementAt<DocumentFormat.OpenXml.Spreadsheet.CellFormat>(0);
              }
              else
              {
                  cf = cellFormats.Descendants<DocumentFormat.OpenXml.Spreadsheet.CellFormat>().ElementAt<DocumentFormat.OpenXml.Spreadsheet.CellFormat>(Convert.ToInt32(cell.StyleIndex.Value));
              }
              formatid = cf.NumberFormatId;

              if (cell != null && cell.InnerText.Length > 0)
              {
                  value = cell.CellValue.Text;
                  if (formatid > 13 && formatid <= 22)
                  {
                      DateTime answer = ReleaseDate.AddDays(Convert.ToDouble(cell.CellValue.Text));
                      value = answer.ToShortDateString();
                  }
              }
              else
              {
                  value = cell.InnerText;
              }
          }
          if (cell.DataType != null)
          {
              switch (cell.DataType.Value)
              {
                  case CellValues.SharedString:
                      return stringTablePart.SharedStringTable.ChildElements[Int32.Parse(cell.CellValue.Text)].InnerText;
                  case CellValues.Boolean:
                      return cell.CellValue.Text == "1" ? "true" : "false";
                  case CellValues.Date:
                      {
                          DateTime answer = ReleaseDate.AddDays(Convert.ToDouble(cell.CellValue.Text));
                          return answer.ToShortDateString();
                      }
                  case CellValues.Number:
                      return Convert.ToDecimal(cell.CellValue.Text).ToString();
                  default:
                      if (cell.CellValue != null)
                          return cell.CellValue.Text;
                      return string.Empty;
              }
          }
          return value.ToString();
      }

      static Regex regex_repeat = new Regex("^(.*) - (%d+)$");

      public static DataSet ExcelToDataSet(string filepath, bool ColumnHeader = true)
      {
          DataSet dataSet = new DataSet();
          // 打开文件
          using (SpreadsheetDocument spreadSheetDocument = SpreadsheetDocument.Open(filepath, false))
          {
              WorkbookPart workbookPart = spreadSheetDocument.WorkbookPart;
              //选择Excel的sheet页，和Excel中的实际顺序对应
              IEnumerable<Sheet> sheets = spreadSheetDocument.WorkbookPart.Workbook.GetFirstChild<Sheets>().Elements<Sheet>();
              foreach (Sheet sheet in sheets)
              {
                  string relationshipId = sheet.Id.Value; // 这个是取得这个页面的id
                  WorksheetPart worksheetPart = (WorksheetPart)spreadSheetDocument.WorkbookPart.GetPartById(relationshipId);
                  Worksheet workSheet = worksheetPart.Worksheet;
                  SheetData sheetData = workSheet.GetFirstChild<SheetData>(); // 这里是取得这个页面的数据了。
                                                                              // 每页做一个DataTable
                  DataTable dt = new DataTable();
                  dt.TableName = sheet.Name; // 这个页面的名称
                  int rowCount = sheetData.Elements<Row>().Count();
                  if (rowCount > 0) // 如果有内容。
                  {
                      
                      IEnumerable<Row> rows = sheetData.Elements<Row>();
                      int columnIndex = 0;  // 当前列的下标。
                      var charcolumn = 1; // 这个表示用数字表示的列名，从1开始吧。
                      foreach (Cell cell in rows.ElementAt(0))
                      {
                          // 这里首先判断一下前面是否有空白的列
                          int cellColumnIndex = (int)GetColumnIndexFromName(GetColumnName(cell.CellReference));
                          cellColumnIndex--;
                          // 这样就得到了这个单元格的列
                          while (columnIndex < cellColumnIndex)
                          {
                              dt.Columns.Add(charcolumn.ToString());
                              charcolumn++;
                              columnIndex++;
                          }

                          if (GetCellValue(spreadSheetDocument, cell).ToString() != "")
                          {
                              if (ColumnHeader)
                              {
                                  string cell_value = GetCellValue(spreadSheetDocument, cell);
                                  if (dt.Columns.Contains(cell_value)) // 如果有重名的，就添加一个新的名字
                                  {
                                      // 这里看看是否是这种格式
                                      if (regex_repeat.IsMatch(cell_value))
                                      {
                                          var match = regex_repeat.Match(cell_value);
                                          cell_value = String.Format("{0} - {1}", match.Groups[1].ToString(), (int.Parse(match.Groups[2].ToString()) + 1));

                                      }
                                      else
                                      {
                                          cell_value = cell_value + " - 2";
                                      }


                                  }

                                  dt.Columns.Add(cell_value);

                              }
                              else
                              {
                                  dt.Columns.Add(charcolumn.ToString());
                                  charcolumn++;
                              }
                          }
                          else
                          {
                              // 如果为空，那么也是以数字命名列吧。
                              dt.Columns.Add(charcolumn.ToString());
                              charcolumn++;
                          }

                          columnIndex++; // 顺序加


                      }
                      foreach (Row row in rows) //this will also include your header row...
                      {

                          DataRow tempRow = dt.NewRow();
                          columnIndex = 0;
                          foreach (Cell cell in row.Descendants<Cell>())
                          {
                              // Gets the column index of the cell with data
                              int cellColumnIndex = (int)GetColumnIndexFromName(GetColumnName(cell.CellReference));
                              cellColumnIndex--; //zero based index
                              if (columnIndex < cellColumnIndex)
                              {
                                  while (columnIndex < cellColumnIndex)
                                  {
                                      tempRow[columnIndex] = ""; //Insert blank data here;
                                      columnIndex++;
                                  }
                              }

                              if (columnIndex < dt.Columns.Count)
                              {
                                  var value = GetCellValue(spreadSheetDocument, cell);
                                  tempRow[columnIndex] = GetCellValue(spreadSheetDocument, cell);
                                  columnIndex++;
                              }
                              //tempRow[columnIndex] = GetCellValue(spreadSheetDocument, cell);
                              //columnIndex++;
                          }
                          dt.Rows.Add(tempRow);
                      }
                  }
                  if (ColumnHeader)
                      dt.Rows.RemoveAt(0); //...so i'm taking it out here.

                  // 这里添加
                  dataSet.Tables.Add(dt);

              }
          }

          return dataSet; ;

      }

  }
```

 

 

# 如下是返回DataTable

```
public static class Excel2DataSet
    {
        public static DataTable MyExcelData(string filepath, bool ColumnHeader = true, bool _Isemptyheader = false)
        {
            DataTable dt = new DataTable();
            using (SpreadsheetDocument spreadSheetDocument = SpreadsheetDocument.Open(filepath, false))
            {
                WorkbookPart workbookPart = spreadSheetDocument.WorkbookPart;
                //选择Excel的sheet页，和Excel中的实际顺序对应
                WorksheetPart worksheetPart = workbookPart.WorksheetParts.ElementAt(0);
                //sheet页中的内容
                SheetData sheetData = worksheetPart.Worksheet.Elements<SheetData>().First();

                int rowCount = sheetData.Elements<Row>().Count();
                if (rowCount == 0)
                {
                    return dt;
                }
                IEnumerable<Row> rows = sheetData.Elements<Row>();

                var charcolumn = 'A';
                foreach (Cell cell in rows.ElementAt(0))
                {
                    if (GetCellValue(spreadSheetDocument, cell).ToString() != "" || _Isemptyheader)
                    {
                        if (ColumnHeader)
                            dt.Columns.Add(GetCellValue(spreadSheetDocument, cell));
                        else
                        {
                            dt.Columns.Add(charcolumn.ToString());
                            charcolumn++;
                        }
                    }
                }
                foreach (Row row in rows) //this will also include your header row...
                {
                    DataRow tempRow = dt.NewRow();
                    int columnIndex = 0;
                    foreach (Cell cell in row.Descendants<Cell>())
                    {
                        // Gets the column index of the cell with data
                        int cellColumnIndex = (int)GetColumnIndexFromName(GetColumnName(cell.CellReference));
                        cellColumnIndex--; //zero based index
                        if (columnIndex < cellColumnIndex)
                        {
                            do
                            {
                                //tempRow[columnIndex] = ""; //Insert blank data here;
                                columnIndex++;
                            }
                            while (columnIndex < cellColumnIndex);
                        }
                        if (columnIndex < dt.Columns.Count)
                        {
                            tempRow[columnIndex] = GetCellValue(spreadSheetDocument, cell);
                            columnIndex++;
                        }
                        //tempRow[columnIndex] = GetCellValue(spreadSheetDocument, cell);
                        //columnIndex++;
                    }
                    dt.Rows.Add(tempRow);
                }
            }
            if (ColumnHeader)
                dt.Rows.RemoveAt(0); //...so i'm taking it out here.
            return dt;
        }

        private static string GetColumnName(string cellReference)
        {
            // Create a regular expression to match the column name portion of the cell name.
            Regex regex = new Regex("[A-Za-z]+");
            Match match = regex.Match(cellReference);
            return match.Value;
        }

        private static int? GetColumnIndexFromName(string columnNameOrCellReference)
        {
            int columnIndex = 0;
            int factor = 1;
            for (int pos = columnNameOrCellReference.Length - 1; pos >= 0; pos--) // R to L
            {
                if (Char.IsLetter(columnNameOrCellReference[pos])) // for letters (columnName)
                {
                    columnIndex += factor * ((columnNameOrCellReference[pos] - 'A') + 1);
                    factor *= 26;
                }
            }
            return columnIndex;

        }

        private static string GetCellValue(SpreadsheetDocument document, DocumentFormat.OpenXml.Spreadsheet.Cell cell)
        {
            DateTime ReleaseDate = new DateTime(1899, 12, 30);
            SharedStringTablePart stringTablePart = document.WorkbookPart.SharedStringTablePart;
            object value = string.Empty;
            DocumentFormat.OpenXml.Spreadsheet.CellFormats cellFormats = (DocumentFormat.OpenXml.Spreadsheet.CellFormats)document.WorkbookPart.WorkbookStylesPart.Stylesheet.CellFormats;

            string format = string.Empty; uint formatid = 0;

            if (cell.DataType == null)
            {
                DocumentFormat.OpenXml.Spreadsheet.CellFormat cf = new CellFormat();
                if (cell.StyleIndex == null)
                {
                    cf = cellFormats.Descendants<DocumentFormat.OpenXml.Spreadsheet.CellFormat>().ElementAt<DocumentFormat.OpenXml.Spreadsheet.CellFormat>(0);
                }
                else
                {
                    cf = cellFormats.Descendants<DocumentFormat.OpenXml.Spreadsheet.CellFormat>().ElementAt<DocumentFormat.OpenXml.Spreadsheet.CellFormat>(Convert.ToInt32(cell.StyleIndex.Value));
                }

                formatid = cf.NumberFormatId;

      

                if (cell != null && cell.InnerText.Length > 0)
                {
                    value = cell.CellValue.Text;
                    if (formatid > 13 && formatid <= 22)
                    {
                        DateTime answer = ReleaseDate.AddDays(Convert.ToDouble(cell.CellValue.Text));
                        value = answer.ToShortDateString();
                    }

                }
                else
                {

                    value = cell.InnerText;
                }
            }

            if (cell.DataType != null)
            {
                switch (cell.DataType.Value)
                {
                    case CellValues.SharedString:
                        return stringTablePart.SharedStringTable.ChildElements[Int32.Parse(cell.CellValue.Text)].InnerText;
                    case CellValues.Boolean:
                        return cell.CellValue.Text == "1" ? "true" : "false";
                    case CellValues.Date:
                        {
                            DateTime answer = ReleaseDate.AddDays(Convert.ToDouble(cell.CellValue.Text));
                            return answer.ToShortDateString();
                        }
                    case CellValues.Number:
                        return Convert.ToDecimal(cell.CellValue.Text).ToString();
                    default:
                        if (cell.CellValue != null)
                            return cell.CellValue.Text;
                        return string.Empty;
                }
            }

            return value.ToString();
        }

    }
```
