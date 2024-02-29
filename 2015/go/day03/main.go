package main

import (
	"fmt"
	"github.com/golang-collections/collections/set"
	"os"
)

type Point struct {
	x int
	y int
}

func (p *Point) move(direction byte) {
	switch direction {
	case '^':
		p.y++
	case 'v':
		p.y--
	case '>':
		p.x++
	case '<':
		p.x--
	}
}

func getData(filename string) []byte {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return data
}

func countHouses(data []byte) int {
	position := Point{0, 0}
	houses := set.New()
	houses.Insert(position)

	for _, direction := range data {
		position.move(direction)
		houses.Insert(position)
	}

	return houses.Len()
}

func part2(data []byte) int {
	santa := Point{0, 0}
	robot := Point{0, 0}
	houses := set.New()
	houses.Insert(santa)

	for idx, direction := range data {
		if idx%2 == 0 {
			santa.move(direction)
			houses.Insert(santa)
		} else {
			robot.move(direction)
			houses.Insert(robot)
		}
	}

	return houses.Len()
}

func main() {
	data := getData("day03.txt")

	fmt.Println("Part 1:", countHouses(data))
	fmt.Println("Part 2:", part2(data))
}

