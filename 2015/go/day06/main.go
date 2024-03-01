package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Pos struct {
	x, y int
}

func (p Pos) Expand(other Pos) []Pos {
	output := []Pos{}
	for x := p.x; x <= other.x; x++ {
		for y := p.y; y <= other.y; y++ {
			output = append(output, Pos{x, y})
		}
	}
	return output
}

func NewPos(s string) Pos {
	items := strings.Split(s, ",")
	x, _ := strconv.Atoi(items[0])
	y, _ := strconv.Atoi(items[1])
	return Pos{x, y}
}

type Lights_1 struct {
	grid [1000][1000]bool
}

func (l Lights_1) Count() int {
	count := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			if l.grid[x][y] {
				count++
			}
		}
	}
	return count
}

type Lights_2 struct {
	grid [1000][1000]int
}

func (l Lights_2) Count() int {
	count := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			count += l.grid[x][y]
		}
	}
	return count
}
func getData(filename string) []byte {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return data
}

func part1(data []byte) int {
	r, _ := regexp.Compile(`(\D+) (\S+) through (\S+)`)
	lights := Lights_1{}
	for _, line := range strings.Split(string(data), "\n") {
		m := r.FindStringSubmatch(line)
		action := m[1]
		start := NewPos(m[2])
		end := NewPos(m[3])
		for _, p := range start.Expand(end) {
			switch action {
			case "turn on":
				lights.grid[p.x][p.y] = true
			case "turn off":
				lights.grid[p.x][p.y] = false
			case "toggle":
				lights.grid[p.x][p.y] = !lights.grid[p.x][p.y]
			}
		}
	}
	return lights.Count()
}

func part2(data []byte) int {
	r, _ := regexp.Compile(`(\D+) (\S+) through (\S+)`)
	lights := Lights_2{}
	for _, line := range strings.Split(string(data), "\n") {
		m := r.FindStringSubmatch(line)
		action := m[1]
		start := NewPos(m[2])
		end := NewPos(m[3])
		for _, p := range start.Expand(end) {
			switch action {
			case "turn on":
				lights.grid[p.x][p.y]++
			case "turn off":
				if lights.grid[p.x][p.y] > 0 {
					lights.grid[p.x][p.y]--
				}
			case "toggle":
				lights.grid[p.x][p.y] += 2
			}
		}
	}
	return lights.Count()
}
func main() {
	data := getData("day06.txt")

	fmt.Println("Part 1:", part1(data))
	fmt.Println("Part 2:", part2(data))
}

