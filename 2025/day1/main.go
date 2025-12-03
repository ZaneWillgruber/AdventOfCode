package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	run(bufio.NewScanner(file), true)
	file.Seek(0, 0)
	run(bufio.NewScanner(file), false)

}

func run(scanner *bufio.Scanner, part1 bool) {
	dial := 50
	zeros := 0
	for scanner.Scan() {
		line := scanner.Text()
		left := line[0] == 'L'
		amount, err := strconv.Atoi(line[1:])
		if err != nil {
			fmt.Println("Error converting number:", err)
		}

		if !part1 {
			zeros += amount / 100
		}
		amount = amount % 100

		if left {
			oldDial := dial
			dial = dial - amount
			if dial < 0 {
				if oldDial != 0 && !part1 {
					zeros++
				}
				dial = 100 + dial
			}
		} else {
			if dial+amount > 100 && !part1 {
				zeros++
			}
			dial = (dial + amount) % 100
		}

		if dial == 0 {
			zeros++
		}
	}

	fmt.Println("Amount of Zeros:", zeros)
}
