<script context="module">
	export const prerender = true;
</script>

<script>
	import OverviewSection from '$lib/overviewSection.svelte';
	import { onMount } from 'svelte';
	import {
		shoppingList,
		firstFetched,
		leftovers,
		fullData,
		filteredList
	} from '../stores/shopping-list-store.js';

	const customMountLeftOvers = async () => {
		return await fetch('http://localhost:8000/' + 'sample?type=leftovers', {
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			method: 'GET'
		})
			.then((response) => response.json())
			.then((data) => {
				$leftovers = data;
			});
	};

	const customMountFilteredData = async () => {
		return await fetch('http://localhost:8000/' + 'sample?type=eco_pasta&filters=vegan,gluten', {
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			method: 'GET'
		})
				.then((response) => response.json())
				.then((data) => {
					$filteredList = data;
				});
	};

	const customMountShoppingList = async () => {
		return await fetch('http://localhost:8000/' + 'sample?type=simple_pasta', {
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			method: 'GET'
		})
			.then((response) => response.json())
			.then((data) => {
				$shoppingList = data.filter(
					(item) =>
						item.product_name == 'Basil Packaging' ||
						item.product_name == 'Aceite de oliva' ||
						item.product_name == 'Parmigiano Reggiano'
				);
				$fullData = data;
				$firstFetched = true;
			});
	};

	onMount(() => {
		if (!$firstFetched) {
			customMountLeftOvers();
			customMountShoppingList();
			customMountFilteredData();
		} 
	});

	const dummyRecipies = [
		{
			product_name: 'Spaghetti Carbonara',
			image_url: '/src/images/Spaghetti.jpeg',
			brands_tags: ['30 min']
		},
		{
			product_name: 'Lasagne',
			image_url: '/src/images/Lasagne.jpeg',
			brands_tags: ['60 min']
		}
	];
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>
<div data-theme="cupcake" class="flex flex-col w-full font-medium  font-nunito ">
	<div class="text-2xl  m-4  ">Welcome Nora!</div>
	{#if $shoppingList.length > 0}
		<a sveltekit:prefetch href="/shopping-list">
			<div>
				<OverviewSection
					data={$shoppingList}
					title="Shopping List"
					subtitle={'There are ' + $shoppingList.length + ' items on your list'}
				/>
			</div>
		</a>

		<div class="divider" />
	{/if}
	{#if $leftovers.length > 0}
		<div class="mt-4">
			<OverviewSection
				data={$leftovers}
				title="Leftovers"
				subtitle={'You have ' + $leftovers.length + ' items left'}
			/>
		</div>
		<div class="divider" />
	{/if}
	<div class="mt-4">
		<OverviewSection
			data={dummyRecipies}
			title="Recipe Recommendations"
			subtitle="Based on your leftovers and shopping list"
		/>
	</div>
</div>
