import os

# This should work for any system. Copy the path into a variable. This splits on / and unpacks the list properly
# If windows, your drive won't be recognized. You have to write out some variables; change it here for quick recall
# If you don't have issues with the drive not separating, enter it as a whole

# YOUR_PATH = os.path.join('YOUR_DRIVE', os.sep, 'REST_OF_YOUR_PATH')

CHAR_TO_REPLACE = '_'
CHAR_THAT_REPLACES = '\''


def get_files_in_directory():
    result = []
    directory = os.listdir(YOUR_PATH)
    for file in directory:
        result.append(file)
    return result


def rename_files(filename):
    new_name = filename.replace(CHAR_TO_REPLACE, CHAR_THAT_REPLACES)
    filename = os.path.join(YOUR_PATH, filename)
    new_filename = os.path.join(YOUR_PATH, new_name)
    os.rename(filename, new_filename)


if __name__ == '__main__':
    all_files = get_files_in_directory()
    for file in all_files:
        if '_' in file:
            rename_files(file)
            print(file+' changed.')
    print('Finished.')
