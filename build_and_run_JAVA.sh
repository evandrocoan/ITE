file_name=$(echo $1 | cut -d'.' -f 1)

javac $1
java $file_name
