<script lang="ts">
	import './layout.css';
	import { ModeWatcher } from "mode-watcher";
	import { browser } from "$app/environment";
	import { beforeNavigate } from "$app/navigation";
	import { goto } from "$app/navigation";
	import { getAccessToken } from "$lib/api";
	import { page } from "$app/stores";

	const { children } = $props();

	const PROTECTED_PREFIXES = ["/dashboard"];

	// Intercept every navigation — redirect to /auth/login if no token
	beforeNavigate(({ to }) => {
		if (!browser) return;
		const path = to?.url.pathname ?? "";
		const needsAuth = PROTECTED_PREFIXES.some((p) => path.startsWith(p));
		if (needsAuth && !getAccessToken()) {
			goto("/auth/login");
		}
	});
</script>

<ModeWatcher />
{@render children()}
