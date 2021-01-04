import setuptools

setuptools.setup(
    name='django-sos',
    version='0.0.7',
    author='Juho Kim',
    author_email='juho-kim@outlook.com',
    description='A Django helper library',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AussieSeaweed/django-sos',
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.9',
    install_requires=['Django'],
)
