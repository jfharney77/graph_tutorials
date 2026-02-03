@echo off
call "%~dp0config.bat"
echo Starting Echo Services on ports %ECHO_PORT1%, %ECHO_PORT2% and GraphQL on port %GRAPHQL_PORT% in separate tabs...
wt new-tab powershell -Command "python %ECHO_SERVER_PATH% %ECHO_PORT1%" ; ^
   new-tab powershell -Command "python %ECHO_SERVER2_PATH% %ECHO_PORT2%" ; ^
   new-tab powershell -Command "python %GRAPHQL_PATH% %GRAPHQL_PORT%"
