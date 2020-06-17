class AppliFashionHomePage:

    def __init__(self, py, width, height, URL):
        self.py = py
        self.py.viewport(width, height, 'portrait')
        self.py.visit(URL)

    def getSearchField(self):
        Id = '#INPUTtext____42'
        return self.py.get(Id)

    def getWishlistIcon(self):
        Id = '#A__wishlist__52'
        return self.py.get(Id)

    def getFilterColumn(self):
        Id = '#filter_col'
        return self.py.get(Id)

    def getTopBannerImage(self):
        Class = '.top_banner'
        return self.py.get(Class)
