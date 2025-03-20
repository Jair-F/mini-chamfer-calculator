cd $PSScriptRoot

$PYTHON_ZIP_PATH="deps/python.zip"
$GET_PIP_PATH="deps/get-pip.py"

mkdir "deps" | Out-Null
mkdir "python_3_10_10" | Out-Null

if (Test-Path($PYTHON_ZIP_PATH))
{
	echo "skipping python download - file exists"
}
else
{
	Invoke-WebRequest "https://www.python.org/ftp/python/3.10.10/python-3.10.10-embed-amd64.zip" -OutFile $PYTHON_ZIP_PATH
}
if (Test-Path($GET_PIP_PATH))
{
	echo "skipping get-pip download - file exists"
}
else
{
	Invoke-WebRequest "https://bootstrap.pypa.io/get-pip.py" -OutFile $GET_PIP_PATH
}

Expand-Archive -LiteralPath "deps/python.zip" -DestinationPath "python_3_10_10"

python_3_10_10\python.exe deps\get-pip.py
Remove-Item "python_3_10_10/python310._pth" -Force # because of that we cant run modules somhow
python_3_10_10\python.exe -m pip install -r requirements.txt

Remove-Item "deps" -Force -Recurse
