#!/usr/bin/bash
# -*- coding: utf-8 -*-

find ./ -name '*.py' | xargs python3 -m pydoc -w $
find ./ -name '*.html' | xargs sed -i -E 's/<a href=\"file:.*\/cardModel\/(.*)\">.*\/cardModel\/.*<\/a>/<a href=\"file:\.\/cardModel\/\1\">\.\/cardModel\/\1<\/a>/g'

