package api

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"github.com/rodims-code/NetPilot/engine_go/scanner"
)

const BackendURL = "http://127.0.0.1:8000/api"

type SyncPayload struct {
	AgentCode string           `json:"agent_code"`
	LocalIP   string           `json:"local_ip"`
	Devices   []scanner.Device `json:"devices"`
}

func SyncWithBackend(agentID string, localIP string, devices []scanner.Device) error {
	payload := SyncPayload{
		AgentCode: agentID,
		LocalIP:   localIP,
		Devices:   devices,
	}

	jsonData, err := json.Marshal(payload)
	if err != nil {
		return err
	}

	// In real world, we'd use Agent ID UUID, but here we use AgentCode.
	// Since we don't have the UUID on first sync, we will use a dummy one or update the view to match by AgentCode.
	// Actually, the view expects the uuid in the URL. For registration, we can just hit /sync/ with a static or generated UUID, 
	// or modify the Go agent to fetch its UUID.
	// Let's use the Agent ID as the UUID or just let the backend find it by agent_code in a generic endpoint.
	// Wait, our backend view is: path('agents/<uuid:agent_id>/sync/', AgentSyncView.as_view())
	// This means we need a UUID. Let's send the agentCode as the UUID if we format it as UUID?
	// No, let's fix backend or just use a dummy endpoint.
	// For V1, let's just make the backend endpoint accept the sync via agent_code.
	
	// I'll update the backend URL temporarily to /agents/sync/ and pass agent_code in body.
	url := fmt.Sprintf("%s/agents/sync_by_code/", BackendURL)

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	if err != nil {
		return err
	}

	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{Timeout: 10 * time.Second}
	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("backend returned status: %d", resp.StatusCode)
	}

	return nil
}
