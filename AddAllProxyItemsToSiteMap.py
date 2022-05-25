from burp import IBurpExtender, IProxyListener
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IProxyListener):

    
    only_in_scope = False


    def registerExtenderCallbacks(self, callbacks):
        extName = "Add all proxy items to site map"
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName(extName)
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        callbacks.registerProxyListener(self)
        self._stdout.println(extName)
        return


    def processProxyMessage(self, messageIsRequest, message):
        if not messageIsRequest:
            if ( not self.only_in_scope ) or ( self.only_in_scope and self._callbacks.isInScope( self._helpers.analyzeRequest( message.getMessageInfo() ).getUrl() ) ):
                self.deduplicate(message)
        return


    def deduplicate(self, message):
        # Provide your own implementation here
        self._callbacks.addToSiteMap(message.getMessageInfo())
        return
