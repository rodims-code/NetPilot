package main

import (
	"fmt"
	"log"
	"time"

	"github.com/rodims-code/NetPilot/engine_go/api"
	"github.com/rodims-code/NetPilot/engine_go/config"
	"github.com/rodims-code/NetPilot/engine_go/scanner"
)

func main() {
	fmt.Println("Starting NetPilot Agent...")

	cfg, err := config.LoadOrGenerateConfig()
	if err != nil {
		log.Fatalf("Failed to load/generate config: %v", err)
	}

	fmt.Printf("Agent ID: %s\n", cfg.AgentID)

	localIP := scanner.GetLocalIP()
	fmt.Printf("Local IP: %s\n", localIP)

	// Heartbeat loop
	ticker := time.NewTicker(10 * time.Second)
	defer ticker.Stop()

	for {
		devices := scanner.SimpleScan()
		fmt.Printf("Found %d MikroTik devices.\n", len(devices))

		err := api.SyncWithBackend(cfg.AgentID, localIP, devices)
		if err != nil {
			fmt.Printf("Error syncing with backend: %v\n", err)
		} else {
			fmt.Println("Successfully synced with backend.")
		}

		<-ticker.C
	}
}