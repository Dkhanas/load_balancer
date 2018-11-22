#!/bin/bash

source venv/Scripts/activate
for VARIABLE in 8001 8002 8003 8004 8005 8006 8007 8008 8009 8010
do
   { python -c "import os; os.system(\"start /wait cmd /c microservice.py $VARIABLE \")" &};
done
