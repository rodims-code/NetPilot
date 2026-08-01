import { browser } from "$app/environment";
import { goto } from "$app/navigation";
import { getAccessToken } from "$lib/api";
import type { Navigation } from "@sveltejs/kit";

// Routes that require authentication
const PROTECTED_PREFIXES = ["/dashboard"];

export function handleNavigation(navigation: Navigation) {
	if (!browser) return;
	
	const to = navigation.to?.url.pathname ?? "";
	const needsAuth = PROTECTED_PREFIXES.some((p) => to.startsWith(p));
	
	if (needsAuth && !getAccessToken()) {
		goto("/auth/login");
	}
}
