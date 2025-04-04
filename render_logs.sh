for file in content/log/*
do
  pandoc -f markdown --standalone --mathml -t html --embed-resources --css style/main.css -o log/$(basename ${file%.md}).html $file 
done

{
  cat content/log_header.md 
  for file in $(ls -r content/log/*.md)
  do
    echo
    echo "## $(basename ${file%.md})" # Markdown header with the filename
    echo
    cat "$file"
  done 
} | pandoc -f markdown --standalone --mathml -t html -o log.html --css style/main.css
