package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getData(filename string) []byte {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return data
}

func getDim(data string) (length, width, height int) {
	d := strings.Split(data, "x")
	length, _ = strconv.Atoi(d[0])
	width, _ = strconv.Atoi(d[1])
	height, _ = strconv.Atoi(d[2])
	return
}

func getLength(data []byte) (int, int) {
	paper := 0
	ribbon := 0
	for _, d := range strings.Split(string(data), "\n") {
		l, w, h := getDim(d)

		// Calculate amount of paper needed
		slack := min(l*w, w*h, h*l)
		paper += (2 * l * w) + (2 * w * h) + (2 * h * l) + slack

		// Calculate amount of ribbon needed
		perimeter := 2 * (l + w + h - max(l, w, h))
		bow := l * w * h
		ribbon += perimeter + bow
	}
	return paper, ribbon
}

func main() {
	data := getData("day02.txt")

	part1, part2 := getLength(data)

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

