# https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/#creating-a-wheel-distribution
from setuptools import setup

# https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "pypi_readme.md").read_text()


try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

requirements = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=PipSession())



# https://stackoverflow.com/questions/41637275/how-can-a-readme-md-file-be-included-in-a-pypi-module-package-using-setup-py

setup(
  name = 'trialtracker',         # How you named your package folder (MyLib)
  packages = ['trialtracker'],   # Chose the same as "name"
  package_dir={"":"src"},
  version = '0.1.8',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Methods to extract and transform clinical trial data',   # Give a short description about your library
  
  # long_description="README.rst",
  long_description=long_description,
  long_description_content_type='text/markdown',

  author = 'Forrest',                   # Type in your name
  author_email = 'zfx0726@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/zfx0726/trialtracker',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/zfx0726/trialtracker/archive/refs/tags/v0.1.8.tar.gz',    # I explain this later on
  keywords = ['clinical', 'trial', 'eligibility','criteria','cancer','oncology','nlp'],   # Keywords that define your package best
  install_requires=[            # https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
  # pip list --format=freeze > requirements.txt
  [str(requirement.requirement) for requirement in requirements] # this is not best practice, yolo
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)