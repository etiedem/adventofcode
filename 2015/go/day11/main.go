package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

func getData(filename string) []byte {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return data
}

func string2Int(s string) []rune {
	output := []rune(s)
	for x := 0; x < len(output); x++ {
		output[x] -= 97
	}
	return output
}

func int2String(s []rune) string {
	output := []rune{}
	for _, x := range s {
		output = append(output, (x + 97))
	}
	return string(output)
}

func incrPassword(pw string) string {
	ints := string2Int(pw)
	slices.Reverse(ints)

	for x := 0; x < len(ints); x++ {
		ints[x] = (ints[x] + 1) % 26
		if ints[x] != 0 {
			break
		}
	}

	slices.Reverse(ints)
	return int2String(ints)
}

func overlapPairs(pw string) bool {
	count := 0
	for x := 1; x < len(pw); x++ {
		if pw[x-1] == pw[x] {
			count++
			x++
		}
	}
	return count > 1
}

func incrStraight(pw string) bool {
	r := []rune(pw)
	for x := 2; x < len(pw); x++ {
		if ((r[x-2] + 1) == r[x-1]) && ((r[x-1] + 1) == r[x]) {
			return true
		}
	}
	return false
}

func checkPass(pw string) bool {
	if strings.ContainsAny(pw, "iol") {
		return false
	}
	if !overlapPairs(pw) {
		return false
	}
	if !incrStraight(pw) {
		return false
	}
	return true
}

func solve(pw string) string {
	output := pw
	for {
		output = incrPassword(output)
		if checkPass(output) {
			break
		}
	}
	return output
}

func main() {
	data := getData("day11.txt")

	p1 := solve(string(data))
	fmt.Println("Part 1:", p1)

	p2 := solve(p1)
	fmt.Println("Part 2:", p2)
}

