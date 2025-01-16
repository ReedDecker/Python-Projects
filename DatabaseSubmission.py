import sqlite3

conn = sqlite3.connect('Decker.db')

# Create Database and a Table #
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtfile TEXT \
        )")
    
    conn.commit()

<sqlite3.Cursor object at 0x110347540>

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')  # FileList with multiple File Types # ADD Files .txt extension to Database #

with conn:
    cur = conn.cursor()
    for fName in fileList:
        if fName.endswith(".txt"):
            cur.execute('INSERT INTO tbl_txtfiles(col_txtfile) VALUES (?)', (fName,)) # Add comma to turn fName into Tuple instead of String #
            conn.commit()

            
<sqlite3.Cursor object at 0x110347d40>
<sqlite3.Cursor object at 0x110347d40>


with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txtfile FROM tbl_txtfiles")
    txtFile = cur.fetchall()
    for file in txtFile:
        txtFile = "The found text file: {}".format(file[0]) # Search for files with .txt extension #

        
<sqlite3.Cursor object at 0x110347ec0>
The found text file: Hello.txt
The found text file: World.txt
