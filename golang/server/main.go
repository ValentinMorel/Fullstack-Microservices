package main

import (
	"log"

	"github.com/jroimartin/rpcmq"
)

func main() {
	s := rpcmq.NewServer("amqp://guest:guest@127.0.0.1:5672//",
		"rpc-queue", "rpc-exchange", "direct")

	if err := s.Register("hello", hello); err != nil {
		log.Fatalf("Register : %v", err)
	}

	if err := s.Init(); err != nil {
		log.Printf("Init : %v", err)
	}

	log.Printf("Listening for Remote Procedure Calls...")
	select {}
}

func hello(id string, data []byte) ([]byte, error) {
	log.Printf("Received %v : hello %v", id, string(data))
	return []byte("hello" + string(data)), nil

}
