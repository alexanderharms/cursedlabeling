#!/usr/bin/env python3
import curses
from curses import wrapper

import pandas as pd

def main(stdscr):
    # Clear screen
    stdscr.clear()
    num_rows, num_cols = stdscr.getmaxyx()

    # Create a window for instructions
    # lines, columns, start line, start column
    instr_rows = 3
    instr_cols = num_cols - 1
    instr_rows_loc = num_rows - 1 - instr_rows
    instr_cols_loc = 0

    instr_window = curses.newwin(instr_rows, instr_cols, 
                                 instr_rows_loc, instr_cols_loc)

    # Create a window for text
    # lines, columns, start line, start column
    text_rows = num_rows - instr_rows - 1
    text_cols = num_cols - 1
    text_rows_loc = 0
    text_cols_loc = 0
    text_window = curses.newwin(text_rows, text_cols, 
                                text_rows_loc, text_cols_loc)

    press = 1
    text_index = 0
    text_array = pd.read_csv(data_filename)
    response_list = []

    stdscr.refresh()
    while chr(press) is not "q" and text_index < text_array.shape[0]:
        # Fill window for text
        text = text_array.text.iloc[text_index]
        text_window.addstr(0, 0, text)
        text_window.refresh()

        # Create a window for instructions
        instr_window.addstr(0, 0, "Press 'q' to close")
        instr_window.refresh()
        
        # Get input
        press = stdscr.getch()
        
        if chr(press) is not "q":
            response_list.append(chr(press))
            text_index += 1

    text_array['response'] = response_list
    text_array.to_csv("labeled.csv")

data_filename = "test.csv"
wrapper(main)
