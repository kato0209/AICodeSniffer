
package main

import (
    "fmt"
)

func binarySearch(arr []int, target int) int {
    low := 0
    high := len(arr) - 1

    for low <= high {
        mid := low + (high-low)/2

        if arr[mid] < target {
            low = mid + 1
        } else if arr[mid] > target {
            high = mid - 1
        } else {
            return mid
        }
    }

    return -1
}

func main() {
    arr := []int{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
    target := 13

    result := binarySearch(arr, target)
    fmt.Println(result)
}