import setuptools


setuptools.setup(
    name="imgdler",
    version="2.0.0",
    description="画像ダウンロード用のライブラリ",
    author="sekine",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=["requests", "rich"],
)
