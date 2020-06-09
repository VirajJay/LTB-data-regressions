import string
import sys

if __name__=="__main__":
    fid=open('Solar PV 15min Feb 23032020.csv', 'r')
    content=fid.readlines();
    fid.close();

    data=[];

    for i in range(len(content)):
        data.append(content[i].split(','))
        data[-1][2]=data[-1][2].split('\n')[0]

    print(data)

    ref_date=data[1][0][0:2]
    pv_1_val=float(0);
    pv_2_val=float(0);
    final_vals=[]
    for i in range(1, len(data)):
        if(data[i][0][0:2]==ref_date):
            pv_1_val=pv_1_val+float(data[i][1])
            #print(float(data[i][1]))
            pv_2_val = pv_2_val + float(data[i][2])
        else:
            final_vals.append([ref_date, pv_1_val, pv_2_val])
            ref_date=data[i][0][0:2]
            pv_1_val=float(data[i][1])
            pv_2_val=float(data[i][2])
    final_vals.append([ref_date, pv_1_val, pv_2_val])#final date

    out_str="time,pv_1,pv_2\n"
    for i in range(len(final_vals)-1, -1, -1):
        out_str+="{},{},{}\n".format(final_vals[i][0], final_vals[i][1], final_vals[i][2])
    print(final_vals)

    fid=open('output.csv', 'w')
    fid.write(out_str)
    fid.close()