---
title: "C# 使用 OleDbConnection 连接读取Excel"
date: "2021-07-20"
categories: 
  - "c"
---

using System.Data.OleDb;

 

Connection类有四种:SqlConnection，OleDbConnection，OdbcConnection和OracleConnection。 （1）Sqlconnetcion类的对象连接是SQL Server数据库； （2）OracleConnection类的对象连接Oracle数据库； （3）OleDbConneetion连接支持OLEDB的数据库，如Access； （4）OdbcConnection类的对象连接支持ODBC的数据库。 与数据库的所有通讯都是通过Connection对象来完成的。

**下面用c#写了个控制台应用实现使用 OleDbConnection 读取Excel（支持.xls与.xlsx文件）**

```
class Program
    {
        //函数用来读取一个excel文件到DataSet集中  
        public static DataSet ExcelToDataSet(string filename, string tableName) 
        {
            //获取文件扩展名
            string strExtension = System.IO.Path.GetExtension(filename);
            OleDbConnection myConn = null;
            switch (strExtension)
            {
                case ".xls":
                    myConn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + filename + ";" + "Extended Properties=\"Excel 8.0;HDR=yes;IMEX=1;\"");
                    break;
                case ".xlsx":
                    myConn = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + filename + ";" + "Extended Properties=\"Excel 12.0;HDR=yes;IMEX=1;\"");
                    //此连接可以操作.xls与.xlsx文件 (支持Excel2003 和 Excel2007 的连接字符串) 
                    //"HDR=yes;"是说Excel文件的第一行是列名而不是数，"HDR=No;"正好与前面的相反。"IMEX=1 "如果列中的数据类型不一致，使用"IMEX=1"可必免数据类型冲突。 
                    break;
                default:
                    myConn = null;
                    break;
            }
            if (myConn == null)
            {
                return null;
            }
            string strCom = " SELECT * FROM ["+ tableName + "$]";      
            myConn.Open();
            //获取Excel指定Sheet表中的信息
            OleDbDataAdapter myCommand = new OleDbDataAdapter(strCom, myConn);
            DataSet ds;
            ds = new DataSet();
            myCommand.Fill(ds, tableName);
            myConn.Close();
            return ds;
        }
        static void Main(string[] args)
        {
            var tablename = "sheet1";
            //括号中为表格地址  
            DataSet ds = ExcelToDataSet("D:\\get.xls", tablename);            
            for (int i = 0; i < ds.Tables[0].Rows.Count; i++)
            {
                string str = ds.Tables[tablename].Rows[i]["价格"].ToString();  //Rows[i]["col1"]表示i行"col1"字段  
                Console.WriteLine(str);
            }
            Console.WriteLine("正确执行...");
            Console.ReadKey();
        }
    }

```
