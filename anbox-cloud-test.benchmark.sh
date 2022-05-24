#! /bin/bash

for i in {1..48} 
do
	anbox-cloud-tests.benchmark \
		--screen-width=1920 \
		--screen-height=1080 \
		--screen-fps=60 \
		--execution-time=10 \
		--application=bombsquad-stress \
		--url=https://10.76.87.226 \
		--auth-token=AgEUYW5ib3gtc3RyZWFtLWdhdGV3YXkCA2RldgACFDIwMjItMDQtMTlUMjI6NDQ6NDlaAAAGICH4K3l9Pd9fyQ49mHKFl3b2IzKSV5kFGiTY1FSTD99a \
		--report-path=/home/ubuntu/anbox/logs/anbox_report_$i.json \
		--format=json \
        	--insecure-tls &
	sleep 1	
done

