set -e

if [ ! -n "$HPCSCAN" ]; then
        HPCSCAN=~/hpcscan
fi 

hash git >/dev/null 2>&1 && env git clone --depth=1 https://github.com/0xa1ed/hpcscan.git $HPCSCAN || {
  echo "please install git"
    exit
    }

export HPCSCAN=~/hpcscan
