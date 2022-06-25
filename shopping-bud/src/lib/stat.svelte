<script>
import globIcon from "../lib/phosphoricons/globe-hemisphere-east-light.svg?raw";
import moneyIcon from "../lib/phosphoricons/money.svg?raw";
import chartIcon from "../lib/phosphoricons/chart-pie-slice.svg?raw";
import Icon from './icon.svelte';
import PieChart from '../lib/pieChart_small.svelte';

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
      </div>
      <div class="stat-title text-center">Budget</div>
      <div class="badge badge-secondary text-center text-lg">{price}€</div>
    </div>
    
    <div class="stat">
      <div class="stat-title text-center">Macro</div>
      <div class="">
      <PieChart macros={[carbs, fat, protein]}></PieChart>
    </div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
      </div>
      <div class="stat-title text-center">EF Score</div>
      <div class=" ml-3 badge badge-secondary text-lg">{ef}</div>
    </div>
    
  </div>