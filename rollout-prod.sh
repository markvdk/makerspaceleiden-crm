#!/bin/sh
set -x
UK=$$

trap cleanup INT
cleanup () {
	test -f /tmp/backup.$UK && echo Warning - you will need to clean up the backup files in /tmp/*.$UK
}

(
set -e
. ./venv/bin/activate

pip install -r requirements.txt  --quiet

python manage.py dumpdata | gzip -c > /tmp/backup.$UK
test -d static && tar zcf /tmp/backup-static.$UK static

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate

sudo apachectl restart
)
E=$?

cleanup
exit $E
