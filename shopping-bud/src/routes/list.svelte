<script>
    import ListItem from '$lib/listItem.svelte';
    const openShoppingList = () => {window.location.href = '/shopping-list';}
    import { shoppingList, currentType, currentFilters } from '../stores/shopping-list-store.js';
    import {onMount} from "svelte";

    onMount(async () => {
        return await fetch(("http://localhost:8000/" + 'sample?type=' + $currentType + "&filters=" + $currentFilters), {
            headers: {

                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            method: 'GET'
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                shoppingList.set(data);
            })
    });
</script>
<svelte:head>
    <title>Shopping List</title>
    <meta name="description" content="ShoppingBud" />
</svelte:head>

<div data-theme="cupcake" class="flex flex-col w-full font-medium  font-nunito ">
    <div class="text-2xl  m-4  ">Welcome Nora!</div>

    <div on:click={() => openShoppingList()}>
        <ListItem
                data={$shoppingList}
                title="Shopping List"
                subtitle={"There are " + $shoppingList.length + " items on your list"}>
        </ListItem>
    </div>
</div>