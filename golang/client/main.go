package main

import (
	"log"

	"github.com/jroimartin/rpcmq"
)

func main() {
	c := rpcmq.NewClient("amqp://guest:guest@127.0.0.1:5672//",
		"rpc-queue", "rpc-client", "rpc-exchange", "direct")

	err := c.Init()
	if err != nil {
		log.Printf("Init : %v", err)
	}

	data := []byte("valentin")
	uuid, err := c.Call("hello", data, 0)

	log.Printf("uuid : %v, err : %v", uuid, err)
}
