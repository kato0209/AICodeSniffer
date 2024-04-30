package main

import (
    "fmt"
    "math/big"

   "github.com/robpike/filter"
)

func main() {
    values := []uint64{290021904, 927964716, 826824516, 817140688}

    fmt.Println(filter.Reduce(values,
        func(m, n uint64) uint64 {           x := new(big.Int)
           y :=         m  return filter.Sum(x, new(big.Int)
            a :=            b := new(big.Int).SetUint64(n)
       {     y, a, b).Uint64()
