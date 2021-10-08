import requests
class BuyingAndSelling:
    # @sales function calls GET api to List sales.
    # the model used is from  SalesAndMarketplaceModel
    # count and page are the required parameters
    # The function returns ' '
    def sales(self,model):
        return "showing " + str(model.count) +' responses for '+ model.user

    # @auctions function calls GET api to List auctions.
    # the model used is from  AuctionsModel
    # count and page are the required parameters
    # The function returns ' '
    def auctions(self,model):
        return 'listing auctions  for user ' + model.user

    # @marketplace function calls GET api to List sales and auctions together.
    # the model used is from  SalesAndMarketplaceModel
    # count and page are the required parameters
    # The function returns ' '
    def marketplace(self,model):
        return 'Listing sales and auctions for '+ model.user

    # @sell function calls POST api to Sell an NFT.
    # the model used is from  SellModel
    # nft and price are the required parameters
    # The function returns ' '
    def sell(self,model):
        return str(model.nft) + ' sold for price '+ str(model.price)

    # @auction function calls POST api to Auction an NFT.
    # the model used is from  Auction
    # mode,nft and start are the required parameters
    # The function returns ' '
    def auction(self,model):
        return str(model.mode)+' Auction set for '+ str(model.nft)

    # @buy function calls POST api to Buy an NFT.
    # nft is the required parameters
    # The function returns ' '
    def buy(self,nft):
        return str(nft)+ ' nft bought'

    # @bid function calls POST api to Bid on an auction.
    # auction and price are the required parameters
    # The function returns '
    def bid(self,auction,price):
        return 'auction subbmited  for '+ auction + ' worth '+ str(price)

    # @cancel function calls POST api to Cancel a sale or auction.
    # The function returns '
    def cancel(self,auction,sale,text):
        return  'sale id '+ sale + ' has been cancelled because ' + text


    # @showcase function calls POST api to Showcase an NFT.
    # the model used is from  ShowcaseAndUnshowcaseModel
    # The function returns ' '
    def showcase(self,model):
        return 'Showcasing nft ' + str(model.nft)

    # @unshowcase function calls POST api to UnShowcase an NFT.
    # the model used is from  ShowcaseAndUnshowcaseModel
    # The function returns ' '
    def unshowcase(self,model):
        return 'Unshowcasing nft ' + str(model.nft)

    # @can_showcase function calls POST api to Check if user is authorised to maintain the showcase.
    # The function returns ' '
    def can_showcase(self):
        return 'The user can showcase'

    # @tag function calls POST api to Tag a NFT.
    # the model used is from  TagModel
    # tags is required parameter
    # The function returns ' '
    def tag(self,model):
        return "tag added to " + str(model.nft)

    # @lock function calls POST api to Lock a NFT.
    # the model used is from  LockAndUnlockModel
    # The function returns ' '
    def lock(self,model):
        return str(model.nft) + " has been locked"

    # @unlock function calls POST api to  UnLock a NFT.
    # the model used is from  LockAndUnlockModel
    # The function returns ' '
    def unlock(self,model):
        return str(model.nft) + ' has been unlocked'

    # @hide function calls POST api to  Hide a NFT or request.
    # the model used is from  HideAndShow
    # The function returns ' '
    def hide(self,model):
        return str(model.nft) + ' has been hidden'

    # @show function calls POST api to  show a NFT or request.
    # the model used is from  HideAndShow
    # The function returns ' '
    def show(self,model):
        return str(model.nft) + ' is been  show'
