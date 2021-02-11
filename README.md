# fmd-npm
Find dependencies from package.json which are missing from npm.js

## Setup

Install dependencies

```bash
$ pip install -r requirements.txt
```

## Usage

1. Open scan.py
2. Change `CURRENT_MODE` to required mode based on your requirement
3. Add list of `URLs` or `FILEs` based on your requirement
4. Save the changes
5. Run using the commad 

```bash
$ python scan.py
```

### Sample Output

```
---------------------------
Current Settings
Mode: file
Value: package.json
---------------------------



Processing:  JSONStream
Processing:  abbrev
Processing:  codermak

----------BROKEN----------
Name: codermak
Version: 5.7.1
----------BROKEN----------

Processing:  arshadkazmi42

----------BROKEN----------
Name: arshadkazmi42
Version: 3.0.1
----------BROKEN----------




--------PACKAGES VULNERABLE TO TAKEOVER-----------
[
  {
    "Name": "codermak",
    "Version": "5.7.1",
    "URL": "https://www.npmjs.com/package/codermak"
  },
  {
    "Name": "arshadkazmi42",
    "Version": "3.0.1",
    "URL": "https://www.npmjs.com/package/arshadkazmi42"
  }
]
--------------------------------------------------

```
