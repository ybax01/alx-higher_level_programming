#!/bin/bash

find . -name "*.py" -exec chmod u+x {} \;

git add .
git commit -m 'Rounding'
git push
