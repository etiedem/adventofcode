package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

func getDataByLine(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return strings.Split(string(data), "\n")
}

func parse(line string) int {
	token_spec := [][]string{
		{"HEX", `\\x[0-9a-f]{2}`},
		{"BACKSLASH", `\\\\`},
		{"QUOTE", `\\\"`},
		{"CHAR", `[a-z]`},
	}

	var token_reg string
	for idx, pair := range token_spec {
		if idx > 0 {
			token_reg += "|"
		}
		token_reg += fmt.Sprintf("(?P<%s>%s)", pair[0], pair[1])
	}
	re := regexp.MustCompile(token_reg)
	items := re.FindAllString(line, -1)
	return len(items)
}

func solve(data []string) (int, int) {
	code, chars := 0, 0
	for _, line := range data {
		code += len(line)
		chars += parse(line)
	}

	return code, chars
}

func encode(data []string) []string {
	output := make([]string, len(data))
	for _, line := range data {
		line = strings.ReplaceAll(line, "\\", "\\\\")
		line = strings.ReplaceAll(line, "\"", "\\\"")
		line = "\"" + line + "\""
		output = append(output, line)
	}
	return output
}

func main() {
	data := getDataByLine("day08.txt")

	code1, chars1 := solve(data)
	fmt.Println("Part 1:", code1-chars1)

	code2, _ := solve(encode(data))
	fmt.Println("Part 2:", code2-code1)
}

