<script lang="ts">
	import { Button } from "$lib/components/ui/button/index.js";
	import { Input } from "$lib/components/ui/input/index.js";
	import { Label } from "$lib/components/ui/label/index.js";
	import * as Card from "$lib/components/ui/card/index.js";
	import * as Alert from "$lib/components/ui/alert/index.js";
	import Shield from "@lucide/svelte/icons/shield";
	import AlertCircle from "@lucide/svelte/icons/alert-circle";
	import { goto } from "$app/navigation";
  	import { ACCESS_TOKEN, REFRESH_TOKEN } from "$lib/constants";
  	import { fetchCurrentUser } from "$lib/userApi";
  	import api from "$lib/api";

	let username = "";
	let password = "";
	let loading = false;
	let errorMessage = "";

	 async function handleLogin(e: SubmitEvent) {
    e.preventDefault();
    loading = true;
    errorMessage = '';

    try {
      // 1. Récupération des tokens
      const res = await api.post('/api/token/', { username, password });
      
      // 2. Stockage immédiat (nécessaire pour que fetchCurrentUser fonctionne car il utilise le token)
      localStorage.setItem(ACCESS_TOKEN, res.data.access);
      localStorage.setItem(REFRESH_TOKEN, res.data.refresh);

      // 3. Récupérer l'utilisateur pour connaître son rôle
      const user = await fetchCurrentUser();

      // 4. Redirection conditionnelle
      if (user?.role === 'client') {
        goto('/dashboard'); // URL pour l'admin
      } else {
        goto('/dashboard/home'); // URL pour student/delegate
      }

    } catch (err: any) {
      console.error(err);
      if (err.response?.status === 401) {
        errorMessage = 'Nom d\'utilisateur ou mot de passe incorrect.';
      } else {
        errorMessage = 'Une erreur est survenue lors de la connexion.';
      }
      // Optionnel : nettoyer le localStorage en cas d'échec
      localStorage.removeItem(ACCESS_TOKEN);
    } finally {
      loading = false;
    }
  }
</script>

<div class="min-h-screen flex items-center justify-center bg-background p-4 relative overflow-hidden">
	<div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-primary/20 blur-[120px] rounded-full pointer-events-none"></div>
	<div class="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] bg-accent/20 blur-[120px] rounded-full pointer-events-none"></div>
	
	<Card.Root class="w-full max-w-md bg-card/80 backdrop-blur-xl border-border shadow-2xl relative z-10">
		<Card.Header class="space-y-2 text-center pb-8 pt-6">
			<div class="mx-auto bg-primary/10 p-4 rounded-2xl w-fit mb-4 ring-1 ring-primary/20">
				<Shield class="w-10 h-10 text-primary" />
			</div>
			<Card.Title class="text-3xl font-bold tracking-tight text-foreground">NetPilot</Card.Title>
			<Card.Description class="text-muted-foreground text-base">Remote MikroTik Management</Card.Description>
		</Card.Header>
		<Card.Content class="space-y-5">
			{#if errorMessage}
				<Alert.Root variant="destructive">
					<AlertCircle class="h-4 w-4" />
					<Alert.Description>{errorMessage}</Alert.Description>
				</Alert.Root>
			{/if}
			<div class="space-y-2">
				<Label for="username" class="font-medium text-foreground">Username</Label>
				<Input
					id="username"
					bind:value={username}
					placeholder="admin"
					autocomplete="username"
					class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background"
				/>
			</div>
			<div class="space-y-2">
				<div class="flex items-center justify-between">
					<Label for="password" class="font-medium text-foreground">Password</Label>
				</div>
				<Input
					id="password"
					type="password"
					bind:value={password}
					placeholder="••••••••"
					autocomplete="current-password"
					class="bg-background/50 border-input text-foreground h-11 transition-all focus:bg-background"
				/>
			</div>
		</Card.Content>
		<Card.Footer class="pb-6 flex-col gap-4">
			<Button
				type='submit'
				class="w-full h-11 text-primary-foreground font-semibold shadow-lg hover:shadow-xl transition-all"
				disabled={loading}
			>
				{#if loading}
					<span class="flex items-center gap-2">
						<div class="w-4 h-4 border-2 border-primary-foreground/30 border-t-primary-foreground rounded-full animate-spin"></div>
						Authenticating...
					</span>
				{:else}
					Sign In to Dashboard
				{/if}
			</Button>
			<div class="text-center text-sm text-muted-foreground">
				Don't have an account? 
				<a href="/auth/register" class="text-primary hover:underline font-medium transition-colors">Create one</a>
			</div>
		</Card.Footer>
	</Card.Root>
</div>
