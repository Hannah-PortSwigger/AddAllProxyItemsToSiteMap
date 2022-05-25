# AddAllProxyItemsToSiteMap
Adds all HTTP requests/responses to "Target > Site map", once a response has been received.

## Add in scope items only
Change the variable `only_in_scope` to `True`

## Deduplicating items
Provide your own logic for deduplicating request/response pairs in the `deduplicate()` function, to determine whether items should be added to the site map.

## Requests without a response
If you would like to add requests to the site map before they receive a response, remove the `if` statement [here](https://github.com/Hannah-PortSwigger/AddAllProxyItemsToSiteMap/blob/7d73706f3ac8a3c428c7f9c04a82e416cd565616/AddAllProxyItemsToSiteMap.py#L22). Make sure to adjust the indentation of the rest of the function.
