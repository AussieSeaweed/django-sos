import setuptools

with open('README.md', 'r') as long_description_file:
    long_description = long_description_file.read()

setuptools.setup(
    name='django-sos',
    version='0.0.1.dev2',
    author='Juho Kim',
    author_email='juho-kim@outlook.com',
    description='A Python package for various Django utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AussieSeaweed/django-sos',
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    install_requires=['Django'],
)
