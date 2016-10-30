import sys
import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

import json

if len(sys.argv) < 4:
    print( "usage: "+str( sys.argv[0] )+" config-file local-file remote-name" )
    sys.exit(-1)

config_file_name = sys.argv[1]
file_name = sys.argv[2]
target_file = sys.argv[3]

with open( config_file_name, 'rb' ) as config_file:
    config = json.load( config_file )

client = dropbox.Dropbox(config["dropbox"]["token"])
account = client.users_get_current_account()

print( "Account: " + str( account ) )
with open( file_name, "rb" ) as f:
    client.files_upload( f.read(), target_file, mode=WriteMode('overwrite') )
