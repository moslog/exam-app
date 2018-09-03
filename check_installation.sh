#!/bin/bash -e

GENERATORRC=$HOME/.generatorrc

cecho() {
  echo "$1 ->> menyimpan"
  echo $1 >> $2
}

aliasreq() {
  echo "$1 $2"
}

checkreq() {
  anaconda_bin="$HOME/anaconda3/bin"
  p3="$(which $1)3"
  p="$(which $1)"
  if [[ $p3 = *$anaconda_bin* ]]; then
    aliasreq $p3 "$13"
  elif [[ $p = *$anaconda_bin* ]]; then
    aliasreq $p $1
  else
    echo "Cannot run $1" 1>&2 # To stderr
    false # Stop execution when condition false. Shebang -e
  fi
}

PIPS=($(checkreq pip))
PIP=${PIPS[1]}

PYTHONS=($(checkreq python))
PYTHON=${PYTHONS[1]}

LOGIC_GENERATOR_LOG=$HOME/.logic_generator.log

cecho "Running with $PIP dan $PYTHON" $LOGIC_GENERATOR_LOG

pip-install() {
  for package in $@; do
    $PIP install $package --user
  done
}

create-run-script() {
  RUN_FILE=$HOME/.run.py
  printf 'import examapp as ea; ea.run()' > $RUN_FILE
  echo "PYTHON=$PYTHON" >> $GENERATORRC
  echo "alias run-generator='$PYTHON $RUN_FILE'" >> $GENERATORRC
  source $GENERATORRC
  echo "source $GENERATORRC" >> $HOME/.bashrc
}

pip-install bcrypt examapp
create-run-script

exit 0