#!/usr/bin/env python3
import curses
from curses import wrapper
import argparse

import pandas as pd

def generate_instr_window(num_rows, num_cols):
    # Create a window for instructions
    # lines, columns, start line, start column
    instr_rows = 3
    instr_cols = num_cols - 1
    instr_rows_loc = num_rows - 1 - instr_rows
    instr_cols_loc = 0

    instr_window = curses.newwin(instr_rows, instr_cols, 
                                 instr_rows_loc, instr_cols_loc)
    instr_win_prop = [instr_rows, instr_cols, 
                      instr_rows_loc, instr_cols_loc]
    return instr_window, instr_win_prop

def generate_text_window(num_rows, num_cols,
                         instr_rows = 3):
    # Create a window for text
    # lines, columns, start line, start column
    text_rows = num_rows - instr_rows - 1
    text_cols = num_cols - 1
    text_rows_loc = 0
    text_cols_loc = 0

    text_window = curses.newwin(text_rows, text_cols, 
                                text_rows_loc, text_cols_loc)
    
    text_win_prop = [text_rows, text_cols,
                     text_rows_loc, text_cols_loc]
    return text_window, text_win_prop

def labeling(stdscr, text_array, text_column, multilabelBool = False):
    # Clear screen
    stdscr.clear()
    num_rows, num_cols = stdscr.getmaxyx()

    # Create a window for instructions and for the text
    instr_window, instr_win_prop = generate_instr_window(num_rows, num_cols)
    text_window, text_win_prop = generate_text_window(num_rows, num_cols,
                                                      instr_win_prop[0])
    text_rows = text_win_prop[0]
    text_cols = text_win_prop[1]

    press = 1
    text_index = 0
    response_list = []
    response_press = []

    stdscr.refresh()

    # Create a window for instructions
    if multilabelBool:
        instr_window.addstr(0, 0, "Multi-label. Press 'n' for next text. " 
                + "Press 'q' to close")
    else:
        instr_window.addstr(0, 0, "Single label. Press 'q' to close")
    instr_window.refresh()

    # Start the labeling procedure
    while True:
        text_window.clear()
        # Fill window for text
        text = text_array[text_column].iloc[text_index]
        # Trim the text short to fit in the window
        text = text[0:((text_cols - 1) * (text_rows - 10))]

        text_window.addstr(0, 0, text)
        text_window.refresh()
        
        # Get input
        press = stdscr.getch()
        
        if multilabelBool:
            if press is ord("q"):
                break
            elif press is ord("n"):
                response_list.append(response_press)
                response_press = []
                text_index += 1
            else:
                # Add response to the list
                response_press.append(chr(press))
        else:
            # Add response to the list
            response_list.append(chr(press))
            text_index += 1

        # If all the texts are labeled, break
        if text_index >= text_array.shape[0]:
            break
    
    if press is not ord("q"):
        text_array['label'] = response_list
        text_array.to_csv("labeled.csv")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Name of file to be labeled")
    parser.add_argument("--column", type=str, default='text', 
                        help="Name of the text column")
    parser.add_argument("-m", "--multi", action="store_true",
                        help="Enable multi-label labeling")
    args = parser.parse_args()

    data_filename = args.filename
    text_column = args.column
    text_array = pd.read_csv(data_filename)
    wrapper(labeling, text_array, text_column, args.multi)
