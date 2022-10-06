#%%
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"Data\data_lapack_wifi.csv", delimiter=',')
df.set_index(['No.'], inplace=True, drop=True)
index=df.index

#print(df['Time'].dtypes)
print(df)

#Number of rows and columns in file
num_rows = len(index)
num_columns = len(df.columns)
print("Number of rows : " , num_rows)
print("Number of columns : " , num_columns)

# Time between first and last packet
first_time=df['Time'].iloc[0] # first element 
last_time=df['Time'].iloc[-1] # last element 

time_diff=last_time-first_time
print('Time between first and last packet : ' , time_diff)

# Average time between packets - maybe not relevant the way its done right now, see avg_time_arrival below
# avg_time=time_diff/num_rows
# print('Average time between packets : ' , avg_time)

# Standard deviation of arrival time
# ADJUST start/end depending on the data!!!
start=1
end=num_rows-3
list_time=df['Time']
list_source=df['Source']
std_time=0
length_list=len(list_time)
arrival_time_source = np.zeros((length_list, 1))
arrival_time_destination = np.zeros((length_list, 1))
last_source=list_time.iloc[start]
last_destination=list_time.iloc[start]

number_source=0
number_destination=0

for x in range(start,end):
    if list_source.iloc[x]=="192.168.0.137":
        arrival_time_destination[x] = list_time.iloc[x]-last_destination
        last_destination=list_time.iloc[x]
        number_destination=number_destination+1
    elif list_source.iloc[x]=="160.36.131.221":
        arrival_time_source[x] = list_time.iloc[x]-last_source
        last_source=list_time.iloc[x]
        number_source=number_source+1


print('Number of arrivals : ' , number_source)
print('Number of departures : ' , number_destination)

avg_time_arrival_source=np.mean(arrival_time_source)
print('Average time between arrivals from the source : ' , avg_time_arrival_source)
avg_time_arrival_destination=np.mean(arrival_time_destination)
print('Average time between departures : ' , avg_time_arrival_destination)

std_time_source=np.std(arrival_time_source)
print('Standard deviation of arrival time from the source : ' , std_time_source)
std_time_destination=np.std(arrival_time_destination)
print('Standard deviation of departure time : ' , std_time_destination)

# Variance of  times
variance_time_source=std_time_source*std_time_source
print('Variance of arrival time from the source : ' , variance_time_source)
variance_time_destination=std_time_destination*std_time_destination
print('Variance of departure time : ' , variance_time_destination)

# Average size of packet
total_pkt_size=df['Length'].sum()
average_pkt_size=total_pkt_size/num_rows
print('Average packet size : ' , average_pkt_size)

# Plot of arrival time
plt.hist(arrival_time_source[range(0,number_source)],bins=300,range=(-0.0000001,0.002),label="Arrival time")
#plt.title('Arrival time of packets from the source')
#plt.show()

# Plot of departure time
plt.hist(arrival_time_destination[range(0,number_destination)],bins=300,range=(-0.0000001,0.002),label="Departure time")
plt.title('Departure and arrival time of packets')
plt.legend(loc="upper right")
plt.savefig('exp3_packettime_hist_wifi', format='eps')
plt.show()


#Number of TCP or HTTP or UDP packets
number_tcp=0
number_http=0
number_udp=0
number_arp=0
number_tls=0
number_mdns=0
number_ieee=0
i=0
list_protocols=df['Protocol']

for x in list_protocols:
    if x=="HTTP":
        number_http=number_http+1
    elif x=="UDP":
        number_udp=number_udp+1
    elif x=="TCP":
        number_tcp=number_tcp+1
    elif x=="ARP":
        number_arp=number_arp+1
    elif x=="TLSv1.2":
        number_tls=number_tls+1
    elif x=="MDNS":
        number_mdns=number_mdns+1
    elif x=="ieee1905":
        number_ieee=number_ieee+1


print('Number of HTTP packets : ' , number_http)
print('Number of TCP packets : ' , number_tcp)
print('Number of UDP packets : ' , number_udp)
print('Number of ARP packets : ' , number_arp)
print('Number of TLS packets : ' , number_tls)
print('Number of MDNS packets : ' , number_mdns)
print('Number of IEEE packets : ' , number_ieee)