<template>
<div>
    <div v-for="(item ,index) in selectedStocks" :key="index">
        <span class="dropdown-item"> {{ item.stockName }}</span>
    </div>
</div>
</template>

<script>
export default {
    name: 'DisplaySelectedstocks',
    props:{
        selectedStocks:Array
    }
}
</script>
