/* 

This list represents the Calories of the food carried by five Elves:

- The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
- The second Elf is carrying one food item with 4000 Calories.
- The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
- The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
- The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
they'd like to know how many Calories are being carried by the Elf carrying the most Calories. 
In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Input: input.txt

*/

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {

	file, err := os.Open("./input.txt")

	if err != nil {
			log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	
	for scanner.Scan() {
			fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
			log.Fatal(err)
	}
}