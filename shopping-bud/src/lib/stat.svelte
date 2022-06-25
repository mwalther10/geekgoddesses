<script>
import globIcon from "../lib/phosphoricons/globe-hemisphere-east-light.svg?raw";
import moneyIcon from "../lib/phosphoricons/money.svg?raw";
import chartIcon from "../lib/phosphoricons/chart-pie-slice.svg?raw";
import Icon from './icon.svelte';
export let  price=0;
export let  fat=0;
export let protein=0
export let carbs=0
export let ef=0;
export let data;
data.forEach(element => {

  fat=fat+element.fat_100g;
  protein=protein+element.protein_100g;
  carbs=carbs+element.carbohydrates_100g;
  ef=ef+element.EF_single_score;
  price=price+element.price;
});
fat=(fat/data.length).toFixed(1)
protein=(protein/data.length).toFixed(1)
carbs=(carbs/data.length).toFixed(1)
ef=(ef/data.length).toFixed(2)

</script>
<style>
	.stat{
		padding-left: 1rem;
    padding-right: 0.1rem;
    padding-top: 0.1rem;
    padding-bottom: 0.1rem;
	}
  .stat-title
  {
    opacity: 1;
  }
</style>

<div class="stats ">
  
    <div class="stat" >
      <div class="stat-figure text-secondary">
        <Icon data={moneyIcon} color={'dark'} size="8" padding="1"  />
      </div>
      <div class="stat-title">Budget</div>
      <div class="badge badge-secondary">{price}€</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
        <Icon data={chartIcon} color={'dark'} size="8" padding="1"  />
      </div>
      <div class="stat-title">Micro</div>
      <div class="stat">f:{fat}%-p:{protein}%-c:{carbs}%</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
        <Icon data={globIcon} color={'dark'} size="8" padding="1"  />
      </div>
      <div class="stat-title">EF Score</div>
      <div class=" badge badge-secondary">{ef}</div>
    </div>
    
  </div>