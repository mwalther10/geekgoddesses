<script>
	import Icon from './icon.svelte';

	export let data;
	export let title;
	export let subtitle;

	import arrowIcon from './phosphoricons/arrow-circle-right-fill.svg?raw';
	const handleClick = () => {
		console.log('clicked');
	};
</script>

<div>
	<div class=" flex items-center text-lg font-bold  ml-4 my-1 text-dark " on:click={handleClick}>
		{title}
		<Icon data={arrowIcon} size="8" padding="1" color="dark" />
	</div>
	<div class="text-l  ml-4 my-1 mb-3" on:click={handleClick}>{subtitle}</div>
	<div class="flex overflow-x-scroll h-fit">
		{#each data as { ...item }, i}
			<div class="flex flex-col justify-center items-center mx-4 flex-none w-fit h-fit py-1 pb-4">
				<div class="stat-figure text-secondary">
					<div class="avatar ">
						<div class="w-16 rounded-full ring ring-primary" >
							<img src={item.image_url} alt={item.product_name} class="w-14 h-14" />
						</div>
					</div>
				</div>
				<div class="stat-title text-dark">{item.product_name}</div>
				<div class="stat-desc color-dark badge badge-outline">{item.brands_tags[0]}</div>
			</div>
		{/each}
	</div>
</div>

<style>
	.color-dark {
		/* border:none;
		border-radius: 0;
		border-right: 1px solid #2C3763; */
		color: #2c3763;
		opacity: 1;
	}
</style>
