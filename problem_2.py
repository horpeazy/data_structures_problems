import os
import sys

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not isinstance(path, str):
        sys.stderr.write("path must be a string\n")
        sys.exit()

    try:
        files = os.listdir(os.path.join(os.getcwd(), path))
    except FileNotFoundError:
        sys.stderr.write("file not found\n")
        sys.exit()

    output_files = []

    for file in files:
        curr_path = os.path.join(os.getcwd(), path, file)
        if os.path.isfile(curr_path):
            if file.endswith(suffix):
                output_files.append(file)
        elif os.path.isdir(curr_path):
            output_files += find_files(suffix, curr_path)

    return output_files

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".c", "testdir") )   # returns a list of all files ending with ".c"
# ['hope.c', 'a.c', 'burna.c', 'b.c', 'burna.c', 'ogbe.c', 'captain.c', 'a.c', 'james.c', 't1.c']

# Test Case 2
print(find_files("c", None) ) #returns path must be a string
# path must be a string

# Test Case 3
print(find_files("c", "/testdir") )   # returns file not found because path is given as an absolute path
# file not found

