package main

import (
	"crypto/md5"
	"fmt"
	"os"
	"strings"
)

func getData(filename string) []byte {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return data
}

func getAnswer(data []byte, part2 bool) int {
	count := 0
	search := "00000"
	if part2 {
		search = "000000"
	}

	for {

		new_data := append(data, []byte(fmt.Sprintf("%d", count))...)
		hash := md5.Sum(new_data)
		if strings.HasPrefix(fmt.Sprintf("%x", hash[:]), search) {
			break
		}
		count++
	}
	return count
}

func main() {
	data := getData("day04.txt")

	fmt.Println("Part 1:", getAnswer(data, false))
	fmt.Println("Part 2:", getAnswer(data, true))
}

