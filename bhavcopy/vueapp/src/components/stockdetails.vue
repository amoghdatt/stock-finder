<template>
    <div class="container">
        <div class = "table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Stock Code</th>
                    <th scope="col">OPEN</th>
                    <th scope="col">HIGH</th>
                    <th scope="col">LOW</th>
                    <th scope="col">CLOSE</th>
                    <th scope="col">LAST</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(stock, index) in stockDetails" :key="index">
                    <td :class="`${backgroundColors[key]}`" v-for="(key, index) in requiredFields" :key="index">{{ stock[key] }}</td>
                </tr>  
            </tbody>
        </table>
    </div>
    </div>
</template>

<script>


export default{
    name: 'Stockdetails',
    data(){
        return{
            backgroundColors:{
                'OPEN': 'table-warning',
                'HIGH':'table-success',
                'LOW':'table-danger',
                'CLOSE':'table-info',
                'LAST':'table-secondary'
            },
            requiredFields:['SC_NAME', 'SC_CODE','OPEN','HIGH','LOW','CLOSE','LAST']
        }
    },
    props:{
        stockDetails:Array
    }
}

</script>

<style scoped>
    .withMargin{
        margin:10px;
    }
</style>