package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetDigit1(t *testing.T) {
	number := []byte("1andfolajldsflkj2")
	answer := getDigit(number)
	assert.Equal(t, 12, answer)
}

func TestGetDigit2(t *testing.T) {
	number := []byte("98745yaksdjf75838")
	answer := getDigit(number)
	assert.Equal(t, 98, answer)
}

func TestGetNum1(t *testing.T) {
	number := []byte("1vmalksdhjfflkahsdfklnine")
	answer := getNumber(number)
	assert.Equal(t, 19, answer)
}

func TestGetNum2(t *testing.T) {
	number := []byte("7zgzsevenftkdfour186")
	answer := getNumber(number)
	assert.Equal(t, 76, answer)
}

func TestGetNum3(t *testing.T) {
	number := []byte("five7fourseven")
	answer := getNumber(number)
	assert.Equal(t, 57, answer)
}

func TestGetNum4(t *testing.T) {
	number := []byte("asldfjalkjdffourasldkfj")
	answer := getNumber(number)
	assert.Equal(t, 44, answer)
}

func TestGetNum5(t *testing.T) {
	number := []byte("jjhxddmg5mqxqbgfivextlcpnvtwothreetwonerzk")
	answer := getNumber(number)
	assert.Equal(t, 51, answer)
}

func TestPart2(t *testing.T) {
	data := getData("example.txt")
	answer := solve(data, getNumber)
	assert.Equal(t, 281, answer)
}
