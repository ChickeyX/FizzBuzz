#! /bin/bash

for i in {1..100}; do
  string=""
  (( $i % 3 == 0 )) && string+="Fizz"
  (( $i % 5 == 0 )) && string+="Buzz"
  echo ${string:-$i}
done
