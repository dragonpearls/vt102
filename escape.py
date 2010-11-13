"""Moves cursor down one line in same column. If cursor is at bottom margin, 
screen performs a scroll-up."""
IND = 0x44

"""Moves cursor up one line in same column. If cursor is at top margin, screen 
performs a scroll-down."""
RI = 0x4d

"""Moves cursor to first position on next line. If cursor is at bottom margin, 
screen performs a scroll-up."""
NEL = 0x45

"""Saves cursor position, character attribute (graphic rendition), character 
set, and origin mode selection. (See restore cursor)."""
DECSC = 0x37

"""Restores previously saved cursor position, character attribute (graphic 
rendition), character set, and origin mode selection. If none were saved, the c
ursor moves to home position."""
DECRC = 0x38

"""Moves cursor up n lines in same column. Cursor stops at top margin."""
CUU = 0x41

"""Moves cursor down n lines in same column. Cursor stops at bottom margin."""
CUD = 0x42

"""Moves cursor right n columns. Cursor stops at right margin."""
CUF = 0x43

"""Moves cursor left n columns. Cursor stops at left margin."""
CUB = 0x44

"""Moves cursor to line n, column m. If n or m are not selected or 
selected as 0, the cursor moves to first line or column, respectively."""
CUP = 0x48

"""Same as CUP."""
HVP = 0x66

"""Erase in line."""
EL = 0x4b

"""Erase in display."""
ED = 0x4a

"""Deletes n characters, starting with the character at cursor position. When 
a character is deleted, all characters to the right of cursor move left. This
creates a space character at right margin."""
DCH = 0x50

"""Inserts n lines at line with cursor. Lines displayed below cursor move down. 
Lines moved past the bottom margin are lost."""
IL = 0x4c

"""Deletes n lines, starting at line with cursor. As lines are deleted, lines 
displayed below cursor move up. Lines added to bottom of screen have spaces 
with same character attributes as last line moved up."""
DL = 0x4d
