package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAnswer(t *testing.T) {
	assert.Equal(t, "abcdffaa", solve("abcdefgh"))
	assert.Equal(t, "ghjaabcc", solve("ghijklmn"))
}

