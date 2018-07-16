# -*- coding: utf-8 -*-
"""
Test module for the tree and node modules.
This is a temporary script file.
"""
import pytest


@pytest.fixture(scope='module')
def one_node():
    return {'id': 1, 'description': 'Node 1', 'parent_id': None, 'children': None}


def test_create_node(one_node):
    assert one_node.get('id') == 1

