<script context="module">
	export const prerender = true;
</script>

<script>
	import BulletList from '$lib/bullet-list.svelte';
	import { location } from '../stores/location';
	import Location from '../lib/location.svelte';
	import { shoppingList, locationSelected } from '../stores/shopping-list-store';
	import List from '$lib/list.svelte';
	import Icon from '$lib/icon.svelte';
	import locationIcon from '../lib/phosphoricons/map-pin-fill.svg?raw';
	import Stats from '$lib/stat.svelte';

	const setLocation = () => {
		$locationSelected = false;
	};
</script>


<svelte:head>
	<title>Shopping List</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>
<div data-theme="cupcake" class="flex flex-col font-medium font-nunito w-full ">
	{#if !$locationSelected}
		<Location />
	{/if}
	{#if $locationSelected}
	<Stats />
		<div class=" m-4 text-dark flex items-center " on:click ={() => (setLocation() )}>
			<Icon
				data={locationIcon}
				color={'dark'}
				size="8"
				padding="1"
				additionalStyle="cursor-pointer"
			/>
			<span class="font-bold">
				{$location}
			</span>
		</div>
		<BulletList />
		{#if $shoppingList.length > 0}
			<div class="m-4 text-dark text-lg">
				Shopping List
				<List />
			</div>
		{/if}
	{/if}
</div>
