package main

import (
    "fmt"
)

// Binary search implementation in Golang
func binarySearch(arr []int, target int) int {
    left := 0
    right := len(arr) - 1

    for left <= right {
        mid := left + (right-left)/2

        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return -1
}

func main() {
    arr := []int{1, 5, 7, 9, 12, 15, 18, 22}
    target := 7
    result := binarySearch(arr, target)
    fmt.Println("Index of target:", result)
}