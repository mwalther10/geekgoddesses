<script>
	import { page } from '$app/stores';
	import Icon from '$lib/icon.svelte';
	import noraImage from '../../images/nora2.webp';

	import locationIcon from '../phosphoricons/map-pin-fill.svg?raw';
	import funnelIcon from '../phosphoricons/funnel-fill.svg?raw';
	import sliderIcon from '../phosphoricons/sliders-horizontal-fill.svg?raw';
	import settingIcon from '../phosphoricons/gear-fill.svg?raw';
</script>

<header data-theme="cupcake">
	<link href="https://fonts.googleapis.com/css?family=Nunito:400,700&display=swap" rel="stylesheet">

	<div class="navbar border-b-2 border-dark bg-100 text-neutral-content ">
		<div class="flex-1">
			<picture class="flex items-center w-20">
				<img src="logo6.svg" alt="logo" />
			</picture>
		</div>
		<div class="flex-none">
			<!-- svelte-ignore a11y-label-has-associated-control -->
			<label tabindex="0" class="btn btn-circle btn btn-primary m-1">
				<a sveltekit:prefetch href="/"
					><Icon
						data={locationIcon}
						color={$page.url.pathname === '/' ? 'dark-blue' : 'light-blue'}
						size="8"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</label>
			<!-- svelte-ignore a11y-label-has-associated-control -->
			<label tabindex="0" class="btn btn-circle btn btn-primary m-1">
				<a sveltekit:prefetch href="/filters"
					><Icon
						data={funnelIcon}
						color={$page.url.pathname === '/filters' ? 'dark-blue' : 'light-blue'}
						size="8"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</label>

			<div class="dropdown dropdown-end">
				<!-- svelte-ignore a11y-label-has-associated-control -->
				<label tabindex="0" class="btn btn-ghost btn-circle avatar">
					<div class="w-12 rounded-full">
						<img alt="Profile" src={noraImage} />
					</div>
				</label>
				<ul
					tabindex="0"
					class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52"
				>
					<li>
						<a class="justify-between"> Profile </a>
					</li>
					<li><a>Settings</a></li>
					<li><a>Logout</a></li>
				</ul>
			</div>
		</div>
	</div>
</header>

