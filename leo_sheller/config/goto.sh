#!/bin/bash
BASE="$LEOsBASE";
ZERO=0;

read -r GOTO <<< `python -c "from leo_sheller import goto; goto.goto('$BASE', '$1')"`;
if [ $GOTO != $ZERO ] ; then
  cd $GOTO;
  return;
fi
