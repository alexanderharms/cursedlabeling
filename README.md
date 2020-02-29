# cursedlabeling 
A small text labeling tool in
['curses'](https://docs.python.org/3.6/howto/curses.html). ![Version 0.5.0](https://img.shields.io/badge/version-0.5.0-brightgreen)

## Usage
```
python cursedlabeling.py (--multi) filename --column columnname 
```
By calling the script in this way it is possible to start labeling the 
column 'columnname' from file 'filename'. By using the flag '--multi' or '-m'
it is possible to assign multiple labels to one text.  

When using the 'multi'-flag the next text can be summoned by pressing 'n';
when not using this flag the next text will be presented as soon as a label
is assigned.

![cursedlabeling multi-label interface](https://alexanderharms.github.io/images/cursedlabeling_multilabel.png)  

Currently the text is displayed in curses 'windows'; in order to prevent
an error the text displayed is shortened.

The labeled file will be stored as labeled.csv with the response in the 
column 'label'. 

This script is tested with Python 3.7 and depends on pandas to process
 the CSV-files.

## To do:
- [ ] Make the text field scrollable.
- [ ] Make it possible to limit the options you can label with.
- [ ] Make it possible to use labels with multiple characters.
- [ ] Remove pandas dependency for the interaction of the csv and replace with
  Python's built in csv functionality.
