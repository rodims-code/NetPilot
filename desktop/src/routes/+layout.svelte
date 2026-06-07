<script lang="ts">
	import './layout.css';

	const { children } = $props();
	import { ModeWatcher } from "mode-watcher";
</script>
<ModeWatcher />
{@render children()}
