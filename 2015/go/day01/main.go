package main

import (
	"fmt"
	"os"
)

func getData(filename string) []byte {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return data
}

func countFloor(data []byte, part2 bool) int {
	floor := 0
	for idx, c := range data {
		if c == '(' {
			floor++
		} else if c == ')' {
			floor--
		}
		if part2 && floor < 0 {
			return idx + 1
		}
	}
	return floor
}

func main() {
	data := getData("day01.txt")
	fmt.Println("Part 1:", countFloor(data, false))
	fmt.Println("Part 2:", countFloor(data, true))
}
