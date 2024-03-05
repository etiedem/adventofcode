package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Action struct {
	action string
	left   string
	right  string
	dest   string
}

func ParseAction(line string) *Action {
	items := strings.Split(line, " ")
	if len(items) == 3 {
		return &Action{action: "ASSIGN", left: items[0], dest: items[2]}
	}
	if len(items) == 4 {
		return &Action{action: "NOT", left: items[1], dest: items[3]}
	}
	if items[1] == "AND" {
		return &Action{action: "AND", left: items[0], right: items[2], dest: items[4]}
	}
	if items[1] == "OR" {
		return &Action{action: "OR", left: items[0], right: items[2], dest: items[4]}
	}
	if items[1] == "LSHIFT" {
		return &Action{action: "LSHIFT", left: items[0], right: items[2], dest: items[4]}
	}
	if items[1] == "RSHIFT" {
		return &Action{action: "RSHIFT", left: items[0], right: items[2], dest: items[4]}
	}
	return &Action{}
}

func getDataByLine(filename string) []string {
	data, error := os.ReadFile(filename)
	if error != nil {
		panic(error)
	}
	return strings.Split(string(data), "\n")
}

func parseData(data []string) map[string]Action {
	output := map[string]Action{}
	for _, line := range data {
		if line == "" {
			continue
		}
		action := ParseAction(line)
		output[(*action).dest] = *action
	}
	return output
}

func solve(action Action, instr *map[string]Action, output *map[string]uint16) {
	switch action.action {
	case "ASSIGN":
		if value, error := strconv.Atoi(action.left); error == nil {
			(*output)[action.dest] = uint16(value)
		} else {
			if val, ok := (*output)[action.left]; ok {
				(*output)[action.dest] = val
			} else {
				solve((*instr)[action.left], instr, output)
				(*output)[action.dest] = (*output)[action.left]
			}
		}
	case "AND":
		value, error := strconv.Atoi(action.left)
		left := uint16(value)
		if error != nil {
			value, ok := (*output)[action.left]
			if !ok {
				solve((*instr)[action.left], instr, output)
				value = (*output)[action.left]
			}
			left = value
		}
		value, error = strconv.Atoi(action.right)
		right := uint16(value)
		if error != nil {
			value, ok := (*output)[action.right]
			if !ok {
				solve((*instr)[action.right], instr, output)
				value = (*output)[action.right]
			}
			right = value
		}
		(*output)[action.dest] = left & right
	case "OR":
		value, error := strconv.Atoi(action.left)
		left := uint16(value)
		if error != nil {
			value, ok := (*output)[action.left]
			if !ok {
				solve((*instr)[action.left], instr, output)
				value = (*output)[action.left]
			}
			left = value
		}
		value, error = strconv.Atoi(action.right)
		right := uint16(value)
		if error != nil {
			value, ok := (*output)[action.right]
			if !ok {
				solve((*instr)[action.right], instr, output)
				value = (*output)[action.right]
			}
			right = value
		}
		(*output)[action.dest] = left | right
	case "LSHIFT":
		left, ok := (*output)[action.left]
		if !ok {
			solve((*instr)[action.left], instr, output)
			left = (*output)[action.left]
		}
		value, _ := strconv.Atoi(action.right)
		(*output)[action.dest] = uint16(left << value)
	case "RSHIFT":
		left, ok := (*output)[action.left]
		if !ok {
			solve((*instr)[action.left], instr, output)
			left = (*output)[action.left]
		}
		value, _ := strconv.Atoi(action.right)
		(*output)[action.dest] = uint16(left >> value)
	case "NOT":
		val, ok := (*output)[action.left]
		if !ok {
			solve((*instr)[action.left], instr, output)
			val = (*output)[action.left]
		}
		(*output)[action.dest] = ^val
	}
}

func main() {
	data := getDataByLine("day07.txt")
	instr := parseData(data)

	output := map[string]uint16{}
	solve(instr["a"], &instr, &output)
	p1 := output["a"]
	fmt.Println("Part 1:", p1)

	output = map[string]uint16{"b": p1}
	solve(instr["a"], &instr, &output)
	p2 := output["a"]
	fmt.Println("Part 2:", p2)
}
