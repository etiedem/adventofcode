package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getData(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return strings.Split(string(data), "")
}

func solve(data []string) []string {
	output, last, count := []string{}, data[0], 1
	for _, item := range data[1:] {
		if item == last {
			count++
			continue
		}
		output = append(output, strconv.Itoa(count), last)
		count = 1
		last = item
	}
	output = append(output, strconv.Itoa(count), last)
	return output
}

func run(data []string, num int) []string {
	for x := 0; x < num; x++ {
		data = solve(data)
	}
	return data
}

func main() {
	data := getData("day10.txt")

	data = run(data, 40)
	fmt.Println("Part 1:", len(data))

	data = run(data, 10)
	fmt.Println("Part 2:", len(data))
}

