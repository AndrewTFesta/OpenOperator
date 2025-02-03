"""
@title

project_properties.py

@description

Common paths and attributes used by and for this project.

"""
import os
import shutil
import logging
from pathlib import Path

from dotenv import load_dotenv

# --------------------------------------------
# Project versioning and attributes
# --------------------------------------------
project_name = 'open_operator'
project_version = '0.1'
TIMEZONE = 'EST'

# --------------------------------------------
# Base paths for relative pathing to the project base
# --------------------------------------------
source_package = Path(__file__).parent
project_path = Path(source_package).parent

# --------------------------------------------
# Default project environment configuration
# --------------------------------------------
env_dir = Path(os.environ.get('ENV_DIR', project_path))
logging.basicConfig(level=logging.ERROR, format='[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')
load_dotenv(env_dir / '.env')

# --------------------------------------------
# Development and source directories
# --------------------------------------------
script_dir = Path(os.environ.get('SCRIPT_DIR', Path(project_path, 'scripts')))
notebook_dir = Path(os.environ.get('NOTEBOOK_DIR', Path(project_path, 'nb')))
execs_dir = Path(os.environ.get('EXECS_DIR', Path(project_path, 'execs')))

# --------------------------------------------
# Paths to store assets and related resources
# --------------------------------------------
resources_dir = Path(os.environ.get('RESOURCES_DIR', Path(project_path, 'resources')))
data_dir = Path(os.environ.get('DATA_DIR', Path(project_path, 'data')))
doc_dir = Path(os.environ.get('DOC_DIR', Path(project_path, 'docs')))
model_dir = Path(os.environ.get('MODEL_DIR', Path(project_path, 'models')))

# --------------------------------------------
# Output directories
# Directories to programs outputs and generated artefacts
# --------------------------------------------
output_dir = Path(os.environ.get('OUTPUT_DIR', Path(project_path, 'output')))
exps_dir = Path(os.environ.get('EXPS_DIR', Path(output_dir, 'exps')))
log_dir = Path(os.environ.get('LOG_DIR', Path(output_dir, 'logs')))
profile_dir = Path(os.environ.get('PROFILE_DIR', Path(output_dir, 'profile')))

# --------------------------------------------
# Cached directories
# Used for caching intermittent and temporary states or information
# to aid in computational efficiency
# no guarantee that a cached dir will exist between runs
# --------------------------------------------
cached_dir = Path(os.environ.get('CACHED_DIR', Path(project_path, 'cached')))

# --------------------------------------------
# Test directories
# Directories to store test code and resources
# --------------------------------------------
test_dir = Path(os.environ.get('test_dir', Path(project_path, 'test')))
test_config_dir = Path(os.environ.get('test_config_dir', Path(test_dir, 'config')))

# --------------------------------------------
# Resource files
# paths to specific resource and configuration files
# --------------------------------------------
config_dir = Path(os.environ.get('CONFIG_DIR', Path(project_path, 'configs')))
env_dir = Path(os.environ.get('ENV_DIR', Path(config_dir, 'envs')))

# --------------------------------------------
# Useful properties and values about the runtime environment
# --------------------------------------------
TERMINAL_COLUMNS, TERMINAL_ROWS = shutil.get_terminal_size()