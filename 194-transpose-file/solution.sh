columns_line=`cat file.txt | head -n 1 | wc -w`
for i in  $(seq 1 $columns_line); do
	qq=$(cat file.txt | awk "{ print \$$i }")
	echo $qq
done
