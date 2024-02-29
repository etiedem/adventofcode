package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAnswer(t *testing.T) {
	assert.Equal(t, true, part1("ugknbfddgicrmopn"))
	assert.Equal(t, true, part1("aaa"))
	assert.Equal(t, false, part1("jchzalrnumimnmhp"))
	assert.Equal(t, false, part1("haegwjzuvuyypxyu"))
	assert.Equal(t, false, part1("dvszwmarrgswjxmb"))
}

func TestAnswer2(t *testing.T) {
	assert.Equal(t, true, part2("qjhvhtzxzqqjkmpb"))
	assert.Equal(t, true, part2("xxyxx"))
	assert.Equal(t, false, part2("uurcxstgmygtbstg"))
	assert.Equal(t, false, part2("ieodomkazucvgmuy"))
}

