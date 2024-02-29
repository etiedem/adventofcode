package main

import (
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

func countVowels(s string) int {
	vowels := "aeiou"
	count := 0
	for _, c := range s {
		if strings.Contains(vowels, string(c)) {
			count++
		}
	}
	return count
}

func hasDouble(s string) bool {
	for i := 0; i < len(s)-1; i++ {
		if s[i] == s[i+1] {
			return true
		}
	}
	return false
}

func part1(s string) bool {
	if strings.Contains(s, "ab") ||
		strings.Contains(s, "cd") ||
		strings.Contains(s, "pq") ||
		strings.Contains(s, "xy") {
		return false
	}
	if countVowels(s) >= 3 && hasDouble(s) {
		return true
	}
	return false
}

func hasRepeatingPair(s string) bool {
	for i := 0; i < len(s)-3; i++ {
		if strings.Contains(s[i+2:], s[i:i+2]) {
			return true
		}
	}
	return false
}

func hasRepeatingLetter(s string) bool {
	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+2] {
			return true
		}
	}
	return false
}

func part2(s string) bool {
	if hasRepeatingPair(s) && hasRepeatingLetter(s) {
		return true
	}
	return false
}

func countNice(data []byte, ispart2 bool) int {
	count := 0
	for _, line := range strings.Split(string(data), "\n") {
		if !ispart2 && part1(line) {
			count++
		} else if ispart2 && part2(line) {
			count++
		}
	}
	return count
}

func main() {
	data := getData("day05.txt")

	fmt.Println("Part 1:", countNice(data, false))
	fmt.Println("Part 2:", countNice(data, true))
}

