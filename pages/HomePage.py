from pylenium import Pylenium
from pylenium.element import Element


class HomePageMap:
    SEARCH_FIELD = '#INPUTtext____42'
    WISHLIST_ICON = '#A__wishlist__52'
    FILTER_COLUMN = '#filter_col'
    TOP_BANNER_IMAGE = '.top_banner'
    PRODUCT_GRID = '#product_grid'
    FILTER_COLORS_PREFIX = '#colors__'
    FILTER_BUTTON = '#filterBtn'


class AppliFashionHomePage:
    def __init__(self, py, width, height, URL):
        self.py = py
        self.py.viewport(width, height, 'portrait')
        self.py.visit(URL)
        self.domId = ''
        self.filterColorDomId = ''
        self.filterButton = ''
        self.map = {
            HomePageMap.SEARCH_FIELD: lambda: self.py.get(HomePageMap.SEARCH_FIELD),
            HomePageMap.WISHLIST_ICON: lambda: self.py.get(HomePageMap.WISHLIST_ICON),
            HomePageMap.FILTER_COLUMN: lambda: self.py.get(HomePageMap.FILTER_COLUMN),
            HomePageMap.TOP_BANNER_IMAGE: lambda: self.py.get(HomePageMap.TOP_BANNER_IMAGE),
            HomePageMap.PRODUCT_GRID: lambda: self.py.get(HomePageMap.PRODUCT_GRID),
            HomePageMap.FILTER_COLORS_PREFIX: lambda: self.py.get(HomePageMap.FILTER_COLORS_PREFIX),
            HomePageMap.FILTER_BUTTON: lambda: self.py.get(HomePageMap.FILTER_BUTTON),
        }

    def __find(self, path):
        return self.map[path]() if path in self.map.keys() else None

    def getSearchField(self):
        return self.__find(HomePageMap.SEARCH_FIELD)

    def getWishlistIcon(self):
        return self.__find(HomePageMap.WISHLIST_ICON)

    def getFilterColumn(self):
        return self.__find(HomePageMap.FILTER_COLUMN)

    def getTopBannerImage(self):
        return self.__find(HomePageMap.TOP_BANNER_IMAGE)

    def getProductGrid(self):
        return self.__find(HomePageMap.PRODUCT_GRID)

    def getFilterColor(self, color):
        return self.__find(HomePageMap.FILTER_COLORS_PREFIX)+color

    def getFilterButton(self):
        return self.__find(HomePageMap.FILTER_BUTTON)
