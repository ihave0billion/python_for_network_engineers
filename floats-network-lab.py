import netmiko

ip_base = '192.168.'
ip_end = 1.211
#1.211 is a float

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = 22

def get_ip_int_br(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, username=username, password=password, port=port)
    return net_connect.send_command('show ip interface br')

#convert ip_end from float to string

while ip_end <= 1.213:
    ip = ip_base + str(ip_end)   
    ip_int_br = get_ip_int_br(ip)   
    print(ip_int_br)   
    print('IP int from ' + ip)   
    print('_' * 80)   
    ip_end += .001
    ip_end = round(ip_end, 2)
  
#float addition in python is converted from faction to binary fractions, and needs to be fixed with round()function