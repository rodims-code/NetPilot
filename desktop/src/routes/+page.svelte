<script lang="ts">
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { getAccessToken } from "$lib/api";
	import { requireAuth } from "$lib/auth";

	onMount(async () => {
		if (!getAccessToken()) {
			// No token at all → go to login immediately
			goto("/auth/login");
			return;
		}
		// Token exists → validate it with the backend
		const ok = await requireAuth();
		if (ok) goto("/dashboard");
		// requireAuth() calls logout() + redirect on failure
	});
</script>

<!-- Shown briefly while checking auth -->
<div class="min-h-screen flex items-center justify-center bg-background">
	<div class="w-8 h-8 border-4 border-primary border-t-transparent rounded-full animate-spin"></div>
</div>
