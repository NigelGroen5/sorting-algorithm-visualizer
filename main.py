# Algorithm Sorter Visualizer - Nigel Groen
import pgzhelper
import pgzrun
from random import *
import os

# Setting up screen
WIDTH = 800
HEIGHT = 600
os.environ['SDL_VIDEO_CENTERED'] = '1' 

class Bar():
    '''
    Bar class creates bars in the sorting visualization.
    
    Attributes:
    - pos: x-coordinate of the bar
    - size: height/size of the bar
    - color: color of the bar
    '''
    def __init__(self, pos, size, color ):
        self.size = size
        self.pos = pos
        self.color = color
    def draw_bar(self):
        '''
        Draws the bar on the screen if called within the draw function.
        '''
        bar_height = self.size
        bar_y = 570 - bar_height  # Adjust position based on accumulated heights
        screen.draw.filled_rect(Rect((self.pos, bar_y), (10, bar_height)), self.color)

class Main_object():
    '''
    Main_object class that act as a organizer of global variables.
    '''
    def __init__(self, i,char,lst,num_ops,curr_stage,sorted_flag):
        self.i = i
        self.char= char
        self.lst = lst
        self.num_ops = num_ops
        self.curr_stage = curr_stage
        self.sorted_flag = sorted_flag

def update():
    '''
    Updates the game based on the current stage
    '''
    # Handles different stages of the game.
    if main_obj.curr_stage == 'welcome':
        if keyboard.space:
            main_obj.curr_stage = 'menu'

    elif main_obj.curr_stage == 'bubble':
        # Check if bars need to be created.
        if len(main_obj.lst) == 0:
            create_bars()
        # Continue bubble sort 
        if main_obj.char < len(main_obj.lst):
            main_obj.i+= 1
            # Allows code to run like a for loop.
            if main_obj.i+1 >= len(main_obj.lst):
                main_obj.char += 1
                main_obj.i=-1
            # Checks if bars need to swap and swaps them.
            elif main_obj.lst[main_obj.i].size > main_obj.lst[main_obj.i+1].size:
                    main_obj.num_ops += 1
                    temp = main_obj.lst[main_obj.i].size
                    main_obj.lst[main_obj.i].size = main_obj.lst[main_obj.i+1].size
                    main_obj.lst[main_obj.i+1].size = temp
                    if main_obj.lst[main_obj.i].pos > main_obj.lst[main_obj.i+1].pos:
                        temp = main_obj.lst[main_obj.i].pos
                        main_obj.lst[main_obj.i].pos = main_obj.lst[main_obj.i+1].pos
                        main_obj.lst[main_obj.i+1].pos = temp
            # Implemenation from: https://www.w3schools.com/python/ref_func_all.asp.
            # Marks bars as sorted if the list is sorted and changes their color to green.
            if all(main_obj.lst[e].size <= main_obj.lst[e + 1].size for e in range(len(main_obj.lst) - 1)):
                main_obj.lst[main_obj.i].color = (0,255,0)
                main_obj.lst[main_obj.i+1].color = (0,255,0)
                main_obj.sorted_flag = True
                
    elif main_obj.curr_stage == 'insertion':
        # Check if bars need to be created.
        if len(main_obj.lst) == 0:
            create_bars()
        # Continue insertion sort .
        if main_obj.i == len(main_obj.lst):
            main_obj.sorted_flag =True
            main_obj.i=0
        tmp = main_obj.lst[main_obj.i].size
        # Is smaller than num to left.
        while main_obj.i>0 and tmp<main_obj.lst[main_obj.i-1].size:
            # Shift elements to make space for the current element.
            main_obj.lst[main_obj.i].size=main_obj.lst[main_obj.i-1].size
            main_obj.i -=1
        # Copy value into open slot.
        main_obj.lst[main_obj.i].size=tmp
        # Iterate through bars.
        main_obj.i+=1
        
    elif main_obj.curr_stage == 'selection':
        # Check if bars need to be created.
        if len(main_obj.lst) == 0:
            create_bars()
        # Check if sort is finished.
        if main_obj.i == len(main_obj.lst):
            main_obj.sorted_flag = True
            main_obj.i = len(main_obj.lst)+1
        # Selection sorts.
        if main_obj.i < len(main_obj.lst):
            # Make all the bars white.
            for bar in main_obj.lst:
                bar.color = (255,255,255)
            min_index = main_obj.i
            for element in range(main_obj.i + 1, len(main_obj.lst)):
                if main_obj.lst[element].size < main_obj.lst[min_index].size:
                    min_index = element
        
            main_obj.lst[main_obj.i].size, main_obj.lst[min_index].size = main_obj.lst[min_index].size, main_obj.lst[main_obj.i].size
            # Highlight the selected bar.
            main_obj.lst[min_index].color = (255,0,0)
            main_obj.lst[main_obj.i].color = (255,0,0)
            # Increment after finding the minimum element.
            main_obj.i += 1
            
    elif main_obj.curr_stage == 'gnome':
        # Check if bars need to be created.
        if len(main_obj.lst) == 0:
            create_bars()
        # Highlights bars white.
        for element in main_obj.lst:
                element.color = (255,255,255)
        # Gnome sort.
        if main_obj.i < len(main_obj.lst) and main_obj.i != 37:
            if main_obj.i == 0:
                main_obj.i += 1
            if main_obj.lst[main_obj.i].size >= main_obj.lst[main_obj.i-1].size:
                main_obj.i += 1
            else:
                main_obj.lst[main_obj.i].size, main_obj.lst[main_obj.i-1].size = main_obj.lst[main_obj.i-1].size, main_obj.lst[main_obj.i].size
                main_obj.i -= 1
            # Highlights seleected bars red.
            if main_obj.i != 37:
                main_obj.lst[main_obj.i].color = (255,0,0)
                main_obj.lst[main_obj.i-1].color = (255,0,0)
        else:
            # If finished bars turn green
            for bar in main_obj.lst:
                bar.color = (0,255,0)



def create_bars():
    '''
    Create randomized bars for sorting.
    '''
    main_obj.lst.clear()           
    initial =40
    main_obj.lst = []
    for f in range(37):
        f = Bar(initial, randint(1,450), (255,255,255))
        initial += 20
        main_obj.lst.append(f)


def draw():
    '''
    Draw the game screen based on the current stage.
    '''
    screen.clear()
    if main_obj.curr_stage == 'welcome':
        # Draws welcome screen.
        screen.fill('grey')
        screen.draw.text(f'Welcome!', (140, 110), fontsize=150, color = 'darkBlue')
        screen.draw.text(f'This is a pygame zero project that visualizes a bunch of different', (25, 250), fontsize=34, color = 'black')
        screen.draw.text(f'sorting algorithms like bubble sort and insertion sort.', (80, 300), fontsize=34, color = 'black')
        screen.draw.text(f'Press SPACE to begin.', (100, 410), fontsize=80, color = 'black')
        
    elif main_obj.curr_stage == 'menu':
        # Draws menu screen.
        screen.fill('darkGrey')
        screen.draw.text(f'Menu!', (240, 80), fontsize=150, color = 'darkBlue')
        screen.draw.text(f'Click on the sorting to algorithm that you want to visualize!', (50, 200), fontsize=36, color = 'black')
        screen.draw.filled_rect(Rect((50,250),(300,120)), (0,0,0))
        screen.draw.text(f'Bubble Sort',(125, 300), fontsize=30, color = 'white')
        screen.draw.filled_rect(Rect((450,250),(300,120)), (0,0,0))
        screen.draw.text(f'Insertion Sort',(525, 300), fontsize=30, color = 'white')
        screen.draw.filled_rect(Rect((50,420),(300,120)), (0,0,0))
        screen.draw.text(f'Selection Sort',(125, 470), fontsize=30, color = 'white')
        screen.draw.filled_rect(Rect((450,420),(300,120)), (0,0,0))
        screen.draw.text(f'Gnome Sort',(525, 470), fontsize=30, color = 'white')


            
    elif main_obj.curr_stage == 'bubble':
        # Draws bubble sort screen.
        screen.fill('black')
        # Draws menu button.
        screen.draw.filled_rect(Rect((580,35),(131,31)), color = 'grey')
        screen.draw.text(f'Menu',(621, 45), fontsize=20, color = 'darkRed')
        # Draws title and num_ops.
        screen.draw.text(f'Bubble sort!', (300, 35), fontsize=40, color = 'white')
        screen.draw.text(f'Number of operations: {main_obj.num_ops}',(300, 85), fontsize=20, color = 'white')
        # Draws randomized bar button.
        screen.draw.filled_rect(Rect((89,35),(131,31)), color = 'grey')
        screen.draw.text(f'Randomize bars',(98, 45), fontsize=20, color = 'darkRed')
        # Highlights used bars.
        if main_obj.char < len(main_obj.lst) and main_obj.sorted_flag == False:    
            main_obj.lst[main_obj.i].color = (255,0,0)
            main_obj.lst[main_obj.i+1].color = (255,0,0)
        # Draws all bars.
        for a in main_obj.lst:
            a.draw_bar()
        # Unhighlighs used bars.
        if main_obj.char < len(main_obj.lst) and main_obj.sorted_flag == False:
            main_obj.lst[main_obj.i].color = (255,255,255)
            main_obj.lst[main_obj.i+1].color = (255,255,255)
            
    elif main_obj.curr_stage == 'insertion':
        # Draws insertion sort screen.
        screen.fill('black')
        screen.draw.filled_rect(Rect((580,35),(131,31)), color = 'grey')
        screen.draw.text(f'Menu',(621, 45), fontsize=20, color = 'darkRed')  
        screen.draw.text(f'Insertion sort!', (300, 35), fontsize=40, color = 'white')
        screen.draw.filled_rect(Rect((89,35),(131,31)), color = 'grey')
        screen.draw.text(f'Randomize bars',(98, 45), fontsize=20, color = 'darkRed')
        # Draws bars.
        if main_obj.sorted_flag == False and main_obj.i < len(main_obj.lst):
            main_obj.lst[main_obj.i].color = (255,0,0)
        for a in main_obj.lst:
            a.draw_bar()
        if main_obj.sorted_flag == False and main_obj.i < len(main_obj.lst):
            main_obj.lst[main_obj.i].color = (255,255,255)
        elif main_obj.sorted_flag == True:
            for u in main_obj.lst:
                u.color = (0,255,0)
   
    elif main_obj.curr_stage == 'selection':
        # Draws insertion sort screen.
        screen.fill('black')
        screen.draw.filled_rect(Rect((580,35),(131,31)), color = 'grey')
        screen.draw.text(f'Menu',(621, 45), fontsize=20, color = 'darkRed')
        screen.draw.text(f'Selection sort!', (300, 35), fontsize=40, color = 'white')
        screen.draw.filled_rect(Rect((89,35),(131,31)), color = 'grey')
        screen.draw.text(f'Randomize bars',(98, 45), fontsize=20, color = 'darkRed')
        # Draws bars.
        for a in main_obj.lst:
            a.draw_bar()
        if main_obj.sorted_flag == True:
            for u in main_obj.lst:
                u.color = (0,255,0)
 
    elif main_obj.curr_stage == 'gnome':
        # Draws gnome sort screen.
        screen.fill('black')
        screen.draw.filled_rect(Rect((580,35),(131,31)), color = 'grey')
        screen.draw.text(f'Menu',(621, 45), fontsize=20, color = 'darkRed')
        screen.draw.text(f'Gnome sort!', (300, 35), fontsize=40, color = 'white')
        screen.draw.filled_rect(Rect((89,35),(131,31)), color = 'grey')
        screen.draw.text(f'Randomize bars',(98, 45), fontsize=20, color = 'darkRed')
        # Draws bars.
        for a in main_obj.lst:
            a.draw_bar()
           
def on_mouse_down(pos, button):
    '''
    Handles mouse clicks.
    '''
    x, y = pos
    if main_obj.curr_stage == 'menu':
        # Makes rect variables for buttons.
        bubble_rect = Rect(50, 250, 300, 120)
        insertion_rect = Rect(450, 250, 300, 120)
        selection_rect = Rect(50,420,300,120)
        gnome_rect = Rect(450,420,300,120)
        # If user hits a button bring them to the selected sort and refresh global variables.
        if bubble_rect.collidepoint(x, y):
            main_obj.curr_stage = 'bubble'
            main_obj.i=-1
            main_obj.char = 0
            main_obj.lst=[]
            main_obj.num_ops = 0
            main_obj.sorted_flag = False
        elif insertion_rect.collidepoint(x, y):
            main_obj.curr_stage = 'insertion'
            main_obj.i=0
            main_obj.char = 0
            main_obj.lst=[]
            main_obj.num_ops = 0
            main_obj.sorted_flag = False
        elif selection_rect.collidepoint(x, y):
            main_obj.curr_stage = 'selection'
            main_obj.i=0
            main_obj.char = 0
            main_obj.lst=[]
            main_obj.num_ops = 0
            main_obj.sorted_flag = False
        elif gnome_rect.collidepoint(x, y):
            main_obj.curr_stage = 'gnome'
            main_obj.i=0
            main_obj.char = 0
            main_obj.lst=[]
            main_obj.num_ops = 0
            main_obj.sorted_flag = False
    
    # Handles buttons of sorting algorithm screens. 
    if main_obj.curr_stage == 'bubble' or main_obj.curr_stage == 'insertion' or main_obj.curr_stage == 'selection' or main_obj.curr_stage == 'gnome':
        menu_rect = Rect(580,35,131,31)
        randomize_rect = Rect(89,35,131,31)
        if menu_rect.collidepoint(x, y):
            main_obj.curr_stage = 'menu'
        if randomize_rect.collidepoint(x, y):
            create_bars()
            main_obj.i=0
            main_obj.char = 0
            main_obj.num_ops = 0
            main_obj.sorted_flag = False

# Initializing the main object with initial values
main_obj = Main_object(0,0,[],0,'welcome',False)

    
pgzrun.go()
