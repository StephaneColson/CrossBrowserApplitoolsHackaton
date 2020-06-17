import pytest

from pages.HomePage import AppliFashionHomePage

URL = 'https://demo.applitools.com/gridHackathonV1.html'

MOBILE = 0
TABLET = 1
DESKTOP = 2

# (Width, Height, type of display (0, 1, 2)?)
testData = [
    (375, 500, MOBILE),
    (767, 700, MOBILE),
    (768, 500, TABLET),
    (991, 700, TABLET),
    (992, 500, DESKTOP),
    (1200, 700, DESKTOP)
]

# def pass_or_fail(status):
#     if status:
#         return "Pass"
#     else:
#         return "Fail"


def initPage(py, width, height, URL):
    homePage = AppliFashionHomePage(py, width, height, URL)
    return homePage


# Check that search field is only displayed on tablet and desktop
@pytest.mark.parametrize("width,height,displayType", testData)
def test_search_field_task1(py, width, height, displayType):
    homePage = initPage(py, width, height, URL)
    searchField = homePage.getSearchField()

    # Check that search field is hidden for mobile display only
    if displayType == MOBILE:
        status = searchField.should().be_hidden()
    else:
        status = searchField.should().be_visible()

    # if isinstance(status, object):
    #     result = "Pass"
    # else:
    #     result = "Fail"
    # print("Avant HackathonReport")
    # HackathonReport(1,
    #                 "Search field is only displayed on tablet and mobile",
    #                 Id,
    #                 "Chrome",
    #                 {width, height},
    #                 display_type,
    #                 result)


# Check that wishlist icon (heart) is only displayed on desktop
@pytest.mark.parametrize("width,height,displayType", testData)
def test_wishlist_icon_task1(py, width, height, displayType):
    homePage = initPage(py, width, height, URL)
    wishlistIcon = homePage.getWishlistIcon()

    # Check that wishlist icon is hidden for mobile and tablet display
    if displayType == DESKTOP:
        status = wishlistIcon.should().be_visible()
    else:
        status = wishlistIcon.should().be_hidden()


# Check that left filter column is only displayed on desktop
@pytest.mark.parametrize("width,height,displayType", testData)
def test_filter_column_task1(py, width, height, displayType):
    homePage = initPage(py, width, height, URL)
    filterColumn = homePage.getFilterColumn()

    # Check that filter column is hidden for mobile and tablet display
    if displayType == DESKTOP:
        status = filterColumn.should().be_visible()
    else:
        status = filterColumn.should().be_hidden()


# Check that div top banner is always displayed
@pytest.mark.parametrize("width,height, displayType", testData)
def test_top_banner_task1(py, width, height, displayType):
    homePage = initPage(py, width, height, URL)
    topBannerImage = homePage.getTopBannerImage()

    # Check that topBannerImage is always visible
    status = topBannerImage.should().be_visible()
