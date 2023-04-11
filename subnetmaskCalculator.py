# the script gives you the subnet mask, NetworkID and broadcast based
# on the number of hosts you require.

bit_values = (128,64,32,16,8,4,2,1)

def host_scale(host):
   scale = 0
   while host>1:
     host //= 2
     scale = scale + 1
   return scale

def subnet_mask(host,n_class):
  s_mask = [255,0,0,0]
  network_id = []
  broadcast = []
  if n_class == 'A':
    network_id.append(10)
    broadcast.append(10)
  elif n_class == 'B':
    network_id.append(172)
    broadcast.append(172)
  elif n_class == 'C':
    network_id.append(192)
    broadcast.append(192)

  scale = 32 - host_scale(host)
  cidr = f'/{scale}'
  return {
	 "Subnet Mask: ":s_mask,
	 "Network ID: ": network_id,
	 "Broadcast: " : broadcast,
	 "CIDR: " : cidr
}
print("Enter the number of hosts needed:[Numeric Value]")
hosts = int(input())
print("Enter the network class:[A,B or C] ")
n_class = input()

print(subnet_mask(hosts, n_class))
