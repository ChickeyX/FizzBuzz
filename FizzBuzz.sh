#! /bin/bash

for x in {1..100}; do
  string=""
  (( $x % 3 == 0 )) && string+="Fizz"
  (( $x % 5 == 0 )) && string+="Buzz"
  echo ${string:-$x}
done
