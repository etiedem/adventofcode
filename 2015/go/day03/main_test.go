package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAnswer(t *testing.T) {
	assert.Equal(t, 2, countHouses([]byte{'>'}))
	assert.Equal(t, 4, countHouses([]byte{'^', '>', 'v', '<'}))
	assert.Equal(t, 2, countHouses([]byte{'^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v'}))
}

