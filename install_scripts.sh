#!/bin/bash
filename=$1

sudo chmod +x $filename
sudo cp $filename /usr/local/bin
