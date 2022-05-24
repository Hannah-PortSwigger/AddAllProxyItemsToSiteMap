# AddAllProxyItemsToSiteMap
Adds all HTTP requests/responses to "Target > Site map", once a response has been received.

If you would like to add requests to the site map before they receive a response, remove the `if` statement on line 16. Make sure to adjust the indentation of `self._callbacks.addToSiteMap(message.getMessageInfo())`.
