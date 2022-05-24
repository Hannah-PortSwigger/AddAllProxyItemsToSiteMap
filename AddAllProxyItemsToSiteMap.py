from burp import IBurpExtender, IProxyListener
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IProxyListener):
    def registerExtenderCallbacks(self, callbacks):
        extName = "Add all proxy items to site map"
        self._callbacks = callbacks
        callbacks.setExtensionName(extName)
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        callbacks.registerProxyListener(self)
        self._stdout.println(extName)
        return


    def processProxyMessage(self, messageIsRequest, message):
        if not messageIsRequest:
            self._callbacks.addToSiteMap(message.getMessageInfo())
        return
