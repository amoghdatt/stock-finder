<template>
    <div>
        <div class="suggest" v-for="(item, index) in matchedList" :key="index">
            <Match @stock-selected="$emit('stock-selected',item)" :matchedValue="item"/>
        </div>
    </div>
</template>

<script>
    import Match from './match'

    export default{
        name: 'Matches',
        props:{
            matchedList:Array
        },
        components:{
            Match
        },
    }
</script>

<style scoped>
    .suggest{
        display: inline;
        padding: 5px;
    }
</style>