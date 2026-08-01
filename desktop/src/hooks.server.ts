import { browser } from "$app/environment";
import { goto } from "$app/navigation";
import type { Handle } from "@sveltejs/kit";

// Protected route prefixes — redirect to login if no token
const PROTECTED = ["/dashboard"];
const AUTH_ROUTES = ["/auth/login", "/auth/register"];

export const handle: Handle = async ({ event, resolve }) => {
	return resolve(event);
};
