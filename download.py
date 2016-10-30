import sys
import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import argparse

import json

if len(sys.argv) < 4:
    print( "usage: "+str( sys.argv[0] )+" config-file local-file remote-name" )
    sys.exit(-1)

parser = argparse.ArgumentParser(description="Download file from dropbox")
parser.add_argument( 'config', nargs='?', default= None, help= 'Client configuration file' )
parser.add_argument( 'local', nargs='?', default= None, help= 'Local file to store download to' )
parser.add_argument( 'dropbox', nargs='?', default= None, help= 'Dropbox file to retreive' )

args = parser.parse_args()
config_file_name = args.config
file_name = args.local
remote_file = args.dropbox

with open( config_file_name, 'rb' ) as config_file:
    config = json.load( config_file )

client = dropbox.Dropbox(config["dropbox"]["token"])
account = client.users_get_current_account()

print( "Account: " + str( account ) )
client.files_download_to_file( file_name, remote_file )
