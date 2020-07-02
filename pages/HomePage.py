# from pylenium import Pylenium
# from pylenium.element import Element


class HomePageMap:
    SEARCH_FIELD = '#INPUTtext____42'
    WISHLIST_ICON = '#A__wishlist__52'
    FILTER_COLUMN = '#filter_col'
    TOP_BANNER_IMAGE = '.top_banner'
    PRODUCT_GRID = '#product_grid'
    FILTER_COLOR_BLACK = '#colors__Black'
    FILTER_BUTTON = '#filterBtn'
    LEFT_SIDE_FILTER_ICON = '#ti-filter'
    SMALL_REFERENCE_ID = '#SMALL____84'
    NICE_SELECT_SIZE = '.nice-select'
    NEW_PRICE_LABEL = "#new_price"
    PROFILE_ICON = ".access_link"
    CART_BUTTON = "#A__cartbt__49"
    FIFTH_STAR = "#I__iconstar__81"
    RATING_COUNT = "#EM____82"  # For V1
    # RATING_COUNT = "#EM__ratingcoun__82" # For V2
    DEFAULT_QUANTITY = "#quantity_1"
    BUTTON_ADD_TO_CART = "#A__btn__114"
    SHOE_IMAGE = "#shoe_img"


class AppliFashionHomePage:
    def __init__(self, py, width, height, URL):
        self.py = py
        self.py.viewport(width, height, 'portrait')
        self.py.visit(URL)
        self.domId = ''
        self.filterColorDomId = ''
        self.filterButton = ''
        self.firstProduct = ''
        self.map = {
            HomePageMap.SEARCH_FIELD: lambda: self.py.get(HomePageMap.SEARCH_FIELD),
            HomePageMap.WISHLIST_ICON: lambda: self.py.get(HomePageMap.WISHLIST_ICON),
            HomePageMap.FILTER_COLUMN: lambda: self.py.get(HomePageMap.FILTER_COLUMN),
            HomePageMap.TOP_BANNER_IMAGE: lambda: self.py.get(HomePageMap.TOP_BANNER_IMAGE),
            HomePageMap.PRODUCT_GRID: lambda: self.py.get(HomePageMap.PRODUCT_GRID),
            HomePageMap.FILTER_COLOR_BLACK: lambda: self.py.get(HomePageMap.FILTER_COLOR_BLACK),
            HomePageMap.FILTER_BUTTON: lambda: self.py.get(HomePageMap.FILTER_BUTTON),
            HomePageMap.LEFT_SIDE_FILTER_ICON: lambda: self.py.get(HomePageMap.LEFT_SIDE_FILTER_ICON),
            HomePageMap.SMALL_REFERENCE_ID: lambda: self.py.get(HomePageMap.SMALL_REFERENCE_ID),
            HomePageMap.NICE_SELECT_SIZE: lambda: self.py.get(HomePageMap.NICE_SELECT_SIZE),
            HomePageMap.NEW_PRICE_LABEL: lambda: self.py.get(HomePageMap.NEW_PRICE_LABEL),
            HomePageMap.PROFILE_ICON: lambda: self.py.get(HomePageMap.PROFILE_ICON),
            HomePageMap.CART_BUTTON: lambda: self.py.get(HomePageMap.CART_BUTTON),
            HomePageMap.FIFTH_STAR: lambda: self.py.get(HomePageMap.FIFTH_STAR),
            HomePageMap.RATING_COUNT: lambda: self.py.get(HomePageMap.RATING_COUNT),
            HomePageMap.DEFAULT_QUANTITY: lambda: self.py.get(HomePageMap.DEFAULT_QUANTITY),
            HomePageMap.BUTTON_ADD_TO_CART: lambda: self.py.get(HomePageMap.BUTTON_ADD_TO_CART),
            HomePageMap.SHOE_IMAGE: lambda: self.py.get(HomePageMap.SHOE_IMAGE),
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

    def getReference(self):
        return self.__find(HomePageMap.SMALL_REFERENCE_ID)

    def getFilterButton(self):
        return self.__find(HomePageMap.FILTER_BUTTON)

    def openLeftSideFilter(self):
        self.__find(HomePageMap.LEFT_SIDE_FILTER_ICON).click()

    def getDefaultSize(self):
        return self.__find(HomePageMap.NICE_SELECT_SIZE)

    def getPrize(self):
        return self.__find(HomePageMap.NEW_PRICE_LABEL).text()

    def checkTopToolsIconsNotOverlapping(self):
        profileIcon = self.__find(HomePageMap.PROFILE_ICON)
        wishListIcon = self.__find(HomePageMap.WISHLIST_ICON)
        cartButton = self.__find(HomePageMap.CART_BUTTON)

        rectProfileIcon = profileIcon.webelement.rect
        rectWishListIcon = wishListIcon.webelement.rect
        rectCartButton = cartButton.webelement.rect

        # Explain: check that right position of icon n < left position of icon n+1
        return (((rectProfileIcon["x"] + rectProfileIcon["width"]) <= rectWishListIcon["x"]) and
                ((rectWishListIcon["x"] + rectWishListIcon["width"]) <= rectCartButton["x"]))

    def checkRatingReviewOverlapping(self):
        fifthStar = self.__find(HomePageMap.FIFTH_STAR)
        ratingCount = self.__find(HomePageMap.RATING_COUNT)

        rectFifthStar = fifthStar.webelement.rect
        rectRatingCount = ratingCount.webelement.rect

        return (rectFifthStar["x"] + rectFifthStar["width"]) <= rectRatingCount["x"]

    def getDefaultQuantity(self):
        return self.__find(HomePageMap.DEFAULT_QUANTITY).get_attribute('value')

    def getButtonAddToCart(self):
        return self.__find(HomePageMap.BUTTON_ADD_TO_CART)

    def getShoeImage(self):
        return self.__find(HomePageMap.SHOE_IMAGE).get_attribute('style')

