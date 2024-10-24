package main

import (
	"bytes"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"unicode"
)

func getData(filename string) []byte {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return data
}

func getDigit(data []byte) int {
	var first rune
	var last rune
	for _, item := range string(data) {
		if unicode.IsDigit(item) {
			last = item
			if first == '\u0000' {
				first = last
			}
		}
	}
	digit := fmt.Sprintf("%c%c", first, last)
	output, err := strconv.Atoi(digit)
	if err != nil {
		panic(fmt.Errorf("Failed to convert %s to an Integer", digit))
	}
	return output
}

func getNumber(data []byte) int {
	query := "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine"
	conv := map[string]int{
		"1":     1,
		"2":     2,
		"3":     3,
		"4":     4,
		"5":     5,
		"6":     6,
		"7":     7,
		"8":     8,
		"9":     9,
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
	re := regexp.MustCompile(query)

	// Hack to find overlapping matches
	var items [][]byte
	for i := 0; i < len(data); i++ {
		m := re.FindIndex(data[i:])
		if m != nil {
			items = append(items, data[i+m[0]:i+m[1]])
		}
	}

	digit := fmt.Sprintf("%d%d", conv[string(items[0])], conv[string(items[len(items)-1])])
	output, err := strconv.Atoi(digit)
	if err != nil {
		panic(fmt.Errorf("Failed to convert %s to an Integer", digit))
	}
	return output

}

func solve(data []byte, f func([]byte) int) int {
	var output int
	for _, line := range bytes.Split(data, []byte("\n")) {
		if len(line) == 0 {
			continue
		}
		number := f(line)
		output += number
	}
	return output
}

func main() {
	data := getData("day01.txt")
	// fmt.Println(string(data))

	getNumber([]byte("1alk;sdjfalkjdfnine"))
	fmt.Println("Part 1:", solve(data, getDigit))
	fmt.Println("Part 2:", solve(data, getNumber))
}

