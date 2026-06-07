<script lang="ts">
	import AppSidebar from "$lib/components/app-sidebar.svelte";
	import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
	import { Separator } from "$lib/components/ui/separator/index.js";
	import * as Sidebar from "$lib/components/ui/sidebar/index.js";
	import { page } from "$app/stores";

	const { children } = $props();

	let currentPage = $derived(() => {
		if ($page.url.pathname.includes('/agents')) return "Agents";
		if ($page.url.pathname.includes('/devices')) return "Devices";
		return "Overview";
	});
</script>

<Sidebar.Provider>
	<div class="h-screen overflow-hidden bg-background px-4 py-4 md:px-6 md:py-6">
		<div class="mx-auto flex h-full max-w-screen-2xl flex-col overflow-hidden rounded-2xl border border-border bg-card shadow-sm dark:border-slate-700 dark:bg-slate-950 md:flex-row md:gap-6">
			<AppSidebar class="order-2 md:order-1" />
			<Sidebar.Inset class="order-1 flex-1 overflow-hidden p-4 md:order-2 md:p-6">
				<header class="sticky top-0 z-20 flex h-20 items-center gap-4 border-b border-border bg-background/95 px-3 backdrop-blur-xl dark:bg-slate-950/95">
					<div class="flex items-center gap-3">
						<Sidebar.Trigger class="-ms-1" />
						<Separator orientation="vertical" class="me-2 h-6" />
						<Breadcrumb.Root>
							<Breadcrumb.List class="flex items-center gap-2 text-sm text-muted-foreground">
								<Breadcrumb.Item class="hidden md:block">
									<Breadcrumb.Link href="/dashboard">Dashboard</Breadcrumb.Link>
								</Breadcrumb.Item>
								<Breadcrumb.Separator class="hidden md:block" />
								<Breadcrumb.Item>
									<Breadcrumb.Page class="font-semibold text-foreground">{currentPage()}</Breadcrumb.Page>
								</Breadcrumb.Item>
							</Breadcrumb.List>
						</Breadcrumb.Root>
					</div>
				</header>
				<main class="flex-1 h-full overflow-y-auto p-4 md:p-6">
					{@render children()}
				</main>
			</Sidebar.Inset>
		</div>
	</div>
</Sidebar.Provider>
