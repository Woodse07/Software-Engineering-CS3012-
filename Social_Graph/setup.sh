#!/bin/bash
# Setup Script

echo "Calling python script to generate Network..."
python network_generator.py
echo "Converting our gml files to json..."
python networks/gml2json_cli.py networks/smallnetwork.gml networks/smallnetwork.json
python networks/gml2json_cli.py networks/med_network.gml networks/med_network.json
echo "Spinning up Flask..."
python start.py
