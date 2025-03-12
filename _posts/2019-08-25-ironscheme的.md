---
title: "IronScheme的"
date: "2019-08-25"
categories: 
  - "lisp"
---

```
(import
    (rnrs)
    (ironscheme clr)
)

(define msgbox (pinvoke-call user32 MessageBox int (intptr string string int)))
(msgbox 0 "Hello, Win32 API(IronScheme) World!" "Hello, World!" 0 )
```

如上这个可以显示messagebox对话框。

```
(import
    (rnrs)
    (ironscheme clr)
)
 
(clr-reference System.Windows.Forms)
(clr-reference System.Drawing)
 
(clr-using System.Windows.Forms)
(clr-using System.Drawing)
 
(begin
    (define form (clr-new Form))
    (clr-prop-set! Form Size form (clr-new Size 640 480))
    (clr-prop-set! Form Text form "Hello, World!")
    (define label1 (clr-new Label))
    (clr-prop-set! Label Size label1 (clr-new Size 320 20))
    (clr-prop-set! Label Text label1 "Hello, Windows Forms(IronScheme) World!")
    (define formControls (clr-prop-get Form Controls form ))
    (clr-call Form+ControlCollection Add formControls label1 )
 
    (clr-static-call Application (Run Form) form)
)
```

```
(import
    (rnrs)
    (ironscheme clr)
)
 
(clr-reference System)
(clr-reference System.Data)
(clr-reference MySql.Data)
 
(clr-using System)
(clr-using MySql.Data.MySqlClient)
 
(begin
    (define conStr "server=localhost;user id=root;password=P@ssW0rd")
    (define sqlStr "SELECT 'Hello, Connector/NET World!' AS Message")
    (define con (clr-new MySqlConnection conStr))
    (define cmd (clr-new MySqlCommand sqlStr con))
    (clr-call MySqlConnection Open con)
    (define reader (clr-call MySqlCommand ExecuteReader cmd))
    (if (clr-call MySqlDataReader Read reader)
        (begin
            (clr-static-call System.Console WriteLine (clr-call MySqlDataReader GetName reader 0))
            (clr-static-call System.Console WriteLine "---------------------")
            (clr-static-call System.Console WriteLine (clr-call MySqlDataReader GetValue reader 0))
        )
    )
    (clr-call MySqlDataReader Close reader)
    (clr-call MySqlConnection Close con)
)
```

```
(import
    (rnrs)
    (ironscheme clr)
)
 
(clr-reference System)
(clr-reference System.Data)
 
(clr-using System)
(clr-using System.Data.OleDb)
 
(begin
    (define conStr "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=hello.mdb")
    (define sqlStr "SELECT 'Hello, ADO.NET World!' AS Message")
    (define con (clr-new OleDbConnection conStr))
    (define cmd (clr-new OleDbCommand sqlStr con))
    (clr-call OleDbConnection Open con)
    (define reader (clr-call OleDbCommand ExecuteReader cmd))
    (if (clr-call OleDbDataReader Read reader)
        (begin
            (clr-static-call System.Console WriteLine (clr-call OleDbDataReader GetName reader 0))
            (clr-static-call System.Console WriteLine "---------------------")
            (clr-static-call System.Console WriteLine (clr-call OleDbDataReader GetValue reader 0))
        )
    )
    (clr-call OleDbDataReader Close reader)
    (clr-call OleDbConnection Close con)
)
```

```
(import
    (rnrs)
    (ironscheme clr)
    (ironscheme clr shorthand)
)

(clr-reference System.Windows.Forms)
(clr-reference System.Drawing)

(clr-using System.Windows.Forms)
(clr-using System.Drawing)

(begin
    ; INITIALIZE
    (define mainForm (clr-new Form))
    (define btnGo (clr-new Button))
    (define btnStop (clr-new Button))
    (define mainControls (clr-prop-get Form Controls mainForm))
    
    ; SETUP EVENTS
    ; mouse enter
    (define mainForm_MouseEnter 
        (lambda (s e) 
            (display "Enter")
            (newline)
        )
    )
    
    ; mouse leave
    (define mainForm_MouseLeave
        (lambda (s e) 
            (display "Leave")
            (newline)
        )
    )
    
    ; click
    (define btnGo_Click
        (lambda (s e)
            (display "GO")
            (newline)
        )
    )
    
    ; click
    (define btnStop_Click
        (lambda (s e)
            (display "STOP")
            (newline)
        )
    )
    
    ; APPLY EVENTS
    (clr-event-add! Form MouseEnter mainForm mainForm_MouseEnter)
    (clr-event-add! Form MouseLeave mainForm mainForm_MouseLeave)
    (clr-event-add! Button Click btnGo btnGo_Click)
    (clr-event-add! Button Click btnStop btnStop_Click)
    
    ; SET PROPERTIES
;    (clr-prop-set! Form Text mainForm "Information Viewer")
;    (clr-prop-set! Button Text btnGo "GO")
    
    (let ((mf mainForm))
        (with-clr-type ((mf Form))
            (mf : Text = "Information Viewer")
        )
    )
    
    (let ((bg btnGo) (bs btnStop))
        (with-clr-type ((bg Button) (bs Button))
            (bg : Text = "GO")
            (bg : Location = (clr-new Point 10 20))
            (bs : Text = "STOP")
            (bs : Location = (clr-new Point 100 20))
        )
    )
    
    (let ((mc mainControls))
        (with-clr-type ((mc Form+ControlCollection))
             (mc : Add (btnGo))
             (mc : Add (btnStop))
        )
    )
    
    ;(clr-call Form+ControlCollection Add mainControls btnGo)
    
    ; SHOW FORM AND RUN PUMP
    (clr-static-call System.Console WriteLine "Start")
    (clr-static-call Application (Run Form) mainForm)
    (clr-static-call System.Console WriteLine "Stop")
    
    ; REMOVE CONTROLS
    (let ((mc mainControls))
        (with-clr-type ((mc Form+ControlCollection))
            (mc : Add (btnGo))
        )
    )


    ;(clr-call Form+ControlCollection Remove mainControls btnGo)
    
    ; REMOVE EVENTS
    (clr-event-remove! Form MouseEnter mainForm mainForm_MouseEnter)
    (clr-event-remove! Form MouseLeave mainForm mainForm_MouseLeave)
    (clr-event-remove! Button Click btnGo btnGo_Click)
    (clr-event-remove! Button Click btnStop btnStop_Click)
)


```
