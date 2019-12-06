# cursedlabeling
A small text labeling tool in
['curses'](https://docs.python.org/3.6/howto/curses.html). 

## Usage
```
python3 cursedlabeling.py (--multi) filename --column columnname 
```
By calling the script in this way it is possible to start labeling the 
column 'columnname' from file 'filename'. By using the flag '--multi' or '-m'
it is possible to assign multiple labels to one text. 

Currently the text is displayed in curses 'windows'; in order to prevent
an error the text displayed is shortened.

The labeled file will be stored as labeled.csv with the response in the 
column 'label'. 

To do:
- Make the text field scrollable.
- Make it possible to limit the options you can label with.
- Make it possible to use labels with multiple characters.
- Remove pandas dependency for the interaction of the csv and replace with
  Python's built in csv functionality.
