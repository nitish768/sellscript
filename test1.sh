rpm -q vlc
rpm -q firefox
rpm -q python2
rpm -q -a
rpm -q -a | grep python
rpm -q -f /user/bin/date
rpm -q -f /user/bin/python3
ls firefox #write only fire and tab it will give that verson and double tab give all verson or related
# rpm -i firefox with verson / rpm -e firefox with verson /install and uninstall
# rpm -i -v -h / i install v vervose h hash#
man rpm
rpm -q -i firefox # all info
rpm -q -l firefox # long list
# eog paste path of png / use this to change png pic with ur or any
wc file2.txt
wc < file2.txt
wc -l file2.txt
wc -w file2.txt
wc -c file2.txt
wc -l < file2.txt
rpm -qa
rpm -qa | wc -l
grep linux file2.txt
grep linux < file2.txt
grep linux
rpm -qu | grep python
rpm -qa | grep python | wc -l
rpm -qa | grep python | wc -l > file2.txt
ls
ls -l
ls -l | wc -l
ls -l | grep ^d
ls -l | grep ^d | wc -l 
ls -l | grep -n ^d
grep -n linux file2.txt
grep -v linux file2.txt
grep -v -n linux file2.txt
ls -l | grep ^d
ls -l | grep ^d | wc -l
ls -l | grep -v ^d | wc -l
date > file2.txt
date | wc -l
date | tee
date | tee file2.txt
date | tee | wc -w
date | tee file3.txt | wc -w
cat file2.txt

