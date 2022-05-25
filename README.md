# AddAllProxyItemsToSiteMap
Adds all HTTP requests/responses to "Target > Site map", once a response has been received.

## Add in scope items only
Change the variable `only_in_scope` to `True`

## Deduplicating items
Provide your own logic for deduplicating request/response pairs in the `deduplicate()` function, to determine whether items should be added to the site map.

## Requests without a response
If you would like to add requests to the site map before they receive a response, remove the `if` statement on line 20. Make sure to adjust the indentation of `self._callbacks.addToSiteMap(message.getMessageInfo())`.
