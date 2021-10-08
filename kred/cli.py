"""Console script for kred."""
import argparse
import sys
from services import Nft, Bundle,Social,Sharing,BuyingAndSelling,Authentication,Marketing,Reporting
from models import NftModels, BundleModels,SocialModel,SharingModels,BuyingAndSellingModels,ReportingModels,AuthenticationModels
from helpers import  Helper


def main():
    """Console script for kred."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    # args = parser.parse_args()

    # batch of nfts api call
    service = Nft.Nft()
    # mint_model = NftModels.MintModels()
    # mint_model.name='Cat nft'
    # mint_model.count=2
    # mint_model.type='card'
    # mint_model.layout='layout1'
    # mint_model.front='img.jpg'
    # mint_model.back='imgB.jpg'
    # mint_model.color='Red'
    # mint_model.pattern='prism'
    # mint_model.pattern_color='green'
    # mint_model.text_color='red'
    # mint_model.payload='payload'
    # mint_model.wrapper='wrapper'
    # mint_model.mesh=True
    # mint_model.nsfw=True
    # response = service.mint(mint_model)
    # print(response)


    # making a NFT draft api call
    # draft_model = NftModels.DaftModel()
    # draft_model.draft=2
    # draft_model.name = 'Cat nft'
    # draft_model.count = 2
    # draft_model.type = 'card'
    # draft_model.layout = 'layout1'
    # draft_model.front = 'img.jpg'
    # draft_model.back = 'imgB.jpg'
    # draft_model.color = 'Red'
    # draft_model.pattern = 'prism'
    # draft_model.pattern_color = 'green'
    # draft_model.text_color = 'red'
    # draft_model.payload = 'payload'
    # draft_model.wrapper = 'wrapper'
    # draft_model.mesh = True
    # draft_model.nsfw = True
    # nft_response = service.draft(draft_model)
    # print(nft_response)
    # print('\n')

    # making a NFT edit api call
    # edit_model = NftModels.DaftAndEditModel()
    # edit_model.draft = 2
    # edit_model.name = 'Cat nft'
    # edit_model.count = 2
    # edit_model.type = 'card'
    # edit_model.layout = 'layout1'
    # edit_model.front = 'img.jpg'
    # edit_model.back = 'imgB.jpg'
    # edit_model.color = 'Red'
    # edit_model.pattern = 'prism'
    # edit_model.pattern_color = 'green'
    # edit_model.text_color = 'red'
    # edit_model.payload = 'payload'
    # edit_model.wrapper = 'wrapper'
    # edit_model.mesh = True
    # edit_model.nsfw = True
    # nft_response = service.edit(edit_model)
    # print(nft_response)
    # print('\n')

    # upload images api call

    # name = "My Image Name"
    # content = "My Base 64 content"
    # image_response = service.upload(name,content)
    # print(image_response)
    # print('\n')
    #
    # # api call for getting NFt details
    # nft_model=NftModels.NftModel
    # nft_model.nft=1231
    # nft_model.uuid='Uuid 123'
    # nft_model.symbol="Square"
    # nft_model.sequence=1
    # nft_response = service.nft(nft_model)
    # print(nft_response)
    #
    # # api call for getting NFts details
    nfts_model=NftModels.NftsModel()
    nfts_model.user= 131
    nfts_model.uuid='UUID 231'
    nfts_model.symbol='corn'
    nfts_model.batch=123
    nfts_model.sequence=12
    nfts_model.nft=12
    nfts_model.creator='123'
    nfts_model.domain='domain'
    nfts_model.wallet=1231
    nfts_model.currency=23
    nfts_model.market=14
    nfts_model.hidden=True
    nfts_model.nsfw=True
    nfts_model.flagged=True
    nfts_model.held=True
    nfts_model.showcase=True
    nfts_model.onsale=True
    nfts_model.batched=True
    nfts_model.tag='Tag'
    nfts_model.tags='tags'
    nfts_model.all_tags='1231'
    nfts_model.any_tags='1234'
    nfts_model.search='s12'
    nfts_model.count=12
    nfts_model.page=12
    nft_response = service.nfts(nfts_model)
    print(nft_response)

    #api to Get NFT metadata in ERC721 compatible format
    # id_nft=10
    # data_reponse=service.data(id_nft)
    # print(data_reponse)







    # # Api call to creating a bundles
    # bundle_service = Bundle.Bundle()
    # create_model = BundleModels.BundleModels()
    # create_model.name="My bundle"
    # create_model.max_subscribers=10
    # create_model.channel="https://www.youtube.com/channel/UCiPI3PDGfbgdVHSGtQbKYyA/"
    # response = bundle_service.create(create_model)
    # print(response)
    #bundel id
    # print('\n')n
    #
    # # api call for updating a bundles
    # bundle_id = 10
    # update_model = BundleModels.BundleModels()
    # update_model.name="New name"
    # update_model.max_subscribers=12
    # update_model.channel="https://www.youtube.com/channel/UCiPI3PDGfbgdVHSGtQbKYyA/"
    # response = bundle_service.update(bundle_id, update_model)
    # print(response)
    # print('\n')
    #
    # #api call for listing marketing bundles
    # bundle_id=10
    # name='Ali'
    # response=bundle_service.bundles(bundle_id,name)
    # print(response)
    # print('\n')
    #
    # #api calls for creatings or updating line
    # bundle_id=10
    # line_model=BundleModels.ListModels()
    # line_model.line=23
    # line_model.status="active"
    # line_model.batches="batch list 12312"
    # line_model.method="random"
    # line_model.odds=5
    # response=bundle_service.line(bundle_id,line_model)
    # print(response)
    # print('\n')
    #
    #api calls for creating claim codes for bundles
    # bundle_id=10
    # count=23
    # response=bundle_service.code(bundle_id,count)
    # print(response)
    # print('\n')

    #api calls for List claim codes for a bundle

    # bundle_id=234
    # count=23
    # page=2
    # response=bundle_service.codes(bundle_id,count,page)
    # print(response)
    # print('\n')
    #
    #api call to claim a bundle
    #
    #
    # code='A2314'
    # response=bundle_service.claim(code)
    # print(response)
    # print('\n')
    #
    # #api call to List the subscribers to a bundle

    # bundle_id=10
    # status='active'
    # response=bundle_service.subscribers(bundle_id,status)
    # print(response)
    # print('\n')
    #
    # #api call to List the bundles the current user is subscribed to
    #
    # status='active'
    # response=bundle_service.subscriptions(status)
    # print(response)
    # print('\n')
    #
    # #api call for Detailed bundle report, including subscribers, delivery statistics, and redemptions
    # bundle_id=10
    # response=bundle_service.report(bundle_id)
    # print(response)
    # print('\n')

    #SOCIAL
    #Post a message
    social_service=Social.Social()
    # post_model=SocialModel.PostModel()
    # post_model.nft=1321
    # post_model.uuid='asvsd'
    # post_model.symbol='abc'
    # post_model.sequence=12
    # post_model.grab="id"
    # post_model.text="text"
    # response=social_service.post(post_model)
    # print(response)

    #Api to reply to a message
    reply_model=SocialModel.ReplyAndCommentModel()
    # reply_model.nft=231
    # reply_model.uuid='acsd'
    # reply_model.symbol='avs'
    # reply_model.sequence=121
    # reply_model.grab="id"
    # reply_model.message="Id213"
    # reply_model.text="This is the reply"
    # response=social_service.reply(reply_model)
    # print(response)

    #Api to comment on a message
    # comment_model=SocialModel.ReplyAndCommentModel()
    # comment_model.nft = 231
    # comment_model.uuid = 'acsd'
    # comment_model.symbol = 'avs'
    # comment_model.sequence = 121
    # comment_model.grab = "id"
    # comment_model.message = "Id213"
    # comment_model.text = "This is the comment"
    # response=social_service.comment(comment_model)
    # print(response)

    #Api to remove a message
    # remove_model=SocialModel.RemoveModel()
    # remove_model.nft = 231
    # remove_model.uuid = 'acsd'
    # remove_model.symbol = 'avs'
    # remove_model.sequence = 121
    # remove_model.grab = "id"
    # remove_model.message = "Id213"
    # response=social_service.remove(remove_model)
    # print(response)


    #Api to get nft messages
    # message_model=SocialModel.Messages()
    # message_model.nft=123
    # message_model.uuid='acds'
    # message_model.symbol='good symbol'
    # message_model.sequence=123
    # message_model.count=241
    # message_model.page=4
    # response=social_service.messages(message_model)
    # print(response)

    #Api to get user memberships
    # user=123412
    # details=True
    # response=social_service.memberships(user,details)
    # print(response)

    #Api to like api or message
    # like_model=SocialModel.LikeAndUnlike()
    # like_model.nft=12234
    # like_model.uuid="id34523"
    # like_model.symbol="This is the symbol"
    # like_model.sequence=124614
    # like_model.message="Hi this is the message"
    # like_model.text=126
    # response=social_service.like(like_model)
    # print(response)

    #Api to unlike api or message
    # unlike_model=SocialModel.LikeAndUnlike()
    # unlike_model.nft = 12234
    # unlike_model.uuid = "id34523"
    # unlike_model.symbol = "This is the symbol"
    # unlike_model.sequence = 124614
    # unlike_model.message = "Hi this is the message Id"
    # unlike_model.text = 126
    # response=social_service.unlike(unlike_model)
    # print(response)

    #Api to ban user
    # ban_model=SocialModel.BanAndUnBan()
    # ban_model.user="UID 2345123"
    # ban_model.nft=124134
    # ban_model.uuid="UUUID 124134AC"
    # ban_model.symbol="symbol"
    # ban_model.sequence=23523
    # ban_model.grab='The grab id is'
    # ban_model.text=1241
    # response=social_service.ban(ban_model)
    # print(response)

    #Api to unban user
    # unban_model = SocialModel.BanAndUnBan()
    # unban_model.user = "UID 2345123"
    # unban_model.nft = 124134
    # unban_model.uuid = "UUUID 124134AC"
    # unban_model.symbol = "symbol"
    # unban_model.sequence = 23523
    # unban_model.grab = 'The grab id is'
    # unban_model.text = 1241
    # response = social_service.ban(unban_model)
    # print(response)

    #Api to List user's available push notification feeds
    # response=social_service.feed()
    # print(response)

    #SHARING APIS
    #Api to send nft
    sharing_service=Sharing.Sharing()
    # send_model=SharingModels.SendModel()
    # send_model.nft=123
    # send_model.uuid="UUID 23SC42"
    # send_model.symbol=1431
    # send_model.sequence="Sequence"
    # send_model.request="This number of request is "
    # send_model.wallet="WID 213423"
    # send_model.text="sending the api"
    # response=sharing_service.send(send_model)
    # print(response)

    #Api to hold nft
    # hold_model=SharingModels.HoldModel()
    # hold_model.nft=5235
    # hold_model.uuid='UUID 2235962'
    # hold_model.symbol="sigil"
    # hold_model.sequence="This sequence is this"
    # hold_model.platform="Twitter"
    # hold_model.address="@UserQ2S4"
    # hold_model.hours=4
    # hold_model.text="Nft held"
    # response=sharing_service.hold(hold_model)
    # print(response)
    #will give hold code

    #Api to show held nft
    # hold_code="Are2342"
    # platform="Twitter"
    # address="@UserQ2S4"
    # response=sharing_service.held(hold_code,platform,address)
    # print(response)

    #Api to collect an NFT
    # collect_code='CC 1231'
    # wallet_id="WID 24naw14"
    # text="Hello "
    # response=sharing_service.collect(collect_code,wallet_id,text)
    # print(response)

    #Api to request an NFT
    # request_model=SharingModels.RequestModel()
    # request_model.nft="Nft 1231"
    # request_model.uuid="UUID 31234d"
    # request_model.symbol="circle"
    # request_model.sequence="sequence 1234"
    # request_model.wallet=234.0
    # request_model.text="demo text"
    # response=sharing_service.request(request_model)
    # print(response)

    #Api to List requestes
    # requests_model=SharingModels.RequestsModel()
    # requests_model.user="ID 13S14"
    # requests_model.sender="ID sender"
    # requests_model.nft=24153
    # requests_model.uuid='UUID 242345'
    # requests_model.symbol='liege'
    # requests_model.currency="CID 242345"
    # requests_model.name="Name of nft"
    # requests_model.count=12
    # requests_model.page=2
    # response=sharing_service.requests(requests_model)
    # print(response)

    #Api to give away one or more NFTs via claim code
    # batch_id="BID 12341"
    # nfts=23
    # text="Message"
    # hours=32
    # response=sharing_service.giveaway(batch_id,nfts,text,hours)
    # print(response)

    #Api to Claim a NFT from a giveaway
    # code="CID 234234"
    # wallet=1234
    # text="Nft claimed form code"
    # response=sharing_service.claim(code,wallet,text)
    # print(response)

    #Api to List reminders for available actions, including held NFTs.
    # user_id='UID 98279'
    # email="acvaads@amail.com"
    # domain='domain'
    # sms='hello'
    # response=sharing_service.remind(user_id,email,domain,sms)
    # print(response)



    #Buying and Selling
    #Api to list sales
    buyAndselling_service=BuyingAndSelling.BuyingAndSelling()
    # sales_model=BuyingAndSellingModels.SalesAndMarketplaceModel()
    # sales_model.user='User add'
    # sales_model.nft=25431
    # sales_model.uuid='UUID 4980'
    # sales_model.symbol='Square'
    # sales_model.sequence='1234'
    # sales_model.currency='Cid 2342'
    # sales_model.name='Cat nft'
    # sales_model.count=33
    # sales_model.page=2
    # response=buyAndselling_service.sales(sales_model)
    # print(response)

    #Api to list auctions
    # auctions_model=BuyingAndSellingModels.AuctionsModel()
    # auctions_model.user = 'User add'
    # auctions_model.nft = 25431
    # auctions_model.uuid = 'UUID 4980'
    # auctions_model.symbol = 'Square'
    # auctions_model.sequence = '1234'
    # auctions_model.currency = 'Cid 2342'
    # auctions_model.count = 33
    # auctions_model.page = 2
    # response = buyAndselling_service.auctions(auctions_model)
    # print(response)

    #List sales and auctions together
    # marketplace_model=BuyingAndSellingModels.SalesAndMarketplaceModel()
    # marketplace_model.user = 'User add'
    # marketplace_model.nft = 25431
    # marketplace_model.uuid = 'UUID 4980'
    # marketplace_model.symbol = 'Square'
    # marketplace_model.sequence = '1234'
    # marketplace_model.currency = 'Cid 2342'
    # marketplace_model.name = 'Cat nft'
    # marketplace_model.count = 33
    # marketplace_model.page = 2
    # response = buyAndselling_service.marketplace(marketplace_model)
    # print(response)

    #api to sell an nft
    # sell_model=BuyingAndSellingModels.SellModel()
    # sell_model.nft = 2341
    # sell_model.uuid = 'UUID 4680'
    # sell_model.symbol = 'Square'
    # sell_model.sequence = '3'
    # sell_model.price=23523.42
    # response=buyAndselling_service.sell(sell_model)
    # print(response)

    # Nft to auction an nft
    # auction_model=BuyingAndSellingModels.Auction()
    # auction_model.mode='normal'
    # auction_model.nft=1231
    # auction_model.uuid='UUID 24123'
    # auction_model.symbol='square'
    # auction_model.sequence='23'
    # auction_model.reserve=34.2
    # auction_model.maximum=56.3
    # auction_model.minimum=24.3
    # auction_model.start=2
    # auction_model.end=5
    # response=buyAndselling_service.auction(auction_model)
    # print(response)

    #Api to buy an nft
    # nft=23
    # response=buyAndselling_service.buy(nft)
    # print(response)

    #Api to bid on auction
    # auction='Auction 2342'
    # price=123.32
    # response=buyAndselling_service.bid(auction,price)
    # print(response)

    #Api to cancel  auction or sale
    # auction='Auction 123'
    # sale='Sale id 2342'
    # text='explation for the cancellation'
    # response=buyAndselling_service.cancel(auction,sale,text)
    # print(response)

    #Api to showcase an nft
    # showcase_model=BuyingAndSellingModels.ShowcaseAndUnshowcaseModel()
    # showcase_model.nft=123
    # showcase_model.uuid='Uid 123'
    # showcase_model.symbol='rectangle'
    # showcase_model.sequence=23
    # showcase_model.text='Text'
    # response=buyAndselling_service.showcase(showcase_model)
    # print(response)

    #Api to unshowcase an nft
    # unshowcase_model=BuyingAndSellingModels.ShowcaseAndUnshowcaseModel()
    # unshowcase_model.nft=123
    # unshowcase_model.uuid='Uid 123'
    # unshowcase_model.symbol='rectangle'
    # unshowcase_model.sequence=23
    # unshowcase_model.text='Text'
    # response=buyAndselling_service.unshowcase(unshowcase_model)
    # print(response)

    #Api to Check if user is authorised to maintain the showcase
    # response=buyAndselling_service.can_showcase()
    # print(response)

    #API to tag a nft
    # tag_model=BuyingAndSellingModels.TagModel()
    # tag_model.nft=123
    # tag_model.uuid='Uid 123'
    # tag_model.symbol='rectangle'
    # tag_model.sequence=23
    # tag_model.tag='Cat'
    # tag_model.mode='add'
    # response=buyAndselling_service.tag(tag_model)
    # print(response)

    #APi to lock an nft
    # lock_model=BuyingAndSellingModels.LockAndUnlockModel()
    # lock_model.nft = 123
    # lock_model.uuid = 'Uid 123'
    # lock_model.symbol = 'rectangle'
    # lock_model.sequence = 23
    # lock_model.text = 'Text'
    # response=buyAndselling_service.lock(lock_model)
    # print(response)

    #Api to unlock an nft
    # unlock_model = BuyingAndSellingModels.LockAndUnlockModel()
    # unlock_model.nft = 123
    # unlock_model.uuid = 'Uid 123'
    # unlock_model.symbol = 'rectangle'
    # unlock_model.sequence = 23
    # unlock_model.text = 'Text'
    # response = buyAndselling_service.unlock(unlock_model)
    # print(response)

    # #Api to hide an nft
    # hide_model = BuyingAndSellingModels.HideAndShow()
    # hide_model.nft = 123
    # hide_model.uuid = 'Uid 123'
    # hide_model.symbol = 'rectangle'
    # hide_model.sequence = 23
    # hide_model.request=1231
    # hide_model.text = 'Text'
    # response=buyAndselling_service.hide(hide_model)
    # print(response)

    #Api to show an nft
    # show_model = BuyingAndSellingModels.HideAndShow()
    # show_model.nft = 123
    # show_model.uuid = 'Uid 123'
    # show_model.symbol = 'rectangle'
    # show_model.sequence = 23
    # show_model.request = 1231
    # show_model.text = 'Text'
    # response = buyAndselling_service.show(show_model)
    # print(response)

    #Marketing Apis
    #Api to redeem Api
    marketing_service=Marketing.Marketing()
    # nft='Id 1231'
    # response=marketing_service.redeem(nft)
    # print(response)

    #  Api to Mark a previously redeemed NFT you created as redeemable again
    # nft='ID 2342'
    # response=marketing_service.unredeem(nft)
    # print(response)

    #Api to Add a one-time payload to an existing NFT
    # nft='Id 12312'
    # payload='payload 0056'
    # response=marketing_service.payload(nft,payload)
    # print(response)

    #Api to consume a payload from existing nft
    # nft='Id 31234'
    # response=marketing_service.consume(nft)
    # print(response)

    #Reporting APIs
    #api to get Nft or user history
    reporting_services=Reporting.Reporting()
    # history_model=ReportingModels.HistoryModel()
    # history_model.nft=1231
    # history_model.uuid='UUid 231'
    # history_model.symbol='square'
    # history_model.sequence='12'
    # history_model.user='UID 234'
    # history_model.action='action type'
    # history_model.sale=2342
    # history_model.auction=14123
    # history_model.request=23
    # history_model.bid=12
    # history_model.hold=12
    # history_model.source=9
    # history_model.dest=1
    # history_model._show_NFTS='details'
    # response=reporting_services.history(history_model)
    # print(response)

    #Api to Get user's transaction ledger
    # user='uid 1232'
    # count=12
    # page=2
    # response=reporting_services.ledger(user,count,page)
    # print(response)

    #Api to Get history of NFTs given
    # given_model = ReportingModels.HistoryModel()
    # given_model.nft = 1231
    # given_model.uuid = 'UUid 231'
    # given_model.symbol = 'square'
    # given_model.sequence = '12'
    # given_model.user = 'UID 234'
    # given_model.sale = 2342
    # given_model.auction = 14123
    # given_model.request = 23
    # given_model.bid = 12
    # given_model.hold = 12
    # given_model.source = 9
    # given_model.dest = 1
    # given_model._show_NFTS = 'details'
    # response = reporting_services.given(given_model)
    # print(response)

    #Api to List top users by NFT ownership, creation, or circulation.
    # leaders_model=ReportingModels.LeadersModel()
    # leaders_model.mode='Nft filter'
    # leaders_model.tag='tag'
    # leaders_model.tags='tags'
    # leaders_model.all_tag='all tag'
    # leaders_model.all_tags='all tags'
    # leaders_model.any_tags='any tags'
    # leaders_model.count=1
    # leaders_model.page=2
    # response=reporting_services.leaders(leaders_model)
    # print(response)

    #api to list List recent popular tags
    # days=1
    # count=13
    # response=reporting_services.popular_tag(days,count)
    # print(response)

    #api to List curent trending tags.
    # days=1
    # count=14
    # response=reporting_services.trending_tags(days,count)
    # print(response)


    #Api Get counts for all tags or a specified set of tags
    # tags='Tag'
    # response=reporting_services.tagcount(tags)
    # print(response)

    # Authentication
    # Api to login
    auth_service = Authentication.Authentication()
    # email = Helper.Helper().get_credentials()[0]
    # password = Helper.Helper().get_credentials()[1]
    # url = Helper.Helper().get_credentials()[2]
    # response = auth_service.login(email, password, url)
    # print(response)

    #api to logout
    # session='Season number'
    # response=auth_service.logout(session)
    # print(response)

    # Api to register
    # register_model=AuthenticationModels.Register()
    # register_model.provider='pro'
    # register_model.email="alasd@gmail.com"
    # register_model.password='asdfa12'
    # register_model.name='ali'
    # register_model.domain='123'
    # response=auth_service.register(register_model)
    # print(response)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
