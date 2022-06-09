import json
with open('./ompugao.json') as f:
    data = json.load(f)

from slugify import slugify
import re
regex_pattern=re.compile(r'[\W_]+')
from datetime import datetime
import os
for page in data['pages']:
    createdtime = datetime.fromtimestamp(page['created'])
    updatedtime = datetime.fromtimestamp(page['updated'])
    title = page['title']
    filename = slugify(title, allow_unicode=True, lowercase=False, regex_pattern=regex_pattern)
    os.system(f"touch -d '{str(updatedtime)}' data/{filename}.md")

