from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Medical Chatbot",
    version="1.0.0",
    author="Bod Mon Ro",
    packages=find_packages(),
    install_requires=requirements
)