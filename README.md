# cursedlabeling
A small text labeling tool in 'curses'. 

In mainscript.py it is possible to change the name of the file with the texts
you want to label. The script expects CSV-files with the text in a column named 
'text'. Currently the text is displayed in curses 'windows'; in order to prevent
an error the text displayed is shortened.

The labeled file will be stored as labeled.csv.

To do:
- Make the text field scrollable.
- Make it possible to limit the options you can label with.
- Enable multi-labeling
