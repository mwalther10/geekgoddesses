<script context="module">
	export const prerender = true;
</script>

<script>
	import OverviewSection from '$lib/overviewSection.svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>
<div class="flex flex-col font-medium text-dark">
	<div class="text-xl  m-4">Welcome Nora!</div>
	<div class="flex w-full bg-white">
		<iframe
			title="ShoppingBud"
			src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2596.224708674731!2d8.679111851243265!3d49.40465607924336!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4797c0df0b865475%3A0xa60b64f5dbf061a8!2sKaufland%20Heidelberg-Weststadt!5e0!3m2!1sde!2sde!4v1656073006266!5m2!1sde!2sde"
			width="390"
			height="300"
			style="border:0;"
			loading="lazy"
			referrerpolicy="no-referrer-when-downgrade"
		/>
	</div>
	<div class=" flex flex-col  justify-center m-4 h-fit">
		You are shopping at:
		<div
			class="flex bg-dark rounded-lg text-white border-1 items-center justify-center w-full text-center mt-2"
		>
			Kaufland Heidelberg-Weststadt
		</div>
	</div>
	<div>
		<OverviewSection
			data={[
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				}
			]}
			title="Current Shopping List"
		/>
	</div>
	<div class="mt-4">
		<OverviewSection
			data={[
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				},
				{
					title: 'Yoghurt',
					image: '$images/yoghurt.jpeg',
					brand: 'Milram'
				}
			]}
			title="Leftovers in your Stock"
		/>
	</div>
</div>
