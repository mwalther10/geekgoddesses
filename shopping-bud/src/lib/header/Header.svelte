<script>
	import { page } from '$app/stores';
	import Icon from '$lib/icon.svelte';
    import noraImage from "../../images/nora.jpeg";

	import locationIcon from '../phosphoricons/map-pin-fill.svg?raw';
	import funnelIcon from '../phosphoricons/funnel-fill.svg?raw';
	import sliderIcon from '../phosphoricons/sliders-horizontal-fill.svg?raw';
	import settingIcon from '../phosphoricons/gear-fill.svg?raw';
</script>
<style>
.border-b {
    border-bottom-width: 2px;
	border-color: #2C3763;
}
</style>
<header data-theme="lemonade" >
	<!-- <nav
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
						size="10"
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
						size="10"
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
						size="10"
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
						size="10"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</li>
		</ul>
	</nav> -->
	<div class="navbar bg-base-100 border-b">
		<div class="flex-1">
			<picture class="flex items-center w-20">
				<img src="logo6.svg" alt="logo" />
			</picture>
		</div>
		<div class="flex-none">
			<!-- svelte-ignore a11y-label-has-associated-control -->
			<label tabindex="0" class="btn btn-ghost btn-circle">
				<a sveltekit:prefetch href="/"
				><Icon
					data={locationIcon}
					color={$page.url.pathname === '/' ? 'red' : 'fill-blue'}
					size="10"
					padding="1"
					additionalStyle="cursor-pointer"
				/></a>
			</label>
			<!-- svelte-ignore a11y-label-has-associated-control -->
			<label tabindex="0" class="btn btn-ghost btn-circle">
				<a sveltekit:prefetch href="/filters"
					><Icon
						data={funnelIcon}
						color={$page.url.pathname === '/filters' ? 'red' : 'fill-blue'}
						size="10"
						padding="1"
						additionalStyle="cursor-pointer"
					/></a
				>
			</label>
			
		  <div class="dropdown dropdown-end">
			<label tabindex="0" class="btn btn-ghost btn-circle avatar">
			  <div class="w-10 rounded-full">
				<img src="{noraImage}"
			 />
			  </div>
			</label>
			<ul tabindex="0" class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
			  <li>
				<a class="justify-between">
				  Profile
				</a>
			  </li>
			  <li><a>Settings</a></li>
			  <li><a>Logout</a></li>
			</ul>
		  </div>
		</div>
	  </div>
</header>
