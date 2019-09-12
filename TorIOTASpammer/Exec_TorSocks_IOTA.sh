#!/bin/bash

while true
do
  sudo service tor restart
  torsocks python TorScriptIOTA.py
  torsocks curl icanhazip.com
  sleep 0.1
done