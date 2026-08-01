<script lang="ts">
	import { Button } from "$lib/components/ui/button/index.js";
	import { Input } from "$lib/components/ui/input/index.js";
	import { Label } from "$lib/components/ui/label/index.js";
	import * as Card from "$lib/components/ui/card/index.js";
	import * as Alert from "$lib/components/ui/alert/index.js";
	import UserPlus from "@lucide/svelte/icons/user-plus";
	import AlertCircle from "@lucide/svelte/icons/alert-circle";
	import { goto } from "$app/navigation";
	import { register } from "$lib/auth";

	let username = "";
	let email = "";
	let password = "";
	let loading = false;
	let errorMessage = "";
	let successMessage = "";

	async function handleRegister() {
		if (!username.trim() || !email.trim() || !password.trim()) {
			errorMessage = "Veuillez remplir tous les champs.";
			return;
		}
		if (password.length < 8) {
			errorMessage = "Le mot de passe doit contenir au moins 8 caractères.";
			return;
		}
		loading = true;
		errorMessage = "";
		successMessage = "";
		try {
			await register(username, email, password);
			successMessage = "Compte créé avec succès ! Vous allez être redirigé...";
			setTimeout(() => goto("/auth/login"), 1500);
		} catch (err: unknown) {
			const e = err as { message?: string };
			errorMessage = e?.message || "Une erreur est survenue. Vérifiez les informations saisies.";
		} finally {
			loading = false;
		}
	}
</script>

<div class="min-h-screen flex items-center justify-center bg-background p-4 relative overflow-hidden">
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
			{#if errorMessage}
				<Alert.Root variant="destructive">
					<AlertCircle class="h-4 w-4" />
					<Alert.Description>{errorMessage}</Alert.Description>
				</Alert.Root>
			{/if}
			{#if successMessage}
				<Alert.Root class="border-green-500/50 bg-green-500/10 text-green-700 dark:text-green-400">
					<Alert.Description>{successMessage}</Alert.Description>
				</Alert.Root>
			{/if}
			<div class="space-y-2">
				<Label for="username" class="font-medium text-foreground">Username</Label>
				<Input
					id="username"
					bind:value={username}
					placeholder="johndoe"
					autocomplete="username"
					class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background"
				/>
			</div>
			<div class="space-y-2">
				<Label for="email" class="font-medium text-foreground">Email Address</Label>
				<Input
					id="email"
					type="email"
					bind:value={email}
					placeholder="john@example.com"
					autocomplete="email"
					class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background"
				/>
			</div>
			<div class="space-y-2">
				<Label for="password" class="font-medium text-foreground">Password</Label>
				<Input
					id="password"
					type="password"
					bind:value={password}
					placeholder="Min. 8 caractères"
					autocomplete="new-password"
					class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background"
				/>
			</div>
		</Card.Content>
		<Card.Footer class="pb-6 flex-col gap-4">
			<Button
				class="w-full h-11 text-primary-foreground font-semibold shadow-lg hover:shadow-xl transition-all"
				onclick={handleRegister}
				disabled={loading}
			>
				{#if loading}
					<span class="flex items-center gap-2">
						<div class="w-4 h-4 border-2 border-primary-foreground/30 border-t-primary-foreground rounded-full animate-spin"></div>
						Creating account...
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
