import { writable } from "svelte/store";
const eatingHabitOptions = [{label: "Vegetarian",checked:false}, {label: "Vegan",checked:false}, {label: "Halal",checked:false}];
const allergyOptions= [{label: "Nuts",checked:false}, {label: "Gluten",checked:false}, {label: "Lactose",checked:false}];
const neutOptions= [{label: "Fat",value:-1, color:"primary", min:0,max:100,steps:1, unit:"%"}, {label: "Protein",value:-1,color:
"secondary",min:0,max:100,steps:1, unit:"%"}, {label: "Carbs",value:-1, color:"accent",min:0,max:100,steps:1, unit:"%"}];
const moneyOptions= [{label: "Total Budget",value:-1, color:"accent",min:0,max:500,steps:0.5, unit:"€"}];
const envOptions= [{label: "Total EF Score",value:-1, color:"primary",min:0,max:1,steps:0.1, unit:""}];
const filters=writable(
    {  "eatingHabbit":eatingHabitOptions, 
    "allergy": allergyOptions, 
    "neutriation":neutOptions,
    "budget":moneyOptions,
    "enviroment":envOptions}
);

export default filters;