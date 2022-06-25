<script>
import globIcon from "../lib/phosphoricons/globe-hemisphere-east-light.svg?raw";
import moneyIcon from "../lib/phosphoricons/money.svg?raw";
import chartIcon from "../lib/phosphoricons/chart-pie-slice.svg?raw";
import Icon from './icon.svelte';
export let  price=100;
export let  micro=[20,30,70];
export let ef=0.2;

</script>
<style>
	.stat{
		padding-left: 1rem;
    padding-right: 0.1rem;
    padding-top: 0.1rem;
    padding-bottom: 0.1rem;
	}
</style>

<div class="stats ">
  
    <div class="stat" >
      <div class="stat-figure text-secondary">
        <Icon data={moneyIcon} color={'dark'} size="8" padding="1"  />
      </div>
      <div class="stat-title">Budget</div>
      <div class="stat">{price}€</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
        <Icon data={chartIcon} color={'dark'} size="8" padding="1"  />
      </div>
      <div class="stat-title">Micro</div>
      <div class="stat">f:{micro[0]}%-p:{micro[1]}%-c:{micro[2]}%</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
        <Icon data={globIcon} color={'dark'} size="8" padding="1"  />
      </div>
      <div class="stat-title">EF Score</div>
      <div class="stat">{ef}</div>
    </div>
    
  </div>