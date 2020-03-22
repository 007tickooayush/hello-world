import sys
import random

#Application part-1

def subnet_calc():
    try:
        print("\n")

        #checking IP address validity
        while True:
            ip_address = input("Enter an IP address: ")

            ip_octets = ip_address.split('.')

            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            else:
                print("The IP address {} is invalid. Please check and try again...".format(ip_address))
                continue
        masks = [255,254,252,248,240,224,192,128,0]

        #checking mask validity
        while True:
            subnet_mask = input("Enter a subnet mask: ")

            #verifying octets 
            mask_octets = subnet_mask.split('.')

            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            else:
                print("Subnet mask {} is invalid. Please check and try again...".format(subnet_mask))
                continue

#Application part-2

        #Algorithm for subnet dneification based on IP and subnet mask
        #converting mask to binary string
        mask_octets_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            #print(binary_octet)

            mask_octets_binary.append(binary_octet.zfill(8))
        
        #print(mask_octets_binary)
        
        binary_mask = "".join(mask_octets_binary)
        #print(decimal_mask)
        #E.g :- 255.255.255.0 => 11111111111111111111111100000000

        #Counting host bits in mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2**no_of_zeros - 2)  #abs for gettinh th positive value for /32 bit mask 

        #print(no_of_zeros)
        #print(no_of_ones)
        #print(no_of_hosts)

        #Obtaining a wildcard mask
        wildcard_octets = []
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))

        #print(wildcard_octets)

        wildcard_mask = ".".join(wildcard_octets)
        #print(wildcard_mask)

#Application part-3

        #Converting ip to binary string
        ip_octets_binary = []

        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            ip_octets_binary.append(binary_octet.zfill(8)) 

        #print(ip_octets_binary)
        binary_ip = "".join(ip_octets_binary)

        #print(binary_ip)
        #E.g :- 192.168.0.1 => 11000000101010000000101000000001

        #Getting network address and broadcast address from te binay string obtained from above 
        network_address_binary = binary_ip[:(no_of_ones)] + "0"*no_of_zeros # .zfill(32) is also valid here
        #print(network_address_binary)

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1"*no_of_zeros
        #print(broadcast_address_binary)

        #Converting everthing back to readable format (Decimal format)
        net_ip_octets = []

        #getting each 8-bit octet using range(0,32,8), i.e, step of 8
        for bit in range(0,32,8):
            net_ip_octet = network_address_binary[bit:bit + 8]
            net_ip_octets.append(net_ip_octet)
        
        #Reslt will be 4 silces of binary IP address : [0:8] , [8:16], [16:24], [24:32]

        #print(net_ip_octets)

        net_ip_address = []

        #Converting fom a base of 2 to integer to a string. -> str(int(each_octet,2))
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet,2))) 

        #print(net_ip_address)

        network_address = ".".join(net_ip_address)
        #print(nework_address)

        bst_ip_octets = []

        #getting each 8-bit octet using range(0,32,8), i.e, step of 8
        for bit in range(0,32,8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)
        #print(bst_i_octets)

        bst_ip_address = []

        for each_octet in bst_ip_octets:
                bst_ip_address.append(str(int(each_octet,2)))
        
        #print(bst_ip_address)
        
        broadcast_address = ".".join(bst_ip_address)
        #print(broadcast_address)

        #Results for selected mask/IP
        print("\n")
        print("Network address is: %s"%network_address)
        print("Broadcast addres is: %s"%broadcast_address)
        print("No of hosts: %s"%no_of_hosts)
        print("No of mask bits: %s"%no_of_ones)
        print("Wildcard mask: %s"%wildcard_mask)
        print("\n")

#Application part-4

        while True:
            generate = input("Generate IP address from this subnet mask? (y/n)")

            if generate == "y":
                generated_ip = []
                
                #Obtaining the available IP address in range, based on the difference between octetsand network address
                for indexb, oct_bst  in enumerate(bst_ip_address):
                    #print(indexb, oct_bst)
                    for indexn, oct_net in enumerate(net_ip_address):
                        #print(indexn, oct_net)
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                #Add identical ip octets to the generated_ip list
                                generated_ip.append(oct_bst)
                            else:
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

                #IP address generated from the subnet pool
                #print(generated_ip)

                y_iaddr = ".".join(generated_ip)
                #print(y_iaddr)

                print("Random IP address is %s"%y_iaddr)
                print("\n")
                continue
            else:
                print("Bye...")
                break
    except KeyboardInterrupt:
        print("\n\nProgram Aborted by user.Exiting...")
        sys.exit()

#calling the function
subnet_calc()

#End of program
