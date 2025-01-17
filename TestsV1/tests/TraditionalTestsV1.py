import pytest, re

from pages.GlobalPage import GlobalPageMap, GlobalPage
from pages.HomePage import HomePageMap, HomePage
from pages.ProductDetailPage import ProductDetailPageMap, ProductDetailPage

MOBILE = 0
TABLET = 1
DESKTOP = 2

backShoe1Page = '?id=1'
backShoe8Page = '?id=8'

class TestData:
    # (Width, Height, type of display (0, 1, 2) and element path?)
    @classmethod
    def forElement(cls, cssPath, testName):
        return [
            (375, 500, MOBILE, cssPath, testName),
            (767, 700, MOBILE, cssPath, testName),
            (768, 500, TABLET, cssPath, testName),
            (991, 700, TABLET, cssPath, testName),
            (992, 500, DESKTOP, cssPath, testName),
            (1200, 700, DESKTOP, cssPath, testName)
        ]


# Check that search field is displayed on tablet and desktop, hidden on mobile
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(GlobalPageMap.SEARCH_FIELD,
                                             'Search field is displayed on tablet and desktop'))
@pytest.mark.task1
def test_search_field_task1(py, report_generator, width, height, displayType, location, testName):
    globalPage = GlobalPage(py, width, height, py.config.custom['environment']['homeUrl'])
    searchField = globalPage.getSearchField()

    # Check that search field is hidden for mobile display only
    if displayType == MOBILE:
        searchField.should().be_hidden()
    else:
        searchField.should().be_visible()


# Check that wishlist icon (heart) is only displayed on Desktop
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(GlobalPageMap.WISHLIST_ICON,
                                             'Wishlist icon is displayed on desktop only'))
@pytest.mark.task1
def test_wishlist_icon_task1(py, report_generator, width, height, displayType, location, testName):
    globalPage = GlobalPage(py, width, height, py.config.custom['environment']['homeUrl'])
    wishlistIcon = globalPage.getWishlistIcon()

    # Check that wishlist icon is hidden for mobile and tablet display
    if displayType == DESKTOP:
        wishlistIcon.should().be_visible()
    else:
        wishlistIcon.should().be_hidden()


# Check that left filter column is visible on desktop, hidden on mobile and tablet
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(HomePageMap.FILTER_COLUMN,
                                             'Left filter column is displayed on desktop only'))
@pytest.mark.task1
def test_filter_column_task1(py, report_generator, width, height, displayType, location, testName):
    homePage = HomePage(py, width, height, py.config.custom['environment']['homeUrl'])
    filterColumn = homePage.getFilterColumn()

    if displayType == DESKTOP:
        filterColumn.should().be_visible()
    else:
        filterColumn.should().be_hidden()


# Check that div top banner is always displayed
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(HomePageMap.TOP_BANNER_IMAGE,
                                             'Div top banner is always displayed'))
@pytest.mark.task1
def test_top_banner_task1(py, report_generator, width, height, displayType, location, testName):
    homePage = HomePage(py, width, height, py.config.custom['environment']['homeUrl'])
    topBannerImage = homePage.getTopBannerImage()

    # Check that topBannerImage is always visible
    topBannerImage.should().be_visible()


# Check that we only retrieve black results when filtering Black Shoes
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(HomePageMap.FILTER_COLOR_BLACK,
                                             'Search black shoes and check results'))
@pytest.mark.task2
def test_blackShoes_filter_task2(py, report_generator, width, height, displayType, location, testName):
    filterPage = HomePage(py, width, height, py.config.custom['environment']['homeUrl'])

    if displayType != DESKTOP:
        filterPage.openLeftSideFilter()

    productsFiltered = filterPage.getBlackColorProducts()

    # @TODO: work with developers in order to have color of results in the DOM
    # Here, I just check that the number of results is 2 and that
    # we only retrieve product_1 and product_8 and nothing else
    # which might not be true in the real world where product list is dynamic

    NbElements = productsFiltered.children().length()
    product1 = filterPage.getProduct_1()
    product2 = filterPage.getProduct_8()

    assert (NbElements == 2 and
            product1.get_attribute('href') == py.config.custom['environment']['productDetailUrl'] + '?id=1' and
            product2.get_attribute('href') == py.config.custom['environment']['productDetailUrl'] + '?id=8')


# Check that reference of the product is visible
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(ProductDetailPageMap.SMALL_REFERENCE_ID,
                                             'Check that reference of the product '
                                             'is visible in black shoes detail page'))
@pytest.mark.task3
def test_blackShoesDetail_reference_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)

    # "displayed" means that the element is in the DOM and has a size
    #  greater than zero such that it is visible to the user.
    # @Todo: so it returns true even if element is not visible (white on white).
    #  getCssValue not supported by pylenium :/
    reference = filterPage.getReference()
    # refWebElement = reference.webelement
    # backgroundColor = refWebElement.getCssValue("background-color")
    # color = refWebElement.getCssValue("color")
    # print("Color: "+color)
    # print("backgroundColor: " + backgroundColor)
    assert (reference.is_displayed())
    # and backgroundColor != color)


# Check that default size is Small (S)
# @Todo But maybe we should use a list of available sizes !?
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(ProductDetailPageMap.NICE_SELECT_SIZE,
                                             'Check that default size of the product is \'Small (S)\' '
                                             'in black shoe detail page'))
@pytest.mark.task3
def test_blackShoesDetail_defaultSize_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)

    filterPage.getDefaultSize().should().have_text('Small (S)')


# Check that price is correctly displayed with decimals
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(ProductDetailPageMap.NEW_PRICE_LABEL,
                                             'Check that price of the product contains .00 in black shoe detail page'))
@pytest.mark.task3
def test_blackShoesDetail_price_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)

    # Using a regexp to check that price starts with $, then several digit, then a '.' and 2 more digits
    assert re.search("[$][0-9]+.[0-9]{2}", filterPage.getPrize()) is not None


# Check that topTools icons (heart, profile and basket) don't overlap
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(GlobalPageMap.PROFILE_ICON,
                                             'Check that topTools icons (heart, profile and basket) '
                                             'don t overlap in black shoe detail page'))
@pytest.mark.task3
def test_blackShoesDetail_topToolsIcons_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)
    filterPage.useGlobalPageMap() # Elements Cart_Button, Profile_icon and Wishlist_icon are in GlobalPage

    assert filterPage.checkTopToolsIconsNotOverlapping()


# Check that rating stars and reviews are not overlapping
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(ProductDetailPageMap.RATING_COUNT,
                                             'Check that rating stars and reviews '
                                             'are not overlapping in black shoe detail page'))
@pytest.mark.task3
def test_blackShoesDetail_ratingStarReviews_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)

    # @Todo: ID has been changed from "#EM____82" (v1) to "#EM__ratingcoun__82" (v2) :'(
    # Issue (33934) created : 3) Hackathon – App issue: Rating count ID has been changed between v1 and v2
    # Change ID in ProductDetailPageMap
    assert filterPage.checkRatingReviewOverlapping()


# Check default quantity is 1
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(ProductDetailPageMap.DEFAULT_QUANTITY,
                                             'Check default quantity is 1 in black shoe detail page'))
@pytest.mark.task3
def test_blackShoesDetail_quantityAddToCart_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)

    assert filterPage.getDefaultQuantity() == '1'


# Check that Add to Cart button is enabled by default
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(ProductDetailPageMap.BUTTON_ADD_TO_CART,
                                             'Check that Add to Cart button is enabled by default '
                                             'in black shoe detail page'))
@pytest.mark.task3
def test_blackShoesDetail_addToCardButton_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)

    assert filterPage.getButtonAddToCart().is_enabled()


# Check product preview display
@pytest.mark.parametrize("width,height,displayType,location,testName",
                         TestData.forElement(ProductDetailPageMap.SHOE_IMAGE,
                                             'Check that product preview '
                                             'is displayed in black shoe detail page'))
@pytest.mark.task3
def test_blackShoesDetail_productPrevDisplay_task3(py, report_generator, width, height, displayType, location, testName):
    filterPage = ProductDetailPage(py, width, height, py.config.custom['environment']['productDetailUrl'], backShoe1Page)
    styleShoeImage = filterPage.getShoeImage()

    assert 'url' in styleShoeImage
