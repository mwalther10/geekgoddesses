<script>
	import Header from '$lib/header/Header.svelte';
	import '../app.css';
</script>


<div class="flex flex-col justify-between h-screen">
	<Header />

	<main class="bg-white mb-auto flex grow ">
		<slot />
	</main>
	
	<footer class="invisible">
		<p>ShoppingBud!</p>
	</footer>
</div>

