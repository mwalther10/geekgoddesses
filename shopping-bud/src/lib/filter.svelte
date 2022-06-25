<script>
	import Icon from './icon.svelte';
	export let icon;
	export let title;
	export let options;
	// options = [{}]
</script>


<div class="collapse">
	<input type="checkbox" /> 
	<div class="collapse-title text-l font-medium">
		<div class="flex flex-row " style="border-radius: 0px;">
			<Icon data={icon} color={'dark'} size="8" padding="1"  />
			<div class="text-l mr-2 pt-1">{title}</div>
			{#each options as option, i}
			{#if option.checked}
			<div class="badge text-sm badge-primary mr-2">{option.label}</div>
			{/if}
			{/each}
		</div>
	</div>
	<div class="collapse-content"> 
		<div class="grid grid-cols-3 ">
			{#each options as option, i}
			<div class="form-control flex justify-center items-center flex-none">
				<label class="label cursor-pointer">
				  <span class="label-text p-2">{option.label}</span>
				  <input type="checkbox" class="toggle toggle-primary" bind:checked={option.checked}/>
				</label>
			  </div>
			{/each}
		</div>	</div>
  </div>
<div class="flex flex-col items-center justify-center w-full">
	
	
</div>
