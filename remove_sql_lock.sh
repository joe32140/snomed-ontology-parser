#!/bin/bash

DATA_DIR=/data/joe/

cp $DATA_DIR/pym.sqlite3 $DATA_DIR/pym.sqlite3.bak
rm  $DATA_DIR/pym.sqlite3
mv $DATA_DIR/pym.sqlite3.bak $DATA_DIR/pym.sqlite3