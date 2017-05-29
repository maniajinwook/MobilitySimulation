from Tkinter import *
import math



def First_Table_Draw(f_result, x, y,pre_x, pre_y, cover_value, cov_per_val):
    #cover_value *= 100
    cover_value = round(cover_value*100, 2)
    f_result.create_line(pre_x, pre_y, x, y, fill = "red", width = 2, smooth = 1)
    f_result.itemconfigure(cov_per_val, text = cover_value)
    
    







def Second_Table_Draw(f_result, x, y, dependence_table, node_num) :

    for i in range(node_num) :
        value = y - dependence_table[i] / 10
        f_result.create_rectangle(x, value, x+25, y, fill = "red")
        x += 100
    





def Cover_Cal(recona_range, x, y, com_range, map_pixel, run_number):
    global table_x, table_y
    count = 0

    a = int(com_range / 2)
    b = int(com_range / 2)
    for i in range(com_range):             #reconnaissance range enter in array
        for j in range(com_range):
            if (x-a >= map_pixel) | (y-b >= map_pixel) | (x-a < 0) | (y-b < 0) :
                b-=1
                continue
            recona_range[x-a][y-b] = 1
            b-=1
        a-=1
        b = int(com_range / 2)
    #end for i
    

    if run_number % 10 == 0 :
        for i in range(map_pixel) :           #reconnaissance range search
            for j in range(map_pixel) :
                if recona_range[i][j] == 1 :
                    count += 1
        
        return float(count)/(map_pixel*map_pixel)
        #print count, float(count)/490000
        
            



def Spatial_Dependence_Cal(node, dependence_table, node_num, communication_range) :
    
    communication_range *= 2

    for i in range(0, node_num, 1) :
        for j in range(i+1, node_num, 1) :
            dist = math.sqrt(((node[i].current_x - node[j].current_x) * (node[i].current_x - node[j].current_x)) + ((node[i].current_y - node[j].current_y) * (node[i].current_y - node[j].current_y)))
            #print "i : ", i, "j : ", j,"dist : ", dist
            if dist < communication_range :
                dependence_table[i] += 1
                dependence_table[j] += 1
        j += 1
