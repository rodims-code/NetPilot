<script lang="ts">
	import AppSidebar from "$lib/components/app-sidebar.svelte";
	import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
	import { Separator } from "$lib/components/ui/separator/index.js";
	import * as Sidebar from "$lib/components/ui/sidebar/index.js";
	import { page } from "$app/stores";
	import { onMount } from "svelte";
	import { requireAuth, currentUser, logout } from "$lib/auth";
	import { goto } from "$app/navigation";

	const { children } = $props();

	let currentPage = $derived(() => {
		if ($page.url.pathname.includes('/agents')) return "Agents";
		if ($page.url.pathname.includes('/devices')) return "Devices";
		return "Overview";
	});

	onMount(async () => {
		const ok = await requireAuth();
		if (!ok) goto("/auth/login");
	});
</script>

<Sidebar.Provider>
	<AppSidebar />
	<Sidebar.Inset>
		<header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
			<div class="flex items-center gap-2 px-4 flex-1">
				<Sidebar.Trigger class="-ms-1" />
				<Separator orientation="vertical" class="me-2 data-[orientation=vertical]:h-4" />
				<Breadcrumb.Root>
					<Breadcrumb.List>
						<Breadcrumb.Item class="hidden md:block">
							<Breadcrumb.Link href="/dashboard">Dashboard</Breadcrumb.Link>
						</Breadcrumb.Item>
						<Breadcrumb.Separator class="hidden md:block" />
						<Breadcrumb.Item>
							<Breadcrumb.Page>{currentPage()}</Breadcrumb.Page>
						</Breadcrumb.Item>
					</Breadcrumb.List>
				</Breadcrumb.Root>
				<div class="ml-auto flex items-center gap-3 pr-2">
					{#if $currentUser}
						<span class="text-sm text-muted-foreground hidden md:block">
							👤 {$currentUser.username}
						</span>
					{/if}
					<button
						onclick={() => logout()}
						class="text-sm text-muted-foreground hover:text-destructive transition-colors"
					>
						Sign out
					</button>
				</div>
			</div>
		</header>
		<div class="flex flex-1 flex-col gap-4 p-4 pt-0">
			{@render children()}
		</div>
	</Sidebar.Inset>
</Sidebar.Provider>
