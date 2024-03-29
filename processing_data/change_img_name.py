import os

def rename_files(directory):
  """Renames all files in a directory from 1 to the number of files.

  Args:
    directory: The path to the directory containing the files to rename.
  """
  files = os.listdir(directory)
  i = 1
  for filename in files:
    # Get the file extension (if any)
    # extension = os.path.splitext(filename)[1]
    # Construct the new filename with a sequential number and extension
    new_filename = f"{i}.jpg"
    # Create the full path for the new filename
    new_filepath = os.path.join(directory, new_filename)
    # Create the full path for the original filename
    old_filepath = os.path.join(directory, filename)
    # Rename the file
    os.rename(old_filepath, new_filepath)
    print(f'Rename file {i} successfully!')

    i += 1

# Get the directory path from the user (or set a default directory)
directory = r'C:\Users\phuen\PycharmProjects\SeleniumImportHeliosData\img\img_pool'

# Check if directory exists
if not os.path.isdir(directory):
  print(f"Error: Directory '{directory}' does not exist.")
else:
  # Rename files in the directory
  rename_files(directory)
  print(f"Files renamed successfully in directory: {directory}")
