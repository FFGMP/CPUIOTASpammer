import requests
import os
import iota
import random
import time
from iota import *
from iota.adapter.wrappers import RoutingWrapper
from random import shuffle

while True:
    text_file = "/proxys.txt"
    text_file_newip = "/text_new_ip.txt"
    file = open(text_file, "r")
    file_new = open(text_file_newip, "r")
    varia = []
    newvaria = []
    for line in file:
        varia.append(line)

    for x in varia:
        newvaria.append(x.replace("A","").replace("B","").replace("C","").replace("D","").replace("E","").replace("F","").replace("G","").replace("H","").replace("I","").replace("J","").replace("K","").replace("L","").replace("M","").replace("N","").replace("O","").replace("P","").replace("Q","").replace("R","").replace("S","").replace("T","").replace("U","").replace("V","").replace("X","").replace("Y","").replace("Z","").replace("+","").replace("-","").replace("!","").replace("W","").replace(" ",""))



    with open('text_new_ip.txt', 'w') as f:
        for item in newvaria:
            f.write(item)

    for line in file:
        varia.append(line)

    Number = 0

    for line in file_new:
        try:
            mystring = str(line)
            proxy = mystring
            proxy = proxy.rstrip()
            os.environ['http_proxy'] = proxy
            os.environ['HTTP_PROXY'] = proxy
            os.environ['https_proxy'] = proxy
            os.environ['HTTPS_PROXY'] = proxy
            print("")

            address = 'ADDRESS'


            api =\
            Iota(
                # Send PoW requests to local node.
                # All other requests go to light wallet node.
                RoutingWrapper('https://nodes.thetangle.org:443')
                .add_route('attachToTangle', 'https://nodes.thetangle.org:443'),

                # Seed used for cryptographic functions.
                seed = b'YOUR SEED HERE'
                )

            pt = iota.ProposedTransaction(address = iota.Address(address),
                                message = iota.TryteString.from_unicode('MESSAGE'),
                                tag     = iota.Tag(b'TAG'),
                                value   = 0)




            FinalBundle = api.send_transfer(depth=2,
                                    transfers=[pt],
                                    min_weight_magnitude=14)


            Number += 1
            print("")
            print Number , "Transactions."

        except:
            print ('Error\n')
