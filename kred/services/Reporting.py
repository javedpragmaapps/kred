import requests

class Reporting:
    # @history function calls GET api to Get NFT or user history.
    # the model used is from  HistoryModel
    # The function returns ' '
    def history(self,model):
        return str(model.nft) + ' history is'

    # @ledger function calls GET api to Get user's transaction ledger.
    # count and page are the required parameters
    # The function returns ' '
    def ledger(self,user,count,page):
        return 'transaction ledger'

    # @given function calls GET api to Get history of NFTs given.
    # The model used is HistoryModel
    # count and page are the required parameters
    # The function returns ' '
    def given(self,model):
        return 'History of the model'

    # @leaders function calls GET api List top users by NFT ownership, creation, or circulation.
    # The model used is LeadersModel
    # count and page are the required parameters
    # The function returns ' '
    def leaders(self,model):
        return 'filtered by ' + model.mode

    # @popular_tag function calls GET api  List recent popular tags.
    # count is the required parameter
    # The function returns ' '
    def popular_tag(self,days,count):
        return  'popular tags since the past ' + str(days) + ' days'

    # @trending_tag function calls GET api  List curent trending tags..
    # count is the required parameter
    # The function returns ' '
    def trending_tags(self,days,count):
        return 'Trending tags since the past ' + str(days) + ' days'

    # @tagcount function calls GET api to  Get counts for all tags or a specified set of tags..
    # The function returns ' '
    def tagcount(self,tag):
        return 'couts for the tag give is'
