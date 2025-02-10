import netmiko

ip_3_octets = '192.168.1.'
ip_last_octet = 211

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = 22

def get_ip_int_br(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, username=username, password=password, port=port)
    return net_connect.send_command('show ip interface br')

#look runs indented code repeatedly until value of ip_last_octet is greater than 213

#str() converts ip_last_octet from integer to a string
while ip_last_octet <= 213:
    ip = ip_3_octets + str(ip_last_octet)
    ip_int_br = get_ip_int_br(ip)
    print(ip_int_br)
    print('_' * 80)
    ip_last_octet += 1

#print '_' * 80 creates a diver between outputs
# special charater += is used in python to increase an integer's value and store new value back in the same variable
