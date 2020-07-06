from pages.GlobalPage import GlobalPageMap, GlobalPage


class HomePageMap(GlobalPageMap):
    FILTER_COLUMN = '#filter_col'
    TOP_BANNER_IMAGE = '.top_banner'
    PRODUCT_GRID = '#product_grid'
    PRODUCT_1 = '#product_1'
    PRODUCT_8 = '#product_8'
    FILTER_COLOR_BLACK = '#colors__Black'
    FILTER_BUTTON = '#filterBtn'
    LEFT_SIDE_FILTER_ICON = '#ti-filter'


class HomePage(GlobalPage):
    def __init__(self, py, width, height, baseUrl):
        self.py = py
        self.py.viewport(width, height, 'portrait')
        self.py.visit(baseUrl)
        self.domId = ''
        self.filterColorDomId = ''
        self.filterButton = ''
        self.firstProduct = ''
        self.map = {
            HomePageMap.FILTER_COLUMN: lambda: self.py.get(HomePageMap.FILTER_COLUMN),
            HomePageMap.TOP_BANNER_IMAGE: lambda: self.py.get(HomePageMap.TOP_BANNER_IMAGE),
            HomePageMap.PRODUCT_GRID: lambda: self.py.get(HomePageMap.PRODUCT_GRID),
            HomePageMap.PRODUCT_1: lambda: self.py.get(HomePageMap.PRODUCT_1),
            HomePageMap.PRODUCT_8: lambda: self.py.get(HomePageMap.PRODUCT_8),
            HomePageMap.FILTER_COLOR_BLACK: lambda: self.py.get(HomePageMap.FILTER_COLOR_BLACK),
            HomePageMap.FILTER_BUTTON: lambda: self.py.get(HomePageMap.FILTER_BUTTON),
            HomePageMap.LEFT_SIDE_FILTER_ICON: lambda: self.py.get(HomePageMap.LEFT_SIDE_FILTER_ICON),
        }

    def __find(self, path):
        return self.map[path]() if path in self.map.keys() else None

    def getFilterColumn(self):
        return self.__find(HomePageMap.FILTER_COLUMN)

    def getTopBannerImage(self):
        return self.__find(HomePageMap.TOP_BANNER_IMAGE)

    def openLeftSideFilter(self):
        self.__find(HomePageMap.LEFT_SIDE_FILTER_ICON).click()

    def getProduct_1(self):
        return self.__find(HomePageMap.PRODUCT_1)

    def getProduct_8(self):
        return self.__find(HomePageMap.PRODUCT_8)

    def getProductGrid(self):
        return self.__find(HomePageMap.PRODUCT_GRID)

    def getBlackColorFilterElement(self):
        return self.__find(HomePageMap.FILTER_COLOR_BLACK)

    def getBlackColorProducts(self):
        x = self.py.webdriver
        # We need to wait for the filter menu to be displayed
        self.py.wait(3, use_py=True).until(lambda x: x.find_element_by_id('filter_col').is_displayed())

        self.getBlackColorFilterElement().check()
        self.getFilterButton().click()
        return self.getProductGrid()

    def gotoFirstBlackColorProduct(self):
        self.getBlackColorProducts().children().first().click()

    def getFilterButton(self):
        return self.__find(HomePageMap.FILTER_BUTTON)



