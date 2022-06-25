<script context="module">
	export const prerender = true;
</script>

<script>
	import OverviewSection from '$lib/overviewSection.svelte';

	const openShoppingList = () => {
		window.location.href = '/shopping-list';
	};
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>
<div data-theme="cupcake" class="flex flex-col font-medium  font-nunito ">
	<div class="text-xl  m-3 ">Welcome Nora!</div>

	<div class="card w-96 bg-base-100 shadow-xl">
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
	  </div>

	
	<h6 class="  text-sm justify-center m-2 h-fit">
		  
		You are shopping at:
		<div class="badge badge-primary ">
			<div>
			  <span>Kaufland Heidelberg-Weststadt</span>
			</div>
		  </div>
		</h6>
	<div>
		<div on:click={() => openShoppingList()}>
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

	</div>
	<div class="divider"></div> 

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
