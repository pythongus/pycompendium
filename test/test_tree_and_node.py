# -*- coding: utf-8 -*-
"""
Test module for the tree and node modules.
This is a temporary script file.
"""
import pytest
from pycompendium.node import create_node


@pytest.fixture(scope='module')
def one_node():
    return create_node(1, 'Node 1')


def test_create_node(one_node):
    assert one_node.get('id') == 1
    assert one_node.get('description') == 'Node 1'


def test_create_child_node(one_node):
    one_node['children'] = [create_node(2, 'Node 2', one_node['id'])]
    check = {'id': 2, 'description': 'Node 2', 'parent_id': 1, 'children': None}
    assert one_node['children'][0] == check


def test_create_tree(one_node):
    one_tree = {'root': create_node(1, 'Root')}
    assert one_tree['root']['id'] == 1

