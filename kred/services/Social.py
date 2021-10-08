import requests
class Social:
    # @post function calls POST api to Post a message.
    # the model used is from  PostModel
    # text is the required parameters
    # The function returns ' '
    def post(self,model):
        #Request
        return 'Message post for nft id ' + str(model.nft)

    # @post function calls POST api to Reply to a message.
    # the model used is from  ReplyAndCommentModel
    # text and message are the required parameters
    # The function returns ' '
    def reply(self,model):
        #Request
        return 'The reply is '+ str(model.text)

    # @comment function calls POST api to Comment on a message.
    # the model used is from  ReplyAndCommentModel
    # text and message are the required parameters
    # The function returns ' '
    def comment(self,model):
        #Request
        return 'The comment text is ' + (model.message)

    # @remove function calls POST api to Remove a message.
    # the model used is from  RemoveModel
    #  message is the required parameter
    # The function returns ' '
    def remove(self,model):
        return "The message is removed for " + (model.message)

    # @message function calls GET api to Get NFT messages.
    # the model used is from  Messages
    #  count and page are the required parameters
    # The function returns ' '
    def messages(self,model):
        return 'Following are the nft messages'

    # @memberships function calls GET api to Get user memberships.
    #  count and page are the required parameters
    # The function returns ' '
    def memberships(self,user,details):
        return  "Get user membership?" + str(details)

    # @like function calls POST api to Like an NFT or message.
    # the model used is from  LikeAndUnlike
    # The function returns ' '
    def like(self,model):
        return 'Nft liked for nft uuid '+ str(model.uuid)

    # @unlike function calls POST api to UnLike an NFT or message.
    # the model used is from  LikeAndUnlike
    # The function returns ' '
    def unlike(self,model):
        return  'Nft unliked for message id ' + model.message

    # @ban function calls POST api to Ban a user from a message stream..
    # the model used is from  BanAndUnBan
    # user is the required parameter
    # The function returns ' '
    def ban(self,model):
        return  model.user + " has been banned"

    # @unban function calls POST api to UnBan a user from a message stream..
    # the model used is from  BanAndUnBan
    # user is the required parameter
    # The function returns ' '
    def unban(self,model):
        return  model.user + " has been unbanned"

    # @feed function calls GET api to List user's available push notification feeds.
    # The function returns ' '
    def feed(self):
        return 'user feed'

