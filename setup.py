# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
from setuptools import setup

# https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
from pathlib import Path
# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text()


# https://stackoverflow.com/questions/41637275/how-can-a-readme-md-file-be-included-in-a-pypi-module-package-using-setup-py
import pypandoc

setup(
  name = 'trialtracker',         # How you named your package folder (MyLib)
  packages = ['trialtracker'],   # Chose the same as "name"
  package_dir={"":"src"},
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Methods to extract and transform clinical trial data',   # Give a short description about your library
  long_description=pypandoc.convert("README.md", "rst"),

  # long_description_content_type='text/markdown',

  author = 'Forrest',                   # Type in your name
  author_email = 'zfx0726@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/zfx0726/trialtracker',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/zfx0726/trialtracker/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['clinical', 'trial', 'eligibility','criteria','cancer','oncology','nlp'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'anyio>=2.2.0',
'appnope>=0.1.2',
'argon2-cffi>=20.1.0',
'async_generator>=1.1',
'attrs>=21.4.0',
'babel>=2.9.1',
'backcall>=0.2.0',
'bar_chart_race>=0.1.0',
'bcolz>=1.2.1',
'beautifulsoup4>=4.11.1',
'blas>=1',
'bleach>=4.1.0',
'bokeh>=2.3.2',
'brotlipy>=0.7.0',
'bs4>=4.11.1',
'bzip2>=1.0.8',
'ca-certificates>=2022.4.26',
'cachetools>=2.0.0',
'cairo>=1.14.12',
'certifi>=2021.5.30',
'cffi>=1.14.6',
'charset-normalizer>=2.0.4',
'click>=8.0.3',
'cloudpickle>=2.0.0',
'colorama>=0.4.5',
'contextvars>=2.4',
'cryptography>=35.0.0',
'cycler>=0.11.0',
'cytoolz>=0.11.0',
'dask>=2021.3.0',
'dask-core>=2021.3.0',
'dataclasses>=0.8',
'decorator>=5.1.1',
'defusedxml>=0.7.1',
'distributed>=2021.3.0',
'entrypoints>=0.3',
'expat>=2.4.4',
'ffmpeg>=4.3.2',
'fontconfig>=2.13.1',
'freetype>=2.10.4',
'fribidi>=1.0.10',
'fsspec>=2022.1.0',
'future>=0.18.2',
'gettext>=0.21.0',
'glib>=2.56.2',
'gmp>=6.2.1',
'gnutls>=3.6.15',
'google-api-python-client>=1.6.7',
'google-auth>=1.0.1',
'graphite2>=1.3.14',
'graphviz>=2.40.1',
'harfbuzz>=1.8.8',
'hdf5>=1.10.1',
'heapdict>=1.0.1',
'httplib2>=0.20.4',
'icu>=58.2',
'idna>=3.3',
'imageio>=2.6.1',
'immutables>=0.16',
'intel-openmp>=2020.2',
'ipykernel>=5.3.4',
'ipython>=7.16.1',
'ipython_genutils>=0.2.0',
'jedi>=0.17.0',
'jenkspy>=0.1.4',
'jinja2>=3.0.3',
'joblib>=0.13.2',
'jpeg>=9e',
'json5>=0.9.6',
'jsonschema>=3.0.2',
'jupyter_client>=7.1.2',
'jupyter_core>=4.8.1',
'jupyter_server>=1.4.1',
'jupyterlab>=3.2.1',
'jupyterlab_pygments>=0.1.2',
'jupyterlab_server>=2.10.3',
'kaleido-core>=0.2.1',
'kiwisolver>=1.3.1',
'krb5>=1.19.2',
'lame>=3.1',
'lcms2>=2.12',
'libblas>=3.9.0',
'libcblas>=3.9.0',
'libcxx>=12.0.0',
'libedit>=3.1.20210910',
'libffi>=3.3',
'libgfortran>=5.0.0',
'libgfortran5>=9.3.0',
'libiconv>=1.16',
'libidn2>=2.3.2',
'liblapack>=3.9.0',
'libpng>=1.6.37',
'libpq>=12.9',
'libprotobuf>=3.18.0',
'libsodium>=1.0.18',
'libtasn1>=4.16.0',
'libtiff>=4.2.0',
'libunistring>=0.9.10',
'libuv>=1.40.0',
'libwebp-base>=1.2.2',
'libxml2>=2.9.12',
'libxslt>=1.1.34',
'llvm-openmp>=14.0.3',
'locket>=0.2.1',
'lxml>=4.6.3',
'lz4-c>=1.9.3',
'lzo>=2.1',
'markupsafe>=2.0.1',
'mathjax>=2.7.7',
'matplotlib-base>=3.2.2',
'mistune>=0.8.4',
'mkl>=2019.4',
'mkl-service>=2.3.0',
'mkl_fft>=1.2.0',
'mkl_random>=1.1.1',
'msgpack-python>=1.0.2',
'nbclassic>=0.2.6',
'nbclient>=0.5.3',
'nbconvert>=6.0.7',
'nbformat>=5.1.3',
'ncurses>=6.3',
'nest-asyncio>=1.5.1',
'nettle>=3.7.3',
'nltk>=3.4.5',
'notebook>=6.4.3',
'numexpr>=2.7.3',
'numpy>=1.19.1',
'numpy-base>=1.19.1',
'oauth2client>=4.1.3',
'olefile>=0.46',
'onnx>=1.10.1',
'openai>=0.8.0',
'openh264>=2.1.1',
'openjdk>=8.0.332',
'openjpeg>=2.4.0',
'openssl>=1.1.1o',
'packaging>=21.3',
'pandoc>=2.12',
'pandocfilters>=1.5.0',
'pango>=1.42.4',
'parso>=0.8.3',
'partd>=1.2.0',
'patsy>=0.5.2',
'pcre>=8.45',
'pexpect>=4.8.0',
'pickleshare>=0.7.5',
'pillow>=8.3.1',
'pip>=21.2.2',
'pixman>=0.40.0',
'plotly>=5.8.0',
'prometheus_client>=0.13.1',
'prompt-toolkit>=3.0.20',
'protobuf>=3.18.0',
'psutil>=5.8.0',
'psycopg2>=2.8.6',
'ptyprocess>=0.7.0',
'pyasn1>=0.4.8',
'pyasn1-modules>=0.2.7',
'pycountry>=20.7.3',
'pycparser>=2.21',
'pydot>=1.4.1',
'pydotplus>=2.0.2',
'pygments>=2.11.2',
'pyopenssl>=22.0.0',
'pyparsing>=3.0.4',
'pyrsistent>=0.17.3',
'pysocks>=1.7.1',
'pytables>=3.4.2',
'python>=3.6.13',
'python-dateutil>=2.8.1',
'python-graphviz>=0.16',
'python-kaleido>=0.2.1',
'python_abi>=3.6',
'pytorch>=1.10.2',
'pytz>=2020.1',
'pyyaml>=5.4.1',
'pyzmq>=22.2.1',
'readline>=8.1.2',
'requests>=2.27.1',
'rsa>=3.4.2',
'scikit-learn>=0.24.2',
'scipy>=1.5.3',
'seaborn>=0.11.2',
'seaborn-base>=0.11.2',
'send2trash>=1.8.0',
'setuptools>=58.0.4',
'simplejson>=3.17.5',
'six>=1.15.0',
'sniffio>=1.2.0',
'sortedcontainers>=2.4.0',
'soupsieve>=2.3.1',
'sqlite>=3.38.2',
'statsmodels>=0.9.0',
'tblib>=1.7.0',
'tenacity>=8.0.1',
'terminado>=0.9.4',
'testpath>=0.5.0',
'threadpoolctl>=2.2.0',
'tk>=8.6.11',
'toolz>=0.11.2',
'torchvision>=0.11.3',
'tornado>=6.1',
'tqdm>=4.64.0',
'traitlets>=4.3.3',
'typing-extensions>=4.1.1',
'typing_extensions>=4.1.1',
'uritemplate>=3.0.1',
'urllib3>=1.26.8',
'wcwidth>=0.2.5',
'webencodings>=0.5.1',
'wheel>=0.37.1',
'wordcloud>=1.8.1',
'x264>=1!161.3030',
'xz>=5.2.5',
'yaml>=0.2.5',
'zeromq>=4.3.4',
'zict>=2.0.0',
'zlib>=1.2.11',
'zstd>=1.4.9'
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