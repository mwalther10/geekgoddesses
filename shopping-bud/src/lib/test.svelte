<script context="module">
    import { browser, dev } from '$app/env';

    // we don't need any JS on this page, though we'll load
    // it in dev so that we get hot module replacement...
    export const hydrate = dev;

    // ...but if the client-side router is already loaded
    // (i.e. we came here from elsewhere in the app), use it
    export const router = browser;

    // since there's no dynamic data here, we can prerender
    // it so that it gets served as a static asset in prod
    export const prerender = true;
</script>

<script>
    import { onMount } from "svelte";
    import { shoppingList, currentType, currentFilters } from '../stores/shopping-list-store.js';

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
    <title>Test</title>
    <meta name="description" content="Test" />
</svelte:head>

<div class="flex flex-col text-dark w-full">
    <ul>
        {#each $shoppingList as shoppingItem}
            <li>{shoppingItem.product_name}</li>
        {/each}
    </ul>
</div>
