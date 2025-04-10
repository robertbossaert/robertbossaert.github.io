Title: Convert Excel redirects to NGINX with Python
Date: 2025-04-10 08:11
Author: Robert Bossaert
Category: Python
Slug: convert-excel-redirects-to-nginx-with-python
Summary: A quick guide to converting Excel-based redirect lists into NGINX 301 rules using a simple Python script.

One of the tasks I often encounter as a developer is handling site migrations. A common part of that process is setting up URL redirects — and occasionally, a client provides us with an Excel file mapping old URLs to new ones.

While Excel is great for organizing data, it’s not ideal when you need to quickly generate NGINX-compatible redirect rules. Thankfully, there’s a simple way to automate this.

Below is a quick Python script I use to convert an .xlsx file into a list of NGINX rewrite directives for 301 (permanent) redirects.

## Python script

```python
import pandas as pd

df = pd.read_excel('redirects.xlsx')

for index, row in df.iterrows():
    old = str(row.iloc[0]).strip()
    new = str(row.iloc[1]).strip()
    print(f'rewrite ^{old}$ {new} permanent;')
```

This assumes your Excel file has:

* Column A: old relative path (e.g. /about)
* Column B: new relative path or absolute URL

## Requirements

Before running the script, make sure you have the following installed:

* Python v3
* The `pandas` and `openpyxl` libraries

You can install them in a virtual environment like so:

```sh
python3 -m venv ~/virtualenvs/nginx-redirects
source ~/virtualenvs/nginx-redirects/bin/activate

pip install pandas openpyxl
```

## Running the script

To execute the script:

```sh
python convert_redirects.py
```

This will output something along the lines of:

```txt
rewrite ^/old-page$ /new-page permanent;
rewrite ^/about$ /company/about permanent;
```

But if you want you can also save the result to a file by redirecting the output:

```sh
python convert_redirects.py > redirects.conf
```

You can then include this file in your NGINX configuration using:

```nginx
include /etc/nginx/snippets/redirects.conf;
```
