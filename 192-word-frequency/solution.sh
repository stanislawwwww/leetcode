cat words.txt | grep -Eo '[a-z]+' | sort | uniq -c | sort -k 1n | tac | awk '{ print $2 " " $1 }'