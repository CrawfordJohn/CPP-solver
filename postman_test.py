#!/usr/bin/env python2.7
from __future__ import print_function

import unittest
import postman
import networkx as nx

class TestPostman(unittest.TestCase):
    def setUp(self):
        pass

    # TODO: test the individual functions

    def test_postman(self):
        """
        Test the end result.
        """
        with open('test_graph.csv', 'r') as csv:
            graph = postman.import_csv_graph(csv)
        components = postman.graph_components(graph)

        # Only use the largest component
        component = components[0]

        eulerian_graph, nodes = postman.single_chinese_postman_path(component)

        in_length = postman.edge_sum(graph) / 1000.0
        path_length = postman.edge_sum(eulerian_graph) / 1000.0
        duplicate_length = path_length - in_length
        nx.draw(eulerian_graph)
        self.assertAlmostEqual(in_length, 14.889)
        self.assertAlmostEqual(path_length, 20.316)
        self.assertAlmostEqual(duplicate_length, 5.427)


if __name__ == '__main__':
    unittest.main()
