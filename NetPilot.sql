CREATE TABLE "users" (
  "id" uuid PRIMARY KEY,
  "username" varchar,
  "email" varchar UNIQUE,
  "role" varchar,
  "is_active" boolean,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "plans" (
  "id" uuid PRIMARY KEY,
  "name" varchar,
  "price" decimal,
  "max_sites" int,
  "max_devices" int,
  "created_at" timestamp
);

CREATE TABLE "subscriptions" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid,
  "plan_id" uuid,
  "status" varchar,
  "started_at" timestamp,
  "expires_at" timestamp,
  "created_at" timestamp
);

CREATE TABLE "sites" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid,
  "name" varchar,
  "description" text,
  "country" varchar,
  "city" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "agents" (
  "id" uuid PRIMARY KEY,
  "site_id" uuid,
  "agent_code" varchar UNIQUE,
  "name" varchar,
  "os" varchar,
  "version" varchar,
  "local_ip" varchar,
  "status" varchar,
  "last_seen" timestamp,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "mikrotik_devices" (
  "id" uuid PRIMARY KEY,
  "agent_id" uuid,
  "identity" varchar,
  "model" varchar,
  "board_name" varchar,
  "routeros_version" varchar,
  "architecture" varchar,
  "ip_address" varchar,
  "mac_address" varchar,
  "status" varchar,
  "last_seen" timestamp,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "mikrotik_metrics" (
  "id" uuid PRIMARY KEY,
  "device_id" uuid,
  "cpu_load" float,
  "free_memory" bigint,
  "total_memory" bigint,
  "latency" float,
  "uptime" bigint,
  "recorded_at" timestamp
);

CREATE TABLE "scans" (
  "id" uuid PRIMARY KEY,
  "agent_id" uuid,
  "subnet" varchar,
  "devices_found" int,
  "started_at" timestamp,
  "completed_at" timestamp
);

CREATE TABLE "alerts" (
  "id" uuid PRIMARY KEY,
  "device_id" uuid,
  "severity" varchar,
  "title" varchar,
  "message" text,
  "resolved" boolean,
  "resolved_at" timestamp,
  "created_at" timestamp
);

CREATE TABLE "notifications" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid,
  "title" varchar,
  "message" text,
  "type" varchar,
  "is_read" boolean,
  "created_at" timestamp
);

CREATE TABLE "remote_sessions" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid,
  "device_id" uuid,
  "action" varchar,
  "started_at" timestamp,
  "ended_at" timestamp
);

CREATE TABLE "device_logs" (
  "id" uuid PRIMARY KEY,
  "device_id" uuid,
  "level" varchar,
  "message" text,
  "created_at" timestamp
);

ALTER TABLE "subscriptions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "subscriptions" ADD FOREIGN KEY ("plan_id") REFERENCES "plans" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "sites" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "agents" ADD FOREIGN KEY ("site_id") REFERENCES "sites" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "mikrotik_devices" ADD FOREIGN KEY ("agent_id") REFERENCES "agents" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "mikrotik_metrics" ADD FOREIGN KEY ("device_id") REFERENCES "mikrotik_devices" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "scans" ADD FOREIGN KEY ("agent_id") REFERENCES "agents" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "alerts" ADD FOREIGN KEY ("device_id") REFERENCES "mikrotik_devices" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "notifications" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "remote_sessions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "remote_sessions" ADD FOREIGN KEY ("device_id") REFERENCES "mikrotik_devices" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "device_logs" ADD FOREIGN KEY ("device_id") REFERENCES "mikrotik_devices" ("id") DEFERRABLE INITIALLY IMMEDIATE;
