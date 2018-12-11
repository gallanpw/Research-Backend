package main

import (
    "fmt"
    "log"
    "net/http"
	"math/rand"
	"strconv"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello Go\n")
	
	for i := 0; i < 10000; i++ {
		number := rand.Intn(1000)
		fmt.Fprintf(w, "Your Number: " + strconv.Itoa(number) + "\n")
	}
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8888", nil))
}