#!/usr/bin/env python
# coding: utf-8

# In[91]:


from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    
 # Implement your code here.
    
    if (
        board[x][y] != old or
        0 > x > len(input_board[x]) or 
        0 > y > len(input_board)
        ):
        return input_board
    
    row = list(input_board[x])
    row[y] = new
    input_board[x] = ''.join(row)
    
    flood_fill(input_board, old, new, x + 1, y)
    flood_fill(input_board, old, new, x - 1, y)
    flood_fill(input_board, old, new, x, y + 1)
    flood_fill(input_board, old, new, x, y - 1)
    



modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in board:
    print(a)


# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....


# In[ ]:

print("lalalala")




