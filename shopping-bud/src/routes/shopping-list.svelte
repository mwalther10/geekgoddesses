<script context="module">
	export const prerender = true;
</script>

<script>
	import BulletList from '$lib/bullet-list.svelte';
	import { location } from '../stores/location';
	import Location from '../lib/location.svelte';
	import { shoppingList } from '../stores/shopping-list-store';
</script>

<svelte:head>
	<title>Shopping List</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>
<div data-theme="cupcake" class="flex flex-col font-medium font-nunito w-full ">
	<Location />
	{#if $location != ''}
		<BulletList />
	{/if}
	{#if $shoppingList.length > 0}
		<div>TEst</div>
	{/if}
</div>
