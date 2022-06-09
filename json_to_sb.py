# -*- coding: utf-8 -*-
from slugify import slugify
import json
import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args()
    with open(args.file) as f:
        data = json.load(f)

    regex_pattern=re.compile(r'[\W_]+')
    lspaces = re.compile(r'(^[ \t]+)')
    for page in data['pages']:
        title = page['title']
        newlines = []
        for line in page['lines']:
            m = lspaces.match(line)
            if m is None:
                newline = line
            else:
                newline = m.groups()[0].replace(" ", "\t") + m.string[m.end():]
            newlines.append(newline)
        content = '\n'.join(newlines)
        with open(f'data/{slugify(title, allow_unicode=True, lowercase=False, regex_pattern=regex_pattern)}.sb', 'w') as f:
            f.write(content)

