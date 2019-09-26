import iota
from iota import *
from iota.adapter.wrappers import RoutingWrapper

while True:

  print("")

  address = 'RANDOM ADDRESS'


  api =\
  Iota(
    # Send PoW requests to local node.
    # All other requests go to light wallet node.
    RoutingWrapper('https://nodes.thetangle.org:443')
      .add_route('attachToTangle', 'https://nodes.thetangle.org:443'),

    # Seed used for cryptographic functions.
    seed = b'RANDOM SEED'
  )
  
  FinalBundle = api.replay_bundle(transaction='OLD TRANSACTION ADDRESS',
                                depth=3,
                                min_weight_magnitude=14)
  print("")
  print("1 More.")

