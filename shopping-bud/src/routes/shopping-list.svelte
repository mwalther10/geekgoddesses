<script context="module">
	export const prerender = true;
</script>

<script>
	import Location from "../lib/location.svelte";
	let selectedStore = "Kaufland Heidelberg-Weststadt";
	
</script>

<svelte:head>
	<title>Shopping List</title>
	<meta name="description" content="ShoppingBud" />
</svelte:head>
<div data-theme="cupcake" class="flex flex-col font-medium font-nunito ">

	<div class="text-dark m-4">
		Select store to proceed with your shopping list
	</div>

	<div class="card w-96 bg-base-100 shadow-xl">
		<div class="flex w-full bg-white mb-4"  >
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
		<Location  />
	</div>

	



</div>
