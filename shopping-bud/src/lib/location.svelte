<script>
	import { location } from '../stores/location.js';
	import { locationSelected } from '../stores/shopping-list-store.js';

	const confirmLocation = (newLocation) => {
		$location = newLocation;
		$locationSelected = true;
	};
</script>

<div class="text-dark m-4">Select store to proceed with your shopping list</div>

<div class="card w-96 bg-base-100 shadow-xl">
	<div class="flex w-full bg-white mb-4">
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
<div>
	<div
		class="flex items-center justify-center bg-dark rounded-full text-white font-medium text-center h-10 my-1 hover:bg-blue"
		on:click={() => confirmLocation('Kaufland Heidelberg-Weststadt')}
	>
		Kaufland Heidelberg-Weststadt
	</div>
	<div
		class="flex items-center justify-center bg-dark rounded-full text-white font-medium text-center h-10 my-1 hover:bg-blue"
		on:click={() => confirmLocation('Kaufland Heidelberg-Pfaffengrund')}
	>
		Kaufland Heidelberg-Pfaffengrund
	</div>
	<div
		class="flex items-center justify-center bg-dark rounded-full text-white font-medium text-center h-10 my-1 hover:bg-blue"
		on:click={() => confirmLocation('Kaufland Heidelberg-Rohrbach')}
	>
		Kaufland Heidelberg-Rohrbach
	</div>
</div>
