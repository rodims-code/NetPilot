<script lang="ts">
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";

	onMount(() => {
		// Verify token here in the future
		// For now, redirect to login
		goto("/auth/login");
	});
</script>

<div class="min-h-screen flex items-center justify-center bg-zinc-950">
	<div class="w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
</div>
