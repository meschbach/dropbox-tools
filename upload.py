import sys
import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

import json

import argparse
parser = argparse.ArgumentParser( description="Uploads a file to dropbox" )
parser.add_argument( 'config', nargs='?', default= None, help= 'Client configuration file' )
parser.add_argument( 'local', nargs='?', default= None, help= 'Local file to store download to' )
parser.add_argument( 'dropbox', nargs='?', default= None, help= 'Dropbox file to retreive' )

args = parser.parse_args()

config_file_name = args.config
file_name = args.local
target_file = args.dropbox

with open( config_file_name, 'r' ) as config_file:
    config = json.load( config_file )

client = dropbox.Dropbox(config["dropbox"]["token"])
account = client.users_get_current_account()

print( "Account: " + str( account ) )
with open( file_name, "rb" ) as f:
    client.files_upload( f.read(), target_file, mode=WriteMode('overwrite') )
