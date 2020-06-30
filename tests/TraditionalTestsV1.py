import pytest

from pages.HomePage import AppliFashionHomePage, HomePageMap

MOBILE = 0
TABLET = 1
DESKTOP = 2


class TestData:
    # (Width, Height, type of display (0, 1, 2) and element path?)
    @classmethod
    def forElement(cls, cssPath):
        return [
            (375, 500, MOBILE, cssPath),
            (767, 700, MOBILE, cssPath),
            (768, 500, TABLET, cssPath),
            (991, 700, TABLET, cssPath),
            (992, 500, DESKTOP, cssPath),
            (1200, 700, DESKTOP, cssPath)
        ]


# Check that search field is displayed on tablet and desktop, hidden on mobile
@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.SEARCH_FIELD))
def test_search_field_task1(py, report_generator, width, height, displayType, location):
    homePage = AppliFashionHomePage(py, width, height, py.config.custom['environment']['url'])
    searchField = homePage.getSearchField()

    # Check that search field is hidden for mobile display only
    if displayType == MOBILE:
        searchField.should().be_hidden()
    else:
        searchField.should().be_visible()


# Check that wishlist icon (heart) is only displayed on Desktop
@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.WISHLIST_ICON))
def test_wishlist_icon_task1(py, report_generator, width, height, displayType, location):
    homePage = AppliFashionHomePage(py, width, height, py.config.custom['environment']['url'])
    wishlistIcon = homePage.getWishlistIcon()

    # Check that wishlist icon is hidden for mobile and tablet display
    if displayType == DESKTOP:
        wishlistIcon.should().be_visible()
    else:
        wishlistIcon.should().be_hidden()


# Check that left filter column is visible on laptop, hidden on mobile and tablet
@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.FILTER_COLUMN))
def test_filter_column_task1(py, report_generator, width, height, displayType, location):
    homePage = AppliFashionHomePage(py, width, height, py.config.custom['environment']['url'])
    filterColumn = homePage.getFilterColumn()

    if displayType == DESKTOP:
        filterColumn.should().be_visible()
    else:
        filterColumn.should().be_hidden()


# Check that div top banner is always displayed
@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.TOP_BANNER_IMAGE))
def test_top_banner_task1(py, report_generator, width, height, displayType, location):
    homePage = AppliFashionHomePage(py, width, height, py.config.custom['environment']['url'])
    topBannerImage = homePage.getTopBannerImage()

    # Check that topBannerImage is always visible
    topBannerImage.should().be_visible()


# Check that we only retrieve black results when filtering Black Shoes
@pytest.mark.parametrize("width,height, displayType, location", TestData.forElement(HomePageMap.PRODUCT_GRID))
def test_blackShoes_filter_task2(py, width, height, displayType, location):
    filterPage = AppliFashionHomePage(py, width, height, py.config.custom['environment']['url'])

    if displayType != DESKTOP:
        filterPage.openLeftSideFilter().click()

    filterPage.checkBlackColorInFilter()

    filterPage.getFilterButton().click()

    productsFiltered = filterPage.getProductGrid()

    # @TODO: work with developers in order to have color of results in the DOM
    # Here, I just check that we only retrieve product_1 and product_8 and nothing else
    # which might not be true in the real world where product list is changed
    assert productsFiltered.children().length() == 2
