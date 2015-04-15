set -e

if [ ! -n "$HPCSCAN" ]; then
        HPCSCAN=~/hpcscan
fi 

echo "checking for pip"
if env pip --version > /dev/null
then
    echo "pip already installed. continuing."
    echo "checking for gitpython module"
    if env pip show gitpython > /dev/null
    then
        echo "gitpython module already installed, continuing"
    else
        echo "gitpython module not found. installing."
        env sudo pip install gitpython
    fi
else
    echo "pip not found. fetching..."
    env curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python
    echo "installed pip."
    echo "now installing gitpython module."
    env sudo pip install gitpython
fi

hash git >/dev/null 2>&1 && env git clone --depth=1 https://github.com/0xa1ed/hpcscan.git $HPCSCAN || {
  echo "please install git"
    exit
    }

export HPCSCAN=~/hpcscan
