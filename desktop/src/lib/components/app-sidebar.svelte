<script lang="ts" module>
	import LayoutDashboardIcon from "@lucide/svelte/icons/layout-dashboard";
	import ServerIcon from "@lucide/svelte/icons/server";
	import RouterIcon from "@lucide/svelte/icons/router";
	import ShieldIcon from "@lucide/svelte/icons/shield";
	import Settings2Icon from "@lucide/svelte/icons/settings-2";
	import GlobeIcon from "@lucide/svelte/icons/globe";
	import BuildingIcon from "@lucide/svelte/icons/building";
	import MapPinIcon from "@lucide/svelte/icons/map-pin";
	import NetworkIcon from "@lucide/svelte/icons/network";

	const data = {
		user: {
			name: "Admin WISP",
			email: "admin@netpilot.local",
			avatar: "/avatars/admin.jpg",
		},
		teams: [
			{
				name: "Global Network",
				logo: GlobeIcon,
				plan: "Enterprise",
			},
			{
				name: "Dakar HQ",
				logo: BuildingIcon,
				plan: "Main Site",
			},
			{
				name: "Abidjan Branch",
				logo: MapPinIcon,
				plan: "Remote Site",
			},
		],
		navMain: [
			{
				title: "Main",
				url: "/dashboard",
				icon: LayoutDashboardIcon,
				isActive: true,
				items: [
					{
						title: "Overview",
						url: "/dashboard",
					},
				],
			},
			{
				title: "Infrastructure",
				url: "#",
				icon: NetworkIcon,
				items: [
					{
						title: "Agents",
						url: "/dashboard/agents",
					},
					{
						title: "MikroTik Devices",
						url: "/dashboard/devices",
					},
				],
			},
			{
				title: "Security & Access",
				url: "#",
				icon: ShieldIcon,
				items: [
					{
						title: "VPN Tunnels",
						url: "#",
					},
					{
						title: "Firewall Rules",
						url: "#",
					},
				],
			},
			{
				title: "Settings",
				url: "#",
				icon: Settings2Icon,
				items: [
					{
						title: "Account",
						url: "#",
					},
					{
						title: "Preferences",
						url: "#",
					},
				],
			},
		],
		projects: [
			{
				name: "Dakar Core Routers",
				url: "#",
				icon: ServerIcon,
			},
			{
				name: "Client Access Points",
				url: "#",
				icon: RouterIcon,
			},
		],
	};
</script>

<script lang="ts">
	import NavMain from "./nav-main.svelte";
	import NavProjects from "./nav-projects.svelte";
	import NavUser from "./nav-user.svelte";
	import TeamSwitcher from "./team-switcher.svelte";
	import * as Sidebar from "$lib/components/ui/sidebar/index.js";
	import type { ComponentProps } from "svelte";

	let {
		ref = $bindable(null),
		collapsible = "icon",
		...restProps
	}: ComponentProps<typeof Sidebar.Root> = $props();
</script>

<Sidebar.Root bind:ref {collapsible} {...restProps}>
	<Sidebar.Header>
		<TeamSwitcher teams={data.teams} />
	</Sidebar.Header>
	<Sidebar.Content>
		<NavMain items={data.navMain} />
		<NavProjects projects={data.projects} />
	</Sidebar.Content>
	<Sidebar.Footer>
		<NavUser user={data.user} />
	</Sidebar.Footer>
	<Sidebar.Rail />
</Sidebar.Root>
