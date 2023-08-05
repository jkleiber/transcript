@echo off

set container="transcript-dev-container"

docker exec -it %container% /bin/bash
@REM docker exec -it %container% env TERM=xterm-256color script -q -c "/bin/bash" /dev/null