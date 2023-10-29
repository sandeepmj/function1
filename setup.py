import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='function1',
    version='0.0.2',
    author='Sandeep Junnarkar',
    author_email='sjnews@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sandeepmj/function1',
    project_urls = {
        "Bug Tracker": "https://github.com/sandeepmj/function1/issues"
    },
    license='MIT',
    packages=['mytools'],
    install_requires=['requests'],
)