#!/bin/bash

#source $HOME/dotfiles/setup/setupnodejs.sh
#source venv/bin/activate
mkdir -p data
python3 json_to_sb.py --file $1
cd data
for f in $(ls *sb); do
	echo $f
	sed -i "s/^/\t/" $f  # for logseq
	$(npm bin)/sb2md $f > $(basename $f .sb).md
done
# rm *.sb
cd ..
python3 touch_md.py
tar czvf data.tar.gz data
