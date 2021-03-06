import { writable} from "svelte/store";

export const shoppingList = writable([]);
export const leftovers = writable([]);
export const fullData = writable([]);
export const filteredList = writable([]);
export const currentType=writable("leftovers");
export const currentFilters=writable("");
export const firstFetched=writable(false);
export const displayFullData = writable(false);
export const locationSelected = writable(false);
