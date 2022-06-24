<script>
	import { page } from '$app/stores';
</script>

<header>

	<nav class="flex items-center justify-between h-24 bg-light-grey  text-xl xl:text-2xl w-full font-bold">
		<picture class="flex items-center w-20">
			<img src="logo4.svg" alt="logo" />
		</picture>
		<ul class="flex items-center justify-between w-40 mx-4">
			<li class={ $page.url.pathname === '/' ? "text-red" : "text-white"}><a sveltekit:prefetch href="/">Home</a></li>
			<li class={ $page.url.pathname === '/about' ? "text-red": "text-white"}>
				<a sveltekit:prefetch href="/about">About</a>
			</li>
		</ul>
	</nav>
</header>
