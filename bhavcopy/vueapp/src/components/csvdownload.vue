<template>
    <div class="row">
        <div class="col">        
        </div>
        <div class="col">       
        </div>
        <div class="col">       
        </div>
        <div class="col">  
            <a download><button @click="prepareCsv" class="btn btn-link searchBtn btn-sm" id="download">EXPORT AS CSV</button></a>
        </div>
    </div>   
</template>

<script>
export default {
    name:"CSVDownloader",
    data(){
        return {
        csvString:"",
        display:"none",
    }
    },
    methods:{
        prepareCsv(){
            this.csvString+='NAME,CODE,OPEN,HIGH,LOW,CLOSE,LAST'
            this.stockDetails.map(stock=>{
                const {SC_NAME, SC_CODE, OPEN, HIGH, LOW, CLOSE, LAST} = stock
                const fieldsValue = [SC_NAME, SC_CODE, OPEN, HIGH, LOW, CLOSE, LAST]
                this.csvString+='\n'+fieldsValue.join()
            })
            
            const blob = new Blob([this.csvString],{type:'text/csv;charset=utf-8'})
            let link = document.createElement("a")
            const url = URL.createObjectURL(blob)
            link.setAttribute("href", url)
            link.setAttribute("download", 'DETAILS.CSV')
            link.style.display = 'none'
            document.body.appendChild(link)
            link.click()
            document.body.removeChild(link)
        }
    },
    props:{
        stockDetails:Array
    },
    // created(){
    //     const element = document.getElementById("download").display
    //     this.stockDetails.length > 1? element.display="none":element.display="block"
    // }
}
</script>