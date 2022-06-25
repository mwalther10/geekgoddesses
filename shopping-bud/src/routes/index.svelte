<script context="module">
	export const prerender = true;
</script>

<script>
	import OverviewSection from '$lib/overviewSection.svelte';

	const openShoppingList = () => {
		window.location.href = '/shopping-list';
	};
	const dummyShoppingList = [
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				}
			];
	const dummyLeftOvers = [
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				}
			];
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>
<div data-theme="cupcake" class="flex flex-col w-full font-medium  font-nunito ">
	<div class="text-2xl  m-4  ">Welcome Nora!</div>

	<div on:click={() => openShoppingList()}>
		<OverviewSection
			data={dummyShoppingList}
			title="Shopping List"
			subtitle={"There are " + dummyShoppingList.length + " items on your list"}
		/>
	</div>
	<div class="divider" />

	<div class="mt-4">
		<OverviewSection
			data={dummyLeftOvers}
			title="Leftovers"
			subtitle={"You have " + dummyLeftOvers.length + " items left"}
		/>
	</div>
	<div class="divider" />
	<div class="">
		<OverviewSection
			data={[
				{
					title: 'Yoghurt Cake',
					image: '/src/images/yoghurt-cake.webp',
					brand: 'Yoghurt'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '/src/images/yoghurt.png',
					brand: 'Milram'
				}
			]}
			title="Recipe Recommendations"
			subtitle="Based on your leftovers and shopping list"
		/>
	</div>
</div>
