#1/bin/bash

if [ ! -f access.log ]; then
	echo "Файл отсутствует"
	exit 1
fi

request=$(awk 'END {print NR}' access.log)
unique=$(awk '{print $1}' access.log | sort | uniq | wc -l)



echo "Общее количество запросов:	$request"
echo "Количество уникальных IP-адресов:		$unique"

echo "Количество запросов по методам:"
awk '{gsub(/"/, "", $6); count[$6]++} END {for (m in count) print m, count[m]}' access.log


echo "Самый популярный URL:"
awk '{count[$7]++} END {max=0; popular=""; for (u in count) if (count[u]>max) {max=count[u]; popular=u} print popular, max}' access.log

