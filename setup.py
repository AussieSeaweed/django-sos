import setuptools

setuptools.setup(
    name='django-sos',
    version='0.0.3',
    author='Juho Kim',
    author_email='juho-kim@outlook.com',
    description='A Django helper library',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AussieSeaweed/django-sos',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=['Django'],
)
