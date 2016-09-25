#!/bin/bash

echo "Hello, I will create a new assignment project for you, now I need to define what course this project is"

PS3='Choose course: '

dirs=`ls`

printf "Please select folder:\n"
select d in $dirs "Quit";
do
	test "$d" == "Quit" && exit;
	test -n "$d" && break;
	echo "Invalid Selection";
done

read -p 'Enter assignment name: ' name

[[ !(-d "$d/labs") ]] && mkdir -p "$d/labs"

list=($d/labs/lab_*[0-9])
last=${list[@]: -1}

current_number=`echo ${last} | grep -o "[0-9]\*" | bc`

nextnum=$((1+${current_number:=0}))

new_folder=$d/labs/lab_${nextnum}

cp -r ./.template ${new_folder}

sed -e "s/#ASSNUMBER#/${nextnum}/g" .template/template.tex | \
sed -e "s/#ASSNAME#/${name}/g" > ${new_folder}/lab_${nextnum}.tex

rm -f ${new_folder}/template.tex