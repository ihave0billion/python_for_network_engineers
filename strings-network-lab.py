import netmiko

csr1kv1 = '192.168.1.211'
csr1kv2 = '192.168.1.212'
csr1kv3 = '192.168.1.213'

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = 22

# The ip inside def get_log(ip): is a parameter. It's a placeholder name that gets bound to whatever value you pass in when you call the function.
#  It doesn't need to be defined anywhere else because the function call itself defines it.

def get_log(ip):
    net_connect = netmiko.ConnectHandler(ip=ip,device_type=device_type, username=username, password=password, port=port)
    return net_connect.send_command('show log')

#these 3 variables will hold the value returned by get_log()

csr1kv1_log = get_log(csr1kv1)
csr1kv2_log = get_log(csr1kv2)
csr1kv3_log = get_log(csr1kv3)

print(csr1kv1_log)
print(csr1kv2_log) 
print(csr1kv3_log)