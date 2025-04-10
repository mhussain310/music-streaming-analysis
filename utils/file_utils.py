import os


def get_absolute_path(relative_path: str, root_dir: str = None) -> str:
    """
    Get the absolute file path from a relative path.

    :param relative_path: The relative path to the file.
    :param base_dir: The base directory to resolve the relative path from (defaults to the root of the project).
    :return: Absolute file path.
    """

    if root_dir is None:
        root_dir = find_project_root()

    return os.path.join(root_dir, relative_path)


def find_project_root(marker_file: str = "README.md"):
    """
    Find the root directory of the project by looking for a marker file.

    :param marker_file: The name of the marker file to look for.
    :return: The absolute path to the root directory of the project.
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir):
        if marker_file in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    raise FileNotFoundError(
        f"Marker file '{marker_file}' not found in any parent directories."
    )
