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
    RoutingWrapper('PUBLIC NODE')
      .add_route('attachToTangle', 'http://localhost:14265'),

    # Seed used for cryptographic functions.
    seed = b'RANDOM SEED HERE'
  )

  pt = iota.ProposedTransaction(address = iota.Address(address),
                              message = iota.TryteString.from_unicode('SOME MESSAGE'),
                              tag     = iota.Tag(b'SOME TAG'),
                              value   = 0)




  FinalBundle = api.send_transfer(depth=3,
                                transfers=[pt],
                                min_weight_magnitude=14)
  print("")
  print("1 More.")
