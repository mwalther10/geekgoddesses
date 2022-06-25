import { writable} from "svelte/store";

export const shoppingList = writable([]);
export const currentType=writable("");
export const currentFilters=writable("");
