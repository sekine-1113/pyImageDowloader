from imgdler.imdgler import ImageDownloader
from imgdler.generator import PathGenerator, MD5HashedPathGenerator
# v3.0.0~:
# from imgdler.generators import PathGenerator, MD5HashedPathGenerator
#              ~~~~~~~~~~


if __name__ == "__main__":
    target_url = "https://sample-img.lb-product.com/wp-content/themes/hitchcock/images/1KB.png"

    downloader = ImageDownloader(filename_generator=PathGenerator())
    hashed_downloader = ImageDownloader(filename_generator=MD5HashedPathGenerator())

    image1 = downloader.download(target_url)
    print(image1.path) # -> .\images\1KB.png
    image2 = hashed_downloader.download(target_url)
    print(image2.path)  # -> .\images\305313081da5f5b097e867a1f68f11c3.png
