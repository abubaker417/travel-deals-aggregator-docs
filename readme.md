**Setup Instructions**
1. Clone the repository:
```
git clone https://github.com/abubaker417/travel-deals-aggregator-docs.git
cd travel-deals-aggregator-docs

**Create Build**
docker-compose build

**Container Up**
docker-compose up

<!-- python3 -m venv env

python3 -m venv docsenv

source docsenv/bin/activate

pip install -r requirements.txt
chgrp www-data ./code
chmod g+rwx  ./code
chmod 775 ./code -R

uvicorn main:app --reload --host 0.0.0.0 --port 8015 -->