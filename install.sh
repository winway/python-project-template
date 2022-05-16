#! /bin/bash
#

yum install python-devel
pip install -r requirements.txt

cp ./service/*.service /etc/systemd/system/
