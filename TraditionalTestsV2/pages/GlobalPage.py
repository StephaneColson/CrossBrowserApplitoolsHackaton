class GlobalPageMap:
    SEARCH_FIELD = '#INPUTtext____42'
    WISHLIST_ICON = '#A__wishlist__52'
    CART_BUTTON = '#A__cartbt__49'
    PROFILE_ICON = '#A__accesslink__56'


class GlobalPage:
    def __init__(self, py, width, height, baseUrl):
        self.py = py
        self.py.viewport(width, height, 'portrait')
        self.py.visit(baseUrl)
        self.map = ''
        self.useGlobalPageMap()

    def __find(self, path):
        return self.map[path]() if path in self.map.keys() else None

    def useGlobalPageMap(self):
        self.map = {
            GlobalPageMap.SEARCH_FIELD: lambda: self.py.get(GlobalPageMap.SEARCH_FIELD),
            GlobalPageMap.WISHLIST_ICON: lambda: self.py.get(GlobalPageMap.WISHLIST_ICON),
            GlobalPageMap.CART_BUTTON: lambda: self.py.get(GlobalPageMap.CART_BUTTON),
            GlobalPageMap.PROFILE_ICON: lambda: self.py.get(GlobalPageMap.PROFILE_ICON),
        }

    def getSearchField(self):
        return self.__find(GlobalPageMap.SEARCH_FIELD)

    def getWishlistIcon(self):
        return self.__find(GlobalPageMap.WISHLIST_ICON)

    def getProfileIcon(self):
        return self.__find(GlobalPageMap.PROFILE_ICON)

    def getCartButton(self):
        return self.__find(GlobalPageMap.CART_BUTTON)

