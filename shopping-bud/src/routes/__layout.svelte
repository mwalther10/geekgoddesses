<script>
	import Header from '$lib/header/Header.svelte';
	import '../app.css';
</script>

<div class="flex flex-col justify-between h-screen">
	<Header />

	<main class="bg-white mb-auto flex grow ">
		<slot />
	</main>
</div>
<!--
<div class="flex items-center justify-center grow">
	<div class="mockup-phone border-blue ">
		<div class="camera" />
		<div class="display">
			<div class="artboard artboard-demo phone-1">
				<div class="flex flex-col justify-between h-screen">
					<Header />

					<main class="bg-white mb-auto flex grow ">
						<slot />
					</main>
				</div>
			</div>
		</div>
	</div>
</div>
-->
