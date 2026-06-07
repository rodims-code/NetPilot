<script lang="ts">
	import RouterIcon from "@lucide/svelte/icons/router";
	import ServerIcon from "@lucide/svelte/icons/server";
	import ActivityIcon from "@lucide/svelte/icons/activity";
	import ZapIcon from "@lucide/svelte/icons/zap";
	import TerminalIcon from "@lucide/svelte/icons/terminal";
	import MonitorIcon from "@lucide/svelte/icons/monitor";
	import ShieldIcon from "@lucide/svelte/icons/shield";
	import Settings2Icon from "@lucide/svelte/icons/settings-2";
	import UserIcon from "@lucide/svelte/icons/user";
	import NetworkIcon from "@lucide/svelte/icons/network";
	import ArrowRightIcon from "@lucide/svelte/icons/arrow-right";
	import AlertTriangleIcon from "@lucide/svelte/icons/alert-triangle";

	const sections = [
		{
			title: "Infrastructure",
			items: [
				{
					icon: ServerIcon,
					color: "bg-blue-500/10 text-blue-600 dark:text-blue-400",
					title: "Agents",
					description: "Register and manage your network agents deployed at client sites.",
					href: "/dashboard/agents",
				},
				{
					icon: RouterIcon,
					color: "bg-green-500/10 text-green-600 dark:text-green-400",
					title: "MikroTik Devices",
					description: "View and monitor all MikroTik routers discovered by your agents.",
					href: "/dashboard/devices",
				},
				{
					icon: NetworkIcon,
					color: "bg-purple-500/10 text-purple-600 dark:text-purple-400",
					title: "Network Topology",
					description: "Visualize the network map across all your managed sites.",
					href: "#",
					badge: "Soon",
				},
				{
					icon: MonitorIcon,
					color: "bg-orange-500/10 text-orange-600 dark:text-orange-400",
					title: "Sites Overview",
					description: "See all your client sites and their overall connection health.",
					href: "#",
					badge: "Soon",
				},
			],
		},
		{
			title: "Monitoring",
			items: [
				{
					icon: ActivityIcon,
					color: "bg-cyan-500/10 text-cyan-600 dark:text-cyan-400",
					title: "Live Status",
					description: "Real-time status of all connected devices. Online, offline, and latency.",
					href: "#",
					badge: "Soon",
				},
				{
					icon: AlertTriangleIcon,
					color: "bg-yellow-500/10 text-yellow-600 dark:text-yellow-400",
					title: "Alerts & Incidents",
					description: "Configure alerts when a device goes offline or CPU spikes.",
					href: "#",
					badge: "Soon",
				},
				{
					icon: ZapIcon,
					color: "bg-rose-500/10 text-rose-600 dark:text-rose-400",
					title: "Performance Metrics",
					description: "Track bandwidth, CPU usage, and memory across all devices.",
					href: "#",
					badge: "Soon",
				},
			],
		},
		{
			title: "Remote Access",
			items: [
				{
					icon: TerminalIcon,
					color: "bg-slate-500/10 text-slate-600 dark:text-slate-400",
					title: "SSH Access",
					description: "Open a direct SSH session to any device from your dashboard.",
					href: "#",
					badge: "Soon",
				},
				{
					icon: MonitorIcon,
					color: "bg-indigo-500/10 text-indigo-600 dark:text-indigo-400",
					title: "Winbox Launcher",
					description: "Launch Winbox for any MikroTik device with a single click.",
					href: "#",
					badge: "Soon",
				},
			],
		},
		{
			title: "Settings",
			items: [
				{
					icon: UserIcon,
					color: "bg-teal-500/10 text-teal-600 dark:text-teal-400",
					title: "Account",
					description: "Manage your technician profile, password and preferences.",
					href: "#",
				},
				{
					icon: ShieldIcon,
					color: "bg-red-500/10 text-red-600 dark:text-red-400",
					title: "Security",
					description: "Configure two-factor authentication and session management.",
					href: "#",
					badge: "Soon",
				},
				{
					icon: Settings2Icon,
					color: "bg-gray-500/10 text-gray-600 dark:text-gray-400",
					title: "Preferences",
					description: "Customize your dashboard layout, notifications and display settings.",
					href: "#",
				},
			],
		},
	];
</script>

<div class="flex flex-col gap-8 pb-8">
	{#each sections as section}
		<div>
			<h2 class="text-lg font-semibold text-foreground mb-4">{section.title}</h2>
			<div class="grid grid-cols-1 md:grid-cols-2 gap-3">
				{#each section.items as item}
					<a
						href={item.href}
						class="group flex items-center gap-4 rounded-lg border border-border bg-card p-4 hover:bg-muted/50 transition-colors"
					>
						<div class={`flex h-10 w-10 shrink-0 items-center justify-center rounded-lg ${item.color}`}>
							<svelte:component this={item.icon} class="h-5 w-5" />
						</div>
						<div class="flex-1 min-w-0">
							<div class="flex items-center gap-2">
								<p class="text-sm font-medium text-foreground">{item.title}</p>
								{#if item.badge}
									<span class="inline-flex items-center rounded-full bg-primary/10 px-2 py-0.5 text-[10px] font-medium text-primary">
										{item.badge}
									</span>
								{/if}
							</div>
							<p class="text-xs text-muted-foreground mt-0.5 line-clamp-2">{item.description}</p>
						</div>
						<ArrowRightIcon class="h-4 w-4 text-muted-foreground shrink-0 transition-transform group-hover:translate-x-1" />
					</a>
				{/each}
			</div>
		</div>
	{/each}
</div>
