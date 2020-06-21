from pylenium.element import Element

class HomePageMap:
    SEARCH_FIELD = '#INPUTtext____42'
    WISHLIST_ICON = '#A__wishlist__52'
    FILTER_COLUMN = '#filter_col'
    TOP_BANNER_IMAGE = '.top_banner'

class AppliFashionHomePage:

    def __init__(self, py, width, height, URL):
        self.py = py
        self.py.viewport(width, height, 'portrait')
        self.py.visit(URL)
        self.map = {
            HomePageMap.SEARCH_FIELD : lambda: self.py.get(HomePageMap.SEARCH_FIELD),
            HomePageMap.WISHLIST_ICON : lambda: self.py.get(HomePageMap.WISHLIST_ICON),
            HomePageMap.FILTER_COLUMN : lambda: self.py.get(HomePageMap.FILTER_COLUMN),
            HomePageMap.TOP_BANNER_IMAGE : lambda: self.py.get(HomePageMap.TOP_BANNER_IMAGE),
        }

    def __find(self, path):
        return  self.map[path]() if path in self.map.keys() else None

    def getSearchField(self):
        return self.__find(HomePageMap.SEARCH_FIELD)

    def getWishlistIcon(self):
        return self.__find(HomePageMap.WISHLIST_ICON)

    def getFilterColumn(self):
        return self.__find(HomePageMap.FILTER_COLUMN)

    def getTopBannerImage(self):
        return self.__find(HomePageMap.TOP_BANNER_IMAGE)
