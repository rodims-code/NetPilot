<script lang="ts">
	import { Button } from "$lib/components/ui/button/index.js";
	import { Input } from "$lib/components/ui/input/index.js";
	import { Label } from "$lib/components/ui/label/index.js";
	import * as Card from "$lib/components/ui/card/index.js";
	import Server from "@lucide/svelte/icons/server";
	import Plus from "@lucide/svelte/icons/plus";

	let agentCode = "";
	let agents = [
		{ id: "NP-A1B2", name: "Dakar Server Room", status: "online", lastSeen: "2 mins ago" },
		{ id: "NP-C3D4", name: "Abidjan Branch", status: "offline", lastSeen: "5 hours ago" }
	];

	function addAgent() {
		if (agentCode.trim() !== "") {
			agents = [...agents, { id: agentCode, name: "New Agent", status: "online", lastSeen: "Just now" }];
			agentCode = "";
		}
	}
</script>

<div class="space-y-6">
	<div class="grid gap-6 md:grid-cols-3">
		<!-- Add Agent Card -->
		<Card.Root class="md:col-span-1 h-fit sticky top-6">
			<Card.Header>
				<Card.Title class="flex items-center gap-2">
					<Server class="w-5 h-5" /> Register Agent
				</Card.Title>
				<Card.Description>Enter the Agent ID generated on the client machine.</Card.Description>
			</Card.Header>
			<Card.Content class="space-y-4">
				<div class="space-y-2">
					<Label for="agentCode">Agent ID</Label>
					<Input id="agentCode" bind:value={agentCode} placeholder="NP-XXXX-XXXX" />
				</div>
			</Card.Content>
			<Card.Footer>
				<Button class="w-full" on:click={addAgent}>
					<Plus class="w-4 h-4 mr-2" /> Add Agent
				</Button>
			</Card.Footer>
		</Card.Root>

		<!-- Agents List -->
		<div class="md:col-span-2 space-y-4">
			{#each agents as agent}
				<Card.Root>
					<Card.Content class="p-6 flex items-center justify-between">
						<div class="flex items-center gap-4">
							<div class={`p-3 rounded-full ${agent.status === 'online' ? 'bg-green-500/10 text-green-500' : 'bg-destructive/10 text-destructive'}`}>
								<Server class="w-6 h-6" />
							</div>
							<div>
								<h3 class="text-lg font-semibold">{agent.name}</h3>
								<p class="text-sm text-muted-foreground font-mono">{agent.id}</p>
							</div>
						</div>
						<div class="text-right">
							<div class="flex items-center gap-2 justify-end">
								<span class="relative flex h-3 w-3">
									{#if agent.status === 'online'}
										<span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
									{/if}
									<span class={`relative inline-flex rounded-full h-3 w-3 ${agent.status === 'online' ? 'bg-green-500' : 'bg-destructive'}`}></span>
								</span>
								<span class="text-sm font-medium capitalize">{agent.status}</span>
							</div>
							<p class="text-xs text-muted-foreground mt-1">Last seen: {agent.lastSeen}</p>
						</div>
					</Card.Content>
				</Card.Root>
			{/each}
			
			{#if agents.length === 0}
				<div class="text-center py-12 border border-dashed rounded-lg bg-muted/50">
					<Server class="w-12 h-12 text-muted-foreground mx-auto mb-4" />
					<p class="text-muted-foreground">No agents registered yet.</p>
				</div>
			{/if}
		</div>
	</div>
</div>
