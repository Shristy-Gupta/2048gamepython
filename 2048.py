from tkinter import Frame, Label, CENTER

import Python2048Game as LogicsFinal
import constants as c
#Inherted from Frame Class in tkinter libraray
#Frame is a widget/container that allows user to keep all its values

class Game2048(Frame):
    def __init__(self):
        #Object of Frame has been initalized
        Frame.__init__(self)
        #tkinter has grid manager that allows to create all the widgets in the form of grid.
        self.grid()
        #Master is a Metada of the grid that stores data like title
        self.master.title('SHRISTY-2048')
        # <Key> denotes event as key, this will bind the main grid on key press event
        self.master.bind("<Key>", self.key_press)
        self.commands = {c.KEY_UP: LogicsFinal.move_up, c.KEY_DOWN: LogicsFinal.move_down,
                         c.KEY_LEFT: LogicsFinal.move_left, c.KEY_RIGHT: LogicsFinal.move_right
                        }
        #The grid cells in the frame is initialized and empty
        self.grid_cells = []
        #Initializes the matrix, used at the very first time, adds two new 2s
        self.init_grid()
        #Sets the color of cells according to numbers
        self.init_matrix()
        #Sets the color of cells according to numbers
        self.update_grid_cells()
        #It will run the main UI
        self.mainloop()

    def init_grid(self):
        #Created another frame in the container called background and it is 400X400
        background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,
                         width=c.SIZE,height=c.SIZE)
        background.grid()
        #Adding Cells
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cell=Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                            width=c.SIZE/c.GRID_LEN,
                            height=c.SIZE/c.GRID_LEN)
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)
                #Label is widget which is a textbox we are binding it to the master i.e cell 
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,
                        width=5,height=2) 
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)


    def init_matrix(self):
        self.matrix = LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    #bg color is color of label background and fg color is label foreground
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],
                    fg=c.CELL_COLOR_DICT[new_number])
        #In Frame Libraray , if any it waits till all the changes are made and then reflect in UI
        self.update_idletasks()

    def key_press(self, event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                LogicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if LogicsFinal.get_current_state(self.matrix)=='WON':
                    self.grid_cells[1][1].configure(text='YOU',bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='WIN!',bg=c.BACKGROUND_COLOR_CELL_EMPTY)

                if LogicsFinal.get_current_state(self.matrix)=='LOST':
                    self.grid_cells[1][1].configure(text='YOU',bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='LOST!',bg=c.BACKGROUND_COLOR_CELL_EMPTY)




gamegrid = Game2048()
