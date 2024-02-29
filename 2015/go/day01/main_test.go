package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAnswer(t *testing.T) {
	assert.Equal(t, 0, countFloor([]byte("(())")))
	assert.Equal(t, 0, countFloor([]byte("()()")))
	assert.Equal(t, 3, countFloor([]byte("))(((((")))
	assert.Equal(t, -1, countFloor([]byte("())")))
	assert.Equal(t, -1, countFloor([]byte("))(")))
}
