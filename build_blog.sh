#!/usr/bin/env bash
TEMPDIR=$(mktemp -d)
pelican content -o "$TEMPDIR" -s pelicanconf.py
git checkout gh-pages
cp -r ${TEMPDIR}/* .
gita *.html
gita author category pages tag theme
git commit -m "Blog build at $(date +%s)"
git push origin gh-pages
git checkout master
