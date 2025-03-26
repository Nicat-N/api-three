class News:

    def __init__(self, tit, des, img):
        self.tit = tit
        self.des = des
        self.img = img

    
news1 = News(
    "Iphone 16 Pro Max",
    "The iPhone 16 Pro Max, released on September 20, 2024, is Apple's flagship smartphone, offering a range of advanced features and enhancements.",
    "https://github.com/Nicat-N/image/blob/main/Apple-iPhone-16-Pro-hero-240909-lp.jpg.news_app_ed.jpg?raw=true"
)

news2 = News(
    "AirPods Pro 2nd Gen",
    "The AirPods Pro 2nd Generation offers an upgraded audio experience with improved noise cancellation, adaptive transparency, and longer battery life.",
    "https://github.com/Nicat-N/image/blob/main/Apple-AirPods-Pro-2nd-gen-hero-220907_big.jpg.large.jpg?raw=true"
)

news3 = News(
    "Apple Watch S9",
    "The Apple Watch Series 9, introduced in September 2023, offers a range of advanced features designed to enhance health monitoring, fitness tracking, and daily convenience. ",
    "https://github.com/Nicat-N/image/blob/main/Apple-Watch-S9-SiP-230912.jpg.large_2x.jpg?raw=true"
)

news_list = [news1, news2, news3]