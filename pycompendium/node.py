"""
Functions for creating and updating a node.
"""


def create_node(node_id, description, parent_id=None, children=None):
    return {'id': node_id,
            'description': description,
            'parent_id': parent_id,
            'children': children}

