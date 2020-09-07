from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-logmachine",
    version="0.1.0",
    author="Ed Chapman",
    author_email="ed@natoora.com",
    description="Django Log Machine client app.",
    long_description=long_description,
    url="https://github.com/Natoora/django-logmachine",
    packages=find_packages(exclude=['tests*']),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires='>=3.6',
    install_requires=[
        "Django>=3"
        "requests>=2",
        "djangorestframework>=3"
    ]
)
