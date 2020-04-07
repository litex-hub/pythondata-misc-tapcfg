# litex-data-misc-tapcfg

Non-Python data files required to use the tapcfg with
[LiteX](https://github.com/enjoy-digital/litex.git).

The data files can be found under the Python module `litex.data.misc.tapcfg`. The
`litex.data.misc.tapcfg.location` value can be used to find the files on the file system.

Example of getting the data file directly;
```python
import litex.data.misc.tapcfg

my_data_file = "abc.txt"

with open(os.path.join(litex.data.misc.tapcfg.data_location, my_data_file)) as f:
    print(f.read())
```

Example of getting the data file using `litex.data.find` API;
```python
from litex.data.find import find_data

my_data_file = "abc.txt"

with open(os.path.join(find_data("misc", "tapcfg"), my_data_file)) as f:
    print(f.read())
```


The data files come from https://github.com/enjoy-digital/tapcfg
and are imported using `git subtrees` to the directory
[litex/data/misc/tapcfg/data](litex/data/misc/tapcfg/data).



## Installing

## Manually

You can install the package manually, however this is **not** recommended.

```
git clone https://github.com/litex-hub/litex-data-misc-tapcfg.git
cd litex-data-misc-tapcfg
sudo python setup.py install
```

## Using [pip](https://pip.pypa.io/)

You can use [pip](https://pip.pypa.io/) to install the data package directly
from github using;

```
pip install --user git+https://github.com/litex-hub/litex-data-misc-tapcfg.git
```

If you want to install for the whole system rather than just the current user,
you need to remove the `--user` argument and run as sudo like so;

```
sudo pip install git+https://github.com/litex-hub/litex-data-misc-tapcfg.git
```

You can install a specific revision of the repository using;
```
pip install --user git+https://github.com/litex-hub/litex-data-misc-tapcfg.git@<tag>
pip install --user git+https://github.com/litex-hub/litex-data-misc-tapcfg.git@<branch>
pip install --user git+https://github.com/litex-hub/litex-data-misc-tapcfg.git@<hash>
```

### With `requirements.txt` file

Add to your Python `requirements.txt` file using;
```
-e git+https://github.com/litex-hub/litex-data-misc-tapcfg.git
```

To use a specific revision of the repository, use the following;
```
-e https://github.com/litex-hub/litex-data-misc-tapcfg.git@<hash>
```
