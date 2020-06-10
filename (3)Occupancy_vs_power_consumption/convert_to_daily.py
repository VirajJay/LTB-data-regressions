'''
Written by Viraj Jayasinghe
'''

import string
import sys

if __name__=="__main__":
    fid=open('Main incomers Bld 92_2020-03-23-16-23-02.csv', 'r')
    power=fid.readlines()
    fid.close()

    fid=open('Clients-connected-to-WiFi-during-February-LTB-Ground.csv','r')
    clients=fid.readlines()
    fid.close()

    power_new=[]
    clients_new=[]

    #pre process the main incomes data
    for i in range(len(power)):
        power_new.append(power[i].split(','))
        power_new[-1][-1]=power_new[-1][-1].split('\n')[0]

    #pre process the wifi clients data
    for i in range(len(clients)):
        clients_new.append(clients[i].split(','))
        clients_new[-1][-1] = clients_new[-1][-1].split('\n')[0]

    ref_date=power_new[1][0][0:2]

    ref_1=power_new[1][32]
    ref_2=power_new[1][72]
    ref_3=power_new[1][92]

    #first, process the power data from main incomers
    power=[]
    for i in range(1, len(power_new)):
        if(power_new[i][0][0:2]!=ref_date):
            ref_date=power_new[i][0][0:2]
            power.append([float(power_new[i-1][32])-float(ref_1), float(power_new[i-1][72])-float(ref_2), float(power_new[i-1][92])-float(ref_3)])
            ref_1 = power_new[i][32]
            ref_2 = power_new[i][72]
            ref_3 = power_new[i][92]

    #now, process the wifi clients data
    ref_date=clients_new[1][0][8:10]
    tmp=0
    clients=[]
    count_clients=0
    for i in range(1, len(clients_new)):
        if(clients_new[i][0][8:10]==ref_date):
            tmp+=int(clients_new[i][1])
            count_clients=count_clients+1
        else:
            ref_date=clients_new[i][0][8:10]
            clients.append(tmp/count_clients)
            count_clients=1;
            tmp=int(clients_new[i][1])

    print(clients)

    #print out everything on a string and send it to the local drive on a csv file
    out_str="date,users(daily),level_1,level_2,level_3\n"
    for i in range(len(clients)):
        out_str+="{},{},{},{},{}\n".format(i+1, clients[i], power[i][0], power[i][1], power[i][2])

    fid=open('output.csv', 'w')
    fid.write(out_str)
    fid.close()

    #print(clients_new)





