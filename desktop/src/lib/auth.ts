import { browser } from "$app/environment";
import { goto } from "$app/navigation";
import { writable } from "svelte/store";
import { apiGet, apiPost, clearTokens, getAccessToken, saveTokens, type Tokens } from "$lib/api";

export type User = {
	id: string;
	username: string;
	email: string;
	role: string | null;
};

export const currentUser = writable<User | null>(null);

export async function login(username: string, password: string) {
	const tokens = await apiPost<Tokens>("/auth/login/", { username, password });
	saveTokens(tokens);
	const user = await loadCurrentUser();
	return user;
}

export async function register(username: string, email: string, password: string) {
	return apiPost<User>("/auth/register/", {
		username,
		email,
		password,
		role: "technician",
	});
}

export async function loadCurrentUser() {
	const user = await apiGet<User>("/auth/me/");
	currentUser.set(user);
	return user;
}

export async function requireAuth() {
	if (!browser) return false;

	if (!getAccessToken()) {
		goto("/auth/login");
		return false;
	}

	try {
		await loadCurrentUser();
		return true;
	} catch {
		logout();
		return false;
	}
}

export function logout() {
	clearTokens();
	currentUser.set(null);
	if (browser) goto("/auth/login");
}
