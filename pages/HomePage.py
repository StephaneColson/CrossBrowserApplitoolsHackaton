from pylenium import Pylenium
from pylenium.element import Element


class HomePageMap:
    SEARCH_FIELD = '#INPUTtext____42'
    WISHLIST_ICON = '#A__wishlist__52'
    FILTER_COLUMN = '#filter_col'
    TOP_BANNER_IMAGE = '.top_banner'
    PRODUCT_GRID = '#product_grid'
    FILTER_COLOR_BLACK = '#colors__Black'
    FILTER_BUTTON = '#filterBtn'
    LEFT_SIDE_FILTER_ICON = '#ti-filter'


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
            HomePageMap.FILTER_COLOR_BLACK: lambda: self.py.get(HomePageMap.FILTER_COLOR_BLACK),
            HomePageMap.FILTER_BUTTON: lambda: self.py.get(HomePageMap.FILTER_BUTTON),
            HomePageMap.LEFT_SIDE_FILTER_ICON: lambda: self.py.get(HomePageMap.LEFT_SIDE_FILTER_ICON)

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

    def getBlackColorInFilter(self):
        return self.__find(HomePageMap.FILTER_COLOR_BLACK)

    def checkBlackColorInFilter(self):
        # py.wait(use_py=True).sleep(3)
        x = self.py.webdriver
        # We need to wait for the filter menu to be displayed
        self.py.wait(3, use_py=True).until(lambda x: x.find_element_by_id('filter_col').is_displayed())
        return self.getBlackColorInFilter().check()

    def getFilterButton(self):
        return self.__find(HomePageMap.FILTER_BUTTON)

    def openLeftSideFilter(self):
        return self.__find(HomePageMap.LEFT_SIDE_FILTER_ICON)

