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
	<section class="grid gap-6 xl:grid-cols-[1.4fr_0.9fr]">
		<div class="space-y-5 rounded-[2rem] border border-slate-200/70 bg-white/90 p-6 shadow-xl shadow-slate-900/5 backdrop-blur-xl dark:border-slate-700/70 dark:bg-slate-950/80">
			<div class="space-y-2">
				<p class="text-xs font-semibold uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">Tableau de bord</p>
				<h1 class="text-3xl font-semibold tracking-tight text-slate-950 dark:text-white">Pilotez votre réseau avec NetPilot</h1>
				<p class="max-w-2xl text-sm leading-6 text-slate-600 dark:text-slate-300">Un aperçu clair de vos agents, vos sites et vos appareils, avec des actions rapides et un design orienté productivité.</p>
			</div>
			<div class="grid gap-3 sm:grid-cols-3">
				<article class="rounded-3xl border border-slate-200/80 bg-slate-50/90 p-4 shadow-sm dark:border-slate-700/70 dark:bg-slate-900/80">
					<p class="text-xs font-semibold uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">Agents</p>
					<p class="mt-3 text-2xl font-semibold text-slate-950 dark:text-white">24</p>
					<p class="mt-2 text-sm text-slate-500 dark:text-slate-400">Connectés et synchronisés</p>
				</article>
				<article class="rounded-3xl border border-slate-200/80 bg-slate-50/90 p-4 shadow-sm dark:border-slate-700/70 dark:bg-slate-900/80">
					<p class="text-xs font-semibold uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">Sites</p>
					<p class="mt-3 text-2xl font-semibold text-slate-950 dark:text-white">12</p>
					<p class="mt-2 text-sm text-slate-500 dark:text-slate-400">Sites gérés</p>
				</article>
				<article class="rounded-3xl border border-slate-200/80 bg-slate-50/90 p-4 shadow-sm dark:border-slate-700/70 dark:bg-slate-900/80">
					<p class="text-xs font-semibold uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">Incidents</p>
					<p class="mt-3 text-2xl font-semibold text-slate-950 dark:text-white">0</p>
					<p class="mt-2 text-sm text-slate-500 dark:text-slate-400">Alertes critiques</p>
				</article>
			</div>
		</div>
		<aside class="space-y-4 rounded-[2rem] border border-slate-200/70 bg-gradient-to-b from-slate-50 to-white/90 p-6 shadow-xl shadow-slate-900/5 backdrop-blur-xl dark:border-slate-700/70 dark:from-slate-950/90 dark:to-slate-950/80 dark:bg-slate-950/95">
			<div class="flex items-center justify-between gap-4">
				<div>
					<p class="text-sm font-semibold text-slate-900 dark:text-white">Actions rapides</p>
					<p class="mt-1 text-sm text-slate-500 dark:text-slate-400">Accédez instantanément à vos vues les plus importantes.</p>
				</div>
				<div class="inline-flex rounded-3xl bg-slate-900/95 px-3 py-2 text-xs font-semibold text-white shadow-sm shadow-slate-900/20">
					Nouveau style
				</div>
			</div>
			<div class="grid gap-3">
				<a href="/dashboard/agents" class="rounded-3xl border border-slate-200/80 bg-white/95 px-4 py-4 text-sm font-medium text-slate-900 transition hover:bg-slate-50 dark:border-slate-700/70 dark:bg-slate-900/90 dark:text-slate-100">Voir les agents</a>
				<a href="/dashboard/devices" class="rounded-3xl border border-slate-200/80 bg-white/95 px-4 py-4 text-sm font-medium text-slate-900 transition hover:bg-slate-50 dark:border-slate-700/70 dark:bg-slate-900/90 dark:text-slate-100">Explorer les appareils</a>
				<a href="#" class="rounded-3xl border border-slate-200/80 bg-white/95 px-4 py-4 text-sm font-medium text-slate-900 transition hover:bg-slate-50 dark:border-slate-700/70 dark:bg-slate-900/90 dark:text-slate-100">Ouvrir la sécurité</a>
			</div>
		</aside>
	</section>

	{#each sections as section}
		<div class="space-y-4 rounded-[2rem] border border-slate-200/70 bg-white/90 p-6 shadow-xl shadow-slate-900/5 backdrop-blur-xl dark:border-slate-700/70 dark:bg-slate-950/80">
			<div class="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
				<h2 class="text-lg font-semibold text-slate-950 dark:text-white">{section.title}</h2>
				<p class="text-sm text-slate-500 dark:text-slate-400">{section.items.length} éléments disponibles</p>
			</div>
			<div class="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-2">
				{#each section.items as item}
					<a
						href={item.href}
						class="group relative overflow-hidden rounded-3xl border border-slate-200/80 bg-white/95 p-5 shadow-sm transition duration-300 hover:-translate-y-0.5 hover:border-slate-300 hover:shadow-lg dark:border-slate-700/70 dark:bg-slate-950/90"
					>
						<div class="absolute inset-x-0 top-0 h-1 bg-gradient-to-r from-sky-500 via-sky-400 to-indigo-500 opacity-30"></div>
						<div class="relative flex items-center gap-4">
							<div class={`flex h-12 w-12 shrink-0 items-center justify-center rounded-3xl ${item.color}`}>
								<svelte:component this={item.icon} class="h-5 w-5" />
							</div>
							<div class="flex-1 min-w-0">
								<div class="flex flex-wrap items-center gap-2">
									<p class="text-base font-semibold text-slate-950 dark:text-white">{item.title}</p>
									{#if item.badge}
										<span class="inline-flex items-center rounded-full bg-sky-500/10 px-2.5 py-1 text-[11px] font-semibold text-sky-600 dark:text-sky-300">{item.badge}</span>
									{/if}
								</div>
								<p class="mt-2 text-sm leading-6 text-slate-600 dark:text-slate-400">{item.description}</p>
							</div>
							<ArrowRightIcon class="h-4 w-4 text-slate-400 transition-transform duration-300 group-hover:translate-x-1 dark:text-slate-500" />
						</div>
					</a>
				{/each}
			</div>
		</div>
	{/each}
</div>
