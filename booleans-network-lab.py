import netmiko

ip_list = [#'192.168.1.211',
    '192.168.1.212',
    #'192.168.1.213'
    ]

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = 22

def get_ip_int_br(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, username=username, password=password, port=port)
    return net_connect.send_command('show ip interface br')

ip_3_octets = '192.168.1.'
ip_last_octet = 211

while ip_last_octet <= 213:
    ip = ip_3_octets +str(ip_last_octet)
    ip_int_br = get_ip_int_br(ip)
    if len(ip_int_br) > 0:
        contains_text = True
    if ip in ip_list and contains_text:
        print('IP interface from ' + ip)
        print(ip_int_br)
        print('_' * 80)
    ip_last_octet += 1