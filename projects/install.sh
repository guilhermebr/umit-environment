#!/bin/sh

echo 'Preparing Umit Enviroment for dev'

cd /home/vagrant/umit
##### Creating virtualenv with access to global packages
virtualenv --system-site-packages env

##### Cloning Network Scanner
git clone --recursive git://github.com/umitproject/network-scanner.git
cd network-scanner
git checkout usoc2014
##### Cloning deps in deps/ directory
##### Installing deps

/bin/bash -c ". /home/vagrant/umit/env/bin/activate; sh umit.sh deps"

##### Installing Packet Manipulator
cd ..
git clone --recursive git://github.com/umitproject/packet-manipulator.git
cd packet-manipulator
git checkout usoc2014
/bin/bash -c ". /home/vagrant/umit/env/bin/activate; pip install -r requirements.txt"
cd deps/pygtkhex
/bin/bash -c ". /home/vagrant/umit/env/bin/activate; python setup.py install"
echo 'End'
