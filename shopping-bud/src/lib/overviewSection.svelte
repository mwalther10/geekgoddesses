<script>
	export let data = [
		{
			title: 'Yoghurt',
			image: 'yoghurt.png',
			brand: 'Milram'
		}
	];
    export let title;
    import yogurtImage from "../images/yoghurt.png";

    const handleClick = () => {
        console.log("clicked");
    };
</script>
<style>
	.color-dark
	{
		/* border:none;
		border-radius: 0;
		border-right: 1px solid #2C3763; */
		color:#2C3763;
		opacity:1;
	}
</style>

<div>
	<div class="text-l  m-4 " on:click={handleClick}>{title}</div>
	<div class="flex overflow-x-scroll">
		{#each data as { ...item }, i}
			 <div class=" flex items-center mx-4 flex-none"><div>
				<div class="stat-figure text-secondary">
				  <div class="avatar">
					<div class="w-16 rounded-full" >
						<img src={yogurtImage} alt={item.title} class="w-14 h-14" />
					</div>
				  </div>
				</div>
				<div class="stat-title color-dark">{item.title}</div>
				<div class="stat-desc color-dark badge badge-accent badge-outline">{item.brand}</div>
			</div>
			  </div>
		{/each}
        </div>
</div>
