<script>
	import { page } from '$app/stores';
	import Icon from '$lib/icon.svelte';

	import locationIcon from '../phosphoricons/map-pin-fill.svg?raw';
	import funnelIcon from '../phosphoricons/funnel-fill.svg?raw';
	import sliderIcon from '../phosphoricons/sliders-horizontal-fill.svg?raw';
	import settingIcon from '../phosphoricons/gear-fill.svg?raw';
</script>

<header>
	<nav
		class="flex items-center justify-between h-16 bg-dark  text-xl xl:text-2xl w-full font-bold"
	>
		<picture class="flex items-center w-20">
			<img src="logo6.svg" alt="logo" />
		</picture>
		<ul class="flex items-center justify-between w-1/2 mx-4">
			<li>
				<a sveltekit:prefetch href="/"
					><Icon
						data={locationIcon}
						color={$page.url.pathname === '/' ? 'red' : 'white'}
						size="12"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</li>

			<li>
				<a sveltekit:prefetch href="/filters"
					><Icon
						data={funnelIcon}
						color={$page.url.pathname === '/filters' ? 'red' : 'white'}
						size="12"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</li>
			<li>
				<a sveltekit:prefetch href="/preferences"
					><Icon
						data={sliderIcon}
						color={$page.url.pathname === '/preferences' ? 'red' : 'white'}
						size="12"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</li>
			<li>
				<a sveltekit:prefetch href="/settings"
					><Icon
						data={settingIcon}
						color={$page.url.pathname === '/settings' ? 'red' : 'white'}
						size="12"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</li>
		</ul>
	</nav>
</header>
