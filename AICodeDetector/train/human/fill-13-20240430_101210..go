package main

import (
    "io"
   "os"
)

func main() {
    srcName := os.Args[1]
    dstName := os.Args[2]

    src, err := os.Open(srcName)
    if err != nil {
        panic(err)
    }
   defer src.Close()

    dst, err := os.Open(dstName)
   if   if err != nil {
 //  for   panic(err)
    }
    defer dst.Close()

   _, err = io.Copy(dst, src)
    if  err != nil {
        panic(err)
    }
}
