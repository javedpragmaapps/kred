


class Bundle:

    # @creat function calls POST api to Create a marketing bundle.
    # the model used is from  BundelModel
    # name and max_subscribers are required parameters
    # The function returns ' '
    def create(self, model):


        return 'nft created and here is the bundle id'

    # @update function calls POST api to Update a marketing bundle.
    # the model used is from  BundelModel
    # bundle  is required parameters
    # The function returns ' '
    def update(self, bundle_id, model):

        # written a code for making a http request to crate a bundle and return the data
        return "Marketing Bundles has been updated successfully"

    # @update function calls POST api to List your marketing bundles.
    # The function returns ' '
    def bundles(self,bundle_id):

        return "Bundles have been listed for id " + str(bundle_id)

    # @line function calls POST api to Create or update bundle line.
    # the model used is from  LineModel
    # batches is required parameters
    # The function returns ' '
    def line(self,bundle_id,model):

        # written a code for making a http request to crate a bundle and return the data
        return  "bundles  line updated for batch " + model.batches

    # @code function calls POST api to Create one or more claim codes for a bundle.
    # bundle is required parameters
    # The function returns ' '
    def code(self,bundle_id,count):
        # written a code for making a http request to crate a bundle and return the data
        return  str(count) + " bundle code created for "  +  str(bundle_id)

    # @codes function calls POST api to List claim codes for a bundle.
    # bundle is required parameters
    # The function returns ' '
    def codes(self,bundle_id,count,page):
        return "bundle codes created for " + str(bundle_id)

    # @claim function calls POST api to List claim codes for a bundle.
    # code is required parameter
    # The function returns ' '
    def claim(self,code):
        return 'Bundle claimed for code ' + code

    # @subscribers function calls POST api to List the subscribers to a bundle.
    # bundle is required parameter
    # The function returns ' '
    def subscribers(self,blundle_id,status):
        return "Listed the subscribers"

    # @subscribers function calls POST api to List the bundles the current user is subscribed to.
    # The function returns ' '
    def subscriptions(self,status):
        return  'The user is subscribed to the following bundles '

    # @report function calls POST api to give Detailed bundle report, including subscribers, delivery statistics, and redemptions
    # bundles is a required parameter
    # The functopn retruns ' '
    def report(self,bundle_id):
        return  'Detailed bundle report, including subscribers, delivery statistics, and redemptions for id ' + str(bundle_id)
