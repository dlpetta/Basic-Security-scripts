#!/bin/bash
for palavra in $(cat wordlist.txt)
do
resposta=$(curl -s -H "User-Agent: IDIC" -o /dev/null -w "%{http_code}" $1/$palavra/)
if [ $resposta == "200" ]
then
echo "Diretorio encontrado: $1/$palavra"
fi
done
