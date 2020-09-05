from setuptools import setup

setup(
    name="Poketinder",
    version="1.0",
    description="Encuetra a tu pokemon ideal mediante una breve encuesta",
    author="Jesús Saldaña",
    url="URL o Email",
    packages=["Interface", "InternalProcessing"],
    install_requires=["datetime", "tkinter", "requests", "bs4", "webbrowser"]
)