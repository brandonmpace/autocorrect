from distutils.core import setup

setup(name='autocorrect',
      version='0.3.0',
      packages=['autocorrect'],
      package_data={'autocorrect': ['words.zip']},
      description='Python 3 Spelling Corrector',
      author='Jonas McCallum',
      author_email='jonasmccallum@gmail.com',
      url='https://github.com/phatpiglet/autocorrect/',
      license='http://www.opensource.org/licenses/mit-license.php',
      platforms=['any'],
      python_requires=">=3.6.5",
      classifiers=('Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',),
      keywords='autocorrect spelling corrector')
