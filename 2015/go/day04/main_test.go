package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAnswer(t *testing.T) {
	assert.Equal(t, 609043, getAnswer([]byte("abcdef")))
	assert.Equal(t, 1048970, getAnswer([]byte("pqrstuv")))
}

