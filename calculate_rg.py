import datetime
import os
import subprocess

from configuration import *

def calculate_replay_gain(path, path_content):
  LOGGER.info(f"Calculating replay gain for {path}")

  music_files = [f for f in path_content if os.path.isfile(os.path.join(path, f)) and any(extension in f for extension in ALLOWED_EXTENSIONS)]

  result = subprocess.run(
    [PYTHON3_PATH, REGAINER_PATH, *music_files],
    cwd=path,
    capture_output=True
  )

  LOGGER.info(result.args)

  stdout = result.stdout
  stderr = result.stderr

  if stdout:
    LOGGER.info(stdout.decode(sys.stdout.encoding))
  if stderr:
    LOGGER.error(stderr.decode(sys.stderr.encoding))

  if result.returncode == 0:
    LOGGER.info(f"Calculating replay gain for path {path} finished successfully")
  else:
    LOGGER.error(f"Calculating replay gain for path {path} finished with error")

def read_path(path):
  LOGGER.info(f"Examining path {path}")
  path_content = os.listdir(path)

  music_files_found = False

  for item in path_content:
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path) and any(extension in item for extension in ALLOWED_EXTENSIONS) and music_files_found is False:
      modified_at = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
      if modified_at > MODIFICATION_DATETIME_THRESHOLD:
        LOGGER.info(f"Path {path} has music files with allowed file extensions {ALLOWED_EXTENSIONS} and is modified ({modified_at}) later than {MODIFICATION_DATETIME_THRESHOLD}")
        music_files_found = True
        calculate_replay_gain(path, path_content)
    elif os.path.isdir(full_path):
      LOGGER.info(f"Found sub directory {full_path}")
      read_path(full_path)
