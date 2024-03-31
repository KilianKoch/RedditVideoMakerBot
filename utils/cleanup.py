import shutil
from os import listdir
from os.path import isfile, join, exists
from pathlib import Path

# Wasn't used anywhere
# def _listdir(d):  # listdir with full path
#     return [os.path.join(d, f) for f in os.listdir(d)]


def cleanup(reddit_id=-1) -> int:
    """Deletes all temporary assets in assets/temp. If reddit_id is -1, deletes all assets in the temp folder.

    Args:
        reddit_id (int, optional): The Reddit post ID or -1 to clean the entire temp folder. Defaults to -1.

    Returns:
        int: How many files or directories were deleted.
    """
    if reddit_id == -1:
        directory = "assets/temp/"
    else:
        directory = f"assets/temp/{reddit_id}/"
    
    file_count = 0

    if exists(directory):
        if reddit_id == -1:
            # Delete everything in the temp directory
            for item in listdir(directory):
                item_path = join(directory, item)
                if isfile(item_path):
                    os.unlink(item_path)
                    file_count += 1
                else:  # If it's a directory
                    shutil.rmtree(item_path)
                    file_count += 1
        else:
            # Delete specific reddit_id directory
            shutil.rmtree(directory)
            file_count = 1  # Since it's a single action for a directory, we count it as one

    return file_count