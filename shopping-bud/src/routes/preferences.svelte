<script context="module">
	import { browser, dev } from '$app/env';

	// we don't need any JS on this page, though we'll load
	// it in dev so that we get hot module replacement...
	export const hydrate = dev;

	// ...but if the client-side router is already loaded
	// (i.e. we came here from elsewhere in the app), use it
	export const router = browser;

	// since there's no dynamic data here, we can prerender
	// it so that it gets served as a static asset in prod
	export const prerender = true;
</script>

<script>
</script>

<svelte:head>
	<title>Preferences</title>
	<meta name="description" content="Shopping preferences" />
</svelte:head>

<div class="w-96 h-96">
	<picture>
		<img src="rocket_cart_logo.svg" alt="Logo" />
	</picture>
</div>
