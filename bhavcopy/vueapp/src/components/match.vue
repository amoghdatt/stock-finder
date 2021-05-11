<template>
    <span @click="$emit('stock-selected', matchedValue)" class="badge rounded-pill bg-light text-dark matchedValue">{{ matchedValue }}</span>
</template>

<script>

    export default{
        name: 'Match',
        props:{
            matchedValue:String
        }
    }

</script>

<style scoped>
    .matchedValue:hover{
        cursor: pointer;
    }
</style>