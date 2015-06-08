find . -type f -name '*.pdf' -print |
  while IFS= read -r file
    do convert -verbose -density 500 -resize 800 "${file}" "${file%.*}.png"
  done