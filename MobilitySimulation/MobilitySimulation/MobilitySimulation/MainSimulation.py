#-*- coding: utf-8 -*-

from Tkinter import *
import random
import time
import Init, Socket_Set, Analysis
import os
import threading
import Queue








#-----------------------------------------------------------------------------------#
#                                   Variable                                        #
#-----------------------------------------------------------------------------------#




run_number = 1

node = []
dependence_table = [0, 0, 0, 0, 0]
recona_range = []




queue = Queue.Queue()  # not use





class Node():

    def __init__(self, nodedraw_name, noderange_name, node_color, current_x, current_y, current_z, destination_x, destination_y, destination_z):

        self.nodedraw_name = nodedraw_name
        self.noderange_name = noderange_name
        self.node_color = node_color

        self.current_x = current_x
        self.current_y = current_y
        self.current_z = current_z

        self.destination_x = destination_x
        self.destination_y = destination_y
        self.destination_z = destination_z

    def update_position(self, current_x, current_y, current_z, destination_x, destination_y, destination_z):

        self.current_x = current_x
        self.current_y = current_y
        self.current_z = current_z

        self.destination_x = destination_x
        self.destination_y = destination_y
        self.destination_z = destination_z






#-----------------------------------------------------------------------------------#
#                                   Function                                        #
#-----------------------------------------------------------------------------------#


def Init_Entry():
    Init.node_num = int(Init.node_num_entry.get())
    Init.com_range = int(Init.com_range_entry.get())
    Init.node_speed = int(Init.node_speed_entry.get())
    Init.cov_range = int(Init.cov_range_entry.get())
    Init.area_side = int(Init.area_side_entry.get())
    Init.runtime = int(Init.runtime_entry.get())

    return True



def Thread_Run():

    check = Init_Entry()
    

    if (check == True)&(Init.mode_state.get() == "simulationmode") :
        t_1 = Thread_Draw_Algorithm(queue)
        t_1.setDaemon(True)
        t_1.start()


        t_2 = File_Open(queue)
        t_2.setDaemon(True)
        t_2.start() 

    elif (check == True)&(Init.mode_state.get() == "replaymode") :
        t_3 = Thread_Draw_Trace(queue)
        t_3.setDaemon(True)
        t_3.start()

    else :
        print "not choice mode error"



   

#-----------------------------------------------------------------------------------#
#                                   Thread_1                                        #
#-----------------------------------------------------------------------------------#

class Thread_Draw_Algorithm(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue




    def run(self):

        global c_scene, f_result
        global node, run_number
        
        
        server = Socket_Set.Setting("server")
        client = Socket_Set.Setting("client")


        now = time.localtime()              # create file
        filename = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+str(now.tm_hour)+str(now.tm_min)+str(now.tm_sec)
        save_file = open("MobilitySimulation_"+filename+".txt",'a')

        for x in range(Init.area_side):         # create to presentation reconnaissance area
            recona_range.append([0] * Init.area_side)
                    

        for i in range(Init.node_num):      #Node Initialization
            node.append(Node(Init.nodedraw_name[i], Init.noderange_name[i], Init.node_color[i], 0, 0, 0, 0, 0, 0))
            node[i].nodedraw_name = c_scene.create_oval(node[i].current_x - 2, node[i].current_y - 2, node[i].current_x + 2, node[i].current_y + 2, fill = node[i].node_color)
            node[i].noderange_name = c_scene.create_oval(node[i].current_x - Init.com_range, node[i].current_y - Init.com_range, node[i].current_x + Init.com_range, node[i].current_y + Init.com_range)        

        for i in range(Init.node_num):
            print node[i].nodedraw_name

        time.sleep(3)

        while True:
            time.sleep(0.05)
            client.sendto("asdf",(Socket_Set.IP, Socket_Set.SENDPORT))
            s, addr = server.recvfrom(1024)
            
            #queue.put(s)
            Socket_Set.Data_Split(s, node, Init.node_num)

            Analysis.Spatial_Dependence_Cal(node, dependence_table, Init.node_num, Init.com_range)
           
            for i in range(Init.node_num):
                c_scene.create_oval(node[i].current_x - 2, node[i].current_y - 2, node[i].current_x + 2, node[i].current_y + 2, fill = node[i].node_color, outline = node[i].node_color) 
                c_scene.coords(node[i].noderange_name, node[i].current_x - Init.com_range, node[i].current_y - Init.com_range, node[i].current_x + Init.com_range, node[i].current_y + Init.com_range)
                
                cover_value = Analysis.Cover_Cal(recona_range, node[i].current_x, node[i].current_y, Init.cov_range, Init.area_side, run_number)                
                
            if run_number % 10 == 0 :
                first_table_percent = Init.first_table_y - cover_value * 100 * 2
                Analysis.First_Table_Draw(f_result, Init.first_table_x, first_table_percent, Init.first_table_prex, Init.first_table_prey, cover_value, Init.cov_per_val)
                Analysis.Second_Table_Draw(f_result, Init.second_table_x, Init.second_table_y, dependence_table, Init.node_num)
                Init.first_table_prex = Init.first_table_x
                Init.first_table_x += 1
                Init.first_table_prey = first_table_percent

            for i in range(Init.node_num):
                #save_data = Init.nodedraw_name[i] + "." + node[i].current_x + "." + str(node[i].current_y)
                save_data = "%d.%d.%d\n" % (node[i].nodedraw_name, node[i].current_x, node[i].current_y)
                save_file.write(save_data)                

            run_number += 1
            c_scene.update()

        save_file.close
            




#-----------------------------------------------------------------------------------#
#                                   Thread_2                                        #
#-----------------------------------------------------------------------------------#


class File_Open(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        Init.Open_File()
        




#-----------------------------------------------------------------------------------#
#                                   Thread_3                                        #
#-----------------------------------------------------------------------------------#


class Thread_Draw_Trace(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue



    def run(self):

        global c_scene, f_result
        global node, run_number

        a_max = 0
        b_max = 0

        trace_file = open("gpsdata.txt","r")
        
               
        
        for x in range(Init.area_side):         # create to presentation reconnaissance area
            recona_range.append([0] * Init.area_side)
                    

        for i in range(Init.node_num):
            node.append(Node(Init.nodedraw_name[i], Init.noderange_name[i], Init.node_color[i], 0, 0, 0, 0, 0, 0))
            node[i].nodedraw_name = c_scene.create_oval(node[i].current_x - 2, node[i].current_y - 2, node[i].current_x + 2, node[i].current_y + 2, fill = node[i].node_color)
            node[i].noderange_name = c_scene.create_oval(node[i].current_x - Init.com_range, node[i].current_y - Init.com_range, node[i].current_x + Init.com_range, node[i].current_y + Init.com_range)        


        while True:
            time.sleep(0.05)            
            
            data=trace_file.readline()
            temp = data.split(",")
            if not data : break
        
            if(temp[2]>a_max):
                a_max=temp[2]
            if(temp[4]>b_max):
                b_max=temp[4]

            print temp[2], temp[4]


            client.sendto("asdf",(Socket_Set.IP, Socket_Set.SENDPORT))
            s, addr = server.recvfrom(1024)
            
            #queue.put(s)
            data = Socket_Set.Data_Split(s, node, Init.node_num)

            Analysis.Spatial_Dependence_Cal(node, dependence_table, Init.node_num, Init.com_range)
           
            for i in range(Init.node_num):
                c_scene.create_oval(node[i].current_x - 2, node[i].current_y - 2, node[i].current_x + 2, node[i].current_y + 2, fill = node[i].node_color, outline = node[i].node_color) 
                c_scene.coords(node[i].noderange_name, node[i].current_x - Init.com_range, node[i].current_y - Init.com_range, node[i].current_x + Init.com_range, node[i].current_y + Init.com_range)

                cover_value = Analysis.Cover_Cal(recona_range, node[i].current_x, node[i].current_y, Init.cov_range, Init.area_side, run_number)                
                
            if run_number % 10 == 0 :
                first_table_percent = Init.first_table_y - cover_value * 100 * 2
                Analysis.First_Table_Draw(f_result, Init.first_table_x, first_table_percent, Init.first_table_prex, Init.first_table_prey, cover_value, Init.cov_per_val)
                Analysis.Second_Table_Draw(f_result, Init.second_table_x, Init.second_table_y, dependence_table, Init.node_num)
                Init.first_table_prex = Init.first_table_x
                Init.first_table_x += 1
                Init.first_table_prey = first_table_percent
                

            run_number += 1

            c_scene.update()

        trace_file.close()









#-----------------------------------------------------------------------------------#
#                                     test                                          #
#-----------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------#
#                                     Main                                          #
#-----------------------------------------------------------------------------------#

master = Tk()
master.title("Mobility Model Simulation")

menubar = Init.Init_Filemenu(master)
f_menu = Init.Init_Framemenu(master)
c_scene = Init.Init_Framescene(master) 
f_result = Init.Init_Frameresult(master)  
   



Button(f_menu, text='start', fg = "black", width = 12, height = 1, command = Thread_Run).grid(row = 0, column = 8, padx =8, pady = 10, sticky = S) #rowspan = 2
Button(f_menu, text='stop', fg = "black", width = 12, height = 1, command = f_menu.quit).grid(row = 1, column = 8, padx =8, pady = 10, sticky = N)
        


mainloop()


