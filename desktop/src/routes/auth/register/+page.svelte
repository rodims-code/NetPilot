<script lang="ts">
	import { Button } from "$lib/components/ui/button/index.js";
	import { Input } from "$lib/components/ui/input/index.js";
	import { Label } from "$lib/components/ui/label/index.js";
	import * as Card from "$lib/components/ui/card/index.js";
	import UserPlus from "@lucide/svelte/icons/user-plus";
	import { goto } from "$app/navigation";

	let username = "";
	let email = "";
	let password = "";
	let loading = false;

	async function handleRegister() {
		loading = true;
		// TODO: Call real API backend
		setTimeout(() => {
			loading = false;
			goto("/auth/login");
		}, 1000);
	}
</script>

<div class="min-h-screen flex items-center justify-center bg-background p-4 relative overflow-hidden">
	<div class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-10 pointer-events-none mix-blend-overlay"></div>
	<div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-primary/20 blur-[120px] rounded-full pointer-events-none"></div>
	<div class="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] bg-accent/20 blur-[120px] rounded-full pointer-events-none"></div>
	
	<Card.Root class="w-full max-w-md bg-card/80 backdrop-blur-2xl border-border shadow-2xl relative z-10">
		<Card.Header class="space-y-2 text-center pb-8 pt-6">
			<div class="mx-auto bg-primary/10 p-4 rounded-2xl w-fit mb-4 ring-1 ring-primary/20">
				<UserPlus class="w-10 h-10 text-primary" />
			</div>
			<Card.Title class="text-3xl font-bold tracking-tight text-foreground">Create Account</Card.Title>
			<Card.Description class="text-muted-foreground text-base">Register as a Technician</Card.Description>
		</Card.Header>
		<Card.Content class="space-y-5">
			<div class="space-y-2">
				<Label for="username" class="font-medium text-foreground">Username</Label>
				<Input id="username" bind:value={username} placeholder="johndoe" class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background" />
			</div>
			<div class="space-y-2">
				<Label for="email" class="font-medium text-foreground">Email Address</Label>
				<Input id="email" type="email" bind:value={email} placeholder="john@example.com" class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background" />
			</div>
			<div class="space-y-2">
				<Label for="password" class="font-medium text-foreground">Password</Label>
				<Input id="password" type="password" bind:value={password} placeholder="••••••••" class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background" />
			</div>
		</Card.Content>
		<Card.Footer class="pb-6 flex-col gap-4">
			<Button class="w-full h-11 text-primary-foreground font-semibold shadow-lg hover:shadow-xl transition-all" on:click={handleRegister} disabled={loading}>
				{#if loading}
					<span class="flex items-center gap-2">
						<div class="w-4 h-4 border-2 border-primary-foreground/30 border-t-primary-foreground rounded-full animate-spin"></div>
						Registering...
					</span>
				{:else}
					Create Account
				{/if}
			</Button>
			<div class="text-center text-sm text-muted-foreground">
				Already have an account? 
				<a href="/auth/login" class="text-primary hover:underline font-medium transition-colors">Sign in</a>
			</div>
		</Card.Footer>
	</Card.Root>
</div>
