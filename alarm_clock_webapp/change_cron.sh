#! /bin/bash
#sudo dpkg-reconfigure tzdata (per cambiare la time zone del tuo dispositivo)
#crontab -l > /home/pi/alarm_clock_webapp/cron_check.txt #just a check of the cron jobs before changing them
if [[ "$3" == "wd" ]] #working day
then
    if [[ "$4" == "" ]] #not updating dir
    then
	crontab -l | awk -v min=$2 -v hours=$1 '{ if ($3 == "*" && $5 == "1-5" && $6 ~ /\/alarm_clock_pi.sh/ ) {$1 = min; $2 = hours; print} else {print} }' | crontab -
    else #updating dir
	crontab -l | awk -v min=$2 -v hours=$1 -v dir=$4 '{ if ($3 == "*" && $5 == "1-5" && $6 ~ /\/alarm_clock_pi.sh/ ) {$1 = min; $2 = hours; $7 = dir; print} else {print} }' | crontab -
    
    fi
    crontab -l | awk -v min=$2 -v hours_plus1=$(( $1 + 1 )) '{ if ($3 == "*" && $5 == "1-5" && $6 ~ /\/killer_alarm/ ) {$1 = min; $2 = hours_plus1; print} else {print} }' | crontab -

elif [[ "$3" == "we" ]] #week-end
then
    if [[ "$4" == "" ]] #not updating dir
    then
	crontab -l | awk -v min=$2 -v hours=$1 '{ if ($3 == "*" && $5 == "6-7" && $6 ~ /\/alarm_clock_pi.sh/ ) {$1 = min; $2 = hours; print} else {print} }' | crontab -
    else #updating dir
	crontab -l | awk -v min=$2 -v hours=$1 -v dir=$4 '{ if ($3 == "*" && $5 == "6-7" && $6 ~ /\/alarm_clock_pi.sh/ ) {$1 = min; $2 = hours; $7 = dir; print} else {print} }' | crontab -
    
    fi
    crontab -l | awk -v min=$2 -v hours_plus1=$(( $1 + 1 )) '{ if ($3 == "*" && $5 == "6-7" && $6 ~ /\/killer_alarm/ ) {$1 = min; $2 = hours_plus1; print} else {print} }' | crontab -
fi
#else
#un particolare cron job per un giorno solo







