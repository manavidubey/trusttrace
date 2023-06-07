const axios = require('axios');
const api="YBCDP8IEEZMKN2C1TTH4CJMUE3XBSASXIF"
// const wallet="0x569402E6D161155e6C77632ac35908305da4E7a0"
const wallet="0x632d0C88EBE5F70942402F3EBbd8627b5b60aA39"
const URL=`https://api-testnet.polygonscan.com/api?module=account&action=txlist&address=${wallet.toLowerCase()}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=${api}`
// const URL=`https://api.polygonscan.com/api?module=account&action=tokentx&contractaddress=0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270&address=0x6813ad11cca98e15ff181a257a3c2855d1eee69e&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey=${api}`


 async function axiosTest() {
    const promise =await axios.get(URL);
    return promise.data
}
async function dataa(){
    const val=await axiosTest();
    let totalCount=0;
    let result=[]
    for (let i = 0; i < val.result.length; i++) {
        if (val.result[i].from==`${wallet.toLowerCase()}` && val.result[i].functionName=="" && val.result[i].to!='') {
            val.result[i].value=`-${val.result[i].value}`
            // console.log(val.result[i]);
            result.push(val.result[i]);
            totalCount++;
        }
         if (val.result[i].to==`${wallet.toLowerCase()}` && val.result[i].functionName=="" ) {
            // console.log(val.result[i]);
            result.push(val.result[i]);
            totalCount++;
        }
    }
    // console.log(val.result.length);
    console.log(result);
    console.log(totalCount);

}
let a= dataa()
// console.log(a)