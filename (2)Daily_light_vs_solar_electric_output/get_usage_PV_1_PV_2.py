import string
import sys

if __name__=="__main__":
    fid=open('PV 1 _ 2 Data Feb 2020_2020-03-23-16-16-04.csv', 'r')
    data_str=fid.readlines()
    fid.close()

    data=[]
    for i in range(len(data_str)):
        data.append(data_str[i].split(','))

    #get the load value per day
    print(data[0][25])
    ref_val=data[1][9]
    ref_val_2=data[1][25]
    output=[]
    for i in range(1, len(data)-1):
        if(data[i+1][0][0:2]!=data[i][0][0:2]):#if different day
            output.append([float(data[i][9])-float(ref_val), float(data[i][25])-float(ref_val_2)])
            ref_val=data[i][9]
            ref_val_2=data[i][25]

    out_str="PV_1_LV_LTB_1_92,PV_2_LV_LTB_2_92\n"
    for i in range(len(output)):
        out_str=out_str+"{},{}\n".format(output[i][0], output[i][1])
    fid=open('output_panel_energy_used.csv', 'w')
    fid.write(out_str)
    fid.close()


