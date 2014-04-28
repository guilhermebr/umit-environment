#!/bin/sh

echo 'Preparing Umit Enviroment for dev'

cd /home/vagrant/umit
##### Creating virtualenv with access to global packages
virtualenv --system-site-packages env

##### Cloning Network Scanner
git clone https://github.com/umitproject/network-scanner.git
cd network-scanner
git checkout usoc2014
##### Cloning deps in deps/ directory
git submodule init
git submodule update
##### Installing deps
source /home/vagrant/umit/env/bin/activate && sh umit.sh deps

##### Installing Packet Manipulator
cd ..
git clone https://github.com/umitproject/packet-manipulator.git
cd packet-manipulator
git checkout usoc2014
pip install -r requirements.txt

echo 'End'
