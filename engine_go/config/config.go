package config

import (
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"os"
)

type Config struct {
	AgentID string `json:"agent_id"`
}

const configPath = "agent_config.json"

func LoadOrGenerateConfig() (*Config, error) {
	if _, err := os.Stat(configPath); os.IsNotExist(err) {
		return generateConfig()
	}

	data, err := os.ReadFile(configPath)
	if err != nil {
		return nil, err
	}

	var cfg Config
	if err := json.Unmarshal(data, &cfg); err != nil {
		return nil, err
	}

	return &cfg, nil
}

func generateConfig() (*Config, error) {
	bytes := make([]byte, 4)
	if _, err := rand.Read(bytes); err != nil {
		return nil, err
	}
	agentID := fmt.Sprintf("NP-%s", hex.EncodeToString(bytes))

	cfg := &Config{AgentID: agentID}

	data, err := json.MarshalIndent(cfg, "", "  ")
	if err != nil {
		return nil, err
	}

	if err := os.WriteFile(configPath, data, 0644); err != nil {
		return nil, err
	}

	return cfg, nil
}
