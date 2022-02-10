#!/bin/bash

# install R/cran
sudo apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common -y
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
sudo apt install r-base -y
R --version

# install git
sudo apt install git -y

# install pip
sudo apt install pip -y

# pip installs
pip install pandas numpy ipython jupyter scikit-learn flask pysqlite3

# install Anaconda3 v2019.10
sudo apt install curl -y
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
bash Anaconda3-2019.10-Linux-x86_64.sh
rm Anaconda3-2019.10-Linux-x86_64.sh
source ~/.bashrc
conda list

# conda installs
conda install keras pytorch tensorflow

# update packages
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt autopurge -y

echo "Installs Complete."

