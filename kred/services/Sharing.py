import requests
class Sharing:

    # @send function calls POST api to Send a NFT to another wallet.
    # the model used is from  SendModel
    # wallet is the required parameters
    # The function returns ' '
    def send(self,model):
        return 'nft sent to  wallet no '+ model.wallet

    # @hold function calls POST api to Hold a NFT for collection by an off-platform user.
    # the model used is from  HoldModel
    # platform and address are the required parameters
    # The function returns ' '
    def hold(self,model):
        #request
        return 'nft help for user '+ model.address+'on  platform '+ model.platform

    # @held function calls GET api to List held NFTs.
    # The function returns ' '
    def held(self,code,platform,address):
        return 'The following nfts are being held for ' + address

    # @collect function calls POST api to Collect an NFT.
    # code is the required parameter
    # The function returns ' '
    def collect(self,code,wallet,text):
        return "The nft has been collected"

    # @request function calls POST api to Request an NFT.
    # the model used is RequestModel
    # nft and wallet  is required parameter
    # The function returns ' '
    def request(self,model):
        return "Nft request for the nft id " + model.nft +' '+str(model.wallet)

    # @request function calls GET api to List requests.
    # the model used is RequestsModel
    # count and page  is required parameter
    # The function returns ' '
    def requests(self,model):
        return "requests model called"

    # @giveaway function calls POST Give away one or more NFTs via claim code.
    # batch  is required parameter
    # The function returns ' '
    def giveaway(self,batch,nfts,text,hours):
        return "given away nft using code " + batch

    # @claim function calls POST  api to Give away one or more NFTs via claim code.
    # code  is required parameter
    # The function returns '
    def claim(self,code,wallet,text):
        return text +' '+ code

    # @remind function calls GET api Give away one or more NFTs via claim code.
    # The function returns
    def remind(self,user,email,domain,sms):
        return 'here are the reminders'
