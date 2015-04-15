printf "Upgrading HPCScan.\n"
cd ~/hpcscan
if git pull --rebase --stat origin master
then
    printf "Update successful.\n"
else
    printf "Update failed. Please try again later.\n"
fi
