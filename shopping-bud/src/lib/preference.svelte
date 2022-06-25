<script>
	import Icon from './icon.svelte';
	export let icon;
	export let title;
	export let options;

	
	// $:disabled=check_disable(options);
	// $:console.log(disabled)

	// function check_disable(opts){
	// 	opts.forEach(element => {
	// 	if (element.value!=-1){
	// 		return false;
	// 	}
	// });
	// return true;
	// }
    /* range-accent range-secondary range-primary * */

</script>


<div class="collapse">
	<input type="checkbox" /> 
	<div class="collapse-title text-l font-medium">
		<div class="flex flex-row " style="border-radius: 0px;">
			<Icon data={icon} color={'dark'} size="8" padding="1"  />
			<div class="text-l mr-2 pt-1">{title}</div>
			{#each options as option, i}
			{#if option.value!=-1}
			<div class="badge text-sm badge-{option.color} mr-2">{option.value}{option.unit}</div>
			{/if}
			{/each}
            <!-- {#if disabled}
            {disabled}
            <div class="badge text-sm badge-accent mr-2">disabled</div>
            {/if} -->
		</div>
	</div>
	<div class="collapse-content"> 
			{#each options as option, i}
			<div class="form-control flex justify-center items-center flex-none">
				{#if option.value!=-1}
				  <span class="label-text p-2">{option.label} - ({option.value} {option.unit})</span>
				  {:else}
				  <span class="label-text p-2">{option.label} - ({option.unit})</span>
				  {/if}
                  <input type="range" min="{option.min}" max="{option.max}" bind:value={option.value} step="{option.steps}"  class="range range-{option.color}" />
			  </div>
			{/each}
			</div>

  </div>
<div class="flex flex-col items-center justify-center w-full">
	
	
</div>
