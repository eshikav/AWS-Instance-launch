import commands

exitcode, output = commands.getstatusoutput("systemctl is-active mysql")

if output == "active":
	exit(0)	# when 0 is returned then state of instance will not change and it will retain IP
elif output == "unknown":
	#need to do this because if we directly check with systemctl is-active mysql then it returns unknown when ran first time after restart
	#or to avoid it we can add systemctl status mysql in the system start script so that whenever next time systemctl is-active mysql is run after system restarts also then it will return failed or active or inactive but not unknown
	commands.getstatusoutput("systemctl status mysql")
	exitcode, output = commands.getstatusoutput("systemctl is-active mysql")
	if output == "active":
		exit(0);
	else:
		exit(1);
else:
	exit(1) # when 1 is returned then state of instance will change to FAULT and it will relinquish IP