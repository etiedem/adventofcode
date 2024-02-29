package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func numToIntSlice(a, b int) []int {
	return []int{a, b}
}

func TestAnswer(t *testing.T) {
	assert.Equal(t, []int{58, 34}, numToIntSlice(getLength([]byte("2x3x4"))))
	assert.Equal(t, []int{43, 14}, numToIntSlice(getLength([]byte("1x1x10"))))
}

