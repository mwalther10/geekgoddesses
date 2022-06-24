<script>
	import { page } from '$app/stores';
</script>

<header>

	<nav class="flex items-center justify-center h-24 bg-light-grey  text-xl xl:text-2xl w-full font-bold">
		<picture>
			<img class="w-24 h-24" src="logo2.svg" alt="rocket_cart_logo" />
		</picture>
		<ul class="flex items-center justify-center w-fit">
			<li class={$page.url.pathname === '/' ? "text-yellow" : "text-white" + " mx-4"}><a sveltekit:prefetch href="/">Home</a></li>
			<li class={$page.url.pathname === '/about' ? "text-yellow": "text-white" + " mx-4"}>
				<a sveltekit:prefetch href="/about">About</a>
			</li>
		</ul>
	</nav>
</header>
