package main

import (
	"fmt"
	"gonum.org/v1/gonum/stat/combin"
	"math"
	"os"
	"strconv"
	"strings"
)

var place map[string]int = map[string]int{
	"AlphaCentauri": 0,
	"Snowdin":       1,
	"Tambi":         2,
	"Faerun":        3,
	"Norrath":       4,
	"Straylight":    5,
	"Tristram":      6,
	"Arbre":         7,
}

func getDataByLine(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return strings.Split(string(data), "\n")
}

func createAdjacencyMatrix(data []string) [][]int {
	matrix := make([][]int, len(place))
	for i := range matrix {
		matrix[i] = make([]int, len(place))
	}
	for _, line := range data {
		if line == "" {
			continue
		}
		words := strings.Split(line, " ")
		matrix[place[words[0]]][place[words[2]]], _ = strconv.Atoi(words[4])
		matrix[place[words[2]]][place[words[0]]], _ = strconv.Atoi(words[4])
	}
	return matrix
}

func solve(matrix [][]int) int {
	minimum := math.MaxInt
	for _, path := range combin.Permutations(len(place), len(place)) {
		value := shortest(path, matrix)
		if value < minimum {
			minimum = value
		}
	}
	return minimum
}

func shortest(path []int, matrix [][]int) int {
	total := 0
	for x := 1; x < len(path); x++ {
		total += matrix[path[x-1]][path[x]]
	}
	return total
}

func negateMatrix(matrix [][]int) [][]int {
	newMatrix := make([][]int, len(matrix))
	for i := range newMatrix {
		newMatrix[i] = make([]int, len(matrix))
	}
	for y, row := range matrix {
		for x, item := range row {
			newMatrix[y][x] = item * -1
		}
	}
	return newMatrix
}

func main() {
	data := getDataByLine("day09.txt")

	matrix := createAdjacencyMatrix(data)
	p1 := solve(matrix)
	fmt.Println("Part 1:", p1)

	negMatrix := negateMatrix(matrix)
	p2 := solve(negMatrix) * -1
	fmt.Println("Part 2:", p2)
}

