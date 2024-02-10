from imgdler import ImageDownloader, FilenameGenerator, MD5HashedFilenameGenerator


if __name__ == "__main__":
    target_url = "https://sample-img.lb-product.com/wp-content/themes/hitchcock/images/1KB.png"

    downloader = ImageDownloader(filename_generator=FilenameGenerator())
    hashed_downloader = ImageDownloader(filename_generator=MD5HashedFilenameGenerator())

    image1 = downloader.download(target_url)
    print(image1.path) # -> .\images\1KB.png
    image2 = hashed_downloader.download(target_url)
    print(image2.path)  # -> .\images\305313081da5f5b097e867a1f68f11c3.png
