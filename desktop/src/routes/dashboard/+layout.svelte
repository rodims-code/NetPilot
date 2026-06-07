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
	<div class="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(56,189,248,0.18),_transparent_28%),radial-gradient(circle_at_bottom_right,_rgba(168,85,247,0.12),_transparent_32%),linear-gradient(180deg,rgba(248,250,252,1),rgba(241,245,249,1))] dark:bg-[radial-gradient(circle_at_top_left,_rgba(59,130,246,0.16),_transparent_28%),radial-gradient(circle_at_bottom_right,_rgba(139,92,246,0.16),_transparent_32%),linear-gradient(180deg,rgba(15,23,42,1),rgba(30,41,59,1))]">
		<div class="mx-auto flex min-h-screen max-w-[1800px] overflow-hidden rounded-[2rem] bg-white/70 shadow-2xl shadow-slate-900/10 backdrop-blur-xl ring-1 ring-slate-900/5 dark:bg-slate-950/85 dark:shadow-none dark:ring-0">
			<AppSidebar class="border-r border-slate-200/80 bg-white/95 shadow-xl shadow-slate-900/5 dark:border-slate-700/70 dark:bg-slate-950/95" />
			<Sidebar.Inset class="flex-1 overflow-hidden">
				<header class="sticky top-0 z-20 flex h-20 items-center justify-between gap-4 border-b border-slate-200/80 bg-white/85 px-4 shadow-sm backdrop-blur-xl transition-colors duration-300 dark:border-slate-700/80 dark:bg-slate-950/90">
					<div class="flex items-center gap-3">
						<Sidebar.Trigger class="-ms-1 text-slate-800 dark:text-slate-100" />
						<Separator orientation="vertical" class="me-2 h-6 text-slate-300 dark:text-slate-600" />
						<Breadcrumb.Root>
							<Breadcrumb.List class="flex items-center gap-2 text-sm text-slate-500 dark:text-slate-400">
								<Breadcrumb.Item class="hidden md:block">
									<Breadcrumb.Link href="/dashboard">Dashboard</Breadcrumb.Link>
								</Breadcrumb.Item>
								<Breadcrumb.Separator class="hidden md:block" />
								<Breadcrumb.Item>
									<Breadcrumb.Page class="font-semibold text-slate-900 dark:text-slate-100">{currentPage()}</Breadcrumb.Page>
								</Breadcrumb.Item>
							</Breadcrumb.List>
						</Breadcrumb.Root>
					</div>
				</header>
				<main class="flex-1 overflow-y-auto p-6">
					{@render children()}
				</main>
			</Sidebar.Inset>
		</div>
	</div>
</Sidebar.Provider>
