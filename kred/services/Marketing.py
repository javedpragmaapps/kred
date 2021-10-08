import requests
class Marketing:
    # @redeem function calls POST api to Redeem an NFT for a reward.
    # nft is the required parameter
    # The function returns ' '
    def redeem(self,nft):
        return 'Nft '+ nft + ' has been redeemed'

    # @unredeem function calls POST api to Mark a previously redeemed NFT you created as redeemable again.
    # nft is the required parameter
    # The function returns ' '
    def unredeem(self,nft):
        return 'Nft ' + nft + ' is redeemabled again'

    # @payload function calls POST api to Add a one-time payload to an existing NFTn.
    # nft and payload are the required parameter
    # The function returns ' '
    def payload(self,nft,payload):
        return  'Nft '+ nft + ' added payload ' + payload

    # @consume function calls POST api to Consume a payload from an existing NFT.
    # nft is required parameter
    # The function returns ' '
    def consume(self,nft):
        return 'payload consume from ' + nft
