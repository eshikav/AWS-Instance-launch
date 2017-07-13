python /usr/sbin/keepalived_scripts/mysql_chk_script.py
if [ $? == 0 ]
then
	exit 0
else
	exit 1
fi
