from pages.GlobalPage import GlobalPageMap, GlobalPage


class ProductDetailPageMap(GlobalPageMap):
    SHOE_IMAGE = '#shoe_img'
    SMALL_REFERENCE_ID = '#SMALL____84'
    NICE_SELECT_SIZE = '.nice-select'
    NEW_PRICE_LABEL = '#new_price'
    FIFTH_STAR = '#I__iconstar__81'
    RATING_COUNT = '#EM____82'
    DEFAULT_QUANTITY = '#quantity_1'
    BUTTON_ADD_TO_CART = '#A__btn__114'


class ProductDetailPage(GlobalPage):
    def __init__(self, py, width, height, baseUrl, page=''):
        self.py = py
        self.py.viewport(width, height, 'portrait')
        self.py.visit(baseUrl+page)
        self.map = {
            ProductDetailPageMap.SHOE_IMAGE: lambda: self.py.get(ProductDetailPageMap.SHOE_IMAGE),
            ProductDetailPageMap.SMALL_REFERENCE_ID: lambda: self.py.get(ProductDetailPageMap.SMALL_REFERENCE_ID),
            ProductDetailPageMap.NICE_SELECT_SIZE: lambda: self.py.get(ProductDetailPageMap.NICE_SELECT_SIZE),
            ProductDetailPageMap.NEW_PRICE_LABEL: lambda: self.py.get(ProductDetailPageMap.NEW_PRICE_LABEL),
            ProductDetailPageMap.FIFTH_STAR: lambda: self.py.get(ProductDetailPageMap.FIFTH_STAR),
            ProductDetailPageMap.RATING_COUNT: lambda: self.py.get(ProductDetailPageMap.RATING_COUNT),
            ProductDetailPageMap.DEFAULT_QUANTITY: lambda: self.py.get(ProductDetailPageMap.DEFAULT_QUANTITY),
            ProductDetailPageMap.BUTTON_ADD_TO_CART: lambda: self.py.get(ProductDetailPageMap.BUTTON_ADD_TO_CART),
        }

    def __find(self, path):
        return self.map[path]() if path in self.map.keys() else None

    def getReference(self):
        return self.__find(ProductDetailPageMap.SMALL_REFERENCE_ID)

    def getDefaultSize(self):
        return self.__find(ProductDetailPageMap.NICE_SELECT_SIZE)

    def getPrize(self):
        return self.__find(ProductDetailPageMap.NEW_PRICE_LABEL).text()

    def checkRatingReviewOverlapping(self):
        fifthStar = self.__find(ProductDetailPageMap.FIFTH_STAR)
        ratingCount = self.__find(ProductDetailPageMap.RATING_COUNT)

        rectFifthStar = fifthStar.webelement.rect
        rectRatingCount = ratingCount.webelement.rect

        return (rectFifthStar["x"] + rectFifthStar["width"]) <= rectRatingCount["x"]

    def getDefaultQuantity(self):
        return self.__find(ProductDetailPageMap.DEFAULT_QUANTITY).get_attribute('value')

    def getButtonAddToCart(self):
        return self.__find(ProductDetailPageMap.BUTTON_ADD_TO_CART)

    def getShoeImage(self):
        return self.__find(ProductDetailPageMap.SHOE_IMAGE).get_attribute('style')

    def checkTopToolsIconsNotOverlapping(self):
        profileIcon = self.getProfileIcon()
        wishListIcon = self.getWishlistIcon()
        cartButton = self.getCartButton()

        rectProfileIcon = profileIcon.webelement.rect
        rectWishListIcon = wishListIcon.webelement.rect
        rectCartButton = cartButton.webelement.rect

        # Explain: check that right position of icon n < left position of icon n+1
        return (((rectProfileIcon["x"] + rectProfileIcon["width"]) <= rectWishListIcon["x"]) and
                ((rectWishListIcon["x"] + rectWishListIcon["width"]) <= rectCartButton["x"]))
