import pytest

from pages.HomePage import AppliFashionHomePage, HomePageMap

URL = 'https://demo.applitools.com/gridHackathonV1.html'

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

def initPage(py, width, height, URL):
    homePage = AppliFashionHomePage(py, width, height, URL)
    return homePage

@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.SEARCH_FIELD))
def test_search_field_task0(py, report_generator, width, height, displayType, location):
    homePage = initPage(py, width, height, URL)
    searchField = homePage.getSearchField()

    # Check that search field is hidden for mobile display only
    if displayType == MOBILE:
        searchField.should().be_hidden()
    else:
        searchField.should().be_visible()

# Check that wishlist icon (heart) is only displayed on desktop
@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.WISHLIST_ICON))
def test_wishlist_icon_task1(py, report_generator, width, height, displayType, location):
    homePage = initPage(py, width, height, URL)
    wishlistIcon = homePage.getWishlistIcon()

    # Check that wishlist icon is hidden for mobile and tablet display
    if displayType == DESKTOP:
        wishlistIcon.should().be_visible()
    else:
        wishlistIcon.should().be_hidden()


# Check that left filter column is only displayed on desktop
@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.FILTER_COLUMN))
def test_filter_column_task1(py, report_generator, width, height, displayType, location):
    homePage = initPage(py, width, height, URL)
    filterColumn = homePage.getFilterColumn()

    # Check that filter column is hidden for mobile and tablet display
    if displayType == DESKTOP:
        filterColumn.should().be_visible()
    else:
        filterColumn.should().be_hidden()


# Check that div top banner is always displayed
@pytest.mark.parametrize("width,height,displayType,location", TestData.forElement(HomePageMap.TOP_BANNER_IMAGE))
def test_top_banner_task1(py, report_generator, width, height, displayType, location):
    homePage = initPage(py, width, height, URL)
    topBannerImage = homePage.getTopBannerImage()

    # Check that topBannerImage is always visible
    topBannerImage.should().be_visible()
