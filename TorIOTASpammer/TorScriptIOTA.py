import iota
from iota import *
from iota.adapter.wrappers import RoutingWrapper

print("")

address = 'Random Adress Here'


api =\
Iota(
  # Send PoW requests to local node.
  # All other requests go to light wallet node.
  RoutingWrapper('https://nodes.thetangle.org:443')
    .add_route('attachToTangle', 'https://nodes.thetangle.org:443'),

  # Seed used for cryptographic functions.
  seed = b'Random Seed Here'
)

pt = iota.ProposedTransaction(address = iota.Address(address),
                            message = iota.TryteString.from_unicode('Your Text Here'),
                            tag     = iota.Tag(b'Your Tag Here'),
                            value   = 0)




FinalBundle = api.send_transfer(depth=3,
                              transfers=[pt],
                              min_weight_magnitude=14)
print("")
print("1 More.")
