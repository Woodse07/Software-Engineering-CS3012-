#!/usr/bin/env python

import sys
import re

def gml_sub(blob):

    lines = []
    for line in blob.split('\n'):
        line = line.strip()
        lines.append(line)
    blob = "\n".join(lines)

    blob = blob.replace('\n\n', '\n')
    blob = blob.replace(']\n', '},\n')
    blob = blob.replace('[\n', '{')
    blob = blob.replace('\n{', '\n    {')
    for s in ['id', 'label', 'source', 'target', 'value', 'level']:
        blob = blob.replace(s, '"%s":' % s)
    blob = blob.replace('\n"', ', "')
    blob = blob.replace('\n}', '}')
    return blob.strip('\n')

def main(graphfile, outfile):
    """
    Converts GraphML file to json
    Usage:
    >>> python convert.py mygraph.gml
    """

    with open(graphfile, 'r') as f:
        blob = f.read()
	blob = ''.join(blob.split('node')[1:])
	nodes = blob.split('edge')[0]
	edges = ''.join(blob.split('edge')[1:]).strip().rstrip(']')

	F = open(outfile, 'w')
	nodes = gml_sub(nodes)
	nodes = re.sub(r'([a-zA-Z]+)("id":)([a-zA-Z]+)', r'\1id\3', nodes)
	nodes = re.sub(r'([a-zA-Z]+)("id":)', r'\1id', nodes)
	nodes = re.sub(r'(""source":)([a-zA-z]+)', r'"\2', nodes)
	edges = gml_sub(edges)
	F.write ('{\n  "nodes":[')
	F.write (nodes.rstrip(','))
	F.write ('  ],\n  "edges":[')
	F.write ('    ' + edges.rstrip(','))
	F.write ('  ]\n}\n')
	F.close()


# Takes in two command line arguments, first is name of gml file, 2nd is name of output file. 
# Example:
# python gml2json_cli.py med_network.gml med_network.json
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
