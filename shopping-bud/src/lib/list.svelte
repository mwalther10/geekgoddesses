<script>
	import ListItem from '$lib/listItem.svelte';
	import { onMount } from 'svelte';
	import { shoppingList, fullData, displayFullData } from '../stores/shopping-list-store.js';
</script>

<svelte:head>
	<title>Shopping List</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>

<div data-theme="cupcake" class="flex flex-col w-full font-medium  font-nunito ">
	{#each $shoppingList as item}
		<ListItem {item} />
	{/each}
</div>
