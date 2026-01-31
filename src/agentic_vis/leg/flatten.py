
def flatten_names_with_depth(data: dict) -> dict:
    """Flatten all values with key 'name' into a mapping of name -> depth.

    Depth is counted from each top-level key in the provided mapping. For each
    top-level key (e.g. 'l1') the depth of its immediate children starts at 1.

    Examples (shape):
    - 'l1' (top-level key) -> its child 'l2_a' has depth 1 when we enter its
        value; a 'name' inside 'l2_a' will therefore be recorded with depth 2.

    Args:
        data: Nested mapping following the user's structure.

    Returns:
        dict: mapping of each encountered name (string) to its integer depth.
    """

    result: dict = {}

    def _walk(node, depth: int):
        # node can be dict, list, or scalar
        if isinstance(node, dict):
            # If this dict has a 'name' key, record it at current depth
            if 'name' in node and isinstance(node['name'], str):
                result[node['name']] = depth

            for k, v in node.items():
                # Skip the 'name' key itself but traverse other values
                if k == 'name':
                    continue
                # Recurse into children, incrementing depth for nested structures
                if isinstance(v, (dict, list)):
                    _walk(v, depth + 1)
                # Scalars under other keys are ignored except 'name'
        elif isinstance(node, list):
            for item in node:
                _walk(item, depth + 1)

    # Iterate top-level keys; entering each top-level value starts at depth=1
    if isinstance(data, dict):
        for key, value in data.items():
            _walk(value, 1)

    return result

