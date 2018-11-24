#!/usr/bin/env python

import sys

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
    for s in ['id', 'label', 'source', 'target', 'value']:
        blob = blob.replace(s, '"%s":' % s)
    blob = blob.replace('\n"', ', "')
    blob = blob.replace('\n}', '}')
    return blob.strip('\n')

def main(graphfile):
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

	F = open("smallnetwork.json", 'w')
	nodes = gml_sub(nodes)
	edges = gml_sub(edges)
	F.write ('{\n  "nodes":[')
	F.write (nodes.rstrip(','))
	F.write ('  ],\n  "edges":[')
	F.write ('    ' + edges.rstrip(','))
	F.write ('  ]\n}\n')
	F.close()

if __name__ == '__main__':
	main(sys.argv[1])
