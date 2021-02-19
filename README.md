# fmd-npm
Find dependencies from package.json which are missing from npm.js

## Setup

Install dependencies

```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python scan.py {URL}
```

## Example

```bash
$ python scan.py https://raw.githubusercontent.com/arshadkazmi42/firefox-cookie/a5d38a3fa0d6dbdc812298bb095d345cc1f6c29e/package-lock.json
```

## Tips

This can be combined with [gh-spj](https://github.com/arshadkazmi42/gh-spj)

### Example

```
$ python scrap.py arshadkazmi42 | xargs -I {} python scan.py {}
```
