<script lang="ts">
	import * as Card from "$lib/components/ui/card/index.js";
	import Router from "@lucide/svelte/icons/router";
	import Search from "@lucide/svelte/icons/search";
	import Filter from "@lucide/svelte/icons/filter";
	import Play from "@lucide/svelte/icons/play";
	import { Input } from "$lib/components/ui/input/index.js";
	import { Button } from "$lib/components/ui/button/index.js";

	let devices = [
		{ id: 1, identity: "MikroTik-Main", model: "hAP ac2", ip: "192.168.88.1", mac: "00:11:22:33:44:55", version: "7.12.1", status: "online", agent: "NP-A1B2" },
		{ id: 2, identity: "Office-GW", model: "RB750Gr3", ip: "10.0.0.1", mac: "AA:BB:CC:DD:EE:FF", version: "6.49.7", status: "online", agent: "NP-A1B2" },
		{ id: 3, identity: "WiFi-Guest", model: "hAP lite", ip: "192.168.2.1", mac: "11:22:33:44:55:66", version: "7.1.1", status: "offline", agent: "NP-C3D4" }
	];
</script>

<div class="space-y-6">
	<div class="flex items-center justify-end gap-2">
		<div class="relative w-64">
			<Search class="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
			<Input type="search" placeholder="Search devices..." class="pl-9" />
		</div>
		<Button variant="outline">
			<Filter class="w-4 h-4 mr-2" /> Filter
		</Button>
	</div>

	<Card.Root class="overflow-hidden">
		<div class="overflow-x-auto">
			<table class="w-full text-sm text-left">
				<thead class="text-xs text-muted-foreground uppercase bg-muted/50 border-b">
					<tr>
						<th scope="col" class="px-6 py-4 font-medium">Status</th>
						<th scope="col" class="px-6 py-4 font-medium">Identity</th>
						<th scope="col" class="px-6 py-4 font-medium">Model</th>
						<th scope="col" class="px-6 py-4 font-medium">IP Address</th>
						<th scope="col" class="px-6 py-4 font-medium">RouterOS</th>
						<th scope="col" class="px-6 py-4 font-medium">Agent</th>
						<th scope="col" class="px-6 py-4 font-medium text-right">Actions</th>
					</tr>
				</thead>
				<tbody class="divide-y divide-border">
					{#each devices as device}
						<tr class="hover:bg-muted/50 transition-colors group">
							<td class="px-6 py-4">
								<div class="flex items-center gap-2">
									<span class={`w-2.5 h-2.5 rounded-full ${device.status === 'online' ? 'bg-green-500' : 'bg-destructive'}`}></span>
									<span class="capitalize">{device.status}</span>
								</div>
							</td>
							<td class="px-6 py-4 font-medium flex items-center gap-3">
								<div class="p-2 rounded-md bg-primary/10 text-primary">
									<Router class="w-4 h-4" />
								</div>
								{device.identity}
							</td>
							<td class="px-6 py-4 text-muted-foreground">{device.model}</td>
							<td class="px-6 py-4 font-mono text-muted-foreground">{device.ip}</td>
							<td class="px-6 py-4">
								<span class="px-2.5 py-1 text-xs rounded-full bg-accent text-accent-foreground border">
									v{device.version}
								</span>
							</td>
							<td class="px-6 py-4 font-mono text-xs text-muted-foreground">{device.agent}</td>
							<td class="px-6 py-4 text-right">
								<Button size="sm" variant="default" class="opacity-0 group-hover:opacity-100 transition-opacity">
									<Play class="w-3 h-3 mr-1" /> Winbox
								</Button>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</Card.Root>
</div>

