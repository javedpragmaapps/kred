import requests



class Nft:

    # @mint function calls POST api to Mint a batch of NFTs
    # the model used is from  MintModel
    # name and count are required parameters
    # The function returns a json
    def mint(self, model):

        # written a code for making a http request
        return "Values has been set on the models and the nft id is"

    # @draft function calls  POST api Design a new NFT.
    # the model used is from  DraftModel
    # name and count are required parameters
    # The function returns a json
    def draft(self, model):

        # written a code for making a http request to mark NFT as draft
        # return the data
        return "Nft mark as draft"

    # @edit function calls  POST api to Edit an existing NFT.
    # the model used is from  EditModel
    # The function returns a json
    def edit(self, model):

        # written a code for making a http request to get edit the NFT based on the batch
        # return the data
        return "Nft batch has been edit successfully"

    # @upload function calls POST api to Upload image assets.
    # The function returns " "
    def upload(self,name,content):
        # written a code for making a http request to save the images in base64 format
        # return the data
        # return array.get("name")
        return  name+" image has been uploaded"

    # @nft function calls  GET api Get NFT details.
    # the model used is from NftModel
    # The function returns " "
    def nft(self, model):


        return 'response is '

    # @nfts function calls  GET api List NFTs.
    # the model used is from NftsModel
    # The function returns " "

    def nfts(self, model):


        return 'All details'

    # @data function calls  GET api to Get NFT metadata in ERC721 compatible format.
    # user id is required
    # The function returns " "
    def data(self,id):

        return 'metadata for id is '+ str(id)
