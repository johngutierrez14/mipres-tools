from setuptools import setup, find_packages

setup(
    name='mipres_tool',
    version='1.0.0',
    author='John E. Gutiérrez',
    author_email='johnegutierrez@gmail.com',
    description='Herramienta para descarga, limpieza y consolidación de archivos MIPRES para análisis en Power BI.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/johngutierrez14/mipres-tools.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'openpyxl',
        'tk',
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'mipres-tool=mipres_tool.main:main'
        ]
    },
)
