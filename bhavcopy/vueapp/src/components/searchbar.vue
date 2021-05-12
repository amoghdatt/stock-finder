<template>
    <div class="shadow-lg p-3 mb-5 bg-body rounded searchAndPick">
        <form class="row g-3"> 
            <div class="col-md-5">
                <input @input="searchStock" id="selectedStock" v-model="stockName" type="text" class="form-control" placeholder="Enter name of the stock here." aria-label="Recipient's username" aria-describedby="button-addon2">
            </div>
            <div class="col-md-3">
                <input class="form-control" id="date" type="date" @input="selectDate">
            </div>
            <div class="col-sm-2">
                <button @click="handleAdd" class="btn btn-success addBtn" type="button" id="button-addon2">Add</button>
            </div>
            <div class="col-sm-2">
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Selections
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <DisplaySelectedstocks :selectedStocks="selectedStocks"/>
                </div>
            </div>
        </div>
        </form>
        <p></p>
        <small class="text-muted">{{ matchedStockNames.length > 0 ? 'Matching stocks found...': 'No Matching stocks found..'}}</small>
        <Matches @stock-selected="handleSelection" :matchedList="matchedStockNames"/>
        <p></p>
        <div class="row">
            <div class="col">        
            </div>
            <div class="col">  
               <button @click="getDetails" class="btn btn-primary searchBtn">Get Details</button>
            </div>
            <div class="col">       
            </div>
        </div>        
    </div>
</template>

<script>
import Matches from './matches'
import DisplaySelectedstocks from './selectedstocks'

export default{

    name: 'Searchbar',
    components:{
        Matches,
        DisplaySelectedstocks
    },
    data() {
        return {
            stockName: "",
            stockNames:[],
            matchedStockNames:[],
            selectedStock:"",
            selectedStocks:[],
            selectedDate:"",
        }
    },
    
    methods:{
        searchStock(event){
            const searchTerm = event.target.value
            let regex = ''
            if(searchTerm=== ''){
                this.matchedStockNames = []
                return
            }else{
                [...searchTerm].forEach(c=>regex+=`[${c.toUpperCase()}${c.toLowerCase()}]`)
                regex = '^'+regex+'.*'
                regex = new RegExp(regex)
                
            }
            this.matchedStockNames = this.stockNames.filter(name=>regex.test(name)).slice(0,9)
        },

        handleSelection(item){
            this.$emit('stock-selected', item)
            this.selectedStock = item
            document.getElementById("selectedStock").value = item
        },

        selectDate(event){
            const { value } = event.target
            this.date = value
        },

        handleAdd(){
            const stockObj = {'stockName':this.selectedStock,date:this.date}
            this.selectedStocks.push(stockObj)
        },

        getDetails(){
            const data = {"data":this.selectedStocks}
            this.$emit('get-details',data)
            this.selectedStocks = []
            document.getElementById("selectedStock").value = ''
            document.getElementById("date").value = ''
            this.matchedStockNames = []
            this.stockName = ''
        }
    },

    async created(){
        const response = await fetch('http://ec2-3-223-158-5.compute-1.amazonaws.com/api/stocks')
        const { stockNames } = await response.json()
        this.stockNames = stockNames
    },

    
}
</script>

<style scoped>
    .searchAndPick{margin-bottom:200px;}
    .searchBtn {
        width:100%;
        border-radius: 0%;
    }
    .addBtn{
        width:100%;
        border-radius: 0%;
    }
</style>