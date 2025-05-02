python3 -m venv env

python3 -m venv docsenv

source docsenv/bin/activate

pip install -r requirements.txt
chgrp www-data ./code
chmod g+rwx  ./code
chmod 775 ./code -R

uvicorn main:app --reload --host 0.0.0.0 --port 8015