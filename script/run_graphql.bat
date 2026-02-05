@echo off
call "%~dp0config.bat"
echo Starting GraphQL Persona Service on port 6001...
python %DEFAULT_PROJ_ROOT%\src\api_test\graphql_test.py 6001
