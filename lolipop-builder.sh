#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/home/users/2/parasite.jp-brush-me-up/web/api.motekuri.jp

if [ ! -d "$STORAGE_DIR/chrome" ]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/web/api.motekuri.jp # Make sure we return to where we were
else
  echo "...Using Chrome from cache"
fi