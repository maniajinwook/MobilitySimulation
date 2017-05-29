from Tkinter import *
import os



#-----------------------------------------------------------------------------------#
#                                Input Value                                        #
#-----------------------------------------------------------------------------------#



node_num, com_range, node_speed, cov_range, area_side, runtime = 0, 0, 0, 0, 0, 6000  # cov_range must need odd, cov_range and com_range is radius.

node_num_entry, com_range_entry, node_speed_entry, cov_range_entry, area_side_entry, runtime_entry = 0, 0, 0, 0, 0, 0



##modelexe_path = "C:\Users\jung\Documents\Visual Studio 2015\Projects\RandomWaypoint\Debug"
modelexe_path = "E:\RandomWaypoint\Debug"

nodedraw_name = ["node0","node1", "node2", "node3", "node4", "node5","node6","node7", "node8", "node9"]
noderange_name = ["noderange0","noderange1", "noderange2", "noderange3", "noderange4", "noderange5","noderange6", "noderange7", "noderange8", "noderange9"]
node_color = ["blue", "red", "green", "yellow", "black","blue", "red", "green", "yellow", "black"]

first_table_x = 100
first_table_y = 250
first_table_prex = 100
first_table_prey = 250

second_table_x = 150
second_table_y = 600
#second_table_prex = 100
#second_table_prey = 650

mode_state = "Simulationmode"  # var type .. you can need function : mode_state.get()


cov_per_val = 0

#node_range_name = ["noderange1", "noderange2", "noderange3", "noderange4", "noderange5"]


#-----------------------------------------------------------------------------------#
#                                EXE_File_Open                                      #
#-----------------------------------------------------------------------------------#

def Open_File():
    global modelexe_path
 
    num1, num2, num3, num4, num5, num6, num7 = 10, 8, 150, 2, 1, 700, 7200
    cmd = "cd %s & RandomWaypoint %d %d %d %d %d %d %d" %(modelexe_path, num1, num2, num3, num4, num5, num6, num7)
    os.system(cmd)
    #test_file = open( 'C:\Users\jung\Desktop\wow.txt', 'w')
    #test_file.write('Hello python file I/O')
    #test_file.close()

 




#-----------------------------------------------------------------------------------#
#                                Local Function                                     #
#-----------------------------------------------------------------------------------#

def Mode_Value_Change() :
    global mode_state  
    
    

    #mode_state = mode_state.get()
    print mode_state.get()







#-----------------------------------------------------------------------------------#
#                                File_Menu                                          #
#-----------------------------------------------------------------------------------#


def Init_Filemenu(master):
    global mode_state
    
    mode_state = StringVar()

    menubar = Menu(master)

    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "New", command = quit)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = quit)
    menubar.add_cascade(label = "File", menu = filemenu)

    

    modemenu = Menu(menubar, tearoff = 0)
    modemenu.add_radiobutton(label = "Simulation Mode", variable = mode_state, value = "simulationmode", command = Mode_Value_Change)
    modemenu.add_radiobutton(label = "Replay Mode", variable = mode_state, value = "replaymode", command = Mode_Value_Change)    
    


    menubar.add_cascade(label = "Mode", menu = modemenu)
    

    helpmenu = Menu(menubar, tearoff = 0)
    helpmenu.add_command(label = "RTS Lab.")
    menubar.add_cascade(label = "Help", menu = helpmenu)

    master.config(menu = menubar)


    return menubar
    





#-----------------------------------------------------------------------------------#
#                                Frame_Menu                                         #
#-----------------------------------------------------------------------------------#

def Init_Framemenu(master):
    #kind of Model
    global node_num_entry, com_range_entry, node_speed_entry, cov_range_entry, area_side_entry, runtime_entry
    options = ["Normal Model", "Random Model", "Super Model"]

    F_Menu = Frame(master, bg = "black", width = 300, height = 220)
    F_Menu.grid(row = 1, column = 0, sticky = W+E+N+S, columnspan = 2, padx = 20, pady = 20)



    Label(F_Menu, text="Setting", bg = "black", fg = "white").grid(row = 0, column = 0, rowspan = 2, padx = 20, pady = 20)

    # Model select
    Label(F_Menu, text="Model", bg = "black", fg = "white").grid(row = 0, column = 1,padx = 10, pady = 10, sticky = S)
    model_select = StringVar()
    om = OptionMenu(F_Menu, model_select, *options)
    om.config(width = 20)
    model_select.set("Mobility model")
    om.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = N)


    
    Label(F_Menu, text="Node", bg = "black", fg = "white").grid(row = 0, column = 2,padx = 10, pady = 10, sticky = S)
    node_num_entry = Entry(F_Menu)
    node_num_entry.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = N)
    

    Label(F_Menu, text="Communication Range(m,radius)", bg = "black", fg = "white").grid(row = 0, column = 3,padx = 10, pady = 10, sticky = S)
    com_range_entry = Entry(F_Menu)
    com_range_entry.grid(row = 1, column = 3, padx = 10, pady = 10, sticky = N)


    Label(F_Menu, text="Node Speed(m/s)", bg = "black", fg = "white").grid(row = 0, column = 4,padx = 10, pady = 10, sticky = S)
    node_speed_entry = Entry(F_Menu)
    node_speed_entry.grid(row = 1, column = 4, padx = 10, pady = 10, sticky = N)
    
    

    Label(F_Menu, text="Cover Range(m,radius)", bg = "black", fg = "white").grid(row = 0, column = 5,padx = 10, pady = 10, sticky = S)
    cov_range_entry = Entry(F_Menu)
    cov_range_entry.grid(row = 1, column = 5, padx = 10, pady = 10, sticky = N)
    
    
    Label(F_Menu, text="Area Side(m)", bg = "black", fg = "white").grid(row = 0, column = 6,padx = 10, pady = 10, sticky = S)
    area_side_entry = Entry(F_Menu)
    area_side_entry.grid(row = 1, column = 6, padx = 10, pady = 10, sticky = N)


    Label(F_Menu, text="Runtime(s)", bg = "black", fg = "white").grid(row = 0, column = 7,padx = 10, pady = 10, sticky = S)
    runtime_entry = Entry(F_Menu)
    runtime_entry.grid(row = 1, column = 7, padx = 10, pady = 10, sticky = N)


    #default
    node_num_entry.insert(0, "5")
    com_range_entry.insert(0, "50")
    node_speed_entry.insert(0, "2")
    cov_range_entry.insert(0, "25")
    area_side_entry.insert(0, "700")
    runtime_entry.insert(0, "6000")

    
    return F_Menu







#-----------------------------------------------------------------------------------#
#                                Frame_Scene                                        #
#-----------------------------------------------------------------------------------#

def Init_Framescene(master):

    C_Scene = Canvas(master, bg = "white", width = 700, height = 700)
    C_Scene.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 20, pady = 20)

    
   
    return C_Scene






#-----------------------------------------------------------------------------------#
#                                Frame_Result                                       #
#-----------------------------------------------------------------------------------#

def Init_Frameresult(master):
    G1_width = 100
    G1_height = 200
    a = 0
    b = 100    # a, b is string of x-axis , y-axis

    global cov_per_val

    F_Result = Canvas(master, bg = "white", width = 650, height = 700)
    F_Result.grid(row = 0, column = 1, sticky = W+E+N+S, padx = 20, pady = 20)

    # Rectangle point : (100.50) ~ (600.250)
    
    for x in range(100, 650, 50) :                            # height draw
        F_Result.create_line(x, 50, x, 250, fill="black")
        F_Result.create_text(x, 270,text = str(a)+"s",fill = "black")
        a += 100

    for y in range(50, 270, 20) :                           # width draw
        F_Result.create_line(100, y, 600, y, fill="black")
        F_Result.create_text(80, y,text = ""+str(b)+"%",fill = "black")
        b -= 10
#--------------------------------------------------------first table finish
    a = 0
    b = 2000

    # Rectangle point : (100.400) ~ (600.600)

    #for x in range(100, 650, 50) :                              # height draw
    #    F_Result.create_line(x, 400, x, 600, fill="gray")
    #    F_Result.create_text(x, 620,text = str(a)+"s",fill = "white")
    #    a += 600
    F_Result.create_line(100, 400, 100, 600, fill="black")
    for x in range(160, 650, 100) :                              # height draw
    #    F_Result.create_line(x, 400, x, 600, fill="gray")
         F_Result.create_text(x, 620,text = "Node_"+str(a)+"",fill = "black")
         a += 1



    for y in range(400, 620, 20) :                              # width draw
        F_Result.create_line(100, y, 600, y, fill="black")
        F_Result.create_text(80, y,text = ""+str(b)+"",fill = "black")
        b -= 200
#--------------------------------------------------------second table finish

    F_Result.create_text(350, 30, text = "Coverage", fill = "black")
    F_Result.create_text(530, 30, text = "current (%) : ", fill = "black")           # value of current percentage
    cov_per_val = F_Result.create_text(580, 30, text = ""+str(0)+"", fill = "black")

    F_Result.create_text(350, 380, text = "Spatial Dependence", fill = "black")


    return F_Result




